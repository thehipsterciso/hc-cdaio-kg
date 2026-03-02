# Knowledge Graph Performance Testing System

Comparative performance analysis for two approaches to querying enterprise knowledge graphs.

## Overview

Tests two methods for answering: **"What's the dependency map of critical systems?"**

- **Option A**: MCP Server Queries (via Claude conversation tools)
- **Option B**: Direct Python Analysis (file-based processing)

## Files

```
performance-tests/
├── perf_monitor.py          # Core performance monitoring framework
├── test_python_approach.py  # Option B: Direct analysis (automated)
├── test_mcp_approach.py     # Option A: MCP queries (manual execution)
├── run_comparison.py        # Comparative test runner
└── README.md                # This file
```

## Quick Start

### Option B: Run Python Analysis (Fully Automated)

```bash
cd /Users/thomasjones/hc-cdaio-kg/performance-tests
python3 test_python_approach.py
```

**Output:**
- Real-time progress indicators
- Detailed timing for each operation
- Memory usage tracking
- Final performance report (JSON)
- Analysis results (markdown)

### Option A: Run MCP Queries (Via Claude)

MCP queries must be executed through Claude conversation due to tool access requirements.

**Execution Plan:**

```python
# 1. Start monitoring
import sys
sys.path.insert(0, '/Users/thomasjones/hc-cdaio-kg/performance-tests')
from perf_monitor import PerformanceMonitor

monitor = PerformanceMonitor(
    "mcp_queries",
    "/Users/thomasjones/hc-cdaio-kg/performance-tests"
)

# 2. Execute MCP queries via Claude, adding checkpoints after each:

# Query 1
get_statistics()
monitor.checkpoint("stats_complete", {
    "entities": <count>,
    "relationships": <count>
})

# Query 2
find_most_connected(top_n=5)
monitor.checkpoint("top_systems_found", {
    "count": 5,
    "max_connections": <value>
})

# Query 3-7 (for each of 5 systems)
for i, system_id in enumerate(top_5_systems):
    get_neighbors(entity_id=system_id, direction="both")
    monitor.checkpoint(f"neighbors_{i}", {"count": <neighbor_count>})
    
    get_blast_radius(entity_id=system_id, max_depth=2)
    monitor.checkpoint(f"blast_radius_{i}", {"affected": <count>})

# 3. Save report
monitor.save_report()
```

### Generate Comparison Report

```bash
python3 run_comparison.py
```

This will:
1. Run Option B (Python) automatically
2. Look for Option A (MCP) results if available
3. Generate comparative performance report

## Performance Metrics Tracked

### Per-Operation Metrics
- **Elapsed Time**: Seconds to complete
- **Memory Delta**: MB allocated during operation
- **Status**: SUCCESS | FAILED
- **Error Details**: Exception info if failed

### Aggregate Metrics
- Total execution time
- Success/failure rates
- Slowest operations (top 5)
- Memory high-water mark

### Custom Checkpoints
- Entity/relationship counts
- Systems processed
- Blast radius sizes
- File sizes generated

## Expected Performance Characteristics

### Option A: MCP Queries
**Pros:**
- Semantic understanding
- Built-in graph algorithms
- Incremental exploration

**Cons:**
- Token overhead per query
- Unpredictable response sizes
- Multiple round trips
- Context contamination risk

**Typical Timing:**
- Statistics: ~0.5-1s
- Find connected: ~1-2s
- Get neighbors: ~1-3s per system
- Blast radius: ~2-5s per system
- **Total: 15-30s** for 5 systems

### Option B: Python Direct
**Pros:**
- Full output control
- File-based results (zero chat tokens)
- Predictable performance
- Batch processing

**Cons:**
- Manual algorithm implementation
- No type safety
- Less exploratory

**Typical Timing:**
- Load graph: ~0.1-0.5s
- Index systems: ~0.1s
- Build dep graph: ~0.5-2s
- Analyze 5 systems: ~0.5-1s
- Write results: ~0.1s
- **Total: 1-4s** for 5 systems

## Sample Output

### Console Progress
```
[14:23:45.123] START: load_graph_file
  └─ Reading /path/to/graph.json
[14:23:45.234] DONE: load_graph_file
  ├─ Time: 0.111s
  ├─ Memory: 145.3MB (+12.4MB)
  └─ Status: ✓

[14:23:45.235] CHECKPOINT: graph_loaded
  ├─ total_entities: 24567
  ├─ total_relationships: 45123
  └─ file_size_mb: 8.34
```

### JSON Report Structure
```json
{
  "test_name": "python_direct_analysis",
  "total_time_seconds": 2.456,
  "total_operations": 7,
  "successful": 7,
  "failed": 0,
  "checkpoints": [...],
  "slowest_operations": [...]
}
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'psutil'"
```bash
pip install psutil --break-system-packages
```

### MCP Queries Timing Out
- Reduce result limits (top_n=3 instead of 5)
- Skip blast_radius for initial test
- Check conversation token budget

### Memory Errors
- Reduce max_depth for blast radius
- Process systems in smaller batches
- Use file output instead of chat

## Next Steps

1. **Run baseline tests** for both approaches
2. **Compare results** to identify bottlenecks
3. **Optimize slow operations** based on profiling data
4. **Document patterns** for future queries

## Questions to Answer

After running both tests:
- Which approach is faster overall?
- Which has more predictable performance?
- Which is easier to debug when it fails?
- Which scales better with graph size?
- Which provides better error handling?
