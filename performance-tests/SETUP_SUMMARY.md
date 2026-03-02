# Performance Testing System - Setup Complete

## ✅ What Was Built

A comprehensive performance measurement system for comparing two approaches to knowledge graph queries:

### Core Framework
- **`perf_monitor.py`** - Performance monitoring utilities
  - Context managers for timing operations
  - Progress bars for iterative tasks
  - Memory usage tracking
  - Checkpoint system for custom metrics
  - JSON report generation

### Test Implementations

**Option A: MCP Server Queries** (`test_mcp_approach.py`)
- Framework for monitoring MCP tool calls via Claude
- Manual checkpoint insertion after each query
- Tracks: Query time, response size, token consumption

**Option B: Direct Python Analysis** (`test_python_approach.py`)
- Fully instrumented graph.json analysis
- Automated timing of all operations
- Produces both analysis results AND performance report
- Tracks: Load time, indexing, graph traversal, file I/O

### Test Runner
- **`run_comparison.py`** - Executes both tests and generates comparison
- **`quickstart.sh`** - One-command test execution

## 🎯 Instrumentation Points

### What Gets Measured

**Time:**
- Per-operation elapsed seconds
- Total test duration
- Progress rates (items/second)
- ETA calculations

**Memory:**
- RSS memory before/after each operation
- Memory deltas per operation
- Peak memory usage

**Custom Metrics:**
- Entity/relationship counts
- Systems processed
- Dependency depths
- Blast radius sizes
- File sizes

### Output Formats

**Console (Real-time):**
```
[14:23:45.123] START: load_graph_file
  └─ Reading /path/to/graph.json
[14:23:45.234] DONE: load_graph_file
  ├─ Time: 0.111s
  ├─ Memory: 145.3MB (+12.4MB)
  └─ Status: ✓
```

**JSON Report (Persistent):**
```json
{
  "test_name": "python_direct_analysis",
  "total_time_seconds": 2.456,
  "successful": 7,
  "failed": 0,
  "slowest_operations": [...]
}
```

## 🚀 How to Execute

### Quick Test (Python Only)
```bash
cd /Users/thomasjones/hc-cdaio-kg/performance-tests
./quickstart.sh
```

### Full Comparison
```bash
# 1. Run Python test
python3 test_python_approach.py

# 2. Run MCP test via Claude conversation (see README.md)
# 3. Generate comparison
python3 run_comparison.py
```

## 📊 Expected Results

### Performance Profiles

**Option A (MCP):**
- Total time: 15-30s
- Per-query overhead: 1-5s
- Token consumption: HIGH
- Risk: Context overflow

**Option B (Python):**
- Total time: 1-4s
- Overhead: Minimal
- Token consumption: ZERO (file output)
- Risk: Large file processing

### Key Metrics to Watch

1. **Total execution time** - Which is faster overall?
2. **Slowest operations** - Where are the bottlenecks?
3. **Memory usage** - Does either approach spike?
4. **Success rate** - Which handles errors better?
5. **Scalability** - What happens with 10K+ entities?

## 🔍 Debugging Features

### Verbose Timing
Both approaches support detailed timing breakdowns:
- Time to first output
- Early exit detection
- Complete event timelines

### Progress Tracking
Real-time progress bars show:
- Items processed
- Processing rate
- Estimated time remaining

### Error Capture
Failed operations include:
- Error messages
- Partial timing data
- Stack traces
- Memory at failure

## 📝 Next Steps

### Immediate
1. ✅ Run `quickstart.sh` to establish Python baseline
2. ⏳ Execute MCP queries via Claude with monitoring
3. ⏳ Compare results with `run_comparison.py`

### Analysis Questions
- Which approach handles large graphs better?
- Where does MCP spend most of its time?
- Is Python fast enough to be worth the manual work?
- Can we hybrid: MCP for exploration, Python for reporting?

### Optimization Targets
- If MCP is slow → Reduce query scope, use pagination
- If Python is slow → Profile with cProfile, optimize algorithms
- If both are slow → Graph too large, needs sampling/filtering

## 🛠 Customization

### Add Custom Metrics
```python
monitor.checkpoint("custom_metric", {
    "systems_analyzed": 150,
    "critical_paths_found": 12
})
```

### Add New Operations
```python
with monitor.operation("new_operation", "Description"):
    # Your code here
    result = do_work()
```

### Adjust Progress Updates
```python
for i in range(total):
    # Update every 100 items instead of 1000
    if i % 100 == 0:
        monitor.progress(i, total, "items")
```

## 📦 Dependencies

Required:
- `psutil` - Memory tracking
- `json` - Report generation
- Standard library: `time`, `pathlib`, `collections`

Install if missing:
```bash
pip install psutil --break-system-packages
```

## 🎓 Key Learnings Expected

After running tests, you'll know:
1. **Performance characteristics** - Actual timing data, not assumptions
2. **Bottleneck locations** - Which operations are slow
3. **Scalability limits** - Where each approach breaks down
4. **Error patterns** - What fails and why
5. **Best use cases** - When to use MCP vs Python

---

**Status:** Ready to execute
**Next Action:** Run `./quickstart.sh` for baseline Python performance
