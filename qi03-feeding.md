# Indicator ID

## Title

Early enteral nutrition and calorie target met.


## ID

03


## Short Name

03-feeding


## Description

Early nutrition of critically ill patients is associated with an improved
outcome.
It should start within 24 to 48 hours of admission and should be enough to meet
individuals daily calorie requirement.
The calorie target is calculated by the insulin requirement and/or phosphate
measurements in a blood sample on a daily basis.


## Justification

Early enteral nutrition is associated with a reduction in
infectious complications and in mortality in critically ill patients.


## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions

### Early Nutrition

Early nutrition starts within 24 to 48 hours of admission on the intensive care
unit.
We count the first enteral calorie intake.

### Calorie Target

Daily required calories.
It should be defined by measuring the daily energy consumption via indirect
calorimetry (gold standard) or alternatively via carbon dioxide production rate
or calculation by a formula.
It is reached if the intaken calories are 10 % less or more than the target.


## Guidance

The calorie target should be
a) measured by indirect calorimetry - in that case the value should be used.
b) continuously estimated by the carbon dioxide production rate measured by the
ventilator - the median of the last 24 hours should be used.
c) estimated using a formula.

The calorie target depends on the body-mass-index (BMI) of the patient.

```
BMI = body weight [kg] / (body height [m])^2
```

The initial calorie target (ICT) is calculate as follows:

```
initial calorie target [kcal/d] =
    IF indirect calorimetry THEN
        IF BMI < 30 THEN
        - measurement value of indirect calorimetry
        ELSE
        - 60 % of measurement value of indirect calorimetry
    ELSE IF carbon dioxide production rate
        IF BMI < 30 THEN
        - median of the carbon dioxide production rate in ml/min:
            VCO2 [ml/min] * 8.19
        ELSE
        - 60 % of median of the carbon dioxide production rate in ml/min:
            VCO2 [ml/min] * 8.19 * 0.6
    ELSE
        IF BMI < 30 THEN
        - 24 kcal/d/kg body weight (actual body weight):
            actual body weight [kg] * 24 [kcal/d/kg]
    ELSE IF BMI >= 30 AND BMI <= 50
        - 14 kcal/d/kg body weight (actual body weight):
            actual body weight [kg] * 14 [kcal/d/kg]
    ELSE (BMI > 50)
        - 24 kcal/d/kg body weight (ideal body weight):
            24 kcal/d/kg * (48.4 + 77 * (body height [m] - 1.5))
```

The calorie target is adjusted by the insulin requirement and phosphate
measurements on a daily basis [see Eike et al. 2019, fig. 3 and 4].
Briefly, on Day 1 75 % of the ICT should be applied.
Depending on the maximum insulin dose the calorie target for Day 2 is
kept (0-1 IE insulin/hour), halved (2-4 IE insulin/hour) or
quartered (> 4 IE insulin/hour).
On Day 3 the target is increased by a quarter (0-1 IE/h), decreased by a quarter
(2-4 IE/h) or decreased by a half (>4 IE/h) of the ICT.
If the patient is not receiving renal replacement therapy
and phosphate measurements are below 0.65 mmol/L, the calorie target is set
to a quarter of the ICT, otherwise it is increased by a quarter.
If insulin doses are high and phosphate measurements are low, the
adjustment with the largest absolute change should be used.
If phosphate measurements are above 0.65 mmol/L, insulin-based changes
should be applied.
The calorie target must not be adjusted below zero or above the ICT.

```
CTD0 (calorie target day 0): 0 [first 24 hours are ignored]
CTD1: 0.75 * ICT
CTDi:
    IF NOT renal replacement therapy AND phosphate on Day i < 0.65 mmol/l
        AND CTD(i-1) >= 0.5 * ICT
        AND maximum insulin dose on Day (i - 1) <= 4 IE/h
        0.25 * ICT
    ELSE IF maximum insulin dose on Day (i - 1) < 2 IE/h
        AND CTD(i-1) < ICT
        CTD(i-1) + 0.25 * ICT
    ELSE IF (maximum insulin dose on Day (i - 1) >= 2 IE/h AND <= 4 IE/h)
        AND CTD(i-1) > 0
        CTD(i-1) - 0.25 * ICT
    ELSE IF maximum insulin dose on Day (i - 1) > 4 IE/h
        AND CTD(i-1) > 0
        CTD(i-1) - 0.5 * ICT
```

A day is not defined as midnight-to-midnight but is a full 24-hour period
that starts at the time of admission to the intensive care unit.
The first 24 hours are ignored because feeding should start within 24 to 48
hours.
The last period before discharge from the intensive care unit is ignored if it
is less than 24 hours.


## Initial Population

All critically ill patients that are 18 years or older during the observation
period.


## Numerator

For each 24 hour period starting at admission + 24 hours the calorie intake has
to be 10 % lower/higher than the individualised daily calorie target.

```
calorie intake >= 0.9 * CTDi AND calorie intake =< 1.1 * CTDi
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

Stapel et al. Critical Care (2015) 19:370
DOI 10.1186/s13054-015-1087-2

Elke et al.
DGEM-Leitlinie: „Klinische Ernährung in der Intensivmedizin“


## Comments

// Contraindications missing:
- shock - we could use the ((nor-)epinephrine dose?,
- acidosis (we could use the pH)
- upper gastrointestinal bleeding (not part of the minimal dataset)?
- ileus (not part of the minimal dataset)?