# Indicator 02

## Title

Weaning from mechanical ventilation.


## ID

02


## Short Name

02-weaning


## Description

The duration of mechanical ventilation should be as short as possible.
Daily spontaneus breathing trial seem to be important for a fast weaning.


## Justification



## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions

There is not a international definition of spontaneus breathing trial.

We expect a "Trial of spontaneous breathing" entry.


## Mapping

**Notes:**
* Identify intensive care episodes using the Intensive Care concept (32037).
  See [INDICATE Mapping recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
  In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence)) with `visit_type_concept_id = 32037`.


| Category                        | Concept ID | Descendants | Vocabulary | Concept Name                                        | Concept Code | DD Concept Set                                                                                         |
|---------------------------------|------------|-------------|------------|-----------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------|
| Intensive Care                  | 32037      | No          | Visit      | Intensive care                                      | OMOP4822460  | N/A                                                                                                    |
|---------------------------------|------------|-------------|------------|-----------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------|
| Intubated (Device exposure)     | 4097216    | Yes         | SNOMED     | Endotracheal tube                                   | 26412008     | [Endotracheal tube](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=299)               |
|---------------------------------|------------|-------------|------------|-----------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------|
| Intubated (Procedure)           | 4119642    | No          | SNOMED     | Awake intubation                                    | 304341005    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4337045    | No          | SNOMED     | Blind nasal intubation                              | 232681006    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4140765    | No          | SNOMED     | Digital assisted intubation                         | 427331009    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4082243    | No          | SNOMED     | Emergency laryngeal intubation                      | 182682004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4335585    | No          | SNOMED     | Endobronchial intubation                            | 232687005    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4058031    | No          | SNOMED     | Endotracheal intubation, emergency procedure        | 16883004     | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 37116698   | No          | SNOMED     | Insertion of double lumen tracheobronchial tube     | 733509002    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4013354    | No          | SNOMED     | Insertion of endotracheal tube                      | 112798008    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4179373    | No          | SNOMED     | Insertion of endotracheal tube using laryngoscope   | 429161001    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4283807    | No          | SNOMED     | Intubation of larynx                                | 66861000     | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 40487536   | No          | SNOMED     | Intubation of respiratory tract                     | 447996002    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4056812    | No          | SNOMED     | Laryngeal intubation for inhalation                 | 182709001    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4335584    | No          | SNOMED     | Nasal intubation awake                              | 232680007    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4337617    | No          | SNOMED     | Nasotracheal fiberoptic intubation                  | 232682004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4337616    | No          | SNOMED     | Nasotracheal intubation                             | 232679009    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4339623    | No          | SNOMED     | Oral intubation awake                               | 232675003    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4337615    | No          | SNOMED     | Orotracheal fiberoptic intubation                   | 232678001    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4335481    | No          | SNOMED     | Orotracheal intubation                              | 232674004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4287921    | No          | SNOMED     | Retrograde intubation                               | 397892004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4303945    | No          | SNOMED     | Tracheal intubation through a laryngeal mask airway | 418613003    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Procedure)           | 4335583    | No          | SNOMED     | Tracheal intubation using rigid bronchoscope        | 232677006    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
|---------------------------------|------------|-------------|------------|-----------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------|
| Intubated (Observation)         | 36660691   | No          | LOINC      | Difficult intubation                                | 95050-1      | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
| Intubated (Meas value)          | 36309319   | No          | LOINC      | Unplanned intubation                                | LA20580-9    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)         |
|---------------------------------|------------|-------------|------------|-----------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------|
| Extubation (Procedure)          | 4148972    | No          | SNOMED     | Extubation of trachea (normal)                      | 309812005    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                      |
| Extubation (Procedure)          | 4150627    | No          | SNOMED     | Removal of endotracheal tube                        | 271280005    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                      |
| Extubation (Procedure)          | 4012607    | No          | SNOMED     | Removal of tracheostomy tube                        | 113153002    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                      |
| Extubation (Procedure)          | 4195943    | No          | SNOMED     | Ventilating tube removal by another physician       | 44482009     | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                      |
|---------------------------------|------------|-------------|------------|-----------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------|
| Extubation (Observation)        | 4231838    | No          | SNOMED     | Inadvertent tracheal extubation (inadvertent)       | 405639008    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                      |
|---------------------------------|------------|-------------|------------|-----------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------|
| Invasive mechanical ventilation | 37158404   | No          | SNOMED     | Invasive mechanical ventilation                     | 1258985005   | [Invasive mechanical ventilation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=306) |
| Trial of spontaneous breathing  | 4308797    | No          | SNOMED     | Trial of spontaneous breathing                      | 424139009    | [Trial of spontaneous breathing](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=309)  |
|---------------------------------|------------|-------------|------------|-----------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------|


## Guidance

A day is not defined as midnight-to-midnight but is a full 24-hour period
that starts at the beginning of mechanical ventilation.
The last period before end of ventilation is ignored if it
is less than 24 hours.


## Initial Population

All critically ill patients that are 18 years or older
    AND mechanical ventilated for at least 48 hours
    AND (are Intubated (Device Exposure)
         OR a period
            between Intubation (Procedure) and Extubation (Procedure)
            overlaps the period in question)
during the observation period.


## Numerator

For each 24 hour period starting at 24 hours after the beginning of
mechanical ventilation there should be at least one period
with

"Trial of spontaneous breathing"
OR
(Extubation OR no mechanical ventilation for >= 5 [min])


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

Fichtner et al. 2025
"S3-Leitlinie Invasive Beatmung und Einsatz extrakorporaler Verfahren bei akuter respiratorischer Insuffizienz"


## Comments
