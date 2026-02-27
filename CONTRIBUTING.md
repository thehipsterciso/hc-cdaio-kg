# Contributing to hc-cdaio-kg

## Quality Standards

Every contribution must meet these requirements:

### 1. Search First, Add Second

**MANDATORY:** Always check if an entity already exists before adding a new one.

```bash
# Search for existing entities
python scripts/sre/validate-commit.py
```

### 2. Required Fields

Every entity MUST have:
- `id` - Unique identifier
- `name` - Human-readable name  
- `entity_type` - Valid type from schema
- `description` - Clear description
- `provenance.primary_data_source` - Where data came from
- `provenance.assessed_by` - Who added it
- `provenance.last_assessed_date` - When added (YYYY-MM-DD)

### 3. Provenance Example

```json
{
  "provenance": {
    "primary_data_source": "SEC 10-K FY2024, docs.rackspace.com",
    "assessed_by": "Your Name",
    "last_assessed_date": "2026-02-27",
    "confidence_level": "0.95"
  }
}
```

### 4. Avoid Duplicates

Before adding, check similarity:
- Case doesn't matter: "Zerto" = "ZERTO" = "zerto"
- Typos caught: "Resiliance" vs "Resilience" (96% similar)
- Punctuation ignored: "Zerto-Platform" = "Zerto_Platform"

**Threshold:** 85%+ similarity = warning

### 5. Relationship Rules

Every relationship MUST:
- Reference existing entity IDs
- Use valid relationship_type from schema
- Have confidence score

### 6. Pre-Commit Hook

Install once:
```bash
cp scripts/sre/pre-commit-hook .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

Hook runs automatically on `git commit`.

### 7. Validation Checks

✅ **BLOCKS commit:**
- Missing required fields
- Dangling relationships (references non-existent entities)
- Invalid schema

⚠️ **WARNS only:**
- Incomplete provenance
- Potential duplicates (85%+ similar names)

### 8. Commit Process

```bash
# Add changes
git add entities/ relationships/

# Commit (validation runs automatically)
git commit -m "feat: add new system entity"

# If validation fails, fix issues
# If validation passes, push
git push origin feature-branch
```

### 9. Common Issues

**"Dangling relationship"**
- Fix: Ensure source_id and target_id exist in graph

**"Potential duplicate detected"**
- Review similar entities
- Either use existing OR explain why new entity needed in commit message

**"Provenance incomplete"**
- Currently warning only (will enforce later)
- Add missing fields for quality

### 10. Quality Gates

| Check | Blocks | Threshold |
|-------|--------|-----------|
| Schema | Yes | 100% |
| Required fields | Yes | 100% |
| Relationships | Yes | 100% |
| Provenance | No | Warning |
| Duplicates | No | 85%+ |

---

**Questions?** Open an issue or check docs/QUALITY_INFRASTRUCTURE.md
