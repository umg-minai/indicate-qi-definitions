#!/usr/bin/env python3
"""Compare concept IDs in QI definition .md files against the INDICATE data dictionary CSV."""

import csv
import re
import sys
from pathlib import Path


def load_data_dictionary(csv_path):
    """Load the data dictionary CSV into a dict keyed by concept_id."""
    concepts = {}
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            cid = row["concept_id"].strip()
            concepts[cid] = row
    return concepts


def extract_concept_ids_from_md(md_path):
    """Extract all concept IDs mentioned in the Mapping section of a QI .md file."""
    text = Path(md_path).read_text()

    # Find the Mapping section
    mapping_match = re.search(r"## Mapping\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    if not mapping_match:
        return [], ""

    mapping_text = mapping_match.group(1)

    # Extract all numbers that look like concept IDs (at least 4 digits)
    # Match patterns like "- 3036277", "| 2100000007 |", standalone numbers
    ids = re.findall(r"\b(\d{4,})\b", mapping_text)

    return ids, mapping_text


def main():
    csv_path = "indicate_project5_concepts.csv"
    dd = load_data_dictionary(csv_path)

    # Also build a lookup by concept_set_name for easier matching
    concept_sets = {}
    for cid, row in dd.items():
        cs_name = row["concept_set_name"]
        if cs_name not in concept_sets:
            concept_sets[cs_name] = []
        concept_sets[cs_name].append(row)

    qi_files = sorted(Path(".").glob("qi[0-9]*.md"))

    for qi_file in qi_files:
        if qi_file.name == "qi00-template.md":
            continue

        ids, mapping_text = extract_concept_ids_from_md(qi_file)
        if not ids:
            print(f"\n{'='*80}")
            print(f"## {qi_file.name}: NO MAPPING SECTION FOUND")
            continue

        print(f"\n{'='*80}")
        print(f"## {qi_file.name}")
        print(f"{'='*80}")

        found_in_dd = []
        not_in_dd = []

        for cid in ids:
            if cid in dd:
                found_in_dd.append(cid)
            else:
                not_in_dd.append(cid)

        if found_in_dd:
            print(f"\n### Concept IDs FOUND in data dictionary ({len(found_in_dd)}):")
            for cid in found_in_dd:
                row = dd[cid]
                print(f"  {cid}: {row['concept_name']} [{row['vocabulary_id']}] "
                      f"(concept set: {row['concept_set_name']})")

        if not_in_dd:
            print(f"\n### Concept IDs NOT in data dictionary ({len(not_in_dd)}):")
            for cid in sorted(set(not_in_dd)):
                # Try to find context in the mapping text
                # Find the line containing this ID
                for line in mapping_text.split("\n"):
                    if cid in line:
                        print(f"  {cid}: (context: {line.strip()})")
                        break
                else:
                    print(f"  {cid}: (no context found)")

    # Also print a summary of all concept sets in the data dictionary
    print(f"\n\n{'='*80}")
    print("## ALL CONCEPT SETS IN DATA DICTIONARY (project 5)")
    print(f"{'='*80}")
    for cs_name in sorted(concept_sets.keys()):
        concepts = concept_sets[cs_name]
        cids = [c["concept_id"] for c in concepts]
        print(f"  {cs_name}: {', '.join(cids[:5])}{'...' if len(cids) > 5 else ''} ({len(cids)} concepts)")


if __name__ == "__main__":
    main()
