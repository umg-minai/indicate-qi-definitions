# Indicator 05

## Title

Prevention of venous thromboembolism


## ID

05


## Short Name

05-vte-prev


## Description

Venous thromboembolism (VTE) is a frequent complication that contributes
significantly to morbidity and mortality among critically ill patients.
Pharmacologic thromboprophylaxis should reduce VTE.


## Justification

The use of prophylactic measures against deep vein thromboembolism (DVTE) during the
ICU stay is associated with a decrease in morbidity and mortality due to thromboembolism.


## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions


## Mapping

**Notes:**
* Identify intensive care episodes using the concept [Intensive Care (32037)](https://athena.ohdsi.org/search-terms/terms/32037).
  See [INDICATE Mapping recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
  In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence) with `visit_type_concept_id = 32037`.

INDICATE Data Dictionary Concept IDs

| Category | Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|----------|------------|------------|--------------|--------------|----------------|
| Intensive Care | 32037 | Visit | Intensive care | OMOP4822460 | N/A |

<!-- inject:AnticoagulationDrugs -->
| Concept ID                                                       | Concept Name         | Descendants | DD Concept Set                                                                                         |
|---                                                               |---                   |---          |---                                                                                                     |
| [19024063](https://athena.ohdsi.org/search-terms/terms/19024063) | acenocoumarol        | yes         | [Acenocoumarol (33)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=33) v1.0.1        |
| [43013024](https://athena.ohdsi.org/search-terms/terms/43013024) | apixaban             | yes         | [Apixaban (34)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=34) v1.0.1             |
| [1322207](https://athena.ohdsi.org/search-terms/terms/1322207)   | argatroban           | yes         | [Argatroban (35)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=35) v1.0.1           |
| [19069137](https://athena.ohdsi.org/search-terms/terms/19069137) | bemiparin            | yes         | [Bemiparin (36)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=36) v1.0.1            |
| [1592988](https://athena.ohdsi.org/search-terms/terms/1592988)   | betrixaban           | yes         | [Betrixaban (37)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=37) v1.0.1           |
| [19084670](https://athena.ohdsi.org/search-terms/terms/19084670) | bivalirudin          | yes         | [Bivalirudin (38)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=38) v1.0.1          |
| [19016072](https://athena.ohdsi.org/search-terms/terms/19016072) | certoparin           | yes         | [Certoparin (341)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=341) v1.0.1         |
| [40798763](https://athena.ohdsi.org/search-terms/terms/40798763) | Clorindione          | yes         | [Clorindione (39)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=39) v1.0.1          |
| [40228152](https://athena.ohdsi.org/search-terms/terms/40228152) | dabigatran etexilate | yes         | [Dabigatran Etexilate (40)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=40) v1.0.1 |
| [1301065](https://athena.ohdsi.org/search-terms/terms/1301065)   | dalteparin           | yes         | [Dalteparin (41)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=41) v1.0.1           |
| [19026343](https://athena.ohdsi.org/search-terms/terms/19026343) | danaparoid           | yes         | [Danaparoid (42)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=42) v1.0.1           |
| [19011712](https://athena.ohdsi.org/search-terms/terms/19011712) | desirudin            | yes         | [Desirudin (43)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=43) v1.0.1            |
| [1325124](https://athena.ohdsi.org/search-terms/terms/1325124)   | dicumarol            | yes         | [Dicumarol (44)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=44) v1.0.1            |
| [45892847](https://athena.ohdsi.org/search-terms/terms/45892847) | edoxaban             | yes         | [Edoxaban (45)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=45) v1.0.1             |
| [1301025](https://athena.ohdsi.org/search-terms/terms/1301025)   | enoxaparin           | yes         | [Enoxaparin (46)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=46) v1.0.1           |
| [19113013](https://athena.ohdsi.org/search-terms/terms/19113013) | fluindione           | yes         | [Fluindione (47)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=47) v1.0.1           |
| [1315865](https://athena.ohdsi.org/search-terms/terms/1315865)   | fondaparinux         | yes         | [Fondaparinux (48)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=48) v1.0.1         |
| [1367571](https://athena.ohdsi.org/search-terms/terms/1367571)   | heparin              | yes         | [Heparin (49)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=49) v1.0.2              |
| [35884360](https://athena.ohdsi.org/search-terms/terms/35884360) | Heparin Sodium       | yes         | [Heparin (49)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=49) v1.0.2              |
| [19092139](https://athena.ohdsi.org/search-terms/terms/19092139) | lepirudin            | yes         | [Lepirudin (50)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=50) v1.0.1            |
| [40798953](https://athena.ohdsi.org/search-terms/terms/40798953) | Melagatran           | yes         | [Melagatran (51)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=51) v1.0.1           |
| [19001014](https://athena.ohdsi.org/search-terms/terms/19001014) | nadroparin           | yes         | [Nadroparin (52)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=52) v1.0.1           |
| [19008276](https://athena.ohdsi.org/search-terms/terms/19008276) | parnaparin           | yes         | [Parnaparin (53)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=53) v1.0.1           |
| [19033934](https://athena.ohdsi.org/search-terms/terms/19033934) | phenindione          | yes         | [Phenindione (54)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=54) v1.0.1          |
| [19035344](https://athena.ohdsi.org/search-terms/terms/19035344) | phenprocoumon        | yes         | [Phenprocoumon (55)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=55) v1.0.1        |
| [19129274](https://athena.ohdsi.org/search-terms/terms/19129274) | reviparin            | yes         | [Reviparin (56)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=56) v1.0.1            |
| [40241331](https://athena.ohdsi.org/search-terms/terms/40241331) | rivaroxaban          | yes         | [Rivaroxaban (57)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=57) v1.0.1          |
| [43009029](https://athena.ohdsi.org/search-terms/terms/43009029) | sulodexide           | yes         | [Sulodexide (58)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=58) v1.0.1           |
| [1308473](https://athena.ohdsi.org/search-terms/terms/1308473)   | tinzaparin           | yes         | [Tinzaparin (59)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=59) v1.0.1           |
| [19018364](https://athena.ohdsi.org/search-terms/terms/19018364) | tioclomarol          | yes         | [Tioclomarol (60)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=60) v1.0.1          |
| [1310149](https://athena.ohdsi.org/search-terms/terms/1310149)   | warfarin             | yes         | [Warfarin (61)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=61) v1.0.1             |
| [40799186](https://athena.ohdsi.org/search-terms/terms/40799186) | Ximelagatran         | yes         | [Ximelagatran (62)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=62) v1.0.1         |

All concepts from the following anticoagulant concept sets in the INDICATE Data Dictionary:

| Concept Set Name     | Number of Concepts | DD Concept Set |
|----------------------|--------------------|----------------|
| Acenocoumarol        | 2                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=33) |
| Apixaban             | 4                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=34) |
| Argatroban           | 9                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=35) |
| Bemiparin            | 10                 | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=36) |
| Betrixaban           | 2                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=37) |
| Bivalirudin          | 7                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=38) |
| Clorindione          | 1                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=39) |
| Dabigatran Etexilate | 9                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=40) |
| Dalteparin           | 47                 | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=41) |
| Danaparoid           | 4                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=42) |
| Desirudin            | 2                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=43) |
| Dicumarol            | 5                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=44) |
| Edoxaban             | 6                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=45) |
| Enoxaparin           | 25                 | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=46) |
| Fluindione           | 2                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=47) |
| Fondaparinux         | 6                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=48) |
| Heparin              | 303                | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=49) |
| Lepirudin            | 5                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=50) |
| Melagatran           | 1                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=51) |
| Nadroparin           | 21                 | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=52) |
| Parnaparin           | 6                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=53) |
| Phenindione          | 3                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=54) |
| Phenprocoumon        | 4                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=55) |
| Reviparin            | 23                 | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=56) |
| Rivaroxaban          | 13                 | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=57) |
| Sulodexide           | 1                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=58) |
| Tinzaparin           | 26                 | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=59) |
| Tioclomarol          | 1                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=60) |
| Warfarin             | 35                 | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=61) |
| Ximelagatran         | 1                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=62) |
| Certoparin           | 9                  | [Link](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=341) |


## Guidance


## Initial Population

All critically ill patients that are 18 years or older during the observation
period.


## Numerator

For each 24 hour period starting at admission + 24 hours
at least one drug of the ones listed in *Mapping* should be used.


## Numerator Exclusion

First 24 hours and incomplete last 24 hour period.


## Denominator

Number of 24 hour periods.


## Denominator Exclusion

First 24 hours and incomplete last 24 hour period


## Expected

100 %


## Improvement Notation

A higher ratio indicates improvement.


## References

- Arabi, Y.M., Mehta, S. Venous thromboprophylaxis in the ICU: navigating evidence, risk, and practice gaps. Intensive Care Med 51, 1508–1510 (2025). https://doi.org/10.1007/s00134-025-08009-6


## Comments