#Requires -Version 5.1
<#
.SYNOPSIS
    Zero-touch hc-enterprise-kg + hc-cdaio-kg setup for CMU CDAIO (Windows).

.DESCRIPTION
    Run from the cloned hc-cdaio-kg directory:
        git clone https://github.com/thehipsterciso/hc-cdaio-kg
        cd hc-cdaio-kg
        powershell -ExecutionPolicy Bypass -File scripts\install.ps1

    What this does (all idempotent — safe to re-run):
      [1/8] Python >= 3.11   (via winget, then py launcher)
      [2/8] Git              (via winget)
      [3/8] Engine repo      (hc-enterprise-kg clone / pull)
      [4/8] Poetry           (official installer)
      [5/8] Dependencies     (poetry install --extras mcp)
      [6/8] Build graph.json (from per-type files)
      [7/8] Claude Desktop MCP registration
      [8/8] Task Scheduler jobs (sync / EOD / morning)
      [+]   GitHub auth + personal sync branch
      [+]   Claude Desktop restart

.PARAMETER InstallDir
    Override the engine repo install location (default: ~\hc-enterprise-kg).

.PARAMETER SkipPull
    Skip git pull on an existing engine clone.

.PARAMETER GitHubToken
    Supply a GitHub PAT non-interactively (or set env:GITHUB_TOKEN).
#>
[CmdletBinding()]
param(
    [string]$InstallDir  = "$env:USERPROFILE\hc-enterprise-kg",
    [switch]$SkipPull,
    [string]$GitHubToken = $env:GITHUB_TOKEN
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# ── Constants ────────────────────────────────────────────────────────────────
$ENGINE_REPO_URL = 'https://github.com/thehipsterciso/hc-enterprise-kg'
$DATA_REPO_FULL  = 'thehipsterciso/hc-cdaio-kg'
$MIN_PY_MAJOR    = 3
$MIN_PY_MINOR    = 11
$TOTAL_STEPS     = 8

$ScriptsDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$DataDir    = Split-Path -Parent $ScriptsDir
$SyncGraph  = Join-Path $DataDir 'graph.json'
$ClaudeConfig = Join-Path $env:APPDATA 'Claude\claude_desktop_config.json'

# ── Output helpers ───────────────────────────────────────────────────────────
$CurrentStep = 0
$ScriptStart = [datetime]::UtcNow

function step {
    param([string]$msg)
    $script:CurrentStep++
    Write-Host "`n" -NoNewline
    Write-Host "[$($script:CurrentStep)/$TOTAL_STEPS] $msg" -ForegroundColor Cyan
}
function ok   { param([string]$m) Write-Host "    v  $m" -ForegroundColor Green  }
function warn { param([string]$m) Write-Host "    !  $m" -ForegroundColor Yellow }
function info { param([string]$m) Write-Host "    $m" }
function die  { param([string]$m) Write-Host "`n    x  ERROR: $m`n" -ForegroundColor Red; exit 1 }

# ── Helpers ──────────────────────────────────────────────────────────────────
function Refresh-EnvPath {
    $m = [System.Environment]::GetEnvironmentVariable('Path','Machine')
    $u = [System.Environment]::GetEnvironmentVariable('Path','User')
    $env:PATH = "$m;$u"
}

function Winget-Install {
    param([string]$id, [string]$label)
    info "Installing $label via winget..."
    winget install --id $id --exact --silent `
        --accept-package-agreements --accept-source-agreements 2>&1 |
        ForEach-Object { info "  $_" }
    # exit 0 = success, -1978335189 = already installed — both are OK
    Refresh-EnvPath
}

# ── Banner ───────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════╗" -ForegroundColor White
Write-Host "║   CMU CDAIO — hc-enterprise-kg installer (Windows)  ║" -ForegroundColor White
Write-Host "╚══════════════════════════════════════════════════════╝" -ForegroundColor White
Write-Host ""
info "Data repo    : $DataDir"
info "Engine dir   : $InstallDir"
info "Graph output : $SyncGraph"

# ── Network pre-check ────────────────────────────────────────────────────────
info "Checking network connectivity to GitHub..."
try {
    Invoke-WebRequest -Uri 'https://github.com' -UseBasicParsing -TimeoutSec 8 -Method Head | Out-Null
    ok "GitHub reachable"
} catch {
    warn "Cannot reach https://github.com — network may be limited. Continuing..."
    Start-Sleep -Seconds 2
}

# ── [1/8] Python >= 3.11 ────────────────────────────────────────────────────
step "Python >=$MIN_PY_MAJOR.$MIN_PY_MINOR"

$PythonCmd = $null

foreach ($c in @('python3.13','python3.12','python3.11','python3','python')) {
    if (Get-Command $c -ErrorAction SilentlyContinue) {
        $ver = & $c -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>$null
        if ($ver -match '^(\d+)\.(\d+)$') {
            $maj = [int]$Matches[1]; $min = [int]$Matches[2]
            if ($maj -gt $MIN_PY_MAJOR -or ($maj -eq $MIN_PY_MAJOR -and $min -ge $MIN_PY_MINOR)) {
                $PythonCmd = $c
                ok "Found: $(& $c --version 2>&1)"
                break
            }
        }
    }
}

# Try py launcher with specific version flags; resolve to the actual python.exe path
if (-not $PythonCmd -and (Get-Command py -ErrorAction SilentlyContinue)) {
    foreach ($v in @('3.13','3.12','3.11')) {
        $ver = & py "-$v" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>$null
        if ($ver -match '^3\.(\d+)$' -and [int]$Matches[1] -ge $MIN_PY_MINOR) {
            # Prefer the concrete executable so all later & $PythonCmd calls work without flags
            $pyExePath = & py "-$v" -c 'import sys; print(sys.executable)' 2>$null
            if ($pyExePath -and (Test-Path $pyExePath)) {
                $PythonCmd = $pyExePath
            } else {
                # Fallback: py launcher is available but executable path unknown
                # Create a wrapper scriptblock that injects the version flag
                $script:PyLauncherVer = "-$v"
                $PythonCmd = 'py'
            }
            ok "Found via py launcher: Python $ver"
            break
        }
    }
}
# If py launcher fallback is in use, redefine all python invocations via a function
if ($PythonCmd -eq 'py' -and $script:PyLauncherVer) {
    function Invoke-Python { & py $script:PyLauncherVer @args }
} else {
    function Invoke-Python { & $script:PythonCmd @args }
}
$script:PythonCmd = $PythonCmd  # capture in script scope for the function

if (-not $PythonCmd) {
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        die "No Python >=$MIN_PY_MAJOR.$MIN_PY_MINOR and winget not available.`nInstall Python from https://python.org then re-run."
    }
    warn "No Python >=$MIN_PY_MAJOR.$MIN_PY_MINOR found — installing Python 3.12 via winget..."
    Winget-Install 'Python.Python.3.12' 'Python 3.12'
    Refresh-EnvPath
    foreach ($c in @('python3.12','python3','python')) {
        if (Get-Command $c -ErrorAction SilentlyContinue) {
            $ver = & $c -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>$null
            if ($ver -match '^3\.(\d+)$' -and [int]$Matches[1] -ge $MIN_PY_MINOR) {
                $PythonCmd = $c; break
            }
        }
    }
    if (-not $PythonCmd) { die "Python installed but binary not found in PATH. Open a new terminal and re-run." }
    $script:PythonCmd = $PythonCmd  # Sync script scope so Invoke-Python uses the new path
    ok "Installed: $(Invoke-Python --version 2>&1)"
}

# ── [2/8] Git ────────────────────────────────────────────────────────────────
step "Git"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    warn "Git not found — installing via winget..."
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        die "winget not available. Install Git from https://git-scm.com then re-run."
    }
    Winget-Install 'Git.Git' 'Git'
    Refresh-EnvPath
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        die "Git installed but not in PATH. Open a new terminal and re-run."
    }
}
ok "$(git --version)"

# ── [3/8] Engine repo ────────────────────────────────────────────────────────
step "Engine repo (hc-enterprise-kg)"

if (Test-Path (Join-Path $InstallDir '.git')) {
    ok "Engine found at $InstallDir"
    if ($SkipPull) {
        info "SkipPull set — skipping git pull"
    } else {
        info "Pulling latest..."
        git -C $InstallDir pull --ff-only 2>&1 | ForEach-Object { info "  $_" }
        if ($LASTEXITCODE -eq 0) { ok "Engine up to date" }
        else { warn "Could not fast-forward. Use -SkipPull if you have local changes." }
    }
} else {
    if (Test-Path $InstallDir) {
        warn "$InstallDir exists but is not a git repo — removing stale directory..."
        Remove-Item -Recurse -Force $InstallDir
    }
    info "Cloning $ENGINE_REPO_URL -> $InstallDir"
    git clone $ENGINE_REPO_URL $InstallDir
    if ($LASTEXITCODE -ne 0) { die "git clone failed." }
    ok "Engine cloned"
}

Set-Location $InstallDir

# ── [4/8] Poetry ────────────────────────────────────────────────────────────
step "Poetry"

$PoetryCmd = $null
foreach ($p in @(
    'poetry',
    "$env:APPDATA\Python\Scripts\poetry.exe",
    "$env:USERPROFILE\.local\bin\poetry.exe",
    "$env:USERPROFILE\AppData\Roaming\Python\Scripts\poetry.exe"
)) {
    if (Get-Command $p -ErrorAction SilentlyContinue) { $PoetryCmd = $p; break }
}

if (-not $PoetryCmd) {
    warn "Poetry not found — installing via official installer..."
    try {
        $installerTmp = Join-Path $env:TEMP 'install-poetry.py'
        Invoke-WebRequest -Uri 'https://install.python-poetry.org' `
            -OutFile $installerTmp -UseBasicParsing
        Invoke-Python $installerTmp 2>&1 | ForEach-Object { info "  $_" }
        Remove-Item $installerTmp -Force -ErrorAction SilentlyContinue
    } catch {
        die "Poetry installer download failed: $_`nInstall manually: https://python-poetry.org/docs/"
    }
    Refresh-EnvPath
    $env:PATH = "$env:APPDATA\Python\Scripts;$env:PATH"
    foreach ($p in @(
        "$env:APPDATA\Python\Scripts\poetry.exe",
        'poetry',
        "$env:USERPROFILE\AppData\Roaming\Python\Scripts\poetry.exe"
    )) {
        if (Get-Command $p -ErrorAction SilentlyContinue) { $PoetryCmd = $p; break }
    }
    if (-not $PoetryCmd) {
        die "Poetry installed but binary not found. Check: $env:APPDATA\Python\Scripts\"
    }
}
ok "$(& $PoetryCmd --version)"

# Bind to the validated Python interpreter
& $PoetryCmd env use $script:PythonCmd --no-interaction 2>&1 | Out-Null

# ── [5/8] Dependencies ───────────────────────────────────────────────────────
step "Python dependencies (mcp extras)"

info "Running poetry install --extras mcp ..."
& $PoetryCmd install --extras 'mcp' --no-interaction 2>&1 | ForEach-Object { info "  $_" }
if ($LASTEXITCODE -ne 0) { die "poetry install failed. See output above." }
ok "Dependencies installed"

# ── [6/8] Build graph.json ───────────────────────────────────────────────────
step "Build knowledge graph"

$BuildPy = Join-Path $ScriptsDir 'lib\kg-build.py'
if (-not (Test-Path $BuildPy)) { die "Missing $BuildPy — is scripts\lib\ intact?" }
if (-not (Test-Path (Join-Path $DataDir 'entities')) -and
    -not (Test-Path (Join-Path $DataDir 'relationships'))) {
    die "No entities\ or relationships\ dirs in $DataDir. Is this a valid hc-cdaio-kg clone?"
}

info "Building graph.json..."
Invoke-Python $BuildPy $DataDir $SyncGraph 2>&1 | ForEach-Object { info "  $_" }
if ($LASTEXITCODE -ne 0) { die "kg-build.py failed." }

$graphInfo = Invoke-Python -c @"
import json, sys
try:
    d = json.load(open(r'$SyncGraph'))
    print(f"{len(d.get('entities',[]))} entities, {len(d.get('relationships',[]))} relationships")
except Exception as e:
    print(f'(could not verify: {e})', file=sys.stderr)
"@ 2>&1
ok "graph.json built — $graphInfo"

# ── [7/8] Claude Desktop MCP registration ────────────────────────────────────
step "Claude Desktop MCP registration"

& $PoetryCmd run hckg install claude --auto-install --graph $SyncGraph 2>&1 |
    ForEach-Object { info "  $_" }

if (Test-Path $ClaudeConfig) {
    Write-Host ""
    info "Registered entry:"
    Invoke-Python -c @"
import json, sys
try:
    cfg = json.load(open(r'$ClaudeConfig'))
    entry = cfg.get('mcpServers', {}).get('hc-enterprise-kg', {})
    if not entry:
        print('    hc-enterprise-kg entry not found', file=sys.stderr); sys.exit(1)
    print(f"    command : {entry.get('command', '?')}")
    for a in entry.get('args', []): print(f"    arg     : {a}")
    print(f"    graph   : {entry.get('env', {}).get('HCKG_DEFAULT_GRAPH', '(none)')}")
except Exception as e:
    print(f'    Could not read config: {e}', file=sys.stderr)
"@ 2>&1 | ForEach-Object { info $_ }
}
ok "MCP server registered"

# ── [8/8] Task Scheduler (sync daemons) ──────────────────────────────────────
step "Task Scheduler jobs"

$_bashCmd = Get-Command bash -ErrorAction SilentlyContinue
$bashExe  = if ($_bashCmd -and $_bashCmd.Source) { $_bashCmd.Source } else { $null }
if (-not $bashExe -or -not (Test-Path $bashExe)) {
    $bashExe = 'C:\Program Files\Git\bin\bash.exe'
}

function Register-KgTask {
    param(
        [string]$TaskName,
        [string]$BashScript,
        [hashtable]$Env,
        [Microsoft.Management.Infrastructure.CimInstance]$Trigger
    )
    if (-not (Test-Path $bashExe)) {
        warn "Git Bash not found at $bashExe — skipping Task: $TaskName"
        return
    }
    $envExports = ($Env.GetEnumerator() | ForEach-Object {
        "export $($_.Key)='$($_.Value)'"
    }) -join '; '
    $action = New-ScheduledTaskAction `
        -Execute $bashExe `
        -Argument "-c `"$envExports; bash '$BashScript'`""
    $settings = New-ScheduledTaskSettingsSet `
        -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
        -StartWhenAvailable -MultipleInstances IgnoreNew
    $principal = New-ScheduledTaskPrincipal `
        -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    Register-ScheduledTask -TaskName $TaskName -Action $action `
        -Trigger $Trigger -Settings $settings -Principal $principal -Force | Out-Null
    info "  Task registered: $TaskName"
}

$sharedEnv = @{
    HCKG_DATA_DIR  = $DataDir
    HCKG_GRAPH_SRC = $SyncGraph
    HCKG_GRAPH_OUT = $SyncGraph
    PYTHON_CMD     = $script:PythonCmd
}

try {
    Register-KgTask -TaskName 'hckg-sync' `
        -BashScript (Join-Path $ScriptsDir 'kg-sync.sh') `
        -Env ($sharedEnv + @{ HCKG_BRANCH = '' }) `
        -Trigger (New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Minutes 30) `
                      -Once -At (Get-Date).AddMinutes(2))

    Register-KgTask -TaskName 'hckg-eod' `
        -BashScript (Join-Path $ScriptsDir 'kg-eod.sh') `
        -Env $sharedEnv `
        -Trigger (New-ScheduledTaskTrigger -Daily -At '17:00')

    Register-KgTask -TaskName 'hckg-eod-night' `
        -BashScript (Join-Path $ScriptsDir 'kg-eod.sh') `
        -Env $sharedEnv `
        -Trigger (New-ScheduledTaskTrigger -Daily -At '23:00')

    Register-KgTask -TaskName 'hckg-morning' `
        -BashScript (Join-Path $ScriptsDir 'kg-morning.sh') `
        -Env $sharedEnv `
        -Trigger (New-ScheduledTaskTrigger -Daily -At '08:00')

    ok "Task Scheduler jobs registered (sync 30min, EOD 5pm+11pm, morning 8am)"
} catch {
    warn "Task Scheduler registration failed: $_`nRun sync scripts manually."
}

# ── [+] Sync branch setup ────────────────────────────────────────────────────
Write-Host "`n[+] Sync branch setup" -ForegroundColor Cyan

$GhUser      = ''
$MemberBranch = ''
$PushReady   = $false

info "Phase 1: ensuring data repo is current"
$_origBranchRaw = git -C $DataDir rev-parse --abbrev-ref HEAD 2>$null
$origBranch = if ($_origBranchRaw) { $_origBranchRaw } else { 'main' }
if ($origBranch -ne 'main') { git -C $DataDir checkout main --quiet 2>$null }
git -C $DataDir fetch origin --quiet 2>$null
git -C $DataDir merge --ff-only origin/main --quiet 2>$null
if ($LASTEXITCODE -ne 0) { warn "Could not fast-forward main — local edits may exist." }
ok "Data repo on main, up to date"

Write-Host ""
info "Phase 2: setting up your personal sync branch"

# Install gh CLI if missing
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    warn "gh CLI not found — installing via winget..."
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        Winget-Install 'GitHub.cli' 'GitHub CLI'
    } else {
        warn "winget not available — install gh from https://cli.github.com then re-run."
    }
}

# GITHUB_TOKEN non-interactive auth
if ($GitHubToken -and (Get-Command gh -ErrorAction SilentlyContinue)) {
    $authOk = (gh auth status 2>$null; $LASTEXITCODE -eq 0)
    if (-not $authOk) {
        info "Authenticating gh via token..."
        $GitHubToken | gh auth login --with-token 2>$null
        if ($LASTEXITCODE -eq 0) { ok "gh authenticated via token" }
        else { warn "Token auth failed — will attempt interactive login." }
    }
}

# Interactive fallback
if ((Get-Command gh -ErrorAction SilentlyContinue) -and
    -not (gh auth status 2>$null; $LASTEXITCODE -eq 0)) {
    Write-Host ""
    info "GitHub authentication needed. A browser window will open..."
    gh auth login --web --git-protocol https
}

if (Get-Command gh -ErrorAction SilentlyContinue) {
    $_ghUserRaw = gh api user --jq '.login' 2>$null
    $GhUser = if ($_ghUserRaw) { $_ghUserRaw } else { '' }
}

if ($GhUser) {
    ok "Authenticated as: $GhUser"
    $MemberBranch = "$GhUser/data"

    $_vpRaw = gh repo view $DATA_REPO_FULL --json viewerPermission `
                --jq '.viewerPermission' 2>$null
    $viewerPerm = if ($_vpRaw) { $_vpRaw } else { 'NONE' }

    if ($viewerPerm -in @('WRITE','MAINTAIN','ADMIN')) {
        $PushReady = $true
    } else {
        info "Requesting collaborator access..."
        $title = "Add collaborator: $GhUser to hc-cdaio-kg"
        $body  = "## New team member install request`n`n**GitHub username:** ``$GhUser```n`n**Action required (admin):**`n``````bash`nbash scripts/kg-add-member.sh $GhUser`n```````n`n> Auto-generated by scripts\install.ps1"
        gh issue create --repo $DATA_REPO_FULL --title $title --body $body `
            --label 'collaborator-request' 2>$null
        if ($LASTEXITCODE -ne 0) {
            gh issue create --repo $DATA_REPO_FULL --title $title --body $body 2>$null
        }
        warn "Access request filed — re-run this installer after accepting the GitHub invitation."
    }
}

if ($PushReady -and $MemberBranch) {
    $remoteOk = (git -C $DataDir ls-remote --exit-code --heads origin $MemberBranch 2>$null; $LASTEXITCODE -eq 0)
    if ($remoteOk) {
        git -C $DataDir checkout $MemberBranch --quiet 2>$null
    } else {
        git -C $DataDir checkout -b $MemberBranch origin/main --quiet 2>$null
        git -C $DataDir push origin $MemberBranch --quiet 2>$null
    }

    # Ensure git identity
    $gitEmail = git -C $DataDir config user.email 2>$null
    if (-not $gitEmail) {
        $_ghEmailRaw = gh api user --jq '.email // empty' 2>$null
        $ghEmail = if ($_ghEmailRaw) { $_ghEmailRaw } else { "$GhUser@users.noreply.github.com" }
        $_ghNameRaw = gh api user --jq '.name // empty' 2>$null
        $ghName  = if ($_ghNameRaw) { $_ghNameRaw } else { $GhUser }
        git -C $DataDir config user.email $ghEmail
        git -C $DataDir config user.name  $ghName
    }

    $SplitPy = Join-Path $ScriptsDir 'lib\kg-split.py'
    if ((Test-Path $SplitPy) -and (Test-Path $SyncGraph)) {
        Invoke-Python $SplitPy $SyncGraph $DataDir 2>$null
        git -C $DataDir add entities/ relationships/ 2>$null
        git -C $DataDir diff --cached --quiet 2>$null
        if ($LASTEXITCODE -ne 0) {
            git -C $DataDir commit -m 'feat: initial graph split from installer' --quiet
            git -C $DataDir push origin $MemberBranch --quiet 2>$null
            if ($LASTEXITCODE -eq 0) { ok "Initial graph split pushed to $MemberBranch" }
            else { warn "Push failed — will retry on first sync run." }
        } else {
            info "Branch already up to date."
        }
    }

    # Patch Task Scheduler jobs with the resolved branch name
    foreach ($taskName in @('hckg-sync','hckg-eod','hckg-eod-night')) {
        $t = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
        if ($t) {
            $t.Actions[0].Arguments = $t.Actions[0].Arguments -replace
                "export HCKG_BRANCH=''", "export HCKG_BRANCH='$MemberBranch'"
            Set-ScheduledTask -InputObject $t -ErrorAction SilentlyContinue | Out-Null
        }
    }
}

# ── [+] Claude Desktop restart ───────────────────────────────────────────────
Write-Host "`n[+] Claude Desktop restart" -ForegroundColor Cyan

$claudeProcs = Get-Process -Name 'Claude' -ErrorAction SilentlyContinue
if (-not $claudeProcs) {
    info "Claude Desktop is not running — open it after this script finishes."
} else {
    info "Restarting Claude Desktop to load new MCP registration..."
    $claudeExe = $claudeProcs[0].Path
    $claudeProcs | Stop-Process -Force -ErrorAction SilentlyContinue
    $waited = 0
    while ((Get-Process -Name 'Claude' -ErrorAction SilentlyContinue) -and $waited -lt 8) {
        Start-Sleep -Seconds 1; $waited++
    }
    ok "Claude Desktop stopped"
    if ($claudeExe -and (Test-Path $claudeExe)) {
        Start-Process $claudeExe; ok "Claude Desktop relaunched"
    } else {
        $found = @(
            "$env:LOCALAPPDATA\AnthropicClaude\claude.exe",
            "$env:LOCALAPPDATA\Programs\Claude\claude.exe",
            "$env:PROGRAMFILES\Claude\claude.exe"
        ) | Where-Object { Test-Path $_ } | Select-Object -First 1
        if ($found) { Start-Process $found; ok "Claude Desktop relaunched ($found)" }
        else { warn "Could not find Claude Desktop binary — open it manually." }
    }
}

# ── Summary ──────────────────────────────────────────────────────────────────
$elapsed = [datetime]::UtcNow - $ScriptStart
Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║   Installation complete!                             ║" -ForegroundColor Green
Write-Host "╚══════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""
Write-Host "  Total time: $([int]$elapsed.TotalMinutes)m $($elapsed.Seconds)s" -ForegroundColor DarkGray
Write-Host ""
Write-Host "How to use the knowledge graph in Claude Desktop:" -ForegroundColor White
Write-Host ""
Write-Host "  The graph is PRE-LOADED — just ask questions directly:"
Write-Host "    `"Show me graph statistics`""
Write-Host "    `"Who are the top 10 most connected people?`""
Write-Host "    `"Find the shortest path between [Entity A] and [Entity B]`""
Write-Host "    `"What is the blast radius of the core firewall?`""
Write-Host ""
Write-Host "Useful commands:" -ForegroundColor White
Write-Host "  Diagnose:    cd $InstallDir; poetry run hckg install doctor"
Write-Host "  Manual sync: Run Task Scheduler task 'hckg-sync'  — or via Git Bash:"
Write-Host "               bash '$($ScriptsDir -replace '\\','/')'/kg-sync.sh"
Write-Host "  Manual EOD:  Run Task Scheduler task 'hckg-eod'   — or via Git Bash:"
Write-Host "               bash '$($ScriptsDir -replace '\\','/')'/kg-eod.sh"
Write-Host ""
