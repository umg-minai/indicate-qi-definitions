# Indicator 05

## Title

Prevention of venous thromboembolism


## ID

05


## Short Name

05-vte-prev


## Description

Venous thromboembolism (VTE) is a frequent complication that contributes
significantly to morbidity and mortality among critically ill patients.
Pharmacologic thromboprophylaxis should reduce VTE.


## Justification

The use of prophylactic measures against deep vein thromboembolism (DVTE) during the
ICU stay is associated with a decrease in morbidity and mortality due to thromboembolism.


## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions


## Mapping

use `omop_concept_id` of all drugs with the `subcategory` *Anticoagulants* in the `minimal_data_dictonary`.

and add

Certoparin (is missing in `minimal_dataset`)
- 19016072


## Guidance


## Initial Population

All critically ill patients that are 18 years or older during the observation
period.


## Numerator

For each 24 hour period starting at admission + 24 hours
at least one drug of the ones listed in *Mapping* should be used.


## Numerator Exclusion

First 24 hours and incomplete last 24 hour period.


## Denominator

Number of 24 hour periods.


## Denominator Exclusion

First 24 hours and incomplete last 24 hour period


## Expected

100 %


## Improvement Notation

A higher ratio indicates improvement.


## References

Arabi, Y.M., Mehta, S. Venous thromboprophylaxis in the ICU: navigating evidence, risk, and practice gaps. Intensive Care Med 51, 1508–1510 (2025). https://doi.org/10.1007/s00134-025-08009-6


## Comments