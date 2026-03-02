#!/usr/bin/env python3
"""
Performance Monitoring System
Tracks timing, memory, and progress for KG analysis operations
"""

import time
import json
import psutil
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class PerformanceMonitor:
    """
    Tracks performance metrics for knowledge graph operations
    """
    
    def __init__(self, test_name: str, output_dir: str = "."):
        self.test_name = test_name
        self.output_dir = Path(output_dir)
        self.start_time = time.time()
        self.checkpoints: List[Dict[str, Any]] = []
        self.current_operation = None
        self.operation_start = None
        
    @contextmanager
    def operation(self, name: str, details: str = ""):
        """
        Context manager for timing individual operations
        
        Usage:
            with monitor.operation("load_graph", "Loading 10K entities"):
                entities, rels = load_graph(path)
        """
        self.current_operation = name
        self.operation_start = time.time()
        
        # Progress indicator
        print(f"\n[{self._timestamp()}] START: {name}")
        if details:
            print(f"  └─ {details}")
        
        # Memory before
        mem_before = psutil.Process().memory_info().rss / 1024 / 1024  # MB
        
        try:
            yield
            
            # Success metrics
            elapsed = time.time() - self.operation_start
            mem_after = psutil.Process().memory_info().rss / 1024 / 1024
            mem_delta = mem_after - mem_before
            
            checkpoint = {
                "operation": name,
                "details": details,
                "status": "SUCCESS",
                "elapsed_seconds": round(elapsed, 3),
                "memory_mb": round(mem_after, 2),
                "memory_delta_mb": round(mem_delta, 2),
                "timestamp": self._timestamp()
            }
            
            self.checkpoints.append(checkpoint)
            
            print(f"[{self._timestamp()}] DONE: {name}")
            print(f"  ├─ Time: {elapsed:.3f}s")
            print(f"  ├─ Memory: {mem_after:.1f}MB ({mem_delta:+.1f}MB)")
            print(f"  └─ Status: ✓")
            
        except Exception as e:
            # Failure metrics
            elapsed = time.time() - self.operation_start
            mem_after = psutil.Process().memory_info().rss / 1024 / 1024
            
            checkpoint = {
                "operation": name,
                "details": details,
                "status": "FAILED",
                "error": str(e),
                "elapsed_seconds": round(elapsed, 3),
                "memory_mb": round(mem_after, 2),
                "timestamp": self._timestamp()
            }
            
            self.checkpoints.append(checkpoint)
            
            print(f"[{self._timestamp()}] FAILED: {name}")
            print(f"  ├─ Time: {elapsed:.3f}s")
            print(f"  ├─ Error: {e}")
            print(f"  └─ Status: ✗")
            
            raise
    
    def checkpoint(self, name: str, metrics: Dict[str, Any] = None):
        """
        Manual checkpoint for recording metrics without timing
        
        Usage:
            monitor.checkpoint("systems_found", {"count": 150, "critical": 12})
        """
        checkpoint = {
            "checkpoint": name,
            "timestamp": self._timestamp(),
            "elapsed_from_start": round(time.time() - self.start_time, 3),
            **(metrics or {})
        }
        
        self.checkpoints.append(checkpoint)
        
        print(f"\n[{self._timestamp()}] CHECKPOINT: {name}")
        if metrics:
            for key, value in metrics.items():
                print(f"  ├─ {key}: {value}")
    
    def progress(self, current: int, total: int, item_name: str = "items"):
        """
        Show progress bar for iterative operations
        
        Usage:
            for i, system in enumerate(systems):
                monitor.progress(i+1, len(systems), "systems")
        """
        pct = (current / total) * 100
        bar_width = 40
        filled = int(bar_width * current / total)
        bar = "█" * filled + "░" * (bar_width - filled)
        
        elapsed = time.time() - self.operation_start if self.operation_start else 0
        rate = current / elapsed if elapsed > 0 else 0
        eta = (total - current) / rate if rate > 0 else 0
        
        print(f"\r  Progress: [{bar}] {pct:5.1f}% | {current}/{total} {item_name} | "
              f"{rate:.1f}/s | ETA: {eta:.1f}s", end="", flush=True)
        
        if current == total:
            print()  # New line when complete
    
    def summary(self) -> Dict[str, Any]:
        """Generate performance summary"""
        total_time = time.time() - self.start_time
        
        operations = [cp for cp in self.checkpoints if "operation" in cp]
        successful = [op for op in operations if op["status"] == "SUCCESS"]
        failed = [op for op in operations if op["status"] == "FAILED"]
        
        summary = {
            "test_name": self.test_name,
            "total_time_seconds": round(total_time, 3),
            "total_operations": len(operations),
            "successful": len(successful),
            "failed": len(failed),
            "checkpoints": self.checkpoints,
            "slowest_operations": sorted(
                successful, 
                key=lambda x: x["elapsed_seconds"], 
                reverse=True
            )[:5]
        }
        
        return summary
    
    def save_report(self):
        """Save detailed performance report to JSON"""
        summary = self.summary()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.test_name}_{timestamp}.json"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"\n{'='*60}")
        print(f"PERFORMANCE REPORT: {self.test_name}")
        print(f"{'='*60}")
        print(f"Total Time: {summary['total_time_seconds']:.3f}s")
        print(f"Operations: {summary['total_operations']} "
              f"({summary['successful']} successful, {summary['failed']} failed)")
        
        if summary['slowest_operations']:
            print(f"\nSlowest Operations:")
            for i, op in enumerate(summary['slowest_operations'], 1):
                print(f"  {i}. {op['operation']}: {op['elapsed_seconds']:.3f}s")
        
        print(f"\nFull report saved: {filepath}")
        print(f"{'='*60}\n")
        
        return filepath
    
    def _timestamp(self) -> str:
        """Current timestamp string"""
        return datetime.now().strftime("%H:%M:%S.%f")[:-3]
