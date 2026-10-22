# Indicator 02

## Title

Weaning from mechanical ventilation.


## ID

02


## Short Name

02-weaning


## Description

The duration of mechanical ventilation should be as short as possible.
Daily spontaneous breathing trial seem to be important for a fast weaning.


## Justification



## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions

There is not a international definition of spontaneous breathing trial.

We expect a "Trial of spontaneous breathing" entry.


## Mapping

**Notes:**
* Identify intensive care episodes using the concept [Intensive Care (32037)](https://athena.ohdsi.org/search-terms/terms/32037).
  See [INDICATE Mapping recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
  In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence) with `visit_type_concept_id = 32037`.


| Category                        | Concept ID | Vocabulary | Concept Name                                  | Concept Code | DD Concept Set                                                                                         |
|---------------------------------|------------|------------|-----------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------|
| Intensive Care                  | 32037      | Visit      | Intensive care                                | OMOP4822460  | N/A                                                                                                    |
| Intubated (tube present)        | 4097216    | SNOMED     | Endotracheal tube                             | 26412008     | [Endotracheal tube](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=299)               |
| Invasive mechanical ventilation | 37158404   | SNOMED     | Invasive mechanical ventilation               | 1258985005   | [Invasive mechanical ventilation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=306) |
| Trial of spontaneous breathing  | 4308797    | SNOMED     | Trial of spontaneous breathing                | 424139009    | [Trial of spontaneous breathing](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=309)  |
|---------------------------------|------------|------------|-----------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------|
| Extubation                      | 4148972    | SNOMED     | Extubation of trachea (normal)                | 309812005    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                      |
| Extubation                      | 4150627    | SNOMED     | Removal of endotracheal tube                  | 271280005    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                      |
| Extubation                      | 4012607    | SNOMED     | Removal of tracheostomy tube                  | 113153002    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                      |
| Extubation                      | 4195943    | SNOMED     | Ventilating tube removal by another physician | 44482009     | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                      |
|---------------------------------|------------|------------|-----------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------|
| Extubation                      | 4231838    | SNOMED     | Inadvertent tracheal extubation (inadvertent) | 405639008    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                      |

<!-- inject:EndotrachealTube,InvasiveMechanicalVentilation,TrialOfSpontaneousBreathing,Extubation -->
| Concept ID                                                       | Concept Name                             | Descendants | DD Concept Set                                                                                                      |
|---                                                               |---                                       |---          |---                                                                                                                  |
| [4097216](https://athena.ohdsi.org/search-terms/terms/4097216)   | Endotracheal tube                        | yes         | [Endotracheal tube (299)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=299) v1.1.0               |
|---                                                               |---                                       |---          |---                                                                                                                  |
| [37158404](https://athena.ohdsi.org/search-terms/terms/37158404) | Invasive mechanical ventilation          | no          | [Invasive mechanical ventilation (306)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=306) v1.1.0 |
|---                                                               |---                                       |---          |---                                                                                                                  |
| [4308797](https://athena.ohdsi.org/search-terms/terms/4308797)   | Trial of spontaneous breathing           | no          | [Trial of spontaneous breathing (309)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=309) v1.0.0  |
|---                                                               |---                                       |---          |---                                                                                                                  |
| [4148972](https://athena.ohdsi.org/search-terms/terms/4148972)   | Extubation of trachea                    | no          | [Extubation (303)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303) v1.1.0                      |
| [4231838](https://athena.ohdsi.org/search-terms/terms/4231838)   | Inadvertent tracheal extubation          | no          | [Extubation (303)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303) v1.1.0                      |
| [4150627](https://athena.ohdsi.org/search-terms/terms/4150627)   | Removal of endotracheal tube             | no          | [Extubation (303)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303) v1.1.0                      |
| [4012607](https://athena.ohdsi.org/search-terms/terms/4012607)   | Removal of tracheostomy tube             | no          | [Extubation (303)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303) v1.1.0                      |
| [4195943](https://athena.ohdsi.org/search-terms/terms/4195943)   | Ventilating tube removal by another phy… | no          | [Extubation (303)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303) v1.1.0                      |

## Guidance

A day is not defined as midnight-to-midnight but is a full 24-hour period
that starts at the beginning of mechanical ventilation.
The last period before end of ventilation is ignored if it
is less than 24 hours.


## Initial Population

```
All critically ill patients that are 18 years or older
    AND mechanical ventilated for at least 48 hours
    AND are intubated
during the observation period.
```

## Numerator

For each 24 hour period starting at 24 hours after the beginning of
mechanical ventilation there should be at least one period
with

```
"Trial of spontaneous breathing"
OR
(Extubation OR no mechanical ventilation for >= 5 [min])
```

## Numerator Exclusion

First 24 hours and incomplete last 24 hour period.


## Denominator

Number of 24 hour periods.


## Denominator Exclusion

First 24 hours and incomplete last 24 hour period.


## Expected

100 %


## Improvement Notation

A higher ratio indicates improvement.


## References

- Fichtner et al. 2025
  "S3-Leitlinie Invasive Beatmung und Einsatz extrakorporaler Verfahren bei akuter respiratorischer Insuffizienz"


## Comments
