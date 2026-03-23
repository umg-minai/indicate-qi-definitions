# Indicator 02

## Title

Weaning from mechanical ventilation.


## ID

02


## Short Name

02-weaning


## Description

The duration of mechanical ventilation should be as short as possible.
Daily spontaneus breathing trial seem to be important for a fast weaning.


## Justification



## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions

There is not a international definition of spontaneus breathing trial.

We expect a "Trial of spontaneous breathing" entry.


## Mapping

| Category | Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|----------|------------|------------|--------------|--------------|----------------|
| Intubated (tube present) | 4097216 | SNOMED | Endotracheal tube | 26412008 | [Endotracheal tube](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=299) |
| Invasive mechanical ventilation | 37158404 | SNOMED | Invasive mechanical ventilation | 1258985005 | [Invasive mechanical ventilation](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=306) |
| Trial of spontaneous breathing | 4308797 | SNOMED | Trial of spontaneous breathing | 424139009 | [Trial of spontaneous breathing](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=309) |
| Extubation | 4148972 | SNOMED | Extubation of trachea (normal) | 309812005 | [Extubation](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=303) |
| Extubation | 4231838 | SNOMED | Inadvertent tracheal extubation (inadvertent) | 405639008 | [Extubation](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=303) |

## Guidance

A day is not defined as midnight-to-midnight but is a full 24-hour period
that starts at the beginning of mechanical ventilation.
The last period before end of ventilation is ignored if it
is less than 24 hours.


## Initial Population

All critically ill patients that are 18 years or older
    AND mechanical ventilated for at least 48 hours
    AND are intubated
during the observation period.


## Numerator

For each 24 hour period starting at 24 hours after the beginning of
mechanical ventilation there should be at least one period
with

"Trial of spontaneous breathing"
OR
(Extubation OR no mechanical ventilation for >= 5 [min])


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

Fichtner et al. 2025
"S3-Leitlinie Invasive Beatmung und Einsatz extrakorporaler Verfahren bei akuter respiratorischer Insuffizienz"


## Comments