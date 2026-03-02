#!/bin/bash
# Quick Start: Run Python performance test

cd /Users/thomasjones/hc-cdaio-kg/performance-tests

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  Knowledge Graph Performance Testing System                 ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check for psutil
if ! python3 -c "import psutil" 2>/dev/null; then
    echo "⚠ Installing required dependency: psutil"
    pip install psutil --break-system-packages
    echo ""
fi

# Run Python test
echo "Running Option B: Python Direct Analysis..."
echo ""
python3 test_python_approach.py

# Show results location
echo ""
echo "📂 Results saved to:"
ls -lt *.json 2>/dev/null | head -1
echo ""
echo "📋 Next: Run MCP queries via Claude to compare approaches"
