# Indicator 09

## Title

Early mobilisation


## ID

09


## Short Name

09-mobilisation


## Description

Critically ill patients on an intensive care unit or their relatives should be
consulted regarding care/treatment plans.


## Justification

Early mobilization has been well established to reduce the duration
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
* Identify intensive care episodes using the Intensive Care concept (32037). See [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary-content/#/mapping-recommendations). In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence)) with `visit_type_concept_id = 32037`.



| Category | Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|----------|------------|------------|--------------|--------------|----------------|
| Intensive Care | 32037 | Visit | Intensive care | OMOP4822460 | N/A |
| Order not to mobilize | 2100000008 | INDICATE | Order not to mobilize | order-not-to-mobilize | [Order not to mobilize](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=295) |
| Mobilization | 4327195 | SNOMED | Mobilization | 74923002 | [Mobilization](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=294) |



## Initial Population

All critically ill patients that are 18 years or older
    AND have been at least 48 hours on the ICU
during the observation period.


## Numerator

At least once per day there has to be

Mobilization


## Numerator Exclusion

Incomplete time period before the first occurence of 6:00 and
incomplete time period after the last occurrence of 22:00
AND
all 6:00 to 22:00 time periods with an

Order to not mobilize


## Denominator

Number of 6:00 to 22:00 time periods.


## Denominator Exclusion

Incomplete time period before the first occurence of 6:00 and
incomplete time period after the last occurrence of 22:00
AND
all 6:00 to 22:00 time periods with an

Order to not mobilize


## Expected

100 %


## Improvement Notation

A higher ratio indicates improvement.


## References

Kumpf et al. 2023 Intensivmedizinische Qualitätsindikatoren für Deutschland
DOI: 10.19224/ai2023.333


## Comments