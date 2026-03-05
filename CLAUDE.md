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
