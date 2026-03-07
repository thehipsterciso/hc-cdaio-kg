# Due Diligence Prompt Library

The execution prompts that drove the entire analysis. Every structured finding, every entity in the knowledge graph, every relationship — all of it traces back to these prompts fed to AI agents operating against public sources.

This is not a template collection. It is a working methodology — 10 stages of progressive constraint discovery, each with orientation gates, atomic execution prompts, and validation synthesis before the next stage unlocks. The prompts enforce their own discipline: evidence hierarchy, falsification mandates, uncertainty classification, and explicit failure conditions at every level.

## How This Works

The framework operates on four layers of control:

**Layer 1 — Constitutional Control.** Stage 0 establishes the evidentiary constitution. Every subsequent prompt inherits and enforces it. Claims must be classified as FACT, INFERENCE, or HYPOTHESIS. Sources follow a strict hierarchy. Confirmation bias gets named and blocked.

**Layer 2 — Stage Orientation.** Before any analysis begins, the AI agent must demonstrate understanding of the stage's intent, boundaries, failure conditions, and dependency role. Orientation is a gate, not a formality.

**Layer 3 — Atomic Execution.** Each sub-stage prompt executes one analytical task with explicit scope boundaries. No bleeding into adjacent analysis. No premature synthesis. The prompt defines what to analyze, what not to touch, and what constitutes failure.

**Layer 4 — Validation Synthesis.** After all sub-stages complete, a synthesis prompt cross-validates outputs, tests for contradictions, enforces completeness, and makes an explicit PASS/FAIL gate decision before progression to the next stage.

## Repository Structure

```
due-diligence-prompts/
├── stage-0-governance/          Constitutional control and epistemic standards
├── stage-1-corporate-legal/     Corporate, legal, and structural reality
├── stage-2-business-model/      Business model, value creation, and economics
├── stage-3-market-reality/      Market structure, competition, and external force
├── stage-4-operating-model/     Organizational reality and execution physics
├── stage-5-financial-reality/   Financial constraints and capital under stress
├── stage-6-technology/          Technology, compute, and platform reality
├── stage-7-data-assets/         Data assets, information flow, and epistemic control
├── stage-8-risk-security/       Risk, security, privacy, and regulatory constraints
└── stage-9-enterprise-resilience/ Enterprise resilience, ESG, and continuity
```

Each stage directory contains:

- **`orientation.md`** — Stage-level orientation prompt. Establishes scope, boundaries, non-goals, failure conditions, and dependency mapping.
- **`X.Y-topic.md`** — Sub-stage execution prompts. Atomic analytical tasks with explicit constraints.
- **`validation-synthesis.md`** — Cross-validation and exit gate prompt. Tests completeness, coherence, and contradiction before stage progression.

## Stage Inventory

| Stage | Focus | Sub-Stages | What It Discovers |
|-------|-------|------------|-------------------|
| [0](stage-0-governance/) | Governance | Constitutional framing | How to prevent the diligence from lying to itself |
| [1](stage-1-corporate-legal/) | Corporate & Legal | 1.1–1.5 | Legal existence, ownership reality, structural debt, change-of-control constraints |
| [2](stage-2-business-model/) | Business Model | 2.1–2.6 | Revenue engine, cost physics, value flow friction, internal contradictions |
| [3](stage-3-market-reality/) | Market Reality | 3.1–3.6 | Market structure, competitive threats, buying behavior, shock sensitivity |
| [4](stage-4-operating-model/) | Operating Model | 4.1–4.5 | Decision rights, coordination load, bottlenecks, incentive misalignment |
| [5](stage-5-financial-reality/) | Financial Reality | 5.1–5.6 | Revenue quality, margin behavior, liquidity, covenants, capital allocation |
| [6](stage-6-technology/) | Technology | 6.1–6.6 | Compute control, cloud dependency, platform fragility, technical debt |
| [7](stage-7-data-assets/) | Data Assets | 7.1–7.7 | Data domains, lineage, quality, stewardship, epistemic coherence |
| [8](stage-8-risk-security/) | Risk & Security | 8.1–8.5 | Cyber posture, privacy, regulatory enforcement, data sovereignty |
| [9](stage-9-enterprise-resilience/) | Resilience | 9.1–9.5 | ESG materiality, business continuity, workforce fragility, ecosystem shocks |

## How to Use These Prompts

**For your own due diligence:**

1. Start with Stage 0. Adapt the governance constitution to your evidentiary standards and scope.
2. Replace the target organization declaration (currently Rackspace Technology) with your target.
3. Execute stages sequentially. Each stage depends on validated outputs from prior stages.
4. Do not skip validation synthesis. The exit gates exist because premature progression produces compounding errors.
5. Feed each prompt to an AI agent with access to public source material (SEC filings, regulatory disclosures, DNS records, job postings, press releases, etc.).

**What makes this different from a standard due diligence checklist:**

These prompts do not ask the AI to confirm a thesis. They ask it to discover constraints — what breaks, what contradicts, what the organization cannot change even if it wanted to. The methodology is adversarial by design. Every stage includes explicit failure conditions. If the analysis cannot demonstrate that the constraint matters, the stage fails.

The output of this framework was a knowledge graph with 2,900+ entities and 6,000+ relationships, plus 401 structured analysis documents — all from public sources, all with provenance and confidence ratings.

## Relationship to Other Repository Content

- **`docs/deliverable-1-due-diligence/`** — The structured analysis outputs produced by executing these prompts. Stage-by-stage findings in JSON format.
- **`entities/` and `relationships/`** — The knowledge graph populated from the analysis. 26 entity types, 40 relationship types.
- **`docs/deliverable-2-data-maturity/`** — DCAM v2 maturity assessment derived from Stage 7 findings.
