# Indicator 01

## Title

Lung-protective ventilation in Acute Respiratory Distress Syndrome (ARDS)


## ID

01


## Short Name

01-lpv-ards


## Description

Lung-protective mechanical ventilation should reduce inflammation and lung
damage.
Therefore patients with ARDS should be ventilated with a tidal volume around
6 mL/kg ideal body weight (IBW).
The positive end expiratory pressure (PEEP) should be adjusted according to the
ARDSnet PEEP table
(mild ARDS: low PEEP table, moderate/severe ARDS: high PEEP table).
The plateau pressure should be lower or equal 30 cmH2O.
The inspiratory pressure difference (driving pressure, Pdelta) should be lower
or equal 14 cmH2O.


## Justification

Invasive mechanical ventilation with extrem parameters
is associated with increased mortality in patients with ARDS.

Fichtner et al., recommendations 32-2025/33-2025
PEEP

Fichtner et al., recomendation 40-2025
VT around 6 mL/kg IBW

Fichtner et al., recommendation 42-2025
Pplat <= 30 cmH2O

Fichtner et al., recommendation 44-2025
Pdelta <= 14 cmH2O


## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions

### ARDS severity

- mild:     200 < PaO2/FiO2 <= 300 mmHg and PEEP >= 5 cmH2O
- moderate: 100 < PaO2/FiO2 <= 200 mmHg and PEEP >= 5 cmH2O
- severe:         PaO2/FiO2 <= 100 mmHg and PEEP >= 5 cmH2O

If no PaO2 is given in the last 6 hours we assume a mild ARDS.


### ARDSnet PEEP tables

The PEEP values will sometimes differ from the values in the table, e.g. PEEP =
6 cmH2O for an FiO2 of 0.3.

We would assume the PEEP as adequate if it is at least the value listed in the
tables below for a given FiO2.
The tables are based on the ARDS-network PEEP tables and simplified to the
lowest PEEP for each FiO2.

For the FiO2 we look up the next lowest entry in the table, e.g. 0.3 for 0.39.


#### low PEEP table

FiO2 | 0.3 | 0.5 | 0.6 | 0.8 | 1.0 |
|----|-----|-----|-----|-----|-----|
PEEP |   5 |   8 |  10 |  14 |  18 |

#### high PEEP table

FiO2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.9 |
|----|-----|-----|-----|-----|-----|
PEEP |   5 |  14 |  16 |  20 |  22 |


### Ideal Body Weight

If the entry IBW is given we chose the most recent one.

If it is missing
we calculate the ideal body weight (IBW) based on the Devine formula:
- women: IBW = 45.5 [kg] + 0.91 [kg] * (body height [cm] - 152.4)
- men:   IBW = 50 [kg] + 0.91 [kg] * (body height [cm] - 152.4)
- if the gender is not available:
         IBW = 47.75 [kg] + 0.91 [kg] * (body height [cm] - 152.4)

The IBW is calculated once for each patient and used for all
calculations.
If multiple body height entries are given we chose the most recent one.

### Ventilation modes

Historically, ventilation modes have been divided into
volume-controlled and pressure-controlled modes.
The decisive factor here is which parameter is set or limited.
Today, there are a variety of modes that combine both methods.
We use the main driving force to differentiate between them.

#### Volume driven (VCV)

- VCV
- CMV, continuous mandatory ventilation
- SIMV, synchronized intermittent mandatory ventilation (volume cycled)
- SIMV+PS, synchronized intermittent mandatory ventilation plus pressure support (volume cycled)

#### Pressure driven (PCV)

- PCV
- VCV-AF, volume-controlled ventilation-auto flow
- PC-AC, pressure-controlled, assist-control
- SIMV, synchronized intermittent mandatory ventilation (pressure cycled, if not explicitely given assume VCV)
- SIMV+PS, synchronized intermittent mandatory ventilation plus pressure support (pressure cycled, if not explicitely given assume VCV)
- CPAP+PS, continuous positive airway pressure plus pressure support
- BIPAP/BILEVEL, biphasic positive airway pressure
- APRV, airway pressure release ventilation

(these list may be incomplete)


### Plateau pressure

Plateau pressure is always defined for VCV mode. When run in PCV mode, only some ventilation devices record Pplat.
For a device in PCV mode that does not record Pplat, we will use the inspiratory pressure (Pinsp).

```
Pplat:
    IF Pplat IS MISSING AND ventilation mode IS PCV
        Pinsp
    ELSE
        Pplat
```

### Pressure difference

```
Pdelta = Pplat - PEEP
```


## Mapping

**Notes**:
* If more than one concepts are available at a specific time points the one with
the highest priority (lowest number) should be used.
* ARDS Changed from 45552897 (ICD10 Code J80 which is a non-standard OMOP code) to 4195694
* Gender is encoded in `person` table, see [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
* Identify intensive care episodes using the Intensive Care concept (32037).
  See [INDICATE Mapping recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
  In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence)) with `visit_type_concept_id = 32037`.


| Category                        | Priority | Concept ID | Descendants | Vocabulary | Concept Name                                                                                                | Concept Code | DD Concept Set                                                                                                  |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Intensive Care                  |          | 32037      | No          | Visit      | Intensive care                                                                                              | OMOP4822460  | N/A                                                                                                             |
| Body height                     |          | 3036277    | No          | LOINC      | Body height                                                                                                 | 8302-2       | [Body height](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=274)                              |
| Gender                          |          | 8532       | No          |            | Female                                                                                                      |              | [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations)     |
| Gender                          |          | 8507       | No          |            | Male                                                                                                        |              | [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations)     |
| IBW                             |          | 4062985    | No          | SNOMED     | Ideal body weight                                                                                           | 170804003    | [Ideal body weight](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284)                        |
| ARDS                            |          | 4195694    | No          | SNOMED     | Acute respiratory distress syndrome                                                                         | 67782005     | [ARDS](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=26)                                      |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Intubated (Device Exposure)     |          | 4097216    | Yes         | SNOMED     | Endotracheal tube                                                                                           | 26412008     | [Endotracheal tube](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=299)                        |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Intubated (Procedure)           |          | 4119642    | No          | SNOMED     | Awake intubation                                                                                            | 304341005    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4337045    | No          | SNOMED     | Blind nasal intubation                                                                                      | 232681006    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4140765    | No          | SNOMED     | Digital assisted intubation                                                                                 | 427331009    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4082243    | No          | SNOMED     | Emergency laryngeal intubation                                                                              | 182682004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4335585    | No          | SNOMED     | Endobronchial intubation                                                                                    | 232687005    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4058031    | No          | SNOMED     | Endotracheal intubation, emergency procedure                                                                | 16883004     | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 37116698   | No          | SNOMED     | Insertion of double lumen tracheobronchial tube                                                             | 733509002    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4013354    | No          | SNOMED     | Insertion of endotracheal tube                                                                              | 112798008    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4179373    | No          | SNOMED     | Insertion of endotracheal tube using laryngoscope                                                           | 429161001    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4283807    | No          | SNOMED     | Intubation of larynx                                                                                        | 66861000     | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 40487536   | No          | SNOMED     | Intubation of respiratory tract                                                                             | 447996002    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4056812    | No          | SNOMED     | Laryngeal intubation for inhalation                                                                         | 182709001    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4335584    | No          | SNOMED     | Nasal intubation awake                                                                                      | 232680007    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4337617    | No          | SNOMED     | Nasotracheal fiberoptic intubation                                                                          | 232682004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4337616    | No          | SNOMED     | Nasotracheal intubation                                                                                     | 232679009    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4339623    | No          | SNOMED     | Oral intubation awake                                                                                       | 232675003    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4337615    | No          | SNOMED     | Orotracheal fiberoptic intubation                                                                           | 232678001    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4335481    | No          | SNOMED     | Orotracheal intubation                                                                                      | 232674004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4287921    | No          | SNOMED     | Retrograde intubation                                                                                       | 397892004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4303945    | No          | SNOMED     | Tracheal intubation through a laryngeal mask airway                                                         | 418613003    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Procedure)           |          | 4335583    | No          | SNOMED     | Tracheal intubation using rigid bronchoscope                                                                | 232677006    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Intubated (Observation)         |          | 36660691   | No          | LOINC      | Difficult intubation                                                                                        | 95050-1      | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
| Intubated (Meas value)          |          | 36309319   | No          | LOINC      | Unplanned intubation                                                                                        | LA20580-9    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)                  |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Extubation (Procedure)          |          | 4148972    | No          | SNOMED     | Extubation of trachea (normal)                                                                              | 309812005    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                               |
| Extubation (Procedure)          |          | 4150627    | No          | SNOMED     | Removal of endotracheal tube                                                                                | 271280005    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                               |
| Extubation (Procedure)          |          | 4012607    | No          | SNOMED     | Removal of tracheostomy tube                                                                                | 113153002    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                               |
| Extubation (Procedure)          |          | 4195943    | No          | SNOMED     | Ventilating tube removal by another physician                                                               | 44482009     | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                               |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Invasive mechanical ventilation |          | 37158404   | No          | SNOMED     | Invasive mechanical ventilation                                                                             | 1258985005   | [Invasive mechanical ventilation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=306)          |
| Ventilation mode (PCV)          |          |            |             |            | see [Ventilation Modes](ventilation-modes.md)                                                               |              | [Ventilation mode - Pressure driven (PCV)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) |
| Ventilation mode (VCV)          |          |            |             |            | see [Ventilation Modes](ventilation-modes.md)                                                               |              | [Ventilation mode - Volume driven (VCV)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=340)   |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| PaO2/FiO2 (Horowitz index)      |          | 3029943    | No          | LOINC      | Horowitz index in Arterial blood                                                                            | 50984-4      | [Horowitz index](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313)                           |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| PaO2                            | 1        | 3027801    | No          | LOINC      | Oxygen [Partial pressure] in Arterial blood (default)                                                       | 2703-7       | [ABG PaO2](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=152)                                 |
| PaO2                            | 2        | 3022803    | No          | LOINC      | Oxygen [Partial pressure] adjusted to patient's actual temperature in Arterial blood (temperature adjusted) | 19255-9      | [ABG PaO2](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=152)                                 |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| FiO2                            |          | 4353936    | No          | SNOMED     | Inspired oxygen concentration                                                                               | 250774007    | [FiO2](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=301)                                     |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| PEEP                            | 1        | 42527140   | No          | LOINC      | Total PEEP Respiratory system (total, measured)                                                             | 76247-6      | [PEEP](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318)                                     |
| PEEP                            | 2        | 4216746    | No          | SNOMED     | Positive end expiratory pressure setting                                                                    | 416595007    | [PEEP](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318)                                     |
| PEEP                            | 3        | 4353713    | No          | SNOMED     | Positive end expiratory pressure (general, no information about setting/measurement)                        | 250854009    | [PEEP](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318)                                     |
| PEEP                            | 4        | 3022875    | No          | LOINC      | Positive end expiratory pressure setting Ventilator                                                         | 20077-4      | [PEEP](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318)                                     |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Pplat                           |          | 44782825   | No          | SNOMED     | Airway plateau pressure                                                                                     | 698822002    | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                         |
| Pplat                           |          | 3006369    | No          | LOINC      | Airway pressure --at zero inspiratory flow on ventilator                                                    | 20060-0      | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                         |
| Pplat                           |          | 3012810    | No          | LOINC      | Airway pressure by Airway pressure monitor --at zero inspiratory flow on ventilator                         | 20059-2      | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                         |
| Pplat                           |          | 21490565   | No          | LOINC      | Dynamic plateau pressure                                                                                    | 60802-6      | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                         |
| Pplat                           |          | 36304439   | No          | LOINC      | Pressure.plateau Respiratory system airway                                                                  | 60829-9      | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                         |
| Pplat                           |          | 36303946   | No          | LOINC      | Pressure.plateau Respiratory system airway --on ventilator                                                  | 76259-1      | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                         |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Pinsp                           | 1        | 4215838    | No          | SNOMED     | Inspiratory pressure setting [cmH2O]                                                                        | 417071008    | [Inspiratory pressure setting](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=314)             |
| Pinsp                           | 2        | 4101694    | No          | SNOMED     | Peak inspiratory pressure [mmHg], CAVE different units, convert to cmH2O                                    | 27913002     | [Peak inspiration pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=319)                |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| VT                              | 1        | 44782826   | No          | SNOMED     | Inspiratory tidal volume                                                                                    | 698823007    | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                             |
| VT                              | 2        | 4108448    | No          | SNOMED     | Spontaneous tidal volume                                                                                    | 250816009    | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                             |
| VT                              | 3        | 3012410    | No          | LOINC      | Tidal volume setting Ventilator                                                                             | 20112-9      | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                             |
| VT                              | 4        | 4029625    | No          | SNOMED     | Tidal volume (general, no information about setting/measurement)                                            | 13621006     | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                             |


## Guidance

We assume that the ventilator settings and measurements are reported at least
hourly.

If the PaO2/FiO2 ratio is not available it has to be calculated as follows:

The PaO2 is measured irregulary in an arterial blood gas analysis.
We assume that ventilated patients have a blood gas analysis every 4-6 hours.
The last PaO2 has to be taken for the calculation of PaO2/FiO2 ratio
(last observation carried forward, LOCF).
If it is missing or older than 6 hours we assume a mild ARDS.

The recommended PEEP has to be chosen as follows:
```
PEEPtable:
    IF PaO2/FiO2 is not given AND PaO2 was taken less than 6 hours before
current timepoint
        PaO2/FiO2 = LOCF(PaO2)/FiO2
    ELSE IF PaO2/FiO2 is not given AND PaO2 is missing or older than 6 hours
        PaO2/FiO2 = 300

    IF PaO2/FiO2 > 200
        low PEEP table
    ELSE
        high PEEP table

recommended PEEP:
    lowest PEEP in PEEPtable listed for the highest FiO2 <= measured FiO2
```

## Initial Population

All critically ill patients that are 18 years or older
    AND ventilation mode IN (VCV OR PCV from ventilation-modes.md)
    AND (are Intubated (Device Exposure)
         OR a period
            between Intubation (Procedure) and Extubation (Procedure)
            overlaps the period in question)
    AND an ARDS is diagnosed
during the observation period.

Note: (ventilation mode IN (VCV OR PCV)) is false if no mechanical ventilation is performed.

## Numerator

Each observation where ALL indicators are fulfilled is treated as
1 otherwise as 0.

```
COUNT
IF ALL(
    PEEP >= recommended PEEP
    AND
    4 * IBW <= VT <= 8 * IBW
    AND
    Pplat <= 30
    AND
    Pdelta <= 14
)
```

## Numerator Exclusion

None.


## Denominator

Number of observations.


## Denominator Exclusion

None.


## Expected

100 %


## Improvement Notation

A higher ratio indicates improvement.


## References

Fichtner et al. 2025
"S3-Leitlinie Invasive Beatmung und Einsatz extrakorporaler Verfahren bei akuter respiratorischer Insuffizienz"


## Comments
