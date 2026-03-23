#!/usr/bin/env python3
"""Generate formatted mapping sections for QI files.

- Keeps only concepts already in the .md files (source of truth)
- Marks each concept as in DD or missing
- Adds links to DD concept sets
"""

import csv
import re
from pathlib import Path

DD_LINK = "https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id={}"


def load_dd(csv_path):
    """Load DD CSV. Returns dict: concept_id_str -> {row data + concept_set_id}"""
    dd = {}
    with open(csv_path) as f:
        for row in csv.DictReader(f):
            cid = row["concept_id"].strip()
            dd[cid] = row
    return dd


def extract_mapping_section(text):
    """Extract the mapping section text from a QI .md file."""
    match = re.search(r"## Mapping\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    return match.group(1) if match else ""


def extract_concept_ids(mapping_text):
    """Extract concept IDs (4+ digit numbers) from mapping text, preserving order and context."""
    # We need to extract IDs and their context (the line they appear on)
    results = []
    seen = set()
    for line in mapping_text.split("\n"):
        for m in re.finditer(r"\b(\d{4,})\b", line):
            cid = m.group(1)
            if cid not in seen:
                seen.add(cid)
                results.append((cid, line.strip()))
    return results


def format_table(rows, dd):
    """Format concepts as a markdown table with DD status."""
    lines = []
    lines.append("| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |")
    lines.append("|------------|------------|--------------|--------------|----------------|")

    for cid, context in rows:
        if cid in dd:
            r = dd[cid]
            cs_id = r["concept_set_id"]
            cs_name = r["concept_set_name"]
            link = f"[{cs_name}]({DD_LINK.format(cs_id)})"
            lines.append(f"| {cid} | {r['vocabulary_id']} | {r['concept_name']} | {r['concept_code']} | {link} |")
        else:
            # Try to extract description from context
            desc = context
            lines.append(f"| {cid} | | {desc} | | **Missing from DD** |")

    return "\n".join(lines)


def process_qi01(dd):
    """QI01 - keep original structure with sections, format each as table."""
    sections = [
        ("Body height", [("3036277", "")]),
        ("Gender", [("4135376", "")]),
        ("Female", [("8532", "")]),
        ("Male", [("8507", "")]),
        ("Ideal body weight (IBW)", [("4062985", "")]),
        ("ARDS", [("45552897", "")]),
        ("Intubated (tube present)", [("4097216", "")]),
        ("Invasive mechanical ventilation", [("37158404", "")]),
        ("Ventilation mode", [("37042784", "")]),
        ("PaO2/FiO2 (Horowitz index)", [("3029943", "")]),
        ("PaO2", [("3027801", "1. default"), ("3022803", "2. temperature adjusted")]),
        ("FiO2", [("4353936", "")]),
        ("PEEP", [("42527140", "1. total, measured"), ("4216746", "2. setting"), ("4353713", "3. general")]),
        ("Plateau pressure (Pplat)", [("44782825", "")]),
        ("Inspiratory pressure (Pinsp)", [("4215838", "1. inspiratory pressure setting [cmH2O]"), ("4101694", "2. peak inspiratory pressure [mmHg], CAVE different units")]),
        ("Tidal volume (VT)", [("44782826", "1. inspiratory"), ("4108448", "2. spontaneous"), ("3012410", "3. setting"), ("4029625", "4. general")]),
    ]

    lines = []
    lines.append("If more than one concepts are available at a specific time points the one with")
    lines.append("the highest priority (lowest number) should be used.")

    for section_name, concepts in sections:
        lines.append(f"\n### {section_name}\n")
        lines.append("| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |")
        lines.append("|------------|------------|--------------|--------------|----------------|")
        for cid, note in concepts:
            if cid in dd:
                r = dd[cid]
                cs_id = r["concept_set_id"]
                cs_name = r["concept_set_name"]
                link = f"[{cs_name}]({DD_LINK.format(cs_id)})"
                name = r["concept_name"]
                if note:
                    name = f"{r['concept_name']} ({note})"
                lines.append(f"| {cid} | {r['vocabulary_id']} | {name} | {r['concept_code']} | {link} |")
            else:
                lines.append(f"| {cid} | | {note if note else section_name} | | **Missing from DD** |")

    return "\n".join(lines)


def process_qi02(dd):
    sections = [
        ("Intubated (tube present)", [("4097216", "")]),
        ("Invasive mechanical ventilation", [("37158404", "")]),
        ("Trial of spontaneous breathing", [("4308797", "")]),
        ("Extubation", [("4148972", "normal"), ("4231838", "inadvertent")]),
    ]

    lines = []
    for section_name, concepts in sections:
        lines.append(f"\n### {section_name}\n")
        lines.append("| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |")
        lines.append("|------------|------------|--------------|--------------|----------------|")
        for cid, note in concepts:
            if cid in dd:
                r = dd[cid]
                cs_id = r["concept_set_id"]
                cs_name = r["concept_set_name"]
                link = f"[{cs_name}]({DD_LINK.format(cs_id)})"
                name = r["concept_name"]
                if note:
                    name = f"{r['concept_name']} ({note})"
                lines.append(f"| {cid} | {r['vocabulary_id']} | {name} | {r['concept_code']} | {link} |")
            else:
                lines.append(f"| {cid} | | {note if note else section_name} | | **Missing from DD** |")

    return "\n".join(lines)


def process_qi03(dd):
    sections = [
        ("Body height", [("3036277", "")]),
        ("Body weight", [("4099154", "")]),
        ("Ideal body weight (IBW)", [("4062985", "")]),
        ("Energy requirement", [("4022415", "")]),
        ("Carbon dioxide production", [("21490580", "")]),
        ("Contraindication to enteral feeding", [("4141768", "")]),
        ("Calorie intake total 24 hour", [("3026267", "")]),
        ("Renal replacement therapy", [
            ("4051330", "continuous venovenous hemofiltration"),
            ("4051329", "continuous venovenous hemodialysis"),
            ("4049846", "continuous venovenous hemodiafiltration"),
            ("4051326", "intermittent hemodialysis"),
        ]),
        ("Phosphate", [("3003458", "serum"), ("3018913", "blood")]),
        ("Insulin", [
            ("35198096", "insulin aspart"),
            ("1544838", "insulin glulisine, human"),
            ("1567198", "insulin aspart, human"),
            ("1516976", "insulin detemir"),
            ("35602717", "insulin degludec"),
        ]),
        ("Calorie intake total", [("3007882", "")]),
    ]

    lines = []
    for section_name, concepts in sections:
        lines.append(f"\n### {section_name}\n")
        lines.append("| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |")
        lines.append("|------------|------------|--------------|--------------|----------------|")
        for cid, note in concepts:
            if cid in dd:
                r = dd[cid]
                cs_id = r["concept_set_id"]
                cs_name = r["concept_set_name"]
                link = f"[{cs_name}]({DD_LINK.format(cs_id)})"
                name = r["concept_name"]
                if note:
                    name = f"{r['concept_name']} ({note})"
                lines.append(f"| {cid} | {r['vocabulary_id']} | {name} | {r['concept_code']} | {link} |")
            else:
                lines.append(f"| {cid} | | {note if note else section_name} | | **Missing from DD** |")

    lines.append("")
    lines.append("@NOTE: @Jan maybe we have to redefine our 24 h period if the calorie intake")
    lines.append("counter is reset at a given time (e.g. every morning at 6:00)")

    return "\n".join(lines)


def process_qi04(dd):
    concepts_mass = [
        ("3004501", "serum"),
        ("3000483", "blood"),
        ("3033408", "venous blood"),
        ("1092148", "mixed venous blood"),
        ("3034962", "capillary blood by glucometer"),
    ]
    concepts_moles = [
        ("3031266", "arterial blood"),
        ("3004077", "capillary blood"),
        ("3020491", "blood"),
        ("3001501", "capillary blood by glucometer"),
        ("1761753", "mixed venous blood"),
        ("3013826", "serum or plasma"),
        ("3038515", "venous blood"),
    ]

    lines = []
    lines.append("\n### Glucose levels\n")
    lines.append("#### Mass/volume\n")
    lines.append("| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |")
    lines.append("|------------|------------|--------------|--------------|----------------|")
    for cid, note in concepts_mass:
        if cid in dd:
            r = dd[cid]
            cs_id = r["concept_set_id"]
            cs_name = r["concept_set_name"]
            link = f"[{cs_name}]({DD_LINK.format(cs_id)})"
            lines.append(f"| {cid} | {r['vocabulary_id']} | {r['concept_name']} | {r['concept_code']} | {link} |")
        else:
            lines.append(f"| {cid} | | Glucose [Mass/volume] ({note}) | | **Missing from DD** |")

    lines.append("\n#### Moles/volume\n")
    lines.append("| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |")
    lines.append("|------------|------------|--------------|--------------|----------------|")
    for cid, note in concepts_moles:
        if cid in dd:
            r = dd[cid]
            cs_id = r["concept_set_id"]
            cs_name = r["concept_set_name"]
            link = f"[{cs_name}]({DD_LINK.format(cs_id)})"
            lines.append(f"| {cid} | {r['vocabulary_id']} | {r['concept_name']} | {r['concept_code']} | {link} |")
        else:
            lines.append(f"| {cid} | | Glucose [Moles/volume] ({note}) | | **Missing from DD** |")

    return "\n".join(lines)


def main():
    dd = load_dd("indicate_project5_concepts.csv")

    print("=== QI01 ===")
    print(process_qi01(dd))
    print("\n=== QI02 ===")
    print(process_qi02(dd))
    print("\n=== QI03 ===")
    print(process_qi03(dd))
    print("\n=== QI04 ===")
    print(process_qi04(dd))


if __name__ == "__main__":
    main()
