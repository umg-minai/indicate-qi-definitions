# Indicator 03

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

## Mapping

### Body height

| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|------------|------------|--------------|--------------|----------------|
| 3036277 | LOINC | Body height | 8302-2 | [Body height](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=274) |

### Body weight

| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|------------|------------|--------------|--------------|----------------|
| 4099154 | SNOMED | Body weight | 27113001 | [Body weight](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=275) |

### Ideal body weight (IBW)

| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|------------|------------|--------------|--------------|----------------|
| 4062985 | SNOMED | Ideal body weight | 170804003 | [Ideal body weight](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=284) |

### Energy requirement

| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|------------|------------|--------------|--------------|----------------|
| 4022415 | SNOMED | Energy requirement | 226244007 | [Energy requirement](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=287) |

### Carbon dioxide production

| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|------------|------------|--------------|--------------|----------------|
| 21490580 | LOINC | Carbon dioxide production (VCO2) in Respiratory system | 60825-7 | [Carbon dioxide production](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=311) |

### Contraindication to enteral feeding

| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|------------|------------|--------------|--------------|----------------|
| 4141768 | SNOMED | Medical contraindication to procedure | 266757004 | [Contraindication to enteral feeding](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=285) |

### Calorie intake total 24 hour

| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|------------|------------|--------------|--------------|----------------|
| 3026267 | LOINC | Calorie intake total 24 hour | 9057-1 | [Energy intake](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=286) |

### Renal replacement therapy
 could be one of:
 
| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|------------|------------|--------------|--------------|----------------|
| 4051330 | SNOMED | Continuous venovenous hemofiltration | 233585000 | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=298) |
| 4051329 | SNOMED | Continuous venovenous hemodialysis | 233580005 | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=298) |
| 4049846 | SNOMED | Continuous venovenous hemodiafiltration | 233590002 | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=298) |
| 4051326 | SNOMED | Intermittent hemodialysis | 233575001 | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=298) |

### Phosphate

| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|------------|------------|--------------|--------------|----------------|
| 3003458 | LOINC | Phosphate [Moles/volume] in Serum or Plasma | 14879-1 | [Plasma phosphate](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=210) |
| 3018913 | LOINC | Phosphate [Moles/volume] in Blood | 24519-1 | [Plasma phosphate](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=210) |

### Insulin

| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|------------|------------|--------------|--------------|----------------|
| 35198096 | | insulin aspart | | **Missing from DD** |
| 1544838 | | insulin glulisine, human | | **Missing from DD** |
| 1567198 | | insulin aspart, human | | **Missing from DD** |
| 1516976 | | insulin detemir | | **Missing from DD** |
| 35602717 | | insulin degludec | | **Missing from DD** |

### Calorie intake total

| Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|------------|------------|--------------|--------------|----------------|
| 3007882 | | Calorie intake total | | **Missing from DD** |

@NOTE: @Jan maybe we have to redefine our 24 h period if the calorie intake
counter is reset at a given time (e.g. every morning at 6:00)
Calorie intake total 24 hour:
- 3026267 (duplicate of above)

## Guidance

The calorie target should be
a) The `minimal_dataset` defines an "energy requirement" item which should be
used if available (may be based on indirect calorimetry, carbon dioxide
production rate or formulas).
b) continuously estimated by the carbon dioxide production rate (VCO2)
measured by the ventilator - the median of the last 24 hours should be used.
c) estimated using a formula.

The calorie target depends on the body-mass-index (BMI) of the patient.

```
BMI = body weight [kg] / (body height [m])^2
```

The initial calorie target (ICT) is calculate as follows:

```
initial calorie target [kcal/d] =
    IF Energy requirement is available THEN
        Energy requirement
    ELSE IF carbon dioxide production rate
        IF BMI < 30 THEN
        - median of the carbon dioxide production rate of the
          previous day in ml/min:
            VCO2 [ml/min] * 8.19
        ELSE
        - 60 % of median of the carbon dioxide production rate of the
          previous day in ml/min:
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

If the insulin is not applied continuously
the "maximum insulin dose" is equivalent to
the sum of all give international units [IE] of insulin derivates per 24 h period
(from 6:00 to 5:59)
divided by 24 h (equals the mean insule dose per hour).

```
CTD0 (calorie target day 0): 0 [first 24 hours are ignored]
CTD1: 0.75 * ICT
CTDi:
    IF NOT renal replacement therapy on Day (i - 1) AND phosphate on Day i < 0.65 mmol/l
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

A day is defined as full period from 6:00 to 5:59 on the next day.
The first incomplete period is ignored as well as the first
complete 6:00 to 5:59 period because feeding should start
within 24 to 48 hours.
The last incomplete 6:00 to 5:59 period before discharge from
the intensive care unit is ignored as well.

If `renal replacement therapy` is missing we assume it was not needed.
If `phosphate` is missing  we assume it was normal (means > 0.65 mmol/l).

If `insulin dose` or `calorie intake` is missing we set the values to `NA`.


## Initial Population

All critically ill patients that are 18 years or older during the observation
period.


## Numerator

For each 6:00 to 5:59 period starting at second complete period
the calorie intake has
to be 10 % lower/higher than the individualised daily calorie target.

```
calorie intake >= 0.9 * CTDi AND calorie intake =< 1.1 * CTDi
```


## Numerator Exclusion

First incomplete 6:00 to 5:59 period and first day (first complete 6:00 to 5:59
period) and incomplete last period.


## Denominator

Number of 24 hour periods.


## Denominator Exclusion

First incomplete 6:00 to 5:59 period and first day (first complete 6:00 to 5:59
period) and incomplete last period.
OR
Contraindication to enteral feeding

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
