# Indicator 06

## Title

Infection rate pneumonia + catheters


## ID

06


## Short Name

06-infection


## Description

This quality indicator compares the incidence of ventilator associated pneumonia
and catheter-related infections.


## Justification

Ventilator associated pneumonia and catheter-related infections
is associated with a longer length of stay and an
increased mortality in critically ill patients.
High rates of ventilator associated pneumonia and catheter-related infections
are a surrogate for poor hygiene practices.


## Measuring Score

Incidences.


## Measuring Type

Outcome.


## Stratification

None.


## Definitions

### Catheter-related bloodstream infection (CRBSI).

The incidence is calculated as number of CRBSI per 1000 catheter days
(across the whole ward/hospital).
We just consider central venous catheters (CVCs).

### Ventilator associated pneumonia

Ventilator associated pneumonia (VAP) is defined as lung infection that occurs
in patients who are on invasive mechanical ventilation for more than 48 hours.
The incidence is calculated as number of VAPs per 1000 days on invasive
mechanical ventilation (across the whole ward/hospital).

### Combine infection rate endpoint

We define a combined infection rate (IR) endpoint that is the sum of
the CRBSI incidence and VAP incidence.


## Mapping

athena concept ids

CRBSI, could be one of:
- 42537216 (general, CRBSI)
- 4149606 (infection of intravenous catheter)
- 764921 (infection of hemodialyses catheter)

CVC:
- 4179206

CVC insertion, any of:
- 4052413 (insertion)
- 4051188 (insertion via internal jugular vein)
- 4052415 (insertion via subclavian vein)
- 4052416 (insertion via femoral vein)

CVC removal:
- 4022792

invasive ventilation:
- 37158404

VAP:
- 429271009


## Guidance

To determine the number of days on a ventilator or days of a CVC we use
the difference between end of ventilation/removal of the CVC and start of
ventilation/insertion of the CVC in hours divided by 24 hours.

Days on invasive ventilation (DV):
(time of end of invasive ventilation - time of start of invasive ventilation)[h] / 24 h

CVC days (CD):
(time of removal of the CVC - time of insertion of the CVC)[h] / 24 h

Note:
Maybe CVC days have to be calulated manually with the mappings
for *CVC removal* and *CVC insertion*, or the *CVC* mapping contains end/start
information.

The incidence of VAP/CRBSI is calculated by
VAPI = VAP / DV * 1000
or
CRBSII = CRBSI / CD * 1000

The combinded endpoint IR is calculated as follows:
IR = VAPI + CRBSII

## Initial Population

All critically ill patients that are 18 years or older
    AND have been on the ICU for more than 24 hours
during the observation period.

## Value

IR per 1000 (CVC/ventilator) days.


## Value Exclusion

None.


## Expected

Less than 5 per 1000 days.


## Improvement Notation

A lower incidence indicates improvement.


## References

Rademacher et al. 2024
S3-Leitlinie Epidemiologie, Diagnostik und Therapie erwachsener Patienten mit nosokomialer
Pneumonie

KRINKO 2017
https://www.rki.de/DE/Themen/Infektionskrankheiten/Krankenhaushygiene/KRINKO/Empfehlungen-der-KRINKO/Device-assoziierte-postoperative-Infektionen/Tabelle_Gefaesskath_Rili.html

## Comments