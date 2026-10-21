# Indicator 04

## Title

Maintaining appropriate glucose levels.

## ID

04

## Short Name

04-glc-ctrl


## Description

The blood glucose levels of critically ill patients should be kept within
an acceptable range.
Regular measurements, at least once per shift and possibly corrective
treatments are required.
The type of treatment differs depending on the type of derangement of blood
glucose disorder, and is not included in this quality indicator.


## Justification

Hypo- and Hyperglycemia have been associated with increased morbidity and
mortality in critically ill patients.


## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions

### Acceptable blood glucose levels

3.3 mmol/l to 10.0 mmol/l


### 8-hour shift

Each day is divided into 3 shifts/periods:
- 06:00:00 to 13:59:59
- 14:00:00 to 21:59:59
- 22:00:00 to 05:59:59

The first and last period of the hospital/intensive care unit stay are ignored
if less than 8 hours.


### Regular measurements

At least one measurement every 10-hours.
If the blood glucose level is not within the acceptable range we expect a
treatment and a control measurement in the next 2 hours.


### Successful treatment

A treatment is considered successful if the blood glucose level is in the
acceptable range or the next one is at least 20 % higher/lower
(e.q. closer to the acceptable range).


## Mapping

**Notes:**
* Identify intensive care episodes using the concept [Intensive Care (32037)](https://athena.ohdsi.org/search-terms/terms/32037).
  See [INDICATE Mapping recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
  In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence) with `visit_type_concept_id = 32037`.

<!-- inject:GlucoseMeasurements -->
| Concept ID                                                       | Concept Name                             | Descendants | DD Concept Set                                                                                       |
|---                                                               |---                                       |---          |---                                                                                                   |
| [3031266](https://athena.ohdsi.org/search-terms/terms/3031266)   | Glucose [Mass/volume] in Arterial blood  | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [1091312](https://athena.ohdsi.org/search-terms/terms/1091312)   | Glucose [Mass/volume] in Arterial blood… | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3000483](https://athena.ohdsi.org/search-terms/terms/3000483)   | Glucose [Mass/volume] in Blood           | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3011424](https://athena.ohdsi.org/search-terms/terms/3011424)   | Glucose [Mass/volume] in Blood by Autom… | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3014053](https://athena.ohdsi.org/search-terms/terms/3014053)   | Glucose [Mass/volume] in Blood by Test … | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3004077](https://athena.ohdsi.org/search-terms/terms/3004077)   | Glucose [Mass/volume] in Capillary blood | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3034962](https://athena.ohdsi.org/search-terms/terms/3034962)   | Glucose [Mass/volume] in Capillary bloo… | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [1092148](https://athena.ohdsi.org/search-terms/terms/1092148)   | Glucose [Mass/volume] in Mixed venous b… | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3004501](https://athena.ohdsi.org/search-terms/terms/3004501)   | Glucose [Mass/volume] in Serum or Plasma | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [44816672](https://athena.ohdsi.org/search-terms/terms/44816672) | Glucose [Mass/volume] in Serum, Plasma … | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3033408](https://athena.ohdsi.org/search-terms/terms/3033408)   | Glucose [Mass/volume] in Venous blood    | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [1092005](https://athena.ohdsi.org/search-terms/terms/1092005)   | Glucose [Mass/volume] in Venous blood b… | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3044242](https://athena.ohdsi.org/search-terms/terms/3044242)   | Glucose [Moles/volume] in Arterial blood | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3020491](https://athena.ohdsi.org/search-terms/terms/3020491)   | Glucose [Moles/volume] in Blood          | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [43055143](https://athena.ohdsi.org/search-terms/terms/43055143) | Glucose [Moles/volume] in Blood by Auto… | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3040151](https://athena.ohdsi.org/search-terms/terms/3040151)   | Glucose [Moles/volume] in Capillary blo… | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3001501](https://athena.ohdsi.org/search-terms/terms/3001501)   | Glucose [Moles/volume] in Capillary blo… | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [1761753](https://athena.ohdsi.org/search-terms/terms/1761753)   | Glucose [Moles/volume] in Mixed venous … | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3013826](https://athena.ohdsi.org/search-terms/terms/3013826)   | Glucose [Moles/volume] in Serum or Plas… | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [46236948](https://athena.ohdsi.org/search-terms/terms/46236948) | Glucose [Moles/volume] in Serum, Plasma… | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |
| [3038515](https://athena.ohdsi.org/search-terms/terms/3038515)   | Glucose [Moles/volume] in Venous blood   | no          | [Glucose in blood (207)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=207) v1.1.0 |

## Guidance

We expect SI units.
To convert blood glucose levels in mg/dl into mmol/l: mg/dl = 1/18 mmol/l.

We just count complete 8-hour shifts.
The first and last period that are less than 8 hours are ignored.


## Initial Population

All critically ill patients that are 18 years or older during the observation
period.


## Numerator

Should be 1 (successful glucose control) or 0 (failure) for an 8-hour shift
period.

A successful glucose control for an 8-hour shift period is defined as:

```
- At least one measurement in an 8-hour shift period.
AND
- All measurements have to fulfill the following rules:
    - The previous blood glucose measurement was taken less than 10 hours ago.
        (except for the very first measurement of each patient)
    AND
    (
        - The blood glucose level is within the acceptable range.
        OR
        (
            - It is followed by another measurement within 2 hours
            (could be in the next period).
            AND
            - The follow-up measurement is:
            (
                - Within the acceptable range.
                OR
                - Increased by at least 20 %:
                  current measurement < lower acceptable range AND
                  follow-up measurement < lower acceptable range AND
                  current measurement * 1.2 < follow-up measurement
                OR
                - Decreased by at least 20 %:
                  current measurement > upper acceptable range AND
                  follow-up measurement > upper acceptable range AND
                  current measurement * 0.8 > follow-up measurement
            )
        )
    )
```

The numerator is the sum of the results above for each 8-hour shift period.


## Numerator Exclusion

First and last incomplete 8-hour shift period.


## Denominator

Number of 8-hour shifts.


## Denominator Exclusion

First and last incomplete 8-hour shift period.


## Expected

80 % (one failure in 48 hours)


## Improvement Notation

A higher ratio indicates improvement.


## Comments
