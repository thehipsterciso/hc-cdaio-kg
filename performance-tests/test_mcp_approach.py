#!/usr/bin/env python3
"""
OPTION A: MCP Server Query Performance Test
Instrumented version with detailed timing
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from perf_monitor import PerformanceMonitor
import time

# This will be run via Claude's MCP tools, but with manual checkpoints

def test_mcp_queries():
    """
    Performance test for MCP server approach
    Run this by having Claude execute the MCP queries with monitoring
    """
    
    monitor = PerformanceMonitor(
        "mcp_queries", 
        "/Users/thomasjones/hc-cdaio-kg/performance-tests"
    )
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║  OPTION A: MCP SERVER QUERY APPROACH                         ║
║  Testing knowledge graph queries via MCP tools               ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    # These checkpoints will be added manually during execution
    # We'll call monitor.checkpoint() after each MCP tool call
    
    instructions = """
EXECUTION PLAN:

1. Call: get_statistics()
   Then: monitor.checkpoint("stats_complete", {...})

2. Call: find_most_connected(top_n=5)
   Then: monitor.checkpoint("top_systems_found", {"count": ...})

3. For each system (5 iterations):
   a. Call: get_neighbors(entity_id=X, direction="both")
      Then: monitor.checkpoint(f"neighbors_{i}", {"neighbor_count": ...})
   
   b. Call: get_blast_radius(entity_id=X, max_depth=2)
      Then: monitor.checkpoint(f"blast_radius_{i}", {"affected": ...})

4. Call: monitor.save_report()

MONITORING METRICS:
- Time per MCP call
- Response token size (estimated)
- Memory usage per operation
- Total conversation tokens consumed
- Delay between calls (Claude processing time)
"""
    
    print(instructions)
    return monitor

if __name__ == "__main__":
    monitor = test_mcp_queries()
    
    # Simulate for testing
    print("\n[NOTE] This script provides the monitoring framework.")
    print("[NOTE] Actual execution happens via Claude MCP tool calls.")
    print("[NOTE] Run this in interactive mode to add checkpoints manually.\n")
