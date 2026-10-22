# Indicator 09

## Title

Early mobilisation


## ID

09


## Short Name

09-mobilisation


## Description

Critically ill adult ICU patients should be mobilised at least once per eligible ICU day, unless there is a documented order not to mobilise.



## Justification

Early mobilisation has been well established to reduce the duration
of mechanical ventilation and shorten ICU length of stay.
Additional evidence suggests that it may yield lower delirium rates,
improved muscle strength and functional independence
in critically ill patients, as well as more days alive and
out of the hospital within 180 days.


## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions

Mobilisation is done during the day.
A day starts at 6:00 and ends at 22:00.


## Guidance


## Mapping

**Notes:**
* Identify intensive care episodes using the concept [Intensive Care (32037)](https://athena.ohdsi.org/search-terms/terms/32037).
  See [INDICATE Mapping recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
  In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence) with `visit_type_concept_id = 32037`.

| Category | Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|----------|------------|------------|--------------|--------------|----------------|
| Intensive Care | 32037 | Visit | Intensive care | OMOP4822460 | N/A |
| Order not to mobilize | 2100000008 | INDICATE | Order not to mobilize | order-not-to-mobilize | [Order not to mobilize](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=295) |
| Mobilization | 4327195 | SNOMED | Mobilization | 74923002 | [Mobilization](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=294) |


<!-- inject:OrderNotToMobilize,MobilizationProcedures -->
| Concept ID                                                       | Concept Name                            | Descendants | DD Concept Set                                                                                            |
|---                                                               |---                                      |---          |---                                                                                                        |
| 2100000008                                                       | Order not to mobilize                   | no          | [Order not to mobilize (295)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=295) v1.0.0 |
|---                                                               |---                                      |---          |---                                                                                                        |
| [4158838](https://athena.ohdsi.org/search-terms/terms/4158838)   | Ambulation therapy                      | no          | [Mobilization (294)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=294) v1.1.0          |
| [1242274](https://athena.ohdsi.org/search-terms/terms/1242274)   | Assistance with getting out of bed      | no          | [Mobilization (294)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=294) v1.1.0          |
| [46272439](https://athena.ohdsi.org/search-terms/terms/46272439) | Assistance with mobility                | no          | [Mobilization (294)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=294) v1.1.0          |
| [37016972](https://athena.ohdsi.org/search-terms/terms/37016972) | Assistance with mobility in bed         | no          | [Mobilization (294)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=294) v1.1.0          |
| [46272440](https://athena.ohdsi.org/search-terms/terms/46272440) | Assistance with walking using device    | no          | [Mobilization (294)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=294) v1.1.0          |
| [46272565](https://athena.ohdsi.org/search-terms/terms/46272565) | Progressive mobility                    | no          | [Mobilization (294)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=294) v1.1.0          |
| [46271859](https://athena.ohdsi.org/search-terms/terms/46271859) | Promotion of physical mobility          | no          | [Mobilization (294)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=294) v1.1.0          |
| [46271857](https://athena.ohdsi.org/search-terms/terms/46271857) | Promotion of walking using mobility aid | no          | [Mobilization (294)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=294) v1.1.0          |
| [4204159](https://athena.ohdsi.org/search-terms/terms/4204159)   | Walking practice                        | no          | [Mobilization (294)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=294) v1.1.0          |
| [4040262](https://athena.ohdsi.org/search-terms/terms/4040262)   | Walking with patient - mobilization     | no          | [Mobilization (294)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=294) v1.1.0          |


## Initial Population

All critically ill patients that are 18 years or older
    AND have been at least 48 hours on the ICU
during the observation period.


## Numerator

At least once per day there has to be

Mobilisation


## Numerator Exclusion

Incomplete time period before the first occurence of 6:00 and
incomplete time period after the last occurrence of 22:00
AND
all 6:00 to 22:00 time periods with an

Order to not mobilise


## Denominator

Number of 6:00 to 22:00 time periods.


## Denominator Exclusion

Incomplete time period before the first occurence of 6:00 and
incomplete time period after the last occurrence of 22:00
AND
all 6:00 to 22:00 time periods with an

Order to not mobilise


## Expected

100 %


## Improvement Notation

A higher ratio indicates improvement.


## References

- Kumpf et al. 2023 Intensivmedizinische Qualitätsindikatoren für Deutschland
  [DOI: 10.19224/ai2023.333](https://doi.org/10.19224/ai2023.333)


## Comments
