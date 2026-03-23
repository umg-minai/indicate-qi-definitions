# Indicator 07

## Title

Pain, Sedation and Delirium


## ID

07


## Short Name

07-pain


## Description

Critically ill patients on an intensive care unit are often exposed to painful
stimuli.
(Over-)sediation and Delirium is common (up to 80 % of all critically ill patients).
Monitoring/Detection is important for early treatment and enforced by national
guidelines regularly, at least once per shift.
Due to the lack of monitoring devices the assessment of scores is critical.


## Justification

Pain, (over-)sedation and delirium are associated with increased morbidity and
mortality.


## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions

### 8-hour shift

Each day is divided into 3 shifts/periods per days:
    - 06:00:00 to 13:59:59
    - 14:00:00 to 21:59:59
    - 22:00:00 to 05:59:59

The first and last period of the hospital/intensive care unit stay are ignored
if less than 8 hours.


### Regular measurements

At least one per shift and at least measurement every 10-hours.


## Guidance

We just count complete 8-hour shifts.
The first and last period that are less than 8 hours are ignored.

Pain is assessed with the following scores:
- BPS (behaviour pain scale)
- NRS (numeric (pain) rating scale)
- VAS (visual analog (pain) scale)

Sedation is assessed with the following scores:
- RASS (Richmond agitation-sedation scale)
- RSS (Ramsay sedation scale)

Delirium is assessed with the following scores:
- CAM-ICU (Confusion Assessment Method for the Intensive Care Unit score)
- 3D-CAM (3-minute Diagnostic Interview for CAM-defined delirium score)
- 4AT (4 A's Test for delirium screening)
- DOS (Delirium Observation Score)
- DRS (Delirium Rating Scale score)
- NU-DESC (Nursing Delirium Screening Scale score)
- DDS (Delirium Detection Score)
- ICDSC (Intensive Care Delirium Screening Checklist score)

We are not interested in the value of these assessment.
It is just important that these assessments were done at a given time point.

## Mapping

athena concept ids

GCS:
- 4093836

RASS:
- 36684829

RSS:
- 4105091

NRS:
- 37151627

VAS:
- 4165600

@TODO: IDs for delirium scores are missing in the `minimal_dataset.xlsx`


## Initial Population

All critically ill patients that are 18 years or older during the observation
period.


## Numerator

Should be 1 (pain, sedation and delirium assessed) or 0 (failure) for
an 8-hour shift period.

```
(
    - At least one assessment of pain.
    AND
    - All assessments have to fulfill the following rules:
        - The previous assessment was done less than 10 hours ago.
        (except for the very first assessment of each patient)
        AND
        - It has to be one of NRS, VAS, BPS
)
AND
(
    - At least one assessment of sedation.
    AND
    - All assessments have to fulfill the following rules:
        - The previous assessment was done less than 10 hours ago.
        (except for the very first assessment of each patient)
        AND
        - It has to be one of RASS, RSS
)
AND
(
    - At least one assessment of delirium.
    AND
    - All assessments have to fulfill the following rules:
        - The previous assessment was done less than 10 hours ago.
        (except for the very first assessment of each patient)
        AND
        - It has to be one of CAM-ICU, 3D-CAM, 4AT, DOS, DRS, NU-DESC, DDS,
          ICDSC
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

100 %

## Improvement Notation

A higher ratio indicates improvement.


## References

S3-Leitlinie Analgesie, Sedierung und Delirmanagement in der Intensivmedizin (DAS-Leitlinie)


## Comments

The minimal dataset contains some sedative drugs, we could evaluate whether a
RASS -4 is followed by a decreasing in sedative drugs
However, opioids and NSAIDs are missing, so we can't do this for pain.