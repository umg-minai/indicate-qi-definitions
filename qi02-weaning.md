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
We define it as follows:
- Disconnected from the ventilator (e.g. T-piece / T-tube)
- CPAP (continuous positive airway pressure) with a
PEEP (positive end expiratory pressure) of 6 cmH2O or less and a pressure support (PS) of 7 cmH2O or less.

both for at least 5 min (if the resolution of the ventilation data is high enough, otherwise the smallest difference in time that is larger than 5 min)

Alternatively the spontaneus breathing trial could be defined by an entry:
"Trial of spontaneous breathing".

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
(Ventilation mode == "CPAP" for >= 5 [min]
    AND PEEP <= 6 [cmH2O]
    AND PS <= 7 [cmH2O])
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