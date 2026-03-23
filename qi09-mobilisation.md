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

INDICATE Data Dictionary Concept IDs

| Concept ID | Vocabulary | Concept Name                  | Concept Code          |
|------------|------------|-------------------------------|-----------------------|
| 2100000008 | INDICATE   | Order not to mobilize         | order-not-to-mobilize |
| 4327195    | SNOMED     | Mobilization                  | 74923002              |



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