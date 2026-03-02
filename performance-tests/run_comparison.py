#!/usr/bin/env python3
"""
Comparative Performance Test Runner
Runs both approaches and generates comparison report
"""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime


def run_python_test():
    """Execute the Python direct analysis test"""
    print("\n" + "="*60)
    print("RUNNING: Option B - Python Direct Analysis")
    print("="*60 + "\n")
    
    result = subprocess.run(
        [sys.executable, "test_python_approach.py"],
        cwd="/Users/thomasjones/hc-cdaio-kg/performance-tests",
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    return result.returncode == 0


def generate_comparison_report(perf_dir):
    """
    Generate comparison report from both test results
    """
    perf_path = Path(perf_dir)
    
    # Find most recent reports for each test
    python_reports = sorted(perf_path.glob("python_direct_analysis_*.json"))
    mcp_reports = sorted(perf_path.glob("mcp_queries_*.json"))
    
    if not python_reports:
        print("⚠ No Python analysis report found")
        return
    
    python_report = json.load(open(python_reports[-1]))
    
    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON REPORT")
    print("="*60 + "\n")
    
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Python results
    print("## Option B: Python Direct Analysis")
    print(f"Total Time: {python_report['total_time_seconds']:.3f}s")
    print(f"Operations: {python_report['total_operations']}")
    print(f"Success Rate: {python_report['successful']}/{python_report['total_operations']}")
    
    if python_report.get('slowest_operations'):
        print("\nSlowest Operations:")
        for i, op in enumerate(python_report['slowest_operations'][:3], 1):
            print(f"  {i}. {op['operation']}: {op['elapsed_seconds']:.3f}s")
    
    # MCP results (if available)
    if mcp_reports:
        mcp_report = json.load(open(mcp_reports[-1]))
        print("\n## Option A: MCP Server Queries")
        print(f"Total Time: {mcp_report['total_time_seconds']:.3f}s")
        print(f"Operations: {mcp_report['total_operations']}")
        print(f"Success Rate: {mcp_report['successful']}/{mcp_report['total_operations']}")
        
        # Comparison
        print("\n## Performance Delta")
        time_diff = mcp_report['total_time_seconds'] - python_report['total_time_seconds']
        pct_diff = (time_diff / python_report['total_time_seconds']) * 100
        
        if time_diff > 0:
            print(f"MCP is {abs(time_diff):.3f}s slower ({abs(pct_diff):.1f}% slower)")
        else:
            print(f"MCP is {abs(time_diff):.3f}s faster ({abs(pct_diff):.1f}% faster)")
    else:
        print("\n⚠ No MCP report available for comparison")
        print("Run MCP tests manually via Claude conversation")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    perf_dir = "/Users/thomasjones/hc-cdaio-kg/performance-tests"
    
    # Run Python test
    success = run_python_test()
    
    if not success:
        print("\n✗ Python test failed")
        sys.exit(1)
    
    # Generate comparison
    generate_comparison_report(perf_dir)
    
    print("\n📋 Next Steps:")
    print("1. Run MCP queries via Claude conversation")
    print("2. Use monitor.checkpoint() after each MCP tool call")
    print("3. Call monitor.save_report() when complete")
    print("4. Re-run this script to see full comparison\n")
