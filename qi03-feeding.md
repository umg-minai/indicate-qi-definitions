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

**Notes:**
* Identify intensive care episodes using the concept [Intensive Care (32037)](https://athena.ohdsi.org/search-terms/terms/32037).
  See [INDICATE Mapping recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
  In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence) with `visit_type_concept_id = 32037`.

<!-- inject:GlucoseMeasurements -->
| Concept ID                                                       | Concept Name                             | Descendants | DD Concept Set                                                                                |
|------------------------------------------------------------------|------------------------------------------|-------------|-----------------------------------------------------------------------------------------------|
| [3031266](https://athena.ohdsi.org/search-terms/terms/3031266)   | Glucose [Mass/volume] in Arterial blood  | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [1091312](https://athena.ohdsi.org/search-terms/terms/1091312)   | Glucose [Mass/volume] in Arterial blood… | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3000483](https://athena.ohdsi.org/search-terms/terms/3000483)   | Glucose [Mass/volume] in Blood           | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3011424](https://athena.ohdsi.org/search-terms/terms/3011424)   | Glucose [Mass/volume] in Blood by Autom… | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3014053](https://athena.ohdsi.org/search-terms/terms/3014053)   | Glucose [Mass/volume] in Blood by Test … | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3004077](https://athena.ohdsi.org/search-terms/terms/3004077)   | Glucose [Mass/volume] in Capillary blood | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3034962](https://athena.ohdsi.org/search-terms/terms/3034962)   | Glucose [Mass/volume] in Capillary bloo… | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [1092148](https://athena.ohdsi.org/search-terms/terms/1092148)   | Glucose [Mass/volume] in Mixed venous b… | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3004501](https://athena.ohdsi.org/search-terms/terms/3004501)   | Glucose [Mass/volume] in Serum or Plasma | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [44816672](https://athena.ohdsi.org/search-terms/terms/44816672) | Glucose [Mass/volume] in Serum, Plasma … | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3033408](https://athena.ohdsi.org/search-terms/terms/3033408)   | Glucose [Mass/volume] in Venous blood    | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [1092005](https://athena.ohdsi.org/search-terms/terms/1092005)   | Glucose [Mass/volume] in Venous blood b… | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3044242](https://athena.ohdsi.org/search-terms/terms/3044242)   | Glucose [Moles/volume] in Arterial blood | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3020491](https://athena.ohdsi.org/search-terms/terms/3020491)   | Glucose [Moles/volume] in Blood          | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [43055143](https://athena.ohdsi.org/search-terms/terms/43055143) | Glucose [Moles/volume] in Blood by Auto… | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3040151](https://athena.ohdsi.org/search-terms/terms/3040151)   | Glucose [Moles/volume] in Capillary blo… | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3001501](https://athena.ohdsi.org/search-terms/terms/3001501)   | Glucose [Moles/volume] in Capillary blo… | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [1761753](https://athena.ohdsi.org/search-terms/terms/1761753)   | Glucose [Moles/volume] in Mixed venous … | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3013826](https://athena.ohdsi.org/search-terms/terms/3013826)   | Glucose [Moles/volume] in Serum or Plas… | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [46236948](https://athena.ohdsi.org/search-terms/terms/46236948) | Glucose [Moles/volume] in Serum, Plasma… | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |
| [3038515](https://athena.ohdsi.org/search-terms/terms/3038515)   | Glucose [Moles/volume] in Venous blood   | False       | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) |

| Category                            | Concept ID | Vocabulary | Concept Name                                           | Concept Code | DD Concept Set                                                                                             |
|-------------------------------------|------------|------------|--------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------|
| Intensive Care                      | 32037      | Visit      | Intensive care                                         | OMOP4822460  | N/A                                                                                                        |
| Body height                         | 3036277    | LOINC      | Body height                                            | 8302-2       | [Body height](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=274)                         |
| Body weight                         | 4099154    | SNOMED     | Body weight                                            | 27113001     | [Body weight](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275)                         |
| IBW                                 | 4062985    | SNOMED     | Ideal body weight                                      | 170804003    | [Ideal body weight](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284)                   |
| Energy requirement                  | 4022415    | SNOMED     | Energy requirement                                     | 226244007    | [Energy requirement](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=287)                  |

| Carbon dioxide production           | 21490580   | LOINC      | Carbon dioxide production (VCO2) in Respiratory system | 60825-7      | [Carbon dioxide production](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=311)           |
| Contraindication to enteral feeding | 4141768    | SNOMED     | Medical contraindication to procedure                  | 266757004    | [Contraindication to enteral feeding](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=285) |
| Calorie intake total 24 hour        | 3026267    | LOINC      | Calorie intake total 24 hour                           | 9057-1       | [Energy intake](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=286)                       |

<!-- inject:RenalReplacementTherapyProcedures -->
| Concept ID                                                       | Concept Name                             | Descendants | DD Concept Set                                                                                                      |
|------------------------------------------------------------------|------------------------------------------|-------------|---------------------------------------------------------------------------------------------------------------------|
| [37018292](https://athena.ohdsi.org/search-terms/terms/37018292) | Continuous renal replacement therapy     | yes         | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0 |
| [4049845](https://athena.ohdsi.org/search-terms/terms/4049845)   | Hemodiafiltration                        | no          | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0 |
| [4120120](https://athena.ohdsi.org/search-terms/terms/4120120)   | Hemodialysis                             | no          | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0 |
| [4050864](https://athena.ohdsi.org/search-terms/terms/4050864)   | Hemofiltration                           | no          | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0 |
| [4052538](https://athena.ohdsi.org/search-terms/terms/4052538)   | Intermittent hemodiafiltration           | no          | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0 |
| [4051326](https://athena.ohdsi.org/search-terms/terms/4051326)   | Intermittent hemodialysis                | no          | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0 |
| [4050862](https://athena.ohdsi.org/search-terms/terms/4050862)   | Intermittent hemodialysis with continuo… | no          | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0 |
| [4051327](https://athena.ohdsi.org/search-terms/terms/4051327)   | Intermittent hemodialysis with sequenti… | no          | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0 |
| [4050865](https://athena.ohdsi.org/search-terms/terms/4050865)   | Intermittent hemofiltration              | no          | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0 |
| [619390](https://athena.ohdsi.org/search-terms/terms/619390)     | Prolonged intermittent renal replacemen… | no          | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0 |
| [44783963](https://athena.ohdsi.org/search-terms/terms/44783963) | Sustained low-efficiency dialysis        | no          | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0 |

| Category                  | Concept ID | Vocabulary | Concept Name                                                                                                                                                            | Concept Code | DD Concept Set                                                                                   |
|---------------------------|------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------|
| Renal replacement therapy | 37018292   | SNOMED     | Continuous renal replacement therapy, incl. all SNOMED descendants (CVVH, CVVHD, CVVHDF, CAVH, CAVHD, CAVHDF, continuous hemodialysis/hemofiltration/hemodiafiltration) | 714749008    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) |
| Renal replacement therapy | 4120120    | SNOMED     | Hemodialysis                                                                                                                                                            | 302497006    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) |
| Renal replacement therapy | 4050864    | SNOMED     | Hemofiltration                                                                                                                                                          | 233581009    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) |
| Renal replacement therapy | 4049845    | SNOMED     | Hemodiafiltration                                                                                                                                                       | 233586004    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) |
| Renal replacement therapy | 4051326    | SNOMED     | Intermittent hemodialysis                                                                                                                                               | 233575001    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) |
| Renal replacement therapy | 4050862    | SNOMED     | Intermittent hemodialysis with continuous ultrafiltration                                                                                                               | 233577009    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) |
| Renal replacement therapy | 4051327    | SNOMED     | Intermittent hemodialysis with sequential ultrafiltration                                                                                                               | 233576000    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) |
| Renal replacement therapy | 4050865    | SNOMED     | Intermittent hemofiltration                                                                                                                                             | 233582002    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) |
| Renal replacement therapy | 4052538    | SNOMED     | Intermittent hemodiafiltration                                                                                                                                          | 233587008    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) |
| Renal replacement therapy | 44783963   | SNOMED     | Sustained low-efficiency dialysis                                                                                                                                       | 698074000    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) |
| Renal replacement therapy | 619390     | SNOMED     | Prolonged intermittent renal replacement therapy                                                                                                                        | 895382009    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) |

<!-- inject:PhosphateMeasurements -->
| Concept ID                                                     | Concept Name                             | Descendants | DD Concept Set                                                                                         |
|----------------------------------------------------------------|------------------------------------------|-------------|--------------------------------------------------------------------------------------------------------|
| [3024232](https://athena.ohdsi.org/search-terms/terms/3024232) | Phosphate [Mass/volume] in Blood         | no          | [Phosphate in blood (210)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) v1.1.0 |
| [3011904](https://athena.ohdsi.org/search-terms/terms/3011904) | Phosphate [Mass/volume] in Serum or Pla… | no          | [Phosphate in blood (210)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) v1.1.0 |
| [3018913](https://athena.ohdsi.org/search-terms/terms/3018913) | Phosphate [Moles/volume] in Blood        | no          | [Phosphate in blood (210)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) v1.1.0 |
| [3003458](https://athena.ohdsi.org/search-terms/terms/3003458) | Phosphate [Moles/volume] in Serum or Pl… | no          | [Phosphate in blood (210)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) v1.1.0 |

| Category  | Concept ID | Vocabulary | Concept Name                                | Concept Code | DD Concept Set                                                                          |
|-----------|------------|------------|---------------------------------------------|--------------|-----------------------------------------------------------------------------------------|
| Phosphate | 3003458    | LOINC      | Phosphate [Moles/volume] in Serum or Plasma | 14879-1      | [Plasma phosphate](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) |
| Phosphate | 3018913    | LOINC      | Phosphate [Moles/volume] in Blood           | 24519-1      | [Plasma phosphate](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) |
| Phosphate | 3024232    | LOINC      | Phosphate [Mass/volume] in Blood            | 2774-8       | [Plasma phosphate](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) |
| Phosphate | 3011904    | LOINC      | Phosphate [Mass/volume] in Serum or Plasma  | 2777-1       | [Plasma phosphate](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) |

All concepts from the following insulin concept sets in the INDICATE Data Dictionary:

<!-- inject:InsulinDrugs -->
| Concept ID                                                       | Concept Name             | Descendants | DD Concept Set                                                                                               |
|------------------------------------------------------------------|--------------------------|-------------|--------------------------------------------------------------------------------------------------------------|
| [1567198](https://athena.ohdsi.org/search-terms/terms/1567198)   | insulin aspart, human    | yes         | [Insulin Aspart, Human (123)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=123) v1.0.1    |
| [35602717](https://athena.ohdsi.org/search-terms/terms/35602717) | insulin degludec         | yes         | [Insulin Degludec (124)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=124) v1.0.1         |
| [1516976](https://athena.ohdsi.org/search-terms/terms/1516976)   | insulin detemir          | yes         | [Insulin Detemir (125)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=125) v1.0.1          |
| [1502905](https://athena.ohdsi.org/search-terms/terms/1502905)   | insulin glargine         | yes         | [Insulin Glargine (126)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=126) v1.0.1         |
| [1544838](https://athena.ohdsi.org/search-terms/terms/1544838)   | insulin glulisine, human | yes         | [Insulin Glulisine, Human (127)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=127) v1.0.1 |

| Concept Set Name | Number of Concepts | DD Concept Set |
|------------------|--------------------|----------------|
| Insulin Aspart | 14 | [Insulin Aspart](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=122) |
| Insulin Aspart, Human | 26 | [Insulin Aspart, Human](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=123) |
| Insulin Degludec | 19 | [Insulin Degludec](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=124) |
| Insulin Detemir | 11 | [Insulin Detemir](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=125) |
| Insulin Glargine | 38 | [Insulin Glargine](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=126) |
| Insulin Glulisine, Human | 13 | [Insulin Glulisine, Human](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=127) |

@NOTE: @Jan maybe we have to redefine our 24 h period if the calorie intake
counter is reset at a given time (e.g. every morning at 6:00)

## Guidance

The calorie target should be
1. The `minimal_dataset` defines an "energy requirement" item which should be used if available (may be based on indirect calorimetry, carbon dioxide production rate or formulas).
2. Continuously estimated by the carbon dioxide production rate (VCO2) measured by the ventilator -- the median of the last 24 hours should be used.
3. Estimated using a formula.

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

If no insulin dosage information is available for a given 24 h period,
0 IE/h is used as the insulin dosage for that period.

```
CTD0 (calorie target day 0): 0 [first 24 hours are ignored]
CTD1: 0.75 * ICT
CTDi:
    IF NOT renal replacement therapy on Day (i - 1) AND phosphate on Day i < 0.65 mmol/l
        AND CTD(i-1) >= 0.5 * ICT
        AND maximum insulin dose on Day (i - 1) <= 4 IE/h
        0.25 * ICT
    ELSE IF maximum insulin dose on Day (i - 1) < 2 IE/h
        Min(CTD(i-1) + 0.25 * ICT, ICT)
    ELSE IF (maximum insulin dose on Day (i - 1) >= 2 IE/h AND <= 4 IE/h)
        Max(CTD(i-1) - 0.25 * ICT, 0)
    ELSE IF maximum insulin dose on Day (i - 1) > 4 IE/h
        Max(CTD(i-1) - 0.5 * ICT, 0)
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

- Stapel et al. Critical Care (2015) 19:370
  DOI 10.1186/s13054-015-1087-2

- Elke et al.
  DGEM-Leitlinie: „Klinische Ernährung in der Intensivmedizin“


## Comments

// Contraindications missing:
- shock - we could use the ((nor-)epinephrine dose?,
- acidosis (we could use the pH)
- upper gastrointestinal bleeding (not part of the minimal dataset)?
- ileus (not part of the minimal dataset)?
