#!/usr/bin/env bash
# =============================================================================
# install.sh — Zero-touch hc-enterprise-kg + hc-cdaio-kg setup for CMU CDAIO
#
# Usage (new team member — two commands, nothing else needed):
#   git clone https://github.com/thehipsterciso/hc-cdaio-kg
#   bash hc-cdaio-kg/scripts/install.sh
#
# Supports: macOS (Intel + Apple Silicon), Linux (apt/dnf)
# Windows:  Use scripts/install.ps1 instead (native PowerShell)
#
# What this does (all idempotent — safe to re-run):
#   [1/8] OS detection
#   [2/8] Python ≥3.11
#   [3/8] Git
#   [4/8] Engine repo (hc-enterprise-kg) clone / pull
#   [5/8] Poetry
#   [6/8] Python dependencies (mcp extras)
#   [7/8] Build knowledge graph from per-type files
#   [8/8] Claude Desktop MCP registration
#   [+]   Sync branch setup (gh auth → personal branch → daemons)
#   [+]   Claude Desktop restart (automatic, if it's running)
# =============================================================================

set -euo pipefail
IFS=$'\n\t'

# ---------------------------------------------------------------------------
# Hard-coded configuration
# ---------------------------------------------------------------------------
readonly ENGINE_REPO_URL="https://github.com/thehipsterciso/hc-enterprise-kg"
readonly ENGINE_REPO_NAME="hc-enterprise-kg"
readonly DEFAULT_INSTALL_DIR="${HOME}/${ENGINE_REPO_NAME}"
readonly DATA_REPO_OWNER="thehipsterciso"
readonly DATA_REPO_NAME="hc-cdaio-kg"
readonly DATA_REPO_FULL="${DATA_REPO_OWNER}/${DATA_REPO_NAME}"
readonly MIN_PYTHON_MAJOR=3
readonly MIN_PYTHON_MINOR=11
readonly TOTAL_STEPS=8

# ---------------------------------------------------------------------------
# Colors — suppressed when stdout is not a TTY
# ---------------------------------------------------------------------------
if [ -t 1 ]; then
  RED='\033[0;31m' GREEN='\033[0;32m' YELLOW='\033[1;33m'
  BLUE='\033[0;34m' BOLD='\033[1m'    DIM='\033[2m' RESET='\033[0m'
  _IS_TTY=1
else
  RED='' GREEN='' YELLOW='' BLUE='' BOLD='' DIM='' RESET=''
  _IS_TTY=0
fi

# ---------------------------------------------------------------------------
# Progress state
# ---------------------------------------------------------------------------
CURRENT_STEP=0
SCRIPT_START=$(date +%s)
_STEP_START=0
_SPINNER_PID=""

# ---------------------------------------------------------------------------
# Spinner
# ---------------------------------------------------------------------------
_LOCALE="${LC_ALL:-${LC_CTYPE:-${LANG:-}}}"
if [[ "$_LOCALE" == *"UTF-8"* || "$_LOCALE" == *"utf-8"* || "$_LOCALE" == *"utf8"* ]]; then
  _FRAMES=('⠋' '⠙' '⠹' '⠸' '⠼' '⠴' '⠦' '⠧' '⠇' '⠏')
else
  _FRAMES=('-' '\' '|' '/')
fi
readonly _FRAME_COUNT=${#_FRAMES[@]}

_start_spinner() {
  [[ "$_IS_TTY" == "0" ]] && return
  local msg="$1"
  (
    local i=0
    while true; do
      printf "\r    ${BLUE}%s${RESET}  %s " "${_FRAMES[i % _FRAME_COUNT]}" "$msg"
      i=$((i + 1))
      sleep 0.08
    done
  ) &
  _SPINNER_PID=$!
  disown "$_SPINNER_PID" 2>/dev/null || true
}

_stop_spinner() {
  if [[ -n "$_SPINNER_PID" ]] && kill -0 "$_SPINNER_PID" 2>/dev/null; then
    kill "$_SPINNER_PID" 2>/dev/null || true
    _SPINNER_PID=""
  fi
  [[ "$_IS_TTY" == "1" ]] && printf "\r\033[2K" || true
}

# ---------------------------------------------------------------------------
# Trap
# ---------------------------------------------------------------------------
_POETRY_TMPOUT=""
_cleanup() {
  _stop_spinner
  [[ -n "$_POETRY_TMPOUT" ]] && rm -f "$_POETRY_TMPOUT" || true
}
trap '_cleanup' EXIT
trap '_cleanup; exit 130' INT
trap '_cleanup; exit 143' TERM

# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------
step() {
  _stop_spinner
  CURRENT_STEP=$((CURRENT_STEP + 1))
  _STEP_START=$(date +%s)
  echo -e "\n${BLUE}${BOLD}[${CURRENT_STEP}/${TOTAL_STEPS}] ${*}${RESET}"
}

ok() {
  _stop_spinner
  local suf=""
  if [[ "$_STEP_START" -gt 0 ]]; then
    local _now; _now=$(date +%s)
    local _secs=$(( _now - _STEP_START ))
    [[ $_secs -ge 2 ]] && suf="  ${DIM}(${_secs}s)${RESET}"
    _STEP_START=0
  fi
  echo -e "    ${GREEN}✓${RESET}  ${*}${suf}"
}

warn() { _stop_spinner; echo -e "    ${YELLOW}!${RESET}  ${*}"; }
info() { echo -e "    ${*}"; }
die()  { _stop_spinner; echo -e "\n    ${RED}✗  ERROR: ${*}${RESET}\n" >&2; exit 1; }

# ---------------------------------------------------------------------------
# Git identity helper — sets user.name and user.email from gh API if unset
# ---------------------------------------------------------------------------
_ensure_git_identity() {
  local repo_dir="${1:-}"
  [[ -z "${repo_dir}" ]] && repo_dir="${_DATA_DIR:-${HOME}/hc-cdaio-kg}"
  if [[ -z "$(git -C "${repo_dir}" config user.email 2>/dev/null || true)" ]]; then
    if command -v gh &>/dev/null && gh auth status &>/dev/null 2>&1; then
      local _gh_email _gh_name
      _gh_email="$(gh api user --jq '.email // empty' 2>/dev/null | head -1 || true)"
      _gh_name="$(gh api user  --jq '.name  // empty' 2>/dev/null | head -1 || true)"
      [[ -z "${_gh_email}" ]] && _gh_email="${_GH_USER:-git}@users.noreply.github.com"
      [[ -z "${_gh_name}"  ]] && _gh_name="${_GH_USER:-git}"
      git -C "${repo_dir}" config user.email "${_gh_email}" 2>/dev/null || true
      git -C "${repo_dir}" config user.name  "${_gh_name}"  2>/dev/null || true
      info "  git identity set: ${_gh_name} <${_gh_email}>"
    fi
  fi
}

# ---------------------------------------------------------------------------
# Usage / argument parsing
# ---------------------------------------------------------------------------
usage() {
  echo ""
  echo -e "${BOLD}CMU CDAIO — hc-enterprise-kg zero-touch installer${RESET}"
  echo ""
  echo "  Usage:  bash $0"
  echo ""
  echo "  No arguments needed.  Graph data comes from this repo (hc-cdaio-kg)."
  echo ""
  echo "  Optional environment variables:"
  echo "    HCKG_INSTALL_DIR    Override engine install location (~/${ENGINE_REPO_NAME})"
  echo "    HCKG_SKIP_PULL      Set to '1' to skip git pull on an existing engine clone"
  echo ""
  exit 1
}

[[ "${1:-}" == "-h" || "${1:-}" == "--help" ]] && usage

INSTALL_DIR="${HCKG_INSTALL_DIR:-${DEFAULT_INSTALL_DIR}}"
SKIP_PULL="${HCKG_SKIP_PULL:-0}"

# Resolve all paths to absolute now — before any cd changes the working directory
_SCRIPTS_DIR="$(cd "$(dirname "$0")" && pwd)"
_DATA_DIR="$(dirname "$_SCRIPTS_DIR")"   # hc-cdaio-kg repo root
_SYNC_GRAPH="${_DATA_DIR}/graph.json"

# ---------------------------------------------------------------------------
# Banner
# ---------------------------------------------------------------------------
echo ""
echo -e "${BOLD}╔══════════════════════════════════════════════════════╗${RESET}"
echo -e "${BOLD}║   CMU CDAIO — hc-enterprise-kg installer             ║${RESET}"
echo -e "${BOLD}╚══════════════════════════════════════════════════════╝${RESET}"
echo ""
info "Data repo    : ${_DATA_DIR}"
info "Engine dir   : ${INSTALL_DIR}"
info "Graph output : ${_SYNC_GRAPH}"
info "Steps        : ${TOTAL_STEPS} (+ sync setup + Claude restart)"

# ---------------------------------------------------------------------------
# Network pre-check
# ---------------------------------------------------------------------------
if command -v curl &>/dev/null; then
  if ! curl -sf --max-time 8 --head "https://github.com" -o /dev/null 2>/dev/null; then
    warn "Cannot reach https://github.com — network may be limited. Continuing..."
    sleep 2
  fi
fi

# ---------------------------------------------------------------------------
# [1/8] OS detection
# ---------------------------------------------------------------------------
step "OS detection"

OS="$(uname -s 2>/dev/null || true)"
ARCH="$(uname -m 2>/dev/null || true)"

case "$OS" in
  Darwin)
    PLATFORM="macos"
    ok "macOS (${ARCH})"
    PYPATH="$(command -v python3 2>/dev/null || true)"
    if [[ "$PYPATH" == /Library/Developer/CommandLineTools/* ]]; then
      warn "Apple Command-Line Tools Python detected — this can break Poetry."
      warn "If Poetry install fails, run:  brew install poetry"
    fi
    ;;
  Linux)
    PLATFORM="linux"
    ok "Linux (${ARCH})"
    ;;
  CYGWIN*|MINGW*|MSYS*)
    die "Windows detected. Use the PowerShell script instead:\n  .\\scripts\\install.ps1"
    ;;
  *)
    die "Unsupported OS: ${OS}. This script supports macOS and Linux.\nOn Windows, use scripts/install.ps1."
    ;;
esac

# ---------------------------------------------------------------------------
# Package manager helper
# ---------------------------------------------------------------------------
PKG_INSTALL_CMD=()
_APT=0
_DNF=0

if [[ "$PLATFORM" == "macos" ]]; then
  if ! command -v brew &>/dev/null; then
    warn "Homebrew not found — installing automatically..."
    NONINTERACTIVE=1 /bin/bash -c \
      "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" \
      2>&1 | sed 's/^/    /'
    # Activate brew in the current shell session
    if [[ -f /opt/homebrew/bin/brew ]]; then
      eval "$(/opt/homebrew/bin/brew shellenv)"
    elif [[ -f /usr/local/bin/brew ]]; then
      eval "$(/usr/local/bin/brew shellenv)"
    fi
    command -v brew &>/dev/null \
      || die "Homebrew install failed. Visit https://brew.sh and retry."
    ok "Homebrew installed"
  fi
  PKG_INSTALL_CMD=(brew install)
elif [[ "$PLATFORM" == "linux" ]]; then
  if command -v apt-get &>/dev/null; then
    PKG_INSTALL_CMD=(sudo apt-get install -y)
    _APT=1
  elif command -v dnf &>/dev/null; then
    PKG_INSTALL_CMD=(sudo dnf install -y)
    _DNF=1
  else
    warn "Unknown Linux package manager — some auto-installs may fail."
  fi
fi

_pkg_install() {
  [[ ${#PKG_INSTALL_CMD[@]} -eq 0 ]] && \
    die "No package manager configured. Install the package manually and re-run."
  "${PKG_INSTALL_CMD[@]}" "$@"
}

# ---------------------------------------------------------------------------
# [2/8] Python ≥3.11
# ---------------------------------------------------------------------------
step "Python ≥${MIN_PYTHON_MAJOR}.${MIN_PYTHON_MINOR}"

PYTHON_CMD=""
for _cmd in python3.13 python3.12 python3.11 python3 python; do
  if command -v "$_cmd" &>/dev/null; then
    _ver="$("$_cmd" -c \
      'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' \
      2>/dev/null || true)"
    _maj="${_ver%%.*}"
    _min="${_ver#*.}"
    if [[ -n "$_ver" ]] && \
       { [[ "$_maj" -gt "$MIN_PYTHON_MAJOR" ]] || \
         [[ "$_maj" -eq "$MIN_PYTHON_MAJOR" && "$_min" -ge "$MIN_PYTHON_MINOR" ]]; }; then
      PYTHON_CMD="$_cmd"
      ok "Found: $("$_cmd" --version 2>&1)"
      break
    fi
  fi
done

if [[ -z "$PYTHON_CMD" ]]; then
  warn "No Python ≥${MIN_PYTHON_MAJOR}.${MIN_PYTHON_MINOR} found — installing Python 3.12..."
  if [[ "$PLATFORM" == "macos" ]]; then
    brew install python@3.12
    _BREW_PY="$(brew --prefix python@3.12 2>/dev/null)/bin/python3.12"
    if [[ -x "${_BREW_PY}" ]]; then
      PYTHON_CMD="${_BREW_PY}"
    else
      PYTHON_CMD="python3.12"
    fi
  elif [[ "$_APT" == "1" ]]; then
    _start_spinner "Updating package lists..."
    sudo apt-get update -q
    _stop_spinner
    if ! apt-cache show python3.12 &>/dev/null; then
      info "Python 3.12 not in standard repos — adding deadsnakes PPA..."
      sudo apt-get install -y software-properties-common
      sudo add-apt-repository -y ppa:deadsnakes/ppa
      _start_spinner "Updating package lists..."
      sudo apt-get update -q
      _stop_spinner
    fi
    sudo apt-get install -y python3.12 python3.12-venv python3.12-dev
    PYTHON_CMD="python3.12"
  elif [[ "$_DNF" == "1" ]]; then
    sudo dnf install -y python3.12
    PYTHON_CMD="python3.12"
  else
    die "Cannot auto-install Python on this platform.\nInstall Python 3.11+ from https://python.org and re-run."
  fi
  ok "Installed: $($PYTHON_CMD --version 2>&1)"
fi

# ---------------------------------------------------------------------------
# [3/8] Git
# ---------------------------------------------------------------------------
step "Git"

if ! command -v git &>/dev/null; then
  warn "Git not found — installing..."
  if [[ "$PLATFORM" == "macos" ]]; then
    brew install git
  elif [[ "$_APT" == "1" ]]; then
    _start_spinner "Updating package lists..."
    sudo apt-get update -q
    _stop_spinner
    _pkg_install git
  else
    _pkg_install git
  fi
fi
ok "$(git --version)"

# ---------------------------------------------------------------------------
# [4/8] Engine repo (hc-enterprise-kg)
# ---------------------------------------------------------------------------
step "Engine repo (hc-enterprise-kg)"

if [[ -d "${INSTALL_DIR}/.git" ]]; then
  ok "Engine found at ${INSTALL_DIR}"
  if [[ "$SKIP_PULL" == "1" ]]; then
    info "HCKG_SKIP_PULL=1 — skipping git pull"
  else
    info "Pulling latest..."
    if git -C "$INSTALL_DIR" pull --ff-only 2>&1 | sed 's/^/    /'; then
      ok "Engine up to date"
    else
      warn "Could not fast-forward — engine is at its current version."
      warn "Set HCKG_SKIP_PULL=1 if you have local changes."
    fi
  fi
else
  if [[ -e "${INSTALL_DIR}" ]]; then
    warn "${INSTALL_DIR} exists but is not a git repo — removing stale directory..."
    rm -rf "${INSTALL_DIR}"
  fi
  info "Cloning ${ENGINE_REPO_URL}"
  info "→ ${INSTALL_DIR}"
  git clone "$ENGINE_REPO_URL" "$INSTALL_DIR"
  ok "Engine cloned"
fi

# All remaining poetry/hckg commands run from inside the engine repo
cd "$INSTALL_DIR" || die "Cannot enter ${INSTALL_DIR} — check permissions and re-run."

# ---------------------------------------------------------------------------
# [5/8] Poetry
# ---------------------------------------------------------------------------
step "Poetry"

POETRY_CMD=""
for _p in poetry "${HOME}/.local/bin/poetry" "${HOME}/.poetry/bin/poetry"; do
  if command -v "$_p" &>/dev/null 2>/dev/null; then
    POETRY_CMD="$_p"
    break
  fi
done

if [[ -z "$POETRY_CMD" ]]; then
  warn "Poetry not found — installing..."
  if [[ "$PLATFORM" == "macos" ]]; then
    brew install poetry
    POETRY_CMD="poetry"
  else
    if ! "$PYTHON_CMD" -m pip --version &>/dev/null 2>&1; then
      info "pip not found — bootstrapping via ensurepip..."
      "$PYTHON_CMD" -m ensurepip --upgrade || \
        die "Cannot bootstrap pip. Install python3-pip manually and re-run."
    fi
    if ! command -v pipx &>/dev/null; then
      _start_spinner "Installing pipx..."
      "$PYTHON_CMD" -m pip install --user --quiet pipx
      _stop_spinner
      export PATH="${HOME}/.local/bin:${PATH}"
      "$PYTHON_CMD" -m pipx ensurepath --force 2>/dev/null || true
    fi
    _start_spinner "Installing Poetry via pipx..."
    pipx install poetry
    _stop_spinner
    export PATH="${HOME}/.local/bin:${PATH}"
    hash -r 2>/dev/null || true
    # Probe absolute paths — PATH may not be refreshed in all shell configurations
    for _p in poetry "${HOME}/.local/bin/poetry"; do
      if command -v "$_p" &>/dev/null 2>/dev/null; then
        POETRY_CMD="$_p"; break
      fi
    done
    [[ -n "$POETRY_CMD" ]] \
      || die "Poetry installed but binary not found. Check: ${HOME}/.local/bin/"
  fi
fi
ok "$($POETRY_CMD --version)"

# Bind Poetry to the validated interpreter so virtual envs use the right Python
"$POETRY_CMD" env use "$PYTHON_CMD" --no-interaction 2>/dev/null || true

# ---------------------------------------------------------------------------
# [6/8] Python dependencies
# ---------------------------------------------------------------------------
step "Python dependencies (mcp extras)"

_POETRY_TMPOUT="$(mktemp)" || die "Cannot create temp file — is /tmp full or read-only?"
_start_spinner "Resolving dependencies..."

if ! "$POETRY_CMD" install --extras "mcp" --no-interaction \
     > "$_POETRY_TMPOUT" 2>&1; then
  _stop_spinner
  warn "poetry install failed. Full output:"
  sed 's/^/    /' "$_POETRY_TMPOUT"
  die "Dependency install failed. Fix the errors above and re-run."
fi

_stop_spinner
grep -E "(Resolving|Installing|Updating|•|Lock)" "$_POETRY_TMPOUT" 2>/dev/null \
  | head -20 | sed 's/^/    /' || true
rm -f "$_POETRY_TMPOUT"; _POETRY_TMPOUT=""

ok "Dependencies installed"

# ---------------------------------------------------------------------------
# [7/8] Build knowledge graph from per-type files
# ---------------------------------------------------------------------------
step "Build knowledge graph"

_BUILD_PY="${_SCRIPTS_DIR}/lib/kg-build.py"

if [[ ! -f "${_BUILD_PY}" ]]; then
  die "Missing ${_BUILD_PY} — is hc-cdaio-kg/scripts/lib/ intact?"
fi

if [[ ! -d "${_DATA_DIR}/entities" && ! -d "${_DATA_DIR}/relationships" ]]; then
  die "No entities/ or relationships/ dirs found in ${_DATA_DIR}.\nIs this a valid hc-cdaio-kg clone?"
fi

_start_spinner "Building graph.json..."
"$PYTHON_CMD" "${_BUILD_PY}" "${_DATA_DIR}" "${_SYNC_GRAPH}" 2>&1 | sed 's/^/    /'
_stop_spinner

# Verify and report counts
export _HCKG_GRAPH_OUT="$_SYNC_GRAPH"
_GRAPH_INFO="$("$PYTHON_CMD" - <<'PYCHECK'
import json, os, sys
p = os.environ.get("_HCKG_GRAPH_OUT", "")
try:
    with open(p) as f:
        d = json.load(f)
    print(f"{len(d.get('entities',[]))} entities, {len(d.get('relationships',[]))} relationships")
except Exception as e:
    print(f"(could not verify: {e})", file=sys.stderr)
PYCHECK
)"
ok "graph.json built — ${_GRAPH_INFO}"

# ---------------------------------------------------------------------------
# [8/8] Claude Desktop MCP registration
# ---------------------------------------------------------------------------
step "Claude Desktop MCP registration"
info "Graph : ${_SYNC_GRAPH}"
info "Writing config..."

"$POETRY_CMD" run hckg install claude \
  --auto-install \
  --graph "$_SYNC_GRAPH" \
  2>&1 | sed 's/^/    /'

# Read back registration for verification — non-fatal
CLAUDE_CONFIG=""
case "$PLATFORM" in
  macos) CLAUDE_CONFIG="${HOME}/Library/Application Support/Claude/claude_desktop_config.json" ;;
  linux) CLAUDE_CONFIG="${XDG_CONFIG_HOME:-${HOME}/.config}/Claude/claude_desktop_config.json" ;;
esac

if [[ -n "$CLAUDE_CONFIG" && -f "$CLAUDE_CONFIG" ]]; then
  echo ""
  info "Registered entry (from $(basename "$CLAUDE_CONFIG")):"
  export _HCKG_CONFIG="$CLAUDE_CONFIG"
  "$PYTHON_CMD" - <<'PYSHOW' || warn "Could not read back config — run 'hckg install doctor' to verify."
import json, os, sys
cfg_path = os.environ.get("_HCKG_CONFIG", "")
try:
    with open(cfg_path) as f:
        cfg = json.load(f)
except Exception as e:
    print(f"    Could not open config: {e}", file=sys.stderr)
    sys.exit(1)
entry = cfg.get("mcpServers", {}).get("hc-enterprise-kg", {})
if not entry:
    print("    hc-enterprise-kg entry not found in config", file=sys.stderr)
    sys.exit(1)
print(f"    command : {entry.get('command', '?')}")
for a in entry.get("args", []):
    print(f"    arg     : {a}")
if entry.get("cwd"):
    print(f"    cwd     : {entry['cwd']}")
graph = entry.get("env", {}).get("HCKG_DEFAULT_GRAPH", "(none)")
print(f"    graph   : {graph}")
print()
print("    Loading chain:")
print("    1. Claude restarts   → MCP server spawned with HCKG_DEFAULT_GRAPH set")
print("    2. Server startup    → auto_load_default_graph() → JSONIngestor.ingest()")
print("    3. Each tool call    → mtime check → auto-reload if graph.json changed")
PYSHOW
fi

ok "MCP server registered"

# ---------------------------------------------------------------------------
# [+] Sync branch setup
#
# Two-phase design:
#   Phase 1 — Pull: ensure local data repo is on main + up to date.
#             No clone needed — we're already running from hc-cdaio-kg.
#   Phase 2 — Write: gh auth → personal branch → daemons.
#             Requires GitHub account + collaborator access.
# ---------------------------------------------------------------------------
echo ""
echo -e "${BLUE}${BOLD}[+] Sync branch setup${RESET}"

_GH_USER=""
_MEMBER_BRANCH=""
_PUSH_READY=0

# ── Phase 1: pull latest main ────────────────────────────────────────────
echo ""
info "Phase 1: ensuring data repo is current"
_ORIG_BRANCH="$(git -C "${_DATA_DIR}" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")"
if [[ "${_ORIG_BRANCH}" != "main" ]]; then
  git -C "${_DATA_DIR}" checkout main --quiet 2>/dev/null || true
fi
_start_spinner "Pulling latest main from origin..."
git -C "${_DATA_DIR}" fetch origin --quiet 2>/dev/null || true
git -C "${_DATA_DIR}" merge --ff-only origin/main --quiet 2>/dev/null \
  || warn "Could not fast-forward main — local edits may exist."
_stop_spinner
ok "Data repo on main, up to date"

# ── Phase 2: gh auth → username → branch → daemons ──────────────────────
echo ""
info "Phase 2: setting up your personal sync branch (requires GitHub account)"

# Install gh CLI if missing
if ! command -v gh &>/dev/null; then
  if [[ "$PLATFORM" == "macos" ]]; then
    _start_spinner "Installing gh CLI..."
    brew install gh; _stop_spinner
  elif [[ "$_APT" == "1" ]]; then
    if apt-cache show gh &>/dev/null 2>&1; then
      _pkg_install gh
    else
      info "Adding GitHub CLI apt repo..."
      sudo mkdir -p -m 755 /etc/apt/keyrings
      wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null
      sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
      echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
        | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
      _start_spinner "Installing gh..."
      sudo apt-get update -q && _pkg_install gh; _stop_spinner
    fi
  elif [[ "$_DNF" == "1" ]]; then
    _start_spinner "Installing gh..."; sudo dnf install -y gh; _stop_spinner
  else
    warn "Cannot auto-install gh — install from https://cli.github.com then re-run."
  fi
fi

# Non-interactive auth via GITHUB_TOKEN env var
if command -v gh &>/dev/null && [[ -n "${GITHUB_TOKEN:-}" ]] && ! gh auth status &>/dev/null 2>&1; then
  echo "${GITHUB_TOKEN}" | gh auth login --with-token \
    && ok "gh authenticated via GITHUB_TOKEN" \
    || warn "GITHUB_TOKEN auth failed — falling back to interactive login"
fi

# Interactive auth (only when stdin is a terminal)
if command -v gh &>/dev/null && ! gh auth status &>/dev/null 2>&1; then
  echo ""
  echo -e "    ${BOLD}GitHub account needed to push your changes${RESET}"
  echo ""
  echo "    hc-cdaio-kg is publicly readable, but pushing your edits back"
  echo "    requires a free GitHub account and collaborator access."
  echo ""
  if [[ -t 0 ]]; then
    printf "    Do you already have a GitHub account? [y/N] "
    read -r _HAS_ACCOUNT; echo ""
    if [[ ! "$_HAS_ACCOUNT" =~ ^[Yy]([Ee][Ss])?$ ]]; then
      echo "    ┌─────────────────────────────────────────────────────┐"
      echo "    │  Create your free GitHub account:                   │"
      echo "    │  https://github.com/signup                          │"
      echo "    │  • Use your work email • Verify before continuing   │"
      echo "    └─────────────────────────────────────────────────────┘"
      echo ""
      [[ "$PLATFORM" == "macos" ]] && open "https://github.com/signup" 2>/dev/null || true
      command -v xdg-open &>/dev/null \
        && xdg-open "https://github.com/signup" 2>/dev/null || true
      printf "    Press Enter once your account is verified: "
      read -r _; echo ""
    fi
    echo "    Launching GitHub authentication (a browser window will open)..."
    echo "    Choose HTTPS when prompted for protocol."
    echo ""
    gh auth login --web --git-protocol https \
      || warn "Authentication failed — sync daemons will not be installed"
  else
    warn "stdin is not a terminal — run: gh auth login  then re-run installer"
  fi
fi

# Discover username
if command -v gh &>/dev/null && gh auth status &>/dev/null 2>&1; then
  _GH_USER="$(gh api user --jq .login 2>/dev/null || echo "")"
fi

if [[ -n "${_GH_USER}" ]]; then
  ok "Authenticated as: ${_GH_USER}"
  _MEMBER_BRANCH="${_GH_USER}/data"

  # Check collaborator / push access
  _VIEWER_PERM="$(gh repo view "${DATA_REPO_FULL}" --json viewerPermission \
    --jq '.viewerPermission' 2>/dev/null || echo "NONE")"

  if [[ "${_VIEWER_PERM}" =~ ^(WRITE|MAINTAIN|ADMIN)$ ]]; then
    _PUSH_READY=1
  else
    echo ""
    info "Requesting collaborator access from admin..."
    _ISSUE_TITLE="Add collaborator: ${_GH_USER} to hc-cdaio-kg"
    _ISSUE_BODY="$(cat <<ISSUEBODY
## New team member install request

**GitHub username:** \`${_GH_USER}\`

**Action required (admin):**
\`\`\`bash
bash scripts/kg-add-member.sh ${_GH_USER}
\`\`\`

Once the invitation is accepted, \`${_GH_USER}\` can re-run the installer to complete sync setup.

> Auto-generated by \`scripts/install.sh\`
ISSUEBODY
)"
    if gh issue create \
         --repo "${DATA_REPO_FULL}" \
         --title "${_ISSUE_TITLE}" \
         --body "${_ISSUE_BODY}" \
         --label "collaborator-request" \
         2>/dev/null \
       || gh issue create \
         --repo "${DATA_REPO_FULL}" \
         --title "${_ISSUE_TITLE}" \
         --body "${_ISSUE_BODY}" \
         2>/dev/null; then
      ok "Access request filed — admin will receive a GitHub notification"
    else
      warn "Could not file GitHub issue (label may not exist — that's OK)"
      warn "Your username is: ${_GH_USER}"
      warn "Ask admin to run: bash scripts/kg-add-member.sh ${_GH_USER}"
    fi
    echo ""
    info "Once the admin grants access and you accept the GitHub invitation email:"
    info "  Re-run: bash $(basename "$0")"
    warn "Sync daemons NOT installed yet — Claude reads from main branch for now."
  fi
fi

# Create branch + initial commit + push
if [[ "$_PUSH_READY" == "1" ]]; then
  if git -C "${_DATA_DIR}" ls-remote --exit-code --heads origin "${_MEMBER_BRANCH}" &>/dev/null; then
    git -C "${_DATA_DIR}" checkout "${_MEMBER_BRANCH}" --quiet 2>/dev/null \
      || git -C "${_DATA_DIR}" checkout -b "${_MEMBER_BRANCH}" "origin/${_MEMBER_BRANCH}" --quiet
  else
    git -C "${_DATA_DIR}" checkout -b "${_MEMBER_BRANCH}" origin/main --quiet 2>/dev/null \
      || git -C "${_DATA_DIR}" checkout -b "${_MEMBER_BRANCH}" --quiet
    git -C "${_DATA_DIR}" push origin "${_MEMBER_BRANCH}" --quiet 2>/dev/null \
      || warn "Branch push failed — will retry on first kg-sync.sh run"
  fi
  info "Branch: ${_MEMBER_BRANCH}"

  # The per-type files are already present (this IS the data repo).
  # Re-split from graph.json to ensure branch is current.
  _SPLIT_PY="${_SCRIPTS_DIR}/lib/kg-split.py"
  if [[ -f "${_SPLIT_PY}" && -f "${_SYNC_GRAPH}" ]]; then
    "$PYTHON_CMD" "${_SPLIT_PY}" "${_SYNC_GRAPH}" "${_DATA_DIR}" 2>/dev/null || true
    git -C "${_DATA_DIR}" add entities/ relationships/ 2>/dev/null || true
    if ! git -C "${_DATA_DIR}" diff --cached --quiet; then
      _ensure_git_identity "${_DATA_DIR}"
      git -C "${_DATA_DIR}" commit -m "feat: initial graph split from installer" --quiet
      git -C "${_DATA_DIR}" push origin "${_MEMBER_BRANCH}" --quiet 2>/dev/null \
        || warn "Push failed — will retry on first kg-sync.sh run"
      ok "Initial graph split pushed to ${_MEMBER_BRANCH}"
    else
      info "Branch already up to date"
    fi
  fi
fi

# Build the daemon PATH — must include Homebrew, Python, Poetry, and ~/.local/bin
# so that all scripts launched by LaunchAgents / systemd find their tools.
_DAEMON_PATH="${HOME}/.local/bin"
if [[ "$PLATFORM" == "macos" ]]; then
  _DAEMON_PATH="/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:${_DAEMON_PATH}"
fi
_PY_DIR="$(dirname "$(command -v "${PYTHON_CMD}" 2>/dev/null || echo "/usr/bin/python3")" 2>/dev/null || true)"
if [[ -n "${_PY_DIR}" && "${_PY_DIR}" != "." ]]; then
  _DAEMON_PATH="${_PY_DIR}:${_DAEMON_PATH}"
fi
if [[ -n "${POETRY_CMD:-}" ]]; then
  _POETRY_DIR="$(dirname "${POETRY_CMD}" 2>/dev/null || true)"
  if [[ -n "${_POETRY_DIR}" && "${_POETRY_DIR}" != "." ]]; then
    _DAEMON_PATH="${_POETRY_DIR}:${_DAEMON_PATH}"
  fi
fi
_DAEMON_PATH="${_DAEMON_PATH}:/usr/bin:/bin:/usr/sbin:/sbin"

# Install daemons
if [[ "$_PUSH_READY" == "1" && -n "${_MEMBER_BRANCH}" ]]; then
  if [[ "$PLATFORM" == "macos" ]]; then
    _LA_DIR="${HOME}/Library/LaunchAgents"
    mkdir -p "${_LA_DIR}"

    # kg-sync every 30 minutes
    _SYNC_PLIST="${_LA_DIR}/com.hccdaio.kg-sync.plist"
    cat > "${_SYNC_PLIST}" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>              <string>com.hccdaio.kg-sync</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${_SCRIPTS_DIR}/kg-sync.sh</string>
    </array>
    <key>EnvironmentVariables</key>
    <dict>
        <key>HCKG_DATA_DIR</key>   <string>${_DATA_DIR}</string>
        <key>HCKG_GRAPH_SRC</key>  <string>${_SYNC_GRAPH}</string>
        <key>HCKG_BRANCH</key>     <string>${_MEMBER_BRANCH}</string>
        <key>HOME</key>            <string>${HOME}</string>
        <key>PATH</key>            <string>${_DAEMON_PATH}</string>
        <key>PYTHON_CMD</key>      <string>${PYTHON_CMD}</string>
    </dict>
    <key>StartInterval</key>      <integer>1800</integer>
    <key>RunAtLoad</key>          <false/>
    <key>StandardOutPath</key>    <string>${_DATA_DIR}/.kg-sync-launchd.log</string>
    <key>StandardErrorPath</key>  <string>${_DATA_DIR}/.kg-sync-launchd.log</string>
</dict>
</plist>
PLIST

    # EOD PR at 17:00 daily
    _EOD_PLIST="${_LA_DIR}/com.hccdaio.kg-eod.plist"
    cat > "${_EOD_PLIST}" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>              <string>com.hccdaio.kg-eod</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${_SCRIPTS_DIR}/kg-eod.sh</string>
    </array>
    <key>EnvironmentVariables</key>
    <dict>
        <key>HCKG_DATA_DIR</key>   <string>${_DATA_DIR}</string>
        <key>HCKG_GRAPH_SRC</key>  <string>${_SYNC_GRAPH}</string>
        <key>HCKG_BRANCH</key>     <string>${_MEMBER_BRANCH}</string>
        <key>HOME</key>            <string>${HOME}</string>
        <key>PATH</key>            <string>${_DAEMON_PATH}</string>
        <key>PYTHON_CMD</key>      <string>${PYTHON_CMD}</string>
    </dict>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>    <integer>17</integer>
        <key>Minute</key>  <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>    <string>${_DATA_DIR}/.kg-eod-launchd.log</string>
    <key>StandardErrorPath</key>  <string>${_DATA_DIR}/.kg-eod-launchd.log</string>
</dict>
</plist>
PLIST

    # Late-night EOD PR at 23:00 — catches work done after the 5pm EOD
    # (kg-eod.sh skips creation if an open PR already exists, so no duplicate)
    _EOD_NIGHT_PLIST="${_LA_DIR}/com.hccdaio.kg-eod-night.plist"
    cat > "${_EOD_NIGHT_PLIST}" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>              <string>com.hccdaio.kg-eod-night</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${_SCRIPTS_DIR}/kg-eod.sh</string>
    </array>
    <key>EnvironmentVariables</key>
    <dict>
        <key>HCKG_DATA_DIR</key>   <string>${_DATA_DIR}</string>
        <key>HCKG_GRAPH_SRC</key>  <string>${_SYNC_GRAPH}</string>
        <key>HCKG_BRANCH</key>     <string>${_MEMBER_BRANCH}</string>
        <key>HOME</key>            <string>${HOME}</string>
        <key>PATH</key>            <string>${_DAEMON_PATH}</string>
        <key>PYTHON_CMD</key>      <string>${PYTHON_CMD}</string>
    </dict>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>    <integer>23</integer>
        <key>Minute</key>  <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>    <string>${_DATA_DIR}/.kg-eod-launchd.log</string>
    <key>StandardErrorPath</key>  <string>${_DATA_DIR}/.kg-eod-launchd.log</string>
</dict>
</plist>
PLIST

    # Morning pull at 08:00 daily
    _MORNING_PLIST="${_LA_DIR}/com.hccdaio.kg-morning.plist"
    cat > "${_MORNING_PLIST}" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>              <string>com.hccdaio.kg-morning</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${_SCRIPTS_DIR}/kg-morning.sh</string>
    </array>
    <key>EnvironmentVariables</key>
    <dict>
        <key>HCKG_DATA_DIR</key>  <string>${_DATA_DIR}</string>
        <key>HCKG_GRAPH_OUT</key> <string>${_SYNC_GRAPH}</string>
        <key>HOME</key>           <string>${HOME}</string>
        <key>PATH</key>           <string>${_DAEMON_PATH}</string>
        <key>PYTHON_CMD</key>     <string>${PYTHON_CMD}</string>
    </dict>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>    <integer>8</integer>
        <key>Minute</key>  <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>    <string>${_DATA_DIR}/.kg-morning-launchd.log</string>
    <key>StandardErrorPath</key>  <string>${_DATA_DIR}/.kg-morning-launchd.log</string>
</dict>
</plist>
PLIST

    _LAUNCHD_DOMAIN="gui/$(id -u)"
    for _plist in "${_SYNC_PLIST}" "${_EOD_PLIST}" "${_EOD_NIGHT_PLIST}" "${_MORNING_PLIST}"; do
      _label="$(basename "${_plist}" .plist)"
      launchctl bootout "${_LAUNCHD_DOMAIN}/${_label}" 2>/dev/null \
        || launchctl unload "${_plist}" 2>/dev/null || true
      if launchctl bootstrap "${_LAUNCHD_DOMAIN}" "${_plist}" 2>/dev/null; then
        info "  LaunchAgent bootstrapped: ${_label}"
      elif launchctl load "${_plist}" 2>/dev/null; then
        info "  LaunchAgent loaded (legacy): ${_label}"
      else
        warn "  Could not load ${_label} — check ${_plist}"
      fi
    done
    ok "LaunchAgents installed (sync every 30 min, EOD at 5pm + 11pm, morning pull at 8am)"

  elif [[ "$PLATFORM" == "linux" ]]; then
    _SYSTEMD_DIR="${HOME}/.config/systemd/user"
    mkdir -p "${_SYSTEMD_DIR}"

    cat > "${_SYSTEMD_DIR}/kg-sync.service" <<UNIT
[Unit]
Description=hc-cdaio-kg sync — split graph.json and push to branch

[Service]
Type=oneshot
ExecStart=/bin/bash ${_SCRIPTS_DIR}/kg-sync.sh
Environment=HCKG_DATA_DIR=${_DATA_DIR}
Environment=HCKG_GRAPH_SRC=${_SYNC_GRAPH}
Environment=HCKG_BRANCH=${_MEMBER_BRANCH}
Environment=PYTHON_CMD=${PYTHON_CMD}
Environment=PATH=${_DAEMON_PATH}
StandardOutput=append:${_DATA_DIR}/.kg-sync-systemd.log
StandardError=append:${_DATA_DIR}/.kg-sync-systemd.log
UNIT

    cat > "${_SYSTEMD_DIR}/kg-sync.timer" <<UNIT
[Unit]
Description=hc-cdaio-kg sync every 30 minutes

[Timer]
OnBootSec=5min
OnUnitActiveSec=30min
Persistent=true

[Install]
WantedBy=timers.target
UNIT

    cat > "${_SYSTEMD_DIR}/kg-eod.service" <<UNIT
[Unit]
Description=hc-cdaio-kg EOD — final sync + PR to main

[Service]
Type=oneshot
ExecStart=/bin/bash ${_SCRIPTS_DIR}/kg-eod.sh
Environment=HCKG_DATA_DIR=${_DATA_DIR}
Environment=HCKG_GRAPH_SRC=${_SYNC_GRAPH}
Environment=HCKG_BRANCH=${_MEMBER_BRANCH}
Environment=PYTHON_CMD=${PYTHON_CMD}
Environment=PATH=${_DAEMON_PATH}
StandardOutput=append:${_DATA_DIR}/.kg-eod-systemd.log
StandardError=append:${_DATA_DIR}/.kg-eod-systemd.log
UNIT

    cat > "${_SYSTEMD_DIR}/kg-eod.timer" <<UNIT
[Unit]
Description=hc-cdaio-kg EOD at 17:00 daily

[Timer]
OnCalendar=*-*-* 17:00:00
Persistent=true

[Install]
WantedBy=timers.target
UNIT

    cat > "${_SYSTEMD_DIR}/kg-eod-night.service" <<UNIT
[Unit]
Description=hc-cdaio-kg late-night EOD — catch after-hours work

[Service]
Type=oneshot
ExecStart=/bin/bash ${_SCRIPTS_DIR}/kg-eod.sh
Environment=HCKG_DATA_DIR=${_DATA_DIR}
Environment=HCKG_GRAPH_SRC=${_SYNC_GRAPH}
Environment=HCKG_BRANCH=${_MEMBER_BRANCH}
Environment=PYTHON_CMD=${PYTHON_CMD}
Environment=PATH=${_DAEMON_PATH}
StandardOutput=append:${_DATA_DIR}/.kg-eod-systemd.log
StandardError=append:${_DATA_DIR}/.kg-eod-systemd.log
UNIT

    cat > "${_SYSTEMD_DIR}/kg-eod-night.timer" <<UNIT
[Unit]
Description=hc-cdaio-kg late-night EOD at 23:00 daily

[Timer]
OnCalendar=*-*-* 23:00:00
Persistent=true

[Install]
WantedBy=timers.target
UNIT

    cat > "${_SYSTEMD_DIR}/kg-morning.service" <<UNIT
[Unit]
Description=hc-cdaio-kg morning pull — rebuild graph.json from main

[Service]
Type=oneshot
ExecStart=/bin/bash ${_SCRIPTS_DIR}/kg-morning.sh
Environment=HCKG_DATA_DIR=${_DATA_DIR}
Environment=HCKG_GRAPH_OUT=${_SYNC_GRAPH}
Environment=PYTHON_CMD=${PYTHON_CMD}
Environment=PATH=${_DAEMON_PATH}
StandardOutput=append:${_DATA_DIR}/.kg-morning-systemd.log
StandardError=append:${_DATA_DIR}/.kg-morning-systemd.log
UNIT

    cat > "${_SYSTEMD_DIR}/kg-morning.timer" <<UNIT
[Unit]
Description=hc-cdaio-kg morning pull at 08:00

[Timer]
OnCalendar=*-*-* 08:00:00
Persistent=true

[Install]
WantedBy=timers.target
UNIT

    loginctl enable-linger "$USER" 2>/dev/null \
      && info "  loginctl linger enabled for ${USER}" \
      || warn "  Could not enable loginctl linger — timers may stop at logout. Run: loginctl enable-linger ${USER}"
    systemctl --user daemon-reload 2>/dev/null \
      || warn "systemctl daemon-reload failed"
    for _svc in kg-sync kg-eod kg-eod-night kg-morning; do
      systemctl --user enable --now "${_svc}.timer" 2>/dev/null \
        && info "  systemd timer enabled: ${_svc}.timer" \
        || warn "  Could not enable ${_svc}.timer — check ~/.config/systemd/user/"
    done
    ok "systemd timers installed (sync every 30 min, EOD at 5pm + 11pm, morning pull at 8am)"
  fi

  echo ""
  info "Sync daemons active:"
  info "  8 am         : kg-morning.sh  — pull main → rebuild graph.json"
  info "                                  + catch-up PR if overnight work found"
  info "  every 30 min : kg-sync.sh     — commit + push your changes"
  info "  5 pm         : kg-eod.sh      — open PR to main"
  info "  11 pm        : kg-eod.sh      — re-check: open PR if after-hours work"
  info "                                  (skipped if 5pm PR is still open)"
  info "  Logs : ${_DATA_DIR}/.kg-*.log"

fi  # end daemon install

# ---------------------------------------------------------------------------
# [+] Claude Desktop restart
# ---------------------------------------------------------------------------
echo ""
echo -e "${BLUE}${BOLD}[+] Claude Desktop restart${RESET}"

_find_claude_pids() {
  if [[ "$PLATFORM" == "macos" ]]; then
    pgrep -x "Claude" 2>/dev/null \
      || pgrep -f "Claude Desktop" 2>/dev/null \
      || true
  else
    pgrep -f "[Cc]laude.?[Dd]esktop" 2>/dev/null \
      || pgrep -x "claude" 2>/dev/null \
      || pgrep -x "Claude" 2>/dev/null \
      || true
  fi
}

CLAUDE_PIDS="$(_find_claude_pids)"
CLAUDE_PIDS_DISPLAY="$(printf '%s' "$CLAUDE_PIDS" | tr '\n' ' ' | sed 's/ $//')"

if [[ -z "$CLAUDE_PIDS" ]]; then
  info "Claude Desktop is not running — open it manually after this script finishes."
else
  echo ""
  info "Restarting Claude Desktop to load new MCP registration..."
  info "Stopping Claude Desktop (PID: ${CLAUDE_PIDS_DISPLAY})..."
  if [[ "$PLATFORM" == "macos" ]]; then
    osascript -e 'quit app "Claude"' 2>/dev/null \
      || kill -TERM $CLAUDE_PIDS 2>/dev/null || true  # SC2086: word-split intentional
  else
    kill -TERM $CLAUDE_PIDS 2>/dev/null || true       # SC2086: word-split intentional
  fi

  _waited=0
  _start_spinner "Waiting for Claude Desktop to exit..."
  while [[ $_waited -lt 5 ]] && [[ -n "$(_find_claude_pids)" ]]; do
    sleep 1
    _waited=$((_waited + 1))
  done
  _stop_spinner

  _LIVE_PIDS="$(_find_claude_pids)"
  if [[ -n "$_LIVE_PIDS" ]]; then
    warn "Still running after ${_waited}s — force stopping..."
    kill -KILL $_LIVE_PIDS 2>/dev/null || true  # SC2086: word-split intentional
    sleep 1
  fi
  ok "Claude Desktop stopped"

  info "Relaunching Claude Desktop..."
  if [[ "$PLATFORM" == "macos" ]]; then
    open -a "Claude" 2>/dev/null \
      && ok "Claude Desktop relaunched" \
      || warn "Could not relaunch — open Claude Desktop manually."
  else
    _CLAUDE_BIN=""
    for _b in claude-desktop claude /usr/bin/claude-desktop \
               /opt/Claude/claude /usr/local/bin/claude-desktop \
               /snap/bin/claude-desktop; do
      if command -v "$_b" &>/dev/null 2>/dev/null; then
        _CLAUDE_BIN="$_b"
        break
      fi
    done
    if [[ -n "$_CLAUDE_BIN" ]]; then
      nohup "$_CLAUDE_BIN" &>/dev/null &
      disown
      ok "Claude Desktop relaunching (${_CLAUDE_BIN})"
    else
      warn "Could not find the Claude Desktop binary — open it manually."
    fi
  fi
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
SCRIPT_END=$(date +%s)
ELAPSED=$(( SCRIPT_END - SCRIPT_START ))
ELAPSED_FMT="$(printf '%dm %ds' $(( ELAPSED / 60 )) $(( ELAPSED % 60 )))"

echo ""
echo -e "${GREEN}${BOLD}╔══════════════════════════════════════════════════════╗${RESET}"
echo -e "${GREEN}${BOLD}║   Installation complete!                             ║${RESET}"
echo -e "${GREEN}${BOLD}╚══════════════════════════════════════════════════════╝${RESET}"
echo ""
echo -e "  ${DIM}Total time: ${ELAPSED_FMT}${RESET}"
echo ""
echo -e "${BOLD}How to use the knowledge graph in Claude Desktop:${RESET}"
echo ""
echo "  The graph is PRE-LOADED — Claude Desktop auto-reads it on startup."
echo "  Do NOT ask Claude to 'open', 'load', or 'read' any files."
echo "  Just ask questions directly, for example:"
echo ""
echo "    \"Show me graph statistics\""
echo "    \"Who are the top 10 most connected people?\""
echo "    \"Search for entities named Rackspace\""
echo "    \"Find the shortest path between [Entity A] and [Entity B]\""
echo "    \"What is the blast radius of the core firewall?\""
echo ""
echo -e "  ${YELLOW}Tip:${RESET} If Claude ever tries to read files instead of using the"
echo "  MCP tools, just say: \"Use the hc-enterprise-kg MCP server tools.\""
echo ""
echo -e "${BOLD}Useful commands:${RESET}"
echo "  Diagnose:      cd ${INSTALL_DIR} && poetry run hckg install doctor"
echo "  Morning pull:  bash ${_SCRIPTS_DIR}/kg-morning.sh"
echo "                 (pulls main → rebuilds graph.json — MCP auto-reloads)"
echo "  Manual sync:   bash ${_SCRIPTS_DIR}/kg-sync.sh"
echo "  Manual EOD:    bash ${_SCRIPTS_DIR}/kg-eod.sh"
echo "  Run tests:     ${PYTHON_CMD} ${_SCRIPTS_DIR}/test-mcp-integration.py"
echo ""
