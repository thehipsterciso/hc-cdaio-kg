# Enterprise Knowledge Graph — Team Orientation

**CDAIO | CMU CDAIO Program | March 2026**

---

## Can You Answer These?

> Which of our systems process customer PII — and are all of them encrypted at rest?

> If we received a GDPR data subject access request today, which systems would we need to query and who owns them?

> We want to build an AI model on our operational data. Which datasets can we legally use?

> Which business capabilities have no data supporting them?

> Which of our security controls are actually mapped to the risks they claim to address?

> If one system failed right now, what's the downstream blast radius across our data landscape?

> Where does our data cross international borders, and are the transfer mechanisms compliant?

---

If you can't answer these — you don't have a data strategy. You have a data hope.

The knowledge graph exists to change that.

---

## What We Built

A connected, queryable map of the enterprise — 2,949 entities, 7,011 relationships across systems, data assets, regulations, risks, controls, and the people responsible for them. Built through systematic OSINT research and architectural inference, with every assumption documented and confidence-scored.

It lives in Claude Desktop. You talk to it in plain English.

**Try these:**

```
"Which data assets are classified restricted and stored in unencrypted systems?"
"What's the blast radius if the MariaDB Galera cluster goes down?"
"Which risks have no controls mapped to them?"
```

---

## The Questions That Build a Data & AI Strategy

A strategy isn't a plan. It's a set of answered questions that make the right moves obvious. These are the questions.

### What data do we actually have?
- What are our data assets, how are they classified, and who owns them?
- Which assets contain PII, PHI, or regulated data?
- What's the quality and completeness of each asset?
- Where are the gaps — data we need but don't have?

### Where does it live and how does it move?
- Which systems store, process, or transmit each asset?
- What are the integration points — where does data flow between systems?
- Which assets have no documented system owner?
- What's the lineage — where did this data come from and where does it go?

### What are we allowed to do with it?
- Which regulations apply to each asset and each system?
- What cross-border transfers are happening and are they covered?
- Which AI use cases are legally viable with our current data?
- Where do consent and retention obligations create constraints?

### What risk does it create?
- Which assets, if breached, create regulatory exposure?
- Which systems are critical paths — failure cascades broadly?
- Where are our control gaps?
- Which risks have no mitigating controls?

### Where does AI actually fit?
- Which business capabilities could be augmented or automated with AI?
- Which of those capabilities have sufficient data to support a model?
- Where is data quality too low to trust a model's output?
- What governance and oversight does each AI use case require?

---

## What You Do With This

The graph is only as good as the knowledge the team puts into it. Every domain lead knows things that aren't in here yet — systems your team owns, data flows you manage, risks you've identified. That knowledge belongs in the graph.

Run `scripts/kg-tour.py` for a live walkthrough. Then bring your domain knowledge back.
