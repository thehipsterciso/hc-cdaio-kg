#!/usr/bin/env python3
"""
Pre-commit validation for hc-cdaio-kg
Prevents low-quality commits from entering the repository
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    from rapidfuzz import fuzz
except ImportError:
    print("⚠️  Installing rapidfuzz for fuzzy matching...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rapidfuzz", "--break-system-packages", "-q"])
    from rapidfuzz import fuzz


class ValidationError(Exception):
    """Validation failure"""
    pass


class GraphValidator:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.graph_path = repo_root / "graph.json"
        
        self.errors = []
        self.warnings = []
        
    def load_graph(self) -> Dict:
        """Load the current graph"""
        if not self.graph_path.exists():
            raise ValidationError("graph.json not found")
        
        with open(self.graph_path) as f:
            return json.load(f)
    
    def validate_schema(self, graph: Dict) -> bool:
        """Check basic graph structure"""
        if "entities" not in graph:
            self.errors.append("Missing 'entities' key in graph.json")
            return False
        
        if "relationships" not in graph:
            self.errors.append("Missing 'relationships' key in graph.json")
            return False
        
        return True
    
    def validate_required_fields(self, graph: Dict) -> bool:
        """Check required fields per entity"""
        missing = []
        
        for entity in graph["entities"]:
            eid = entity.get("id")
            if not eid:
                missing.append("Entity missing 'id' field")
                continue
            
            if not entity.get("name"):
                missing.append(f"{eid}: missing 'name'")
            
            if not entity.get("entity_type"):
                missing.append(f"{eid}: missing 'entity_type'")
        
        if missing:
            self.errors.append(f"Required fields missing for {len(missing)} entities:")
            for item in missing[:10]:
                self.errors.append(f"  - {item}")
            if len(missing) > 10:
                self.errors.append(f"  ... and {len(missing) - 10} more")
            return False
        
        return True
    
    def validate_relationships(self, graph: Dict) -> bool:
        """Check relationship integrity"""
        entity_ids = {e["id"] for e in graph["entities"]}
        dangling = []
        
        for rel in graph["relationships"]:
            rid = rel.get("id", "unknown")
            source = rel.get("source_id")
            target = rel.get("target_id")
            
            if source not in entity_ids:
                dangling.append(f"{rid}: source_id '{source}' does not exist")
            
            if target not in entity_ids:
                dangling.append(f"{rid}: target_id '{target}' does not exist")
        
        if dangling:
            self.errors.append(f"Found {len(dangling)} dangling relationships:")
            for item in dangling[:10]:
                self.errors.append(f"  - {item}")
            if len(dangling) > 10:
                self.errors.append(f"  ... and {len(dangling) - 10} more")
            return False
        
        return True
    
    def check_provenance(self, graph: Dict) -> bool:
        """Validate provenance completeness - WARNING ONLY"""
        incomplete = []
        
        for entity in graph["entities"]:
            eid = entity.get("id", "unknown")
            prov = entity.get("provenance", {})
            
            if not prov.get("primary_data_source"):
                incomplete.append(f"{eid}: missing primary_data_source")
            
            if not prov.get("assessed_by"):
                incomplete.append(f"{eid}: missing assessed_by")
            
            if not prov.get("last_assessed_date"):
                incomplete.append(f"{eid}: missing last_assessed_date")
        
        if incomplete:
            self.warnings.append(f"⚠️  Provenance incomplete for {len(incomplete)} entities")
            self.warnings.append(f"   Goal: Reach 100% provenance coverage over time")
        
        return True
    
    def find_duplicates(self, graph: Dict, threshold: float = 0.85) -> List[Tuple]:
        """Find potential duplicate entities using fuzzy matching"""
        duplicates = []
        entities = graph["entities"]
        
        # Group by entity_type for faster comparison
        by_type = {}
        for entity in entities:
            etype = entity.get("entity_type", "unknown")
            if etype not in by_type:
                by_type[etype] = []
            by_type[etype].append(entity)
        
        # Check within each type
        for etype, entity_list in by_type.items():
            for i, e1 in enumerate(entity_list):
                for e2 in entity_list[i+1:]:
                    name1 = e1.get("name", "")
                    name2 = e2.get("name", "")
                    
                    if not name1 or not name2:
                        continue
                    
                    similarity = fuzz.ratio(name1.lower(), name2.lower()) / 100.0
                    
                    if similarity >= threshold:
                        duplicates.append((
                            e1.get("id"),
                            e2.get("id"),
                            name1,
                            name2,
                            similarity
                        ))
        
        if duplicates:
            self.warnings.append(f"Found {len(duplicates)} potential duplicates (≥{threshold*100}% similar):")
            for eid1, eid2, n1, n2, score in duplicates[:5]:
                self.warnings.append(f"  - {eid1} '{n1}' ↔ {eid2} '{n2}' ({score:.0%})")
            if len(duplicates) > 5:
                self.warnings.append(f"  ... and {len(duplicates) - 5} more")
        
        return duplicates
    
    def run_all_checks(self) -> bool:
        """Run full validation suite"""
        print("🔍 Running graph validation...")
        
        try:
            graph = self.load_graph()
        except Exception as e:
            self.errors.append(f"Failed to load graph: {e}")
            return False
        
        passed = True
        
        # Critical checks (must pass)
        print("  → Validating schema...")
        if not self.validate_schema(graph):
            passed = False
        
        print("  → Validating required fields...")
        if not self.validate_required_fields(graph):
            passed = False
        
        print("  → Checking relationship integrity...")
        if not self.validate_relationships(graph):
            passed = False
        
        print("  → Validating provenance...")
        self.check_provenance(graph)
        
        # Warning checks (informational)
        print("  → Detecting duplicates...")
        self.find_duplicates(graph, threshold=0.85)
        
        return passed
    
    def print_results(self):
        """Print validation results"""
        if self.errors:
            print("\n❌ VALIDATION FAILED")
            print("\nErrors:")
            for error in self.errors:
                print(f"  {error}")
        
        if self.warnings:
            print("\n⚠️  Warnings:")
            for warning in self.warnings:
                print(f"  {warning}")
        
        if not self.errors and not self.warnings:
            print("\n✅ All validation checks passed")


def main():
    """Main validation entry point"""
    repo_root = Path(__file__).parent.parent.parent
    
    validator = GraphValidator(repo_root)
    passed = validator.run_all_checks()
    validator.print_results()
    
    if not passed:
        print("\n💡 Fix these issues before committing")
        print("   See CONTRIBUTING.md for guidelines")
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
