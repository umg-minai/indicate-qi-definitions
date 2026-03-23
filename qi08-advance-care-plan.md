# Indicator 08

## Title

Advance care plan


## ID

08


## Short Name

08-adv-care-plan


## Description

Critically ill patients on an intensive care unit or their relatives should be
consulted regarding care/treatment plans.


## Justification


## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions


## Guidance


## Mapping

**Notes:**
* Identify intensive care episodes using the Intensive Care concept (32037). See [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary-content/#/mapping-recommendations). In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence)) with `visit_type_concept_id = 32037`.



| Category | Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|----------|------------|------------|--------------|--------------|----------------|
| Intensive Care | 32037 | Visit | Intensive care | OMOP4822460 | N/A |
| Advance care plan agreed | 36685263 | SNOMED | Advance care plan agreed | 1095851000000100 | [Advance care plan agreed](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=288) |
| Consultation with patient | 37164964 | SNOMED | Consultation with patient | 1237136005 | [Consultation with patient](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=289) |
| Decision authority documented | 1032192 | LOINC | Decision authority documented | LP74704-5 | [Decision authority documented](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=342) |

## Initial Population

All critically ill patients that are 18 years or older
    AND have been more than 72 hours on ICU
during the observation period.


## Numerator

At least once during the first 72 hours for each patient
there has to be

Advance care plan agreed
AND
Consultation with patient
AND
Decision authority documented


## Numerator Exclusion

None.


## Denominator

Initial population.

## Denominator Exclusion

None.


## Expected

100 %

## Improvement Notation

A higher ratio indicates improvement.


## References


## Comments