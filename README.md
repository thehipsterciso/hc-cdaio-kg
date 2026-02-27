# hc-cdaio-kg — CMU CDAIO Knowledge Graph Data

Per-entity-type and per-relationship-type JSON files for the
[hc-enterprise-kg](https://github.com/thehipsterciso/hc-enterprise-kg) MCP server.

## Structure

```
entities/
    person.json
    system.json
    department.json
    ...
relationships/
    works_in.json
    depends_on.json
    ...
```

Each file is a JSON array of objects of that type.

## Workflow

| Time | Action |
|------|--------|
| 8 am | `kg-morning.sh` pulls main → rebuilds `graph.json` |
| every 30 min | `kg-sync.sh` splits graph → commits → pushes to your branch |
| 5 pm | `kg-eod.sh` final sync + opens PR to main |

## Admin

- **Add a new member:** `bash kg-add-member.sh <github-username>`
- **Merge branches:** review and merge PRs in GitHub

## graph.json

`graph.json` is **gitignored** and assembled locally.  To rebuild it:

```bash
python3 ~/hc-enterprise-kg/scripts/lib/kg-build.py ~/hc-cdaio-kg ~/hc-cdaio-kg/graph.json
```
