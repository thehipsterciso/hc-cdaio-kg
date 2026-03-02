#!/usr/bin/env python3
"""
OPTION B: Direct graph.json Analysis Performance Test
Fully instrumented Python analysis with timing
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from perf_monitor import PerformanceMonitor
import json
from collections import defaultdict, Counter
from pathlib import Path


def load_graph(path):
    """Load and validate graph structure"""
    with open(path) as f:
        data = json.load(f)
    return data['entities'], data['relationships']


def calculate_blast_radius(start_id, relationships, systems, max_depth=2):
    """BFS to find all reachable systems within max_depth hops"""
    visited = {start_id}
    current_level = {start_id}
    
    for depth in range(max_depth):
        next_level = set()
        for node in current_level:
            for rel in relationships:
                if rel['source_id'] == node and rel['target_id'] in systems:
                    next_level.add(rel['target_id'])
                elif rel['target_id'] == node and rel['source_id'] in systems:
                    next_level.add(rel['source_id'])
        
        next_level -= visited
        visited.update(next_level)
        current_level = next_level
        
        if not current_level:
            break
    
    return visited - {start_id}


def analyze_dependencies(graph_path, monitor):
    """
    Main analysis with full performance instrumentation
    """
    
    output_path = Path(graph_path).parent / "performance-tests" / "dependency_analysis.md"
    
    # OPERATION 1: Load graph
    with monitor.operation("load_graph_file", f"Reading {graph_path}"):
        entities, relationships = load_graph(graph_path)
    
    monitor.checkpoint("graph_loaded", {
        "total_entities": len(entities),
        "total_relationships": len(relationships),
        "file_size_mb": round(Path(graph_path).stat().st_size / 1024 / 1024, 2)
    })
    
    # OPERATION 2: Index systems
    with monitor.operation("index_systems", "Building system index"):
        systems = {e['id']: e for e in entities if e['entity_type'] == 'system'}
    
    monitor.checkpoint("systems_indexed", {
        "system_count": len(systems),
        "pct_of_total": round(len(systems) / len(entities) * 100, 1)
    })
    
    # OPERATION 3: Build dependency graph
    with monitor.operation("build_dependency_graph", "Analyzing relationships"):
        depends_on = defaultdict(list)
        depended_by = defaultdict(list)
        all_connections = Counter()
        
        rel_count = len(relationships)
        for idx, rel in enumerate(relationships):
            if idx % 1000 == 0:
                monitor.progress(idx, rel_count, "relationships")
            
            src, tgt = rel['source_id'], rel['target_id']
            rel_type = rel['relationship_type']
            
            if src in systems:
                all_connections[src] += 1
            if tgt in systems:
                all_connections[tgt] += 1
            
            if rel_type == 'depends_on':
                if src in systems and tgt in systems:
                    depends_on[src].append((tgt, systems[tgt]['name']))
                    depended_by[tgt].append((src, systems[src]['name']))
        
        monitor.progress(rel_count, rel_count, "relationships")
    
    monitor.checkpoint("dependency_graph_built", {
        "systems_with_dependencies": len(depends_on),
        "systems_with_dependents": len(depended_by),
        "max_connections": all_connections.most_common(1)[0][1] if all_connections else 0
    })
    
    # OPERATION 4: Write analysis to file
    with monitor.operation("write_analysis_file", f"Writing to {output_path}"):
        with open(output_path, 'w') as out:
            out.write("# Critical System Dependency Analysis\n\n")
            out.write(f"Total Systems: {len(systems)}\n")
            out.write(f"Total Relationships: {len(relationships)}\n\n")
            
            # Top 5 most connected
            out.write("## Top 5 Most Connected Systems\n\n")
            
            top_5 = all_connections.most_common(5)
            
            for rank, (sys_id, conn_count) in enumerate(top_5, 1):
                # OPERATION 5.x: Analyze each top system
                with monitor.operation(f"analyze_system_{rank}", f"System: {systems[sys_id]['name']}"):
                    system = systems[sys_id]
                    
                    out.write(f"### {rank}. {system['name']}\n")
                    out.write(f"- **Total Connections**: {conn_count}\n")
                    out.write(f"- **Status**: {system.get('status', 'Unknown')}\n")
                    
                    # Dependencies
                    deps = depends_on.get(sys_id, [])
                    out.write(f"- **Dependencies** ({len(deps)}): ")
                    if deps:
                        dep_names = [name for _, name in deps[:5]]
                        out.write(", ".join(dep_names))
                        if len(deps) > 5:
                            out.write(f" ...and {len(deps)-5} more")
                    else:
                        out.write("None")
                    out.write("\n")
                    
                    # Dependents
                    dependents = depended_by.get(sys_id, [])
                    out.write(f"- **Dependents** ({len(dependents)}): ")
                    if dependents:
                        dep_names = [name for _, name in dependents[:5]]
                        out.write(", ".join(dep_names))
                        if len(dependents) > 5:
                            out.write(f" ...and {len(dependents)-5} more")
                    else:
                        out.write("None")
                    out.write("\n")
                    
                    # Blast radius
                    blast = calculate_blast_radius(sys_id, relationships, systems, max_depth=2)
                    out.write(f"- **Blast Radius (2 hops)**: {len(blast)} systems\n\n")
                    
                    monitor.checkpoint(f"system_{rank}_complete", {
                        "name": system['name'],
                        "connections": conn_count,
                        "dependencies": len(deps),
                        "dependents": len(dependents),
                        "blast_radius": len(blast)
                    })
            
            # Single points of failure
            out.write("\n## Potential Single Points of Failure\n\n")
            spof_candidates = [
                (sys_id, len(depended_by[sys_id])) 
                for sys_id in systems 
                if len(depended_by[sys_id]) >= 5
            ]
            spof_candidates.sort(key=lambda x: x[1], reverse=True)
            
            for sys_id, dependent_count in spof_candidates[:10]:
                system = systems[sys_id]
                out.write(f"- **{system['name']}**: {dependent_count} systems depend on this\n")
    
    monitor.checkpoint("analysis_written", {
        "output_file": str(output_path),
        "file_size_kb": round(output_path.stat().st_size / 1024, 2)
    })
    
    return output_path


def main():
    """Run the instrumented Python analysis"""
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║  OPTION B: DIRECT PYTHON ANALYSIS                            ║
║  Testing knowledge graph analysis via direct file access     ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    graph_path = "/Users/thomasjones/hc-cdaio-kg/graph.json"
    
    monitor = PerformanceMonitor(
        "python_direct_analysis",
        "/Users/thomasjones/hc-cdaio-kg/performance-tests"
    )
    
    try:
        output_path = analyze_dependencies(graph_path, monitor)
        print(f"\n✓ Analysis complete: {output_path}")
        
    except Exception as e:
        print(f"\n✗ Analysis failed: {e}")
        raise
    finally:
        report_path = monitor.save_report()
        print(f"📊 Performance report: {report_path}")


if __name__ == "__main__":
    main()
