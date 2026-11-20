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


| Category                            | Concept ID | Vocabulary | Concept Name                                           | Concept Code | DD Concept Set                                                                                             |
|-------------------------------------|------------|------------|--------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------|
| Intensive Care                      | 32037      | Visit      | Intensive care                                         | OMOP4822460  | N/A                                                                                                        |
| Body height                         | 3036277    | LOINC      | Body height                                            | 8302-2       | [Body height](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=274)                         |
| Body weight                         | 4099154    | SNOMED     | Body weight                                            | 27113001     | [Body weight](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275)                         |
| IBW                                 | 4062985    | SNOMED     | Ideal body weight                                      | 170804003    | [Ideal body weight](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284)                   |
| IBW                                 | 3032445    | LOINC      | Ideal body weight                                      | 50064-5      | [Ideal body weight](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284)                   |
| Energy requirement                  | 4022415    | SNOMED     | Energy requirement                                     | 226244007    | [Energy requirement](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=287)                  |
| Carbon dioxide production           | 21490580   | LOINC      | Carbon dioxide production (VCO2) in Respiratory system | 60825-7      | [Carbon dioxide production](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=311)           |
| Contraindication to feeding         | 2100000009 | INDICATE   | Contraindication to feeding                            | contraindication-to-feeding | [Contraindication to feeding](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=285) |
| Calorie intake total 24 hour        | 3026267    | LOINC      | Calorie intake total 24 hour                           | 9057-1       | [Energy intake](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=286)                       |
| Renal replacement therapy           | 37018292   | SNOMED     | Continuous renal replacement therapy, incl. all SNOMED descendants (CVVH, CVVHD, CVVHDF, CAVH, CAVHD, CAVHDF, continuous hemodialysis/hemofiltration/hemodiafiltration) | 714749008    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298)           |
| Renal replacement therapy           | 4120120    | SNOMED     | Hemodialysis                                           | 302497006    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298)           |
| Renal replacement therapy           | 4050864    | SNOMED     | Hemofiltration                                         | 233581009    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298)           |
| Renal replacement therapy           | 4049845    | SNOMED     | Hemodiafiltration                                      | 233586004    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298)           |
| Renal replacement therapy           | 4051326    | SNOMED     | Intermittent hemodialysis                              | 233575001    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298)           |
| Renal replacement therapy           | 4050862    | SNOMED     | Intermittent hemodialysis with continuous ultrafiltration | 233577009    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298)           |
| Renal replacement therapy           | 4051327    | SNOMED     | Intermittent hemodialysis with sequential ultrafiltration | 233576000    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298)           |
| Renal replacement therapy           | 4050865    | SNOMED     | Intermittent hemofiltration                            | 233582002    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298)           |
| Renal replacement therapy           | 4052538    | SNOMED     | Intermittent hemodiafiltration                         | 233587008    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298)           |
| Renal replacement therapy           | 44783963   | SNOMED     | Sustained low-efficiency dialysis                      | 698074000    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298)           |
| Renal replacement therapy           | 619390     | SNOMED     | Prolonged intermittent renal replacement therapy       | 895382009    | [Renal replacement therapy](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298)           |
| Phosphate                           | 3003458    | LOINC      | Phosphate [Moles/volume] in Serum or Plasma            | 14879-1      | [Plasma phosphate](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210)                    |
| Phosphate                           | 3018913    | LOINC      | Phosphate [Moles/volume] in Blood                      | 24519-1      | [Plasma phosphate](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210)                    |
| Phosphate                           | 3024232    | LOINC      | Phosphate [Mass/volume] in Blood                       | 2774-8       | [Plasma phosphate](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210)                    |
| Phosphate                           | 3011904    | LOINC      | Phosphate [Mass/volume] in Serum or Plasma             | 2777-1       | [Plasma phosphate](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210)                    |

All concepts from the following insulin concept sets in the INDICATE Data Dictionary:

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

<!-- inject:Insulin Aspart, Human|Insulin Degludec|Insulin Detemir|Insulin Glargine|Insulin Glulisine, Human|Phosphate in blood|Body height|Body weight|Ideal body weight|Enteral feeding|Contraindication to enteral feeding|Energy intake per 24 hours|Energy requirement per 24 hours|Renal replacement therapy (RRT)|Carbon dioxide production (VCO2) -->
| Priority | Concept ID                                                       | Descendants | Vocabulary | Concept Name                               | Concept Code                        | DD Concept Set                                                                                                         |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [1567198](https://athena.ohdsi.org/search-terms/terms/1567198)   | yes         | RxNorm     | insulin aspart, human                      | 51428                               | [Insulin Aspart, Human (123)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=123) v1.1.0              |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [35602717](https://athena.ohdsi.org/search-terms/terms/35602717) | yes         | RxNorm     | insulin degludec                           | 1670007                             | [Insulin Degludec (124)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=124) v1.0.1                   |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [1516976](https://athena.ohdsi.org/search-terms/terms/1516976)   | yes         | RxNorm     | insulin detemir                            | 139825                              | [Insulin Detemir (125)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=125) v1.0.1                    |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [1502905](https://athena.ohdsi.org/search-terms/terms/1502905)   | yes         | RxNorm     | insulin glargine                           | 274783                              | [Insulin Glargine (126)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=126) v1.0.1                   |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [1544838](https://athena.ohdsi.org/search-terms/terms/1544838)   | yes         | RxNorm     | insulin glulisine, human                   | 400008                              | [Insulin Glulisine, Human (127)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=127) v1.0.1           |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [3024232](https://athena.ohdsi.org/search-terms/terms/3024232)   | no          | LOINC      | Phosphate \[Mass/volume\] in Blood         | 2774-8                              | [Phosphate in blood (210)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) v1.1.0                 |
|          | [3011904](https://athena.ohdsi.org/search-terms/terms/3011904)   | no          | LOINC      | Phosphate \[Mass/volume\] in Serum or Pla… | 2777-1                              | [Phosphate in blood (210)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) v1.1.0                 |
|          | [3018913](https://athena.ohdsi.org/search-terms/terms/3018913)   | no          | LOINC      | Phosphate \[Moles/volume\] in Blood        | 24519-1                             | [Phosphate in blood (210)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) v1.1.0                 |
|          | [3003458](https://athena.ohdsi.org/search-terms/terms/3003458)   | no          | LOINC      | Phosphate \[Moles/volume\] in Serum or Pl… | 14879-1                             | [Phosphate in blood (210)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=210) v1.1.0                 |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [3036277](https://athena.ohdsi.org/search-terms/terms/3036277)   | no          | LOINC      | Body height                                | 8302-2                              | [Body height (274)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=274) v1.2.0                        |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [3025315](https://athena.ohdsi.org/search-terms/terms/3025315)   | no          | LOINC      | Body weight                                | 29463-7                             | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [4099154](https://athena.ohdsi.org/search-terms/terms/4099154)   | no          | SNOMED     | Body weight                                | 27113001                            | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [4178502](https://athena.ohdsi.org/search-terms/terms/4178502)   | no          | SNOMED     | Body weight measure                        | 363808001                           | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [3013762](https://athena.ohdsi.org/search-terms/terms/3013762)   | no          | LOINC      | Body weight Measured                       | 3141-9                              | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [3013853](https://athena.ohdsi.org/search-terms/terms/3013853)   | no          | LOINC      | Body weight Measured --ante partum         | 8338-6                              | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [3009617](https://athena.ohdsi.org/search-terms/terms/3009617)   | no          | LOINC      | Body weight Measured --post dialysis       | 8344-4                              | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [3010147](https://athena.ohdsi.org/search-terms/terms/3010147)   | no          | LOINC      | Body weight Measured --post partum         | 8345-1                              | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [3015644](https://athena.ohdsi.org/search-terms/terms/3015644)   | no          | LOINC      | Body weight Measured --postoperative       | 8346-9                              | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [3019336](https://athena.ohdsi.org/search-terms/terms/3019336)   | no          | LOINC      | Body weight Measured --pre dialysis        | 8347-7                              | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [3005422](https://athena.ohdsi.org/search-terms/terms/3005422)   | no          | LOINC      | Body weight Measured --preoperative        | 8349-3                              | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [40761330](https://athena.ohdsi.org/search-terms/terms/40761330) | no          | LOINC      | Body weight Measured --when specimen ta…   | 58229-6                             | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [3010220](https://athena.ohdsi.org/search-terms/terms/3010220)   | no          | LOINC      | Body weight Measured --with clothes        | 8350-1                              | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [3011054](https://athena.ohdsi.org/search-terms/terms/3011054)   | no          | LOINC      | Body weight Measured --without clothes     | 8351-9                              | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [4310154](https://athena.ohdsi.org/search-terms/terms/4310154)   | no          | SNOMED     | Body weight with shoes                     | 424927000                           | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [4175354](https://athena.ohdsi.org/search-terms/terms/4175354)   | no          | SNOMED     | Body weight without shoes                  | 425024002                           | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [42536495](https://athena.ohdsi.org/search-terms/terms/42536495) | no          | SNOMED     | Current body weight                        | 735395000                           | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [37160438](https://athena.ohdsi.org/search-terms/terms/37160438) | no          | SNOMED     | Post-amputation measured body weight       | 1162415002                          | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [37160443](https://athena.ohdsi.org/search-terms/terms/37160443) | no          | SNOMED     | Post-dialysis body weight                  | 1162420002                          | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|          | [37160447](https://athena.ohdsi.org/search-terms/terms/37160447) | no          | SNOMED     | Pre-dialysis body weight                   | 1162421003                          | [Body weight (275)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=275) v1.2.0                        |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [4062985](https://athena.ohdsi.org/search-terms/terms/4062985)   | no          | SNOMED     | Ideal body weight                          | 170804003                           | [Ideal body weight (284)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284) v1.2.0                  |
|          | [3032445](https://athena.ohdsi.org/search-terms/terms/3032445)   | no          | LOINC      | Ideal body weight                          | 50064-5                             | [Ideal body weight (284)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284) v1.2.0                  |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [4042005](https://athena.ohdsi.org/search-terms/terms/4042005)   | yes         | SNOMED     | Enteral feeding                            | 229912004                           | [Enteral feeding (293)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=293) v1.2.0                    |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | 2100000009                                                       | no          | INDICATE   | Contraindication to enteral feeding        | contraindication-to-enteral-feeding | [Contraindication to enteral feedi… (285)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=285) v1.1.0 |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [46234687](https://athena.ohdsi.org/search-terms/terms/46234687) | no          | LOINC      | Calorie intake 24 hour                     | 75302-0                             | [Energy intake per 24 hours (286)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=286) v1.2.0         |
|          | [46235231](https://athena.ohdsi.org/search-terms/terms/46235231) | no          | LOINC      | Calorie intake 24 hour Estimated           | 75298-0                             | [Energy intake per 24 hours (286)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=286) v1.2.0         |
|          | [21493096](https://athena.ohdsi.org/search-terms/terms/21493096) | no          | LOINC      | Calorie intake 24 hour Measured            | 80494-8                             | [Energy intake per 24 hours (286)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=286) v1.2.0         |
|          | [3026267](https://athena.ohdsi.org/search-terms/terms/3026267)   | no          | LOINC      | Calorie intake total 24 hour               | 9057-1                              | [Energy intake per 24 hours (286)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=286) v1.2.0         |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [604877](https://athena.ohdsi.org/search-terms/terms/604877)     | no          | SNOMED     | Estimated required quantity of energy i…   | 1003837001                          | [Energy requirement per 24 hours (287)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=287) v1.3.0    |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [37018292](https://athena.ohdsi.org/search-terms/terms/37018292) | yes         | SNOMED     | Continuous renal replacement therapy       | 714749008                           | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0    |
|          | [4049845](https://athena.ohdsi.org/search-terms/terms/4049845)   | no          | SNOMED     | Hemodiafiltration                          | 233586004                           | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0    |
|          | [4120120](https://athena.ohdsi.org/search-terms/terms/4120120)   | no          | SNOMED     | Hemodialysis                               | 302497006                           | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0    |
|          | [4050864](https://athena.ohdsi.org/search-terms/terms/4050864)   | no          | SNOMED     | Hemofiltration                             | 233581009                           | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0    |
|          | [4052538](https://athena.ohdsi.org/search-terms/terms/4052538)   | no          | SNOMED     | Intermittent hemodiafiltration             | 233587008                           | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0    |
|          | [4051326](https://athena.ohdsi.org/search-terms/terms/4051326)   | no          | SNOMED     | Intermittent hemodialysis                  | 233575001                           | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0    |
|          | [4050862](https://athena.ohdsi.org/search-terms/terms/4050862)   | no          | SNOMED     | Intermittent hemodialysis with continuo…   | 233577009                           | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0    |
|          | [4051327](https://athena.ohdsi.org/search-terms/terms/4051327)   | no          | SNOMED     | Intermittent hemodialysis with sequenti…   | 233576000                           | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0    |
|          | [4050865](https://athena.ohdsi.org/search-terms/terms/4050865)   | no          | SNOMED     | Intermittent hemofiltration                | 233582002                           | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0    |
|          | [619390](https://athena.ohdsi.org/search-terms/terms/619390)     | no          | SNOMED     | Prolonged intermittent renal replacemen…   | 895382009                           | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0    |
|          | [44783963](https://athena.ohdsi.org/search-terms/terms/44783963) | no          | SNOMED     | Sustained low-efficiency dialysis          | 698074000                           | [Renal replacement therapy (RRT) (298)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=298) v1.1.0    |
|---       |---                                                               |---          |---         |---                                         |---                                  |---                                                                                                                     |
|          | [21490580](https://athena.ohdsi.org/search-terms/terms/21490580) | no          | LOINC      | Carbon dioxide production (VCO2) in Res…   | 60825-7                             | [Carbon dioxide production (VCO2) (311)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=311) v1.0.0   |

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
Contraindication to feeding

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
