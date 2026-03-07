# Claude Code Instructions — hc-cdaio-kg

## Commit attribution
- **Never** add `Co-Authored-By:` trailers to git commits in this repo
- Attribution is only permitted in GitHub issues and issue comments

## Knowledge Graph MCP Server
- The `hc-enterprise-kg` MCP server is pre-configured and the graph is pre-loaded. **Never** attempt to load, locate, or resolve graph file paths. The graph is already available.
- To access the graph, use the query tools directly: `get_statistics`, `list_entities`, `get_entity`, `get_neighbors`, `search_entities`, `find_shortest_path`, `get_blast_radius`, `compute_centrality`, `find_most_connected`.
- If `get_statistics` returns "No graph loaded," inform the user that the graph needs to be loaded on their end. **Do not** attempt to find or load graph files yourself.
- **Never** use Desktop Commander, Bash, Glob, or any file search tools to hunt for graph.json or any KG data files. The MCP server manages its own state.

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
