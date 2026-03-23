#!/usr/bin/env python3
"""Download all concept sets for INDICATE project 5 and compile into a CSV."""

import csv
import json
import sys
import time
import urllib.request

BASE_URL = "https://raw.githubusercontent.com/indicate-eu/data-dictionary-content/main"

def fetch_json(url):
    """Fetch and parse JSON from a URL."""
    req = urllib.request.Request(url, headers={"User-Agent": "indicate-qi-tool"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

def main():
    # Fetch project definition
    print("Fetching project 5 definition...", file=sys.stderr)
    project = fetch_json(f"{BASE_URL}/projects/5.json")
    concept_set_ids = project["conceptSetIds"]
    print(f"Found {len(concept_set_ids)} concept sets", file=sys.stderr)

    rows = []
    for i, cs_id in enumerate(concept_set_ids):
        # Fetch resolved concepts
        resolved_url = f"{BASE_URL}/concept_sets_resolved/{cs_id}.json"
        # Fetch concept set metadata for the name
        meta_url = f"{BASE_URL}/concept_sets/{cs_id}.json"
        try:
            cs_resolved = fetch_json(resolved_url)
            cs_meta = fetch_json(meta_url)
        except Exception as e:
            print(f"  [{i+1}/{len(concept_set_ids)}] Failed to fetch concept set {cs_id}: {e}", file=sys.stderr)
            continue

        cs_name = cs_meta.get("name", "")
        concepts = cs_resolved.get("resolvedConcepts", [])
        print(f"  [{i+1}/{len(concept_set_ids)}] Concept set {cs_id}: {cs_name} ({len(concepts)} concepts)", file=sys.stderr)

        for c in concepts:
            rows.append({
                "concept_set_id": cs_id,
                "concept_set_name": cs_name,
                "concept_id": c.get("conceptId", ""),
                "concept_name": c.get("conceptName", ""),
                "vocabulary_id": c.get("vocabularyId", ""),
                "concept_code": c.get("conceptCode", ""),
                "standard_concept": c.get("standardConcept", ""),
                "domain_id": c.get("domainId", ""),
                "concept_class_id": c.get("conceptClassId", ""),
            })

        # Small delay to be nice to GitHub
        if i % 10 == 9:
            time.sleep(0.5)

    # Write CSV
    outfile = "indicate_project5_concepts.csv"
    fieldnames = [
        "concept_set_id", "concept_set_name",
        "concept_id", "concept_name", "vocabulary_id", "concept_code",
        "standard_concept", "domain_id", "concept_class_id",
    ]
    with open(outfile, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nWrote {len(rows)} concepts to {outfile}", file=sys.stderr)

if __name__ == "__main__":
    main()
