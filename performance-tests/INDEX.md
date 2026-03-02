# Knowledge Graph Performance Testing System
## Complete Setup - Ready to Execute

---

## 📁 File Structure

```
performance-tests/
├── INDEX.md                    ← You are here (start here!)
├── SETUP_SUMMARY.md            ← What was built and why
├── README.md                   ← Detailed usage guide
├── DECISION_MATRIX.md          ← How to interpret results
│
├── perf_monitor.py             ← Core performance framework
├── test_python_approach.py     ← Option B test (automated)
├── test_mcp_approach.py        ← Option A test (manual)
├── run_comparison.py           ← Comparative runner
└── quickstart.sh               ← One-command execution
```

---

## 🚀 Quick Start (30 seconds)

```bash
cd /Users/thomasjones/hc-cdaio-kg/performance-tests
./quickstart.sh
```

This will:
1. Check dependencies (install psutil if needed)
2. Run Python performance test
3. Generate timing report
4. Create dependency analysis

**Expected output:** JSON report + markdown analysis in 1-5 seconds

---

## 📖 Read First

**New to this system?** Start here:
1. **SETUP_SUMMARY.md** - Understand what was built (5 min read)
2. **README.md** - Learn how to run tests (10 min read)
3. **Run the tests** - Execute and observe
4. **DECISION_MATRIX.md** - Interpret your results (5 min read)

**Already familiar?** Jump to execution:
- Python test: `python3 test_python_approach.py`
- Full comparison: `python3 run_comparison.py`

---

## 🎯 The Core Question

**"What's the dependency map of critical systems?"**

Two approaches to answer this:

### Option A: MCP Server Queries
- Natural language via Claude conversation
- Uses `hc-enterprise-kg` MCP tools
- ~15-30 seconds expected
- Token consumption: HIGH
- Manual execution required

### Option B: Direct Python Analysis
- File-based graph.json processing
- Automated timing and reporting
- ~1-4 seconds expected
- Token consumption: ZERO
- Fully scriptable

**Goal:** Measure both, compare results, choose wisely for future queries.

---

## ⚡ Performance Tracking

### What Gets Measured

**Time:**
- Per-operation elapsed seconds
- Total test duration
- Processing rates
- Progress indicators

**Memory:**
- RSS before/after operations
- Memory deltas
- Peak usage

**Custom Metrics:**
- Entity counts
- Relationship processing
- Systems analyzed
- Blast radius calculations
- File I/O

### Where Results Go

**Console:** Real-time progress + summary
**JSON:** `{test_name}_{timestamp}.json` - Complete metrics
**Markdown:** `dependency_analysis.md` - Human-readable results

---

## 📊 Expected Performance

| Metric | Option A (MCP) | Option B (Python) |
|--------|----------------|-------------------|
| Total Time | 15-30s | 1-4s |
| Per-query | 1-5s | N/A (batch) |
| Token Cost | HIGH | ZERO |
| Scalability | Limited | High |
| Flexibility | Excellent | Manual |

**Note:** These are estimates. Your actual results will vary based on graph size.

---

## 🔍 Execution Paths

### Path 1: Quick Python Baseline
```bash
./quickstart.sh
```
**Time:** 30 seconds
**Output:** Python performance report
**Next:** Review results, decide if MCP test needed

### Path 2: Full Comparison
```bash
# Step 1: Python (automated)
python3 test_python_approach.py

# Step 2: MCP (via Claude conversation)
# See README.md for detailed MCP execution plan

# Step 3: Compare results
python3 run_comparison.py
```
**Time:** 5-10 minutes
**Output:** Comparative performance analysis
**Next:** Use DECISION_MATRIX.md to choose approach

### Path 3: Custom Analysis
```python
from perf_monitor import PerformanceMonitor

monitor = PerformanceMonitor("my_test", ".")

with monitor.operation("custom_work"):
    # Your code here
    pass

monitor.save_report()
```

---

## 🛠 Key Components

### `perf_monitor.py`
Core monitoring framework. Features:
- `operation()` context manager for timing
- `checkpoint()` for custom metrics
- `progress()` for visual feedback
- `save_report()` for JSON output

### `test_python_approach.py`
Fully instrumented graph analysis:
- Loads graph.json
- Indexes systems
- Builds dependency graph
- Analyzes top 5 connected systems
- Calculates blast radii
- Writes markdown report
- Generates performance JSON

### `test_mcp_approach.py`
Framework for MCP monitoring:
- Execution plan template
- Checkpoint insertion points
- Manual timing workflow
- Comparable to Python test

### `run_comparison.py`
Orchestrates both tests:
- Runs Python automatically
- Loads MCP results if available
- Generates comparison report
- Highlights performance delta

---

## 🎓 What You'll Learn

### After Running Tests

**Performance Characteristics:**
- Which approach is actually faster?
- Where does time get spent?
- What causes slowdowns?

**Resource Usage:**
- Memory requirements
- Token consumption
- I/O patterns

**Scalability:**
- How does each handle large graphs?
- At what size does each break down?
- What are the hard limits?

**Use Case Fit:**
- When to use MCP?
- When to use Python?
- When to combine both?

---

## 📋 Checklist

### Before Running
- [ ] Graph file exists at `/Users/thomasjones/hc-cdaio-kg/graph.json`
- [ ] Python 3 installed
- [ ] `psutil` available (or will auto-install)

### First Run
- [ ] Execute `./quickstart.sh`
- [ ] Review console output
- [ ] Check JSON report exists
- [ ] Verify dependency_analysis.md created

### Optional: MCP Test
- [ ] Read MCP execution plan in README.md
- [ ] Run queries via Claude conversation
- [ ] Add checkpoints after each query
- [ ] Save MCP performance report

### Analysis
- [ ] Run `python3 run_comparison.py`
- [ ] Review comparative results
- [ ] Read DECISION_MATRIX.md
- [ ] Choose approach for future work

---

## 🆘 Troubleshooting

### Test Fails to Run
**Error:** `ModuleNotFoundError: No module named 'psutil'`
**Fix:** `pip install psutil --break-system-packages`

**Error:** `FileNotFoundError: graph.json`
**Fix:** Verify graph file path in test script

### Slow Performance
**Symptom:** Python test takes >10s
**Check:** Graph file size (should be <50MB for fast performance)
**Action:** Consider sampling or filtering

### Memory Errors
**Symptom:** Process killed during execution
**Check:** Available system memory
**Action:** Reduce max_depth or batch size

---

## 📞 Next Steps

### Immediate
1. ✅ Review this INDEX
2. ⏳ Run `./quickstart.sh`
3. ⏳ Examine results

### Follow-up
4. ⏳ Read DECISION_MATRIX.md
5. ⏳ Decide on MCP test necessity
6. ⏳ Document findings for future reference

### Advanced
7. ⏳ Optimize slow operations
8. ⏳ Build custom analysis scripts
9. ⏳ Integrate with workflows

---

## 🎯 Success Criteria

You'll know this system is working when:
- ✅ Python test completes in 1-5 seconds
- ✅ JSON report contains detailed timings
- ✅ Dependency analysis is readable and accurate
- ✅ You can explain which approach to use when
- ✅ Performance bottlenecks are identified

---

**Status:** ✅ Setup Complete
**Action:** Run `./quickstart.sh` to begin testing
**Documentation:** All files in this directory
