#!/usr/bin/env python3
"""Second-pass cleanup: remove financial_profile from non-financial entities
and remove remaining baggage fields from financial entities.
"""
import json
from pathlib import Path

GRAPH_PATH = Path("/Users/thomasjones/hc-cdaio-kg/graph.json")

FINANCIAL_ENTITY_TYPES = {
    "product_portfolio", "product", "organizational_unit", "department",
    "customer", "vendor", "business_capability", "initiative",
    "system", "site", "contract", "market_segment", "data_asset",
}

NON_FINANCIAL_ENTITY_TYPES = {
    "person", "role", "policy", "control", "risk", "regulation",
    "geography", "jurisdiction", "location", "network",
    "integration", "data_domain", "incident",
}

# Remaining baggage on financial entities missed by v1
REMAINING_BAGGAGE = {
    "revenue_attribution",  # Pydantic schema field on BC and OU, not enrichment
    "revenue_trend",        # On products
}


def main():
    print(f"Loading graph from {GRAPH_PATH}")
    with open(GRAPH_PATH) as f:
        graph = json.load(f)

    entities = graph.get("entities", [])
    print(f"Total entities: {len(entities)}")

    fp_removed_from_non_financial = 0
    baggage_removed = 0

    for entity in entities:
        eid = entity.get("id", "???")
        etype = entity.get("entity_type", "")

        # Remove financial_profile from non-financial entities
        if etype in NON_FINANCIAL_ENTITY_TYPES:
            if "financial_profile" in entity:
                del entity["financial_profile"]
                fp_removed_from_non_financial += 1

        # Remove remaining baggage from financial entities
        if etype in FINANCIAL_ENTITY_TYPES:
            for field in list(REMAINING_BAGGAGE):
                if field in entity:
                    del entity[field]
                    baggage_removed += 1

    # Save
    print(f"\nSaving cleaned graph to {GRAPH_PATH}")
    with open(GRAPH_PATH, "w") as f:
        json.dump(graph, f, indent=2)

    print(f"\n{'='*60}")
    print(f"V2 CLEANUP REPORT")
    print(f"{'='*60}")
    print(f"financial_profile removed from non-financial entities: {fp_removed_from_non_financial}")
    print(f"Remaining baggage fields removed: {baggage_removed}")
    print("Done.")


if __name__ == "__main__":
    main()
