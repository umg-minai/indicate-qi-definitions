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

Each day is divided into 3 shifts/periods per days:
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


## Guidance

We expect SI units.
To convert blood glucose levels in mg/dl into mmol/l: mg/dl = 1/18.02 mmol/l.

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