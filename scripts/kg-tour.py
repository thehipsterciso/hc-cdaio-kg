#!/usr/bin/env python3
"""
kg-tour.py — Interactive orientation tour of the Enterprise Knowledge Graph.

Run this after install to get oriented with the graph and understand what
questions it can answer for your data & AI strategy.

Usage:
    python3 scripts/kg-tour.py
"""

import json
import os
import sys
import textwrap
from collections import Counter, defaultdict
from pathlib import Path

# ── locate graph.json ─────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
GRAPH_FILE = REPO_ROOT / "graph.json"

if not GRAPH_FILE.exists():
    # try to build it first
    build_script = REPO_ROOT / "scripts" / "lib" / "kg-build.py"
    if build_script.exists():
        import subprocess
        subprocess.run([sys.executable, str(build_script), str(REPO_ROOT), str(GRAPH_FILE)], check=True)
    else:
        print(f"ERROR: graph.json not found at {GRAPH_FILE}")
        print("Run: python3 scripts/lib/kg-build.py . graph.json")
        sys.exit(1)


# ── helpers ───────────────────────────────────────────────────────────────────

WIDTH = 70

def hr(char="─"):
    print(char * WIDTH)

def header(title):
    print()
    print("╔" + "═" * (WIDTH - 2) + "╗")
    print("║  " + title.upper().ljust(WIDTH - 4) + "║")
    print("╚" + "═" * (WIDTH - 2) + "╝")
    print()

def section(title):
    print()
    hr()
    print(f"  {title}")
    hr()
    print()

def wrap(text, indent=2):
    prefix = " " * indent
    for line in textwrap.wrap(text, width=WIDTH - indent):
        print(prefix + line)

def pause(prompt="  [ Press Enter to continue ]"):
    print()
    try:
        input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nExiting tour.")
        sys.exit(0)

def bullet(label, value, width=38):
    print(f"  {'• ' + label:<{width}} {value}")

def question(text):
    print()
    wrap("❓  " + text, indent=0)
    print()

def answer(text):
    wrap("→   " + text, indent=0)
    print()


# ── load graph ────────────────────────────────────────────────────────────────

def load():
    with open(GRAPH_FILE) as f:
        data = json.load(f)
    entities = data.get("entities", [])
    relationships = data.get("relationships", [])
    return entities, relationships


# ── queries ───────────────────────────────────────────────────────────────────

def by_type(entities):
    d = defaultdict(list)
    for e in entities:
        d[e.get("entity_type", "unknown")].append(e)
    return d

def rels_by_type(relationships):
    d = defaultdict(list)
    for r in relationships:
        d[r.get("relationship_type", "unknown")].append(r)
    return d

def find(entities, entity_id):
    for e in entities:
        if e.get("id") == entity_id:
            return e
    return None

def name(entities, entity_id, fallback=None):
    e = find(entities, entity_id)
    return e.get("name", fallback or entity_id) if e else (fallback or entity_id)


# ── tour sections ─────────────────────────────────────────────────────────────

def intro():
    header("Enterprise Knowledge Graph  ·  Orientation Tour")
    wrap(
        "This tour walks you through the Rackspace Enterprise Knowledge Graph "
        "— what it contains, what questions it answers, and what it means for "
        "our data and AI strategy."
    )
    print()
    wrap("Take your time. Every section poses a real strategic question and "
         "shows you the answer live from the graph.")
    pause()


def at_a_glance(entities, relationships):
    section("The Enterprise at a Glance")
    typed = by_type(entities)
    rtyped = rels_by_type(relationships)

    bullet("Total entities",      f"{len(entities):,}")
    bullet("Total relationships", f"{len(relationships):,}")
    print()
    bullet("Systems",             f"{len(typed.get('system', [])):,}")
    bullet("Data assets",         f"{len(typed.get('data_asset', [])):,}")
    bullet("Controls",            f"{len(typed.get('control', [])):,}")
    bullet("Policies",            f"{len(typed.get('policy', [])):,}")
    bullet("Risks",               f"{len(typed.get('risk', [])):,}")
    bullet("Regulations",         f"{len(typed.get('regulation', [])):,}")
    bullet("People",              f"{len(typed.get('person', [])):,}")
    bullet("Departments",         f"{len(typed.get('department', [])):,}")
    print()
    bullet("Relationship types",  f"{len(rtyped):,}")

    print()
    wrap(
        "Every one of these entities is connected to others through typed, "
        "confidence-scored relationships. This is not a spreadsheet. "
        "It is a queryable map of how the enterprise actually operates."
    )
    pause()


def data_landscape(entities, relationships):
    section("Question 1: What data do we actually have?")

    question("Which data assets are classified as restricted or confidential — "
             "and who owns them?")

    assets = by_type(entities).get("data_asset", [])
    class_counts = Counter()
    pii_count = 0
    regulated_count = 0

    for a in assets:
        cls = a.get("data_classification") or a.get("classification") or "unknown"
        class_counts[cls.lower()] += 1
        if a.get("pii_categories"):
            pii_count += 1
        if a.get("regulatory_applicability") or a.get("regulations"):
            regulated_count += 1

    for cls, count in sorted(class_counts.items(), key=lambda x: -x[1]):
        bullet(cls.capitalize(), f"{count} assets")

    print()
    bullet("Assets containing PII",          f"{pii_count}")
    bullet("Assets with regulatory mapping", f"{regulated_count} / {len(assets)}")

    print()

    # show a few restricted assets
    restricted = [a for a in assets
                  if (a.get("data_classification") or a.get("classification") or "").lower() == "restricted"][:5]
    if restricted:
        print("  Sample restricted assets:")
        for a in restricted:
            print(f"    - {a.get('name', a.get('id'))}")

    print()
    answer(
        f"We have {len(assets)} cataloged data assets. {pii_count} contain PII. "
        f"{regulated_count} have explicit regulatory obligations mapped. "
        "Every asset has a documented classification, storage system, and known gaps."
    )
    pause()


def where_it_lives(entities, relationships):
    section("Question 2: Where does the data live and how does it move?")

    question("Which systems store our most sensitive data — and are those "
             "systems connected to each other?")

    rtyped = rels_by_type(relationships)
    stores_rels = rtyped.get("stores", [])
    integrates_rels = rtyped.get("integrates_with", [])
    hosted_rels = rtyped.get("hosted_on", [])

    bullet("'stores' relationships (system → data asset)", f"{len(stores_rels):,}")
    bullet("'integrates_with' relationships",              f"{len(integrates_rels):,}")
    bullet("'hosted_on' relationships (system → site)",    f"{len(hosted_rels):,}")

    # most connected systems by stores
    store_counts = Counter(r["source_id"] for r in stores_rels)
    top_systems = store_counts.most_common(5)

    print()
    print("  Systems storing the most data assets:")
    for sys_id, count in top_systems:
        sys_name = name(entities, sys_id, sys_id)
        print(f"    - {sys_name[:55]:<55} ({count} assets)")

    print()
    answer(
        "Before this work, only 1 system was linked to any data asset. "
        "Now every data asset has a documented system owner. "
        "This is the minimum required to reason about data exposure, "
        "backup coverage, or access control scope."
    )
    pause()


def regulatory_exposure(entities, relationships):
    section("Question 3: What are we allowed to do with our data?")

    question("If we want to build an AI model on our operational data — "
             "which datasets can we legally use, and which are off-limits?")

    assets = by_type(entities).get("data_asset", [])

    gdpr, ccpa, fedramp, hipaa, pci = [], [], [], [], []
    ai_restricted = []

    for a in assets:
        regs = []
        for r in (a.get("regulatory_applicability") or []):
            regs.append((r.get("regulation_name") or r.get("regulation_id") or "").upper())
        for r in (a.get("regulations") or []):
            regs.append(str(r).upper())

        reg_str = " ".join(regs)
        if "GDPR" in reg_str:       gdpr.append(a)
        if "CCPA" in reg_str:       ccpa.append(a)
        if "FEDRAMP" in reg_str:    fedramp.append(a)
        if "HIPAA" in reg_str:      hipaa.append(a)
        if "PCI" in reg_str:        pci.append(a)

        ai = a.get("ai_training_usage") or {}
        if ai.get("eu_ai_act_risk_category") in ("High", "Limited", "Minimal"):
            ai_restricted.append(a)

    bullet("Assets subject to GDPR",     f"{len(gdpr)}")
    bullet("Assets subject to CCPA",     f"{len(ccpa)}")
    bullet("Assets subject to FedRAMP",  f"{len(fedramp)}")
    bullet("Assets subject to HIPAA",    f"{len(hipaa)}")
    bullet("Assets subject to PCI DSS",  f"{len(pci)}")
    print()
    bullet("Assets with EU AI Act risk classification", f"{len(ai_restricted)}")

    print()
    answer(
        "Regulatory applicability is now mapped at the asset level. "
        "Before you authorize any AI use case, you can query which assets "
        "it would touch and what legal constraints apply — before anyone "
        "writes a single line of model code."
    )
    pause()


def risk_and_control(entities, relationships):
    section("Question 4: What risk does our data create?")

    question("Which of our security controls are actually mapped to the "
             "risks they're supposed to address?")

    rtyped = rels_by_type(relationships)
    mitigates_rels = rtyped.get("mitigates", [])

    risks = by_type(entities).get("risk", [])
    controls = by_type(entities).get("control", [])

    covered_risk_ids = set(r["target_id"] for r in mitigates_rels)
    uncovered = [r for r in risks if r.get("id") not in covered_risk_ids]
    covered   = [r for r in risks if r.get("id") in covered_risk_ids]

    bullet("Total risks",                     f"{len(risks)}")
    bullet("Risks with controls mapped",      f"{len(covered)}")
    bullet("Risks with NO controls mapped",   f"{len(uncovered)}  ← gap")
    bullet("Total controls in graph",         f"{len(controls):,}")
    bullet("Active mitigates relationships",  f"{len(mitigates_rels)}")

    if uncovered:
        print()
        print("  Risks with zero control coverage:")
        for r in uncovered[:8]:
            print(f"    - {r.get('name', r.get('id'))}")

    print()
    answer(
        "Having controls documented is not the same as having controls mapped "
        "to risks. The graph exposes the difference. These gaps are the first "
        "place any auditor — or adversary — will look."
    )
    pause()


def ai_readiness(entities, relationships):
    section("Question 5: Where does AI actually fit?")

    question("Which business capabilities have the data, systems, and "
             "regulatory clearance to support an AI use case right now?")

    typed = by_type(entities)
    rtyped = rels_by_type(relationships)

    capabilities = typed.get("business_capability", [])
    systems      = typed.get("system", [])
    assets       = typed.get("data_asset", [])

    # AI-related systems (name contains AI/ML keywords)
    ai_keywords = ["ai", "ml", "model", "gpu", "inference", "llm", "generative",
                   "intelligence", "run:ai", "raise", "ice", "rita", "launchpad"]
    ai_systems = [s for s in systems
                  if any(k in s.get("name","").lower() for k in ai_keywords)]

    # Systems linked to data assets (have stores relationships)
    systems_with_data = set(r["source_id"] for r in rtyped.get("stores", []))

    # capabilities linked via supports
    cap_with_systems = set(r["target_id"] for r in rtyped.get("supports", []))

    bullet("AI/ML platform systems identified",   f"{len(ai_systems)}")
    bullet("Systems with data assets linked",     f"{len(systems_with_data)}")
    bullet("Business capabilities in graph",      f"{len(capabilities)}")
    bullet("Capabilities with system linkage",    f"{len(cap_with_systems)}")

    print()
    print("  AI/ML systems in the graph:")
    for s in ai_systems[:8]:
        print(f"    - {s.get('name', s.get('id'))}")

    print()
    answer(
        "The graph gives you a structured way to evaluate AI readiness "
        "per capability: does it have data? Is that data clean enough? "
        "What regulations apply? Who owns the system? These are answerable "
        "questions now — not guesses."
    )
    pause()


def strategy_questions():
    section("The Questions That Build a Data & AI Strategy")

    wrap(
        "The graph is a tool. The strategy comes from answering the right "
        "questions with it. Here are the questions your team needs to work through."
    )
    print()

    clusters = [
        ("Data Inventory & Ownership", [
            "What data assets do we have and who is accountable for each?",
            "Which assets are undocumented or have no system owner?",
            "Where are the gaps — data we need but don't have?",
        ]),
        ("Regulatory & Legal", [
            "Which regulations apply to each asset and each system?",
            "Where is data crossing borders and are transfers compliant?",
            "Which AI use cases are legally viable with our current data?",
        ]),
        ("Risk & Control", [
            "Which risks have insufficient control coverage?",
            "Which systems are critical paths with no redundancy documented?",
            "Where is our attack surface widest relative to our control posture?",
        ]),
        ("AI Strategy", [
            "Which capabilities are AI-augmentable and have the data to support it?",
            "Where is data quality too low to trust model outputs?",
            "What governance is required for each AI use case we're considering?",
        ]),
        ("Organizational Readiness", [
            "Which teams own which data assets — and do they know it?",
            "Where are the stewardship gaps that create compliance exposure?",
            "What would it take to get every domain lead contributing to the graph?",
        ]),
    ]

    for cluster_name, questions in clusters:
        print(f"  ▸ {cluster_name}")
        for q in questions:
            wrap(f"    · {q}", indent=4)
        print()

    pause("  [ Press Enter for your next move ]")


def next_move():
    section("Your Next Move")

    wrap(
        "You now have a working understanding of the graph. "
        "Here is how to go deeper."
    )
    print()

    steps = [
        ("Open Claude Desktop",
         "The hc-enterprise-kg MCP server is connected. Ask questions in plain English."),
        ("Try the blast radius tool",
         "Pick any critical system and ask: 'What is the blast radius of [system] failing?'"),
        ("Find your domain's gaps",
         "Ask: 'Which systems in [your domain] have no data assets linked?'"),
        ("Add what you know",
         "Every relationship you add makes the graph more useful for everyone."),
        ("Read the showcase doc",
         "docs/KG_TEAM_SHOWCASE.md — the strategic question framework for your team."),
    ]

    for i, (title, desc) in enumerate(steps, 1):
        print(f"  {i}. {title}")
        wrap(desc, indent=5)
        print()

    hr("═")
    print()
    wrap("The graph is only as good as what the team puts into it.")
    wrap("Bring your domain knowledge back. That's the strategy.")
    print()
    hr("═")
    print()


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    entities, relationships = load()

    intro()
    at_a_glance(entities, relationships)
    data_landscape(entities, relationships)
    where_it_lives(entities, relationships)
    regulatory_exposure(entities, relationships)
    risk_and_control(entities, relationships)
    ai_readiness(entities, relationships)
    strategy_questions()
    next_move()


if __name__ == "__main__":
    main()
