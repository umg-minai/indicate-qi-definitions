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
* Identify intensive care episodes using the concept [Intensive Care (32037)](https://athena.ohdsi.org/search-terms/terms/32037).
  See [INDICATE Mapping recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
  In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence) with `visit_type_concept_id = 32037`.
* "Decision authority documented" is satisfied by either the designated decision-maker (LOINC LA11786-3) or an active healthcare surrogate (SNOMED 762209), see [issue #10](https://github.com/umg-minai/indicate-qi-definitions/issues/10).

| Category                               | Concept ID | Vocabulary | Concept Name                                  | Concept Code     | DD Concept Set                                                                                       |
|----------------------------------------|------------|------------|-----------------------------------------------|------------------|------------------------------------------------------------------------------------------------------|
| Intensive Care                         | 32037      | Visit      | Intensive care                                | OMOP4822460      | N/A                                                                                                  |
|----------------------------------------|------------|------------|-----------------------------------------------|------------------|------------------------------------------------------------------------------------------------------|
| Advance care plan agreed               | 36685263   | SNOMED     | Advance care plan agreed                      | 1095851000000100 | [Advance care plan agreed](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=288)      |
| Consultation with patient              | 37164964   | SNOMED     | Consultation with patient                     | 1237136005       | [Consultation with patient](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=289)     |
| Consultation with patient              | 37168078   | SNOMED     | Face to face consultation with patient        | 1237136005       | [Consultation with patient](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=289)     |
| Consultation with patient              | 4089048    | SNOMED     | New patient consultation                      | 185387006        | [Consultation with patient](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=289)     |
| Discussion about care plan with family | 4247376    | SNOMED     | Discussion about care plan with family        | 406140001        | ?                                                                                                    |
| Decision authority documented          | 45877806   | LOINC      | The patient has designated a decision-maker … | LA11786-3        | [Decision authority documented](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=342) |
| Decision authority documented          | 762209     | SNOMED     | Active healthcare surrogate                   | 3021000175108    | [Surrogate decision maker documented](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=290) |

<!-- inject:AdvanceCarePlanAgreed,ConsultationWithPatient,DecisionAuthorityDocumented,SurrogateDecisionMakerDocumented -->
| Concept ID                                                       | Concept Name                           | Descendants | DD Concept Set                                                                                                         |
|---                                                               |---                                     |---          |---                                                                                                                     |
| [36685263](https://athena.ohdsi.org/search-terms/terms/36685263) | Advance care plan agreed               | no          | [Advance care plan agreed (288)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=288) v1.1.0           |
|---                                                               |---                                     |---          |---                                                                                                                     |
| [37164964](https://athena.ohdsi.org/search-terms/terms/37164964) | Consultation with patient              | no          | [Consultation with patient (289)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=289) v1.1.0          |
| [4247376](https://athena.ohdsi.org/search-terms/terms/4247376)   | Discussion about care plan with family | no          | Added by UMG                                                                                                           |
| [37168078](https://athena.ohdsi.org/search-terms/terms/37168078) | Face to face consultation with patient | no          | [Consultation with patient (289)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=289) v1.1.0          |
| [4089048](https://athena.ohdsi.org/search-terms/terms/4089048)   | New patient consultation               | no          | [Consultation with patient (289)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=289) v1.1.0          |
|---                                                               |---                                     |---          |---                                                                                                                     |
| [45877806](https://athena.ohdsi.org/search-terms/terms/45877806) | Decision authority documented          | no          | Added by UMG                                                                                                           |
|---                                                               |---                                     |---          |---                                                                                                                     |
| [762209](https://athena.ohdsi.org/search-terms/terms/762209)     | Active healthcare surrogate            | no          | [Surrogate decision maker document… (290)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=290) v1.1.0 |

## Initial Population

All critically ill patients that are 18 years or older
    AND have been more than 72 hours on ICU
during the observation period.

## Numerator

At least once during the first 72 hours for each patient
there has to be

Advance care plan agreed
AND
(Consultation with patient OR Discussion about care plan with family)
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
