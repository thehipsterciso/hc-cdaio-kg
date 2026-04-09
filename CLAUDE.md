# Claude Code Instructions — hc-cdaio-kg

## Commit attribution
- **Never** add `Co-Authored-By:` trailers to git commits in this repo
- Attribution is only permitted in GitHub issues and issue comments

## Knowledge Graph MCP Server
- The `hc-enterprise-kg` MCP server is pre-configured and the graph is pre-loaded. **Never** attempt to load, locate, or resolve graph file paths. The graph is already available.
- To access the graph, use the query tools directly: `get_statistics`, `list_entities`, `get_entity`, `get_neighbors`, `search_entities`, `find_shortest_path`, `get_blast_radius`, `compute_centrality`, `find_most_connected`.
- If `get_statistics` returns "No graph loaded," inform the user that the graph needs to be loaded on their end. **Do not** attempt to find or load graph files yourself.
- **Never** use Desktop Commander, Bash, Glob, or any file search tools to hunt for graph.json or any KG data files. The MCP server manages its own state.

## Interaction Style
- **Never** tell the user what to do. Do not prescribe next steps, suggest actions, or offer unsolicited recommendations. Execute what is asked. Report what happened. Stop.

## Financial Profile Population — Mandatory Preflight
These rules apply to any work that touches `financial_profile` on any entity, any `phase<N>_payload.py` or `apply_phase<N>.py` script, any statement about entity counts or phase scope, or any write to `graph.json`.
- **Before the first tool call that writes anything**, read `docs/POPULATION_PREFLIGHT.md` in full. No exceptions.
- POPULATION_PREFLIGHT defines seven mechanical gates: (1) verify scope against the real graph, (2) confirm minimum viable ask, (3) per-field reasoning not template math, (4) tier honesty, (5) NULL bar confirmation, (6) proof plan before merge, (7) document creation gate.
- On loading the checklist, state "Preflight: Gates 1–7 loaded." in the reply so the acknowledgment is explicit.
- If any gate fails, report the failure and stop. Do not work around gates.
- The gates exist because each one corresponds to a specific failure mode that has already cost Thomas time in this repo. They are not aspirational.

## General MCP Tool Usage
- When an MCP server is available, use its tools directly. Do not try to manage, configure, or troubleshoot MCP server internals.
- If an MCP tool returns an error, report it to the user. Do not attempt workarounds involving file system access unless explicitly asked.

## The CDAIO Papers — Series Content Production
These rules apply **only** when drafting posts for The CDAIO Papers series (chapters and posts defined in `docs/substack-series-bible.md`). They do not apply to other content, LinkedIn posts, or writing produced outside this series.
- **Before drafting any CDAIO Papers post**, read `docs/EDITORIAL_CONSTITUTION.md` in full. No exceptions.
- The Editorial Constitution contains pre-flight checklists, scope boundaries, consistency logs, and drift protocols. It is a living document — update it as posts are published.
- The Series Bible (`docs/substack-series-bible.md`) defines the full series architecture: 16 chapters × 3 tracks (Strategic, Operational, Technical).
- **Before voice audit**, run `python tools/voice_lint.py <draft.md>` from the hc-substack-series-cdaio workspace. Exit code 1 = FAIL = do not proceed. Hard limits: em dashes ≤ 2, tricolons ≤ 1, antithetical mirrors ≤ 2. These are mechanical gates, not guidelines.
- Every CDAIO Papers post must pass the `thomas-jones-content` skill enforcement system (voice_audit.py, Passes 1–5, Gates 1–2) before it is presented.
- After publishing or finalizing any post, update the **Series Consistency Log** and **Decision Log** in the Editorial Constitution.
- When scope drift is detected during drafting, follow Section 9 of the Editorial Constitution immediately.
