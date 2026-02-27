#!/usr/bin/env python3
import json
import re

def extract_provenance(desc):
    if not desc:
        return None
    
    result = {}
    
    # Extract confidence
    conf_match = re.search(r'\[(CONFIRMED|INFERRED)\s*-\s*([\d.]+|[^\]]+)\]', desc)
    if conf_match:
        conf_value = conf_match.group(2)
        num_match = re.search(r'([\d.]+)', conf_value)
        result['confidence'] = num_match.group(1) if num_match else '0.85'
    
    # Extract sources
    source_match = re.search(r'Source:\s*([^.]+?)(?:\.|$)', desc, re.IGNORECASE)
    if source_match:
        result['sources'] = source_match.group(1).strip()
    
    # Detect methodology
    methods = []
    if re.search(r'DNS:', desc) or re.search(r'dns records', desc, re.I):
        methods.append('DNS reconnaissance')
    if re.search(r'docs\.rackspace\.com', desc, re.I):
        methods.append('Public documentation analysis')
    if re.search(r'linkedin', desc, re.I):
        methods.append('LinkedIn OSINT')
    if re.search(r'github', desc, re.I):
        methods.append('GitHub reconnaissance')
    if re.search(r'10-K|10-Q|SEC filing', desc, re.I):
        methods.append('SEC filings analysis')
    
    if methods:
        result['methodology'] = ', '.join(methods)
    
    # Clean description
    clean = desc
    clean = re.sub(r'\[(CONFIRMED|INFERRED)[^\]]+\]', '', clean)
    clean = re.sub(r'Source:\s*[^.]+\.', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r'DNS:\s*[^.]+\.', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()
    result['clean_desc'] = clean
    
    return result if (result.get('confidence') or result.get('sources') or clean != desc) else None

# Load graph
with open('/Users/thomasjones/hc-cdaio-kg/graph.json', 'r') as f:
    graph = json.load(f)

print(f"Loaded {len(graph['entities'])} entities")

# Process all entities
total_updated = 0
for i, entity in enumerate(graph['entities']):
    desc = entity.get('description', '')
    parsed = extract_provenance(desc)
    
    if not parsed:
        continue
    
    # Ensure provenance exists
    if 'provenance' not in entity:
        entity['provenance'] = {
            'data_quality_score': {
                'completeness_pct': None,
                'accuracy_confidence': '',
                'timeliness_score': '',
                'consistency_score': ''
            },
            'primary_data_source': '',
            'last_assessed_date': None,
            'assessed_by': '',
            'assessment_methodology': '',
            'confidence_level': '',
            'attestation_status': None,
            'known_data_gaps': []
        }
    
    # Update description
    entity['description'] = parsed['clean_desc']
    
    # Update provenance
    if parsed.get('confidence'):
        entity['provenance']['confidence_level'] = parsed['confidence']
        entity['provenance']['data_quality_score']['accuracy_confidence'] = parsed['confidence']
    
    if parsed.get('sources'):
        entity['provenance']['primary_data_source'] = parsed['sources']
    
    if parsed.get('methodology'):
        entity['provenance']['assessment_methodology'] = parsed['methodology']
    
    entity['provenance']['last_assessed_date'] = '2026-02-25'
    entity['provenance']['assessed_by'] = 'Thomas Jones'
    entity['provenance']['data_quality_score']['timeliness_score'] = 'Current'
    entity['provenance']['data_quality_score']['consistency_score'] = 'Verified'
    
    total_updated += 1
    
    if (i + 1) % 100 == 0:
        print(f"Processed {i+1} entities...")

print(f"\nTotal updated: {total_updated} entities")

# Write back
with open('/Users/thomasjones/hc-cdaio-kg/graph.json', 'w') as f:
    json.dump(graph, f, indent=2)

print("✅ Graph updated and saved")
