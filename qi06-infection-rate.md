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

**Notes:**
* Identify intensive care episodes using the Intensive Care concept (32037). See [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary-content/#/mapping-recommendations). In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence)) with `visit_type_concept_id = 32037`.


| Category | Concept ID | Vocabulary | Concept Name | Concept Code | DD Concept Set |
|----------|------------|------------|--------------|--------------|----------------|
| Intensive Care | 32037 | Visit | Intensive care | OMOP4822460 | N/A |
| CRBSI | 42537216 | SNOMED | Catheter related bloodstream infection | 788163003 | [Catheter infection](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=31) |
| CRBSI | 764921 | SNOMED | Infection of hemodialysis catheter | 6011000124100 | [Catheter infection](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=31) |
| CRBSI | 4149606 | SNOMED | Infection of intravenous catheter | 312133006 | [Catheter infection](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=31) |
| CVC | 4179206 | SNOMED | Central venous catheter | 52124006 | [Central venous catheter](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=291) |
| CVC insertion | 4052413 | SNOMED | Central venous cannula insertion | 233527006 | [Central venous catheter](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=291) |
| CVC insertion | 4051188 | SNOMED | Central venous cannula insertion via internal jugular vein | 233523003 | [Central venous catheter](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=291) |
| CVC insertion | 4052415 | SNOMED | Central venous cannula insertion via subclavian vein | 233529009 | [Central venous catheter](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=291) |
| CVC insertion | 4052416 | SNOMED | Central venous cannula insertion via femoral vein | 233530004 | [Central venous catheter](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=291) |
| CVC removal | 4022792 | SNOMED | Removal of central venous line | 225749003 | [Central venous catheter](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=291) |
| Invasive ventilation | 37158404 | SNOMED | Invasive mechanical ventilation | 1258985005 | [Invasive mechanical ventilation](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=306) |
| VAP | 259992 | SNOMED | Ventilator associated pneumonia | 429271009 | [Ventilator-associated pneumonia](https://indicate-eu.github.io/data-dictionary-content/#/concept-sets?id=32) |


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