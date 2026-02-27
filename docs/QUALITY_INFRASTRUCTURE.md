# Knowledge Graph Quality Infrastructure

**Status:** ✅ Operational  
**Deployed:** 2026-02-27  
**Owner:** Thomas Jones

## Overview

Automated quality gates that prevent low-quality commits from entering the repository.

## Components

### 1. Validation Script
**Location:** `scripts/sre/validate-commit.py`

**Checks:**
- ✅ Schema structure
- ✅ Required fields (id, name, entity_type)
- ✅ Relationship integrity (no dangling references)
- ⚠️  Provenance completeness (warning)
- ⚠️  Duplicate detection (85%+ similarity)

**Usage:**
```bash
python scripts/sre/validate-commit.py
```

### 2. Pre-Commit Hook
**Location:** `.git/hooks/pre-commit`

Runs validation automatically before every commit.

**Install:**
```bash
cp scripts/sre/pre-commit-hook .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### 3. GitHub Actions
**Location:** `.github/workflows/graph-validation.yml`

Validates all PRs and pushes to main.

### 4. Contributing Guide
**Location:** `CONTRIBUTING.md`

Quality standards and workflow documentation.

## Current Quality Status

**Graph:** 2,908 entities | 5,247 relationships

**Quality:**
- ✅ Schema: Valid
- ✅ Required fields: 100%
- ✅ Relationship integrity: 100%
- ⚠️  Provenance: 3,780 entities incomplete
- ⚠️  Duplicates: 452 candidates detected

## Quality Gates

| Check | Blocks Commit | Threshold |
|-------|--------------|-----------|
| Schema validation | Yes | 100% |
| Required fields | Yes | 100% |
| Relationship integrity | Yes | 100% |
| Provenance | No (warning) | Future: 100% |
| Duplicates | No (warning) | 85%+ similarity |

## Test Results

Duplicate detection tested with 17 variations of "Zerto IT Resilience Platform":

- **Blocks (≥95%):** 3 variations (typos, case changes)
- **Warns (85-94%):** 8 variations (prefixes, punctuation)
- **Passes (<85%):** 6 variations (synonyms, shortened)

## Installation

```bash
cd /Users/thomasjones/hc-cdaio-kg

# Install pre-commit hook
cp scripts/sre/pre-commit-hook .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# Test
python scripts/sre/validate-commit.py
```

## Next Steps

1. ✅ Pre-commit hook operational
2. ✅ GitHub Actions configured
3. ✅ Duplicate detection tested
4. 🔄 Address 452 duplicate candidates
5. 🔄 Backfill provenance (3,780 entities)
6. 🔄 Enable strict provenance mode

---

**Execution:** ~2 hours  
**Runtime:** ~0.2 seconds per validation
