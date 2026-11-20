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

- Invasive mechanical ventilation with extreme parameters
  is associated with increased mortality in patients with ARDS.

- Fichtner et al., recommendations 32-2025/33-2025: PEEP

- Fichtner et al., recommendation 40-2025: VT around 6 mL/kg IBW

- Fichtner et al., recommendation 42-2025: Pplat <= 30 cmH2O

- Fichtner et al., recommendation 44-2025: Pdelta <= 14 cmH2O

## Measuring Score

Ratio.


## Measuring Type

Process.


## Stratification

None.


## Definitions

### ARDS severity

- mild:     `200 mmHg < PaO2/FiO2 <= 300 mmHg and PEEP >= 5 cmH2O`
- moderate: `100 mmHg < PaO2/FiO2 <= 200 mmHg and PEEP >= 5 cmH2O`
- severe:              `PaO2/FiO2 <= 100 mmHg and PEEP >= 5 cmH2O`

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
- women: `IBW = 45.5 [kg] + 0.91 [kg] * (body height [cm] - 152.4)`
- men:   `IBW = 50 [kg] + 0.91 [kg] * (body height [cm] - 152.4)`
- if the gender is not available:
         `IBW = 47.75 [kg] + 0.91 [kg] * (body height [cm] - 152.4)`

The IBW is calculated once for each patient and used for all
calculations.
If multiple body height entries are given we chose the most recent one.

### Plateau pressure

Not all ventilation devices record the plateau pressure (Pplat) in all ventilation modes.
If Pplat measurements are not available for a given patient and time period, the quality indicator cannot be computed for that time period.

### Pressure difference

```
Pdelta = Pplat - PEEP
```


## Mapping

**Notes**:
* If more than one concepts are available at a specific time points the one with the highest priority (lowest number) should be used.
* ARDS Changed from 45552897 (ICD10 Code J80 which is a non-standard OMOP code) to 4195694
* Gender is encoded in `person` table, see [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
* Identify intensive care episodes using the Intensive Care concept (32037).
  See [INDICATE Mapping recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
  In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence)) with `visit_type_concept_id = 32037`.


| Category                        | Priority | Concept ID | Descendants | Vocabulary | Concept Name                                                                                                | Concept Code | DD Concept Set                                                                                              |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| Intensive Care                  |          | 32037      | No          | Visit      | Intensive care                                                                                              | OMOP4822460  | N/A                                                                                                         |
| Body height                     |          | 3036277    | No          | LOINC      | Body height                                                                                                 | 8302-2       | [Body height](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=274)                          |
| Gender                          |          | 8532       | No          |            | Female                                                                                                      |              | [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations) |
| Gender                          |          | 8507       | No          |            | Male                                                                                                        |              | [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations) |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| IBW                             |          | 4062985    | No          | SNOMED     | Ideal body weight                                                                                           | 170804003    | [Ideal body weight](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284)                    |
| IBW                             |          | 3032445    | No          | LOINC      | Ideal body weight                                                                                           | 50064-5      | [Ideal body weight](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284)                    |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| ARDS                            |          | 4195694    | No          | SNOMED     | Acute respiratory distress syndrome                                                                         | 67782005     | [ARDS](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=26)                                  |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| Intubated (Device Exposure)     |          | 4097216    | Yes         | SNOMED     | Endotracheal tube                                                                                           | 26412008     | [Endotracheal tube](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=299)                    |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| Intubated (Procedure)           |          | 4119642    | No          | SNOMED     | Awake intubation                                                                                            | 304341005    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4337045    | No          | SNOMED     | Blind nasal intubation                                                                                      | 232681006    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4140765    | No          | SNOMED     | Digital assisted intubation                                                                                 | 427331009    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4082243    | No          | SNOMED     | Emergency laryngeal intubation                                                                              | 182682004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4335585    | No          | SNOMED     | Endobronchial intubation                                                                                    | 232687005    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4058031    | No          | SNOMED     | Endotracheal intubation, emergency procedure                                                                | 16883004     | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 37116698   | No          | SNOMED     | Insertion of double lumen tracheobronchial tube                                                             | 733509002    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4013354    | No          | SNOMED     | Insertion of endotracheal tube                                                                              | 112798008    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4179373    | No          | SNOMED     | Insertion of endotracheal tube using laryngoscope                                                           | 429161001    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4283807    | No          | SNOMED     | Intubation of larynx                                                                                        | 66861000     | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 40487536   | No          | SNOMED     | Intubation of respiratory tract                                                                             | 447996002    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4056812    | No          | SNOMED     | Laryngeal intubation for inhalation                                                                         | 182709001    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4335584    | No          | SNOMED     | Nasal intubation awake                                                                                      | 232680007    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4337617    | No          | SNOMED     | Nasotracheal fiberoptic intubation                                                                          | 232682004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4337616    | No          | SNOMED     | Nasotracheal intubation                                                                                     | 232679009    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4339623    | No          | SNOMED     | Oral intubation awake                                                                                       | 232675003    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4337615    | No          | SNOMED     | Orotracheal fiberoptic intubation                                                                           | 232678001    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4335481    | No          | SNOMED     | Orotracheal intubation                                                                                      | 232674004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4287921    | No          | SNOMED     | Retrograde intubation                                                                                       | 397892004    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4303945    | No          | SNOMED     | Tracheal intubation through a laryngeal mask airway                                                         | 418613003    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
| Intubated (Procedure)           |          | 4335583    | No          | SNOMED     | Tracheal intubation using rigid bronchoscope                                                                | 232677006    | [Endotracheal intubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305)              |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| Extubation (Procedure)          |          | 4148972    | No          | SNOMED     | Extubation of trachea (normal)                                                                              | 309812005    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                           |
| Extubation (Procedure)          |          | 4150627    | No          | SNOMED     | Removal of endotracheal tube                                                                                | 271280005    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                           |
| Extubation (Procedure)          |          | 4012607    | No          | SNOMED     | Removal of tracheostomy tube                                                                                | 113153002    | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                           |
| Extubation (Procedure)          |          | 4195943    | No          | SNOMED     | Ventilating tube removal by another physician                                                               | 44482009     | [Extubation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303)                           |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| Invasive mechanical ventilation |          | 37158404   | No          | SNOMED     | Invasive mechanical ventilation                                                                             | 1258985005   | [Invasive mechanical ventilation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=306)      |
| PaO2/FiO2 (Horowitz index)      |          | 3029943    | No          | LOINC      | Horowitz index in Arterial blood                                                                            | 50984-4      | [Horowitz index](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313)                       |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| PaO2                            | 1        | 3027801    | No          | LOINC      | Oxygen [Partial pressure] in Arterial blood (default)                                                       | 2703-7       | [ABG PaO2](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=152)                             |
| PaO2                            | 2        | 3022803    | No          | LOINC      | Oxygen [Partial pressure] adjusted to patient's actual temperature in Arterial blood (temperature adjusted) | 19255-9      | [ABG PaO2](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=152)                             |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| FiO2                            |          | 4353936    | No          | SNOMED     | Inspired oxygen concentration                                                                               | 250774007    | [FiO2](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=301)                                 |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| PEEP                            | 1        | 42527140   | No          | LOINC      | Total PEEP Respiratory system (total, measured)                                                             | 76247-6      | [PEEP](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318)                                 |
| PEEP                            | 2        | 4216746    | No          | SNOMED     | Positive end expiratory pressure setting                                                                    | 416595007    | [PEEP](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318)                                 |
| PEEP                            | 3        | 4353713    | No          | SNOMED     | Positive end expiratory pressure (general, no information about setting/measurement)                        | 250854009    | [PEEP](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318)                                 |
| PEEP                            | 4        | 3022875    | No          | LOINC      | Positive end expiratory pressure setting Ventilator                                                         | 20077-4      | [PEEP](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318)                                 |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| Pplat                           |          | 44782825   | No          | SNOMED     | Airway plateau pressure                                                                                     | 698822002    | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                     |
| Pplat                           |          | 3006369    | No          | LOINC      | Airway pressure --at zero inspiratory flow on ventilator                                                    | 20060-0      | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                     |
| Pplat                           |          | 3012810    | No          | LOINC      | Airway pressure by Airway pressure monitor --at zero inspiratory flow on ventilator                         | 20059-2      | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                     |
| Pplat                           |          | 21490565   | No          | LOINC      | Dynamic plateau pressure                                                                                    | 60802-6      | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                     |
| Pplat                           |          | 36304439   | No          | LOINC      | Pressure.plateau Respiratory system airway                                                                  | 60829-9      | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                     |
| Pplat                           |          | 36303946   | No          | LOINC      | Pressure.plateau Respiratory system airway --on ventilator                                                  | 76259-1      | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                     |
|---------------------------------|----------|------------|-------------|------------|-------------------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|
| VT                              | 1        | 44782826   | No          | SNOMED     | Inspiratory tidal volume                                                                                    | 698823007    | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                         |
| VT                              | 2        | 4108448    | No          | SNOMED     | Spontaneous tidal volume                                                                                    | 250816009    | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                         |
| VT                              | 3        | 3012410    | No          | LOINC      | Tidal volume setting Ventilator                                                                             | 20112-9      | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                         |
| VT                              | 4        | 4029625    | No          | SNOMED     | Tidal volume (general, no information about setting/measurement)                                            | 13621006     | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                         |


<!-- inject:Acute respiratory distress syndrome (ARDS)|Oxygen partial pressure in arterial blood|Body height|Ideal body weight|Endotracheal tube|Fraction of inspired oxygen (FiO2)|Extubation|Endotracheal intubation|Invasive mechanical ventilation|Ventilation mode|Horowitz index (PaO2/FiO2)|Applied Positive End-Expiratory Pressure (PEEP)|Total Positive End-Expiratory Pressure (Total PEEP)|Intrinsic Positive End-Expiratory Pressure (auto-PEEP)|Inspiratory pressure setting (Pinsp)|Peak inspiratory pressure (PIP)|Plateau pressure (Pplat)|Driving Pressure (ΔP)|Tidal volume (Vt) -->
| Priority | Concept ID                                                       | Descendants | Vocabulary | Concept Name                               | Concept Code     | DD Concept Set                                                                                                         |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [4195694](https://athena.ohdsi.org/search-terms/terms/4195694)   | no          | SNOMED     | Acute respiratory distress syndrome        | 67782005         | [Acute respiratory distress syndrom… (26)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=26) v1.1.0  |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
| 1        | [3027801](https://athena.ohdsi.org/search-terms/terms/3027801)   | no          | LOINC      | Oxygen \[Partial pressure\] in Arterial b… | 2703-7           | [Oxygen partial pressure in arteri… (152)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=152) v1.2.0 |
| 2        | [3022803](https://athena.ohdsi.org/search-terms/terms/3022803)   | no          | LOINC      | Oxygen \[Partial pressure\] adjusted to p… | 19255-9          | [Oxygen partial pressure in arteri… (152)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=152) v1.2.0 |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [3036277](https://athena.ohdsi.org/search-terms/terms/3036277)   | no          | LOINC      | Body height                                | 8302-2           | [Body height (274)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=274) v1.2.0                        |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [4062985](https://athena.ohdsi.org/search-terms/terms/4062985)   | no          | SNOMED     | Ideal body weight                          | 170804003        | [Ideal body weight (284)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284) v1.2.0                  |
|          | [3032445](https://athena.ohdsi.org/search-terms/terms/3032445)   | no          | LOINC      | Ideal body weight                          | 50064-5          | [Ideal body weight (284)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284) v1.2.0                  |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [4097216](https://athena.ohdsi.org/search-terms/terms/4097216)   | yes         | SNOMED     | Endotracheal tube                          | 26412008         | [Endotracheal tube (299)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=299) v1.1.0                  |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [3020716](https://athena.ohdsi.org/search-terms/terms/3020716)   | no          | LOINC      | Inhaled oxygen concentration               | 3150-0           | [Fraction of inspired oxygen (FiO2) (301)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=301) v1.1.1 |
|          | [4353936](https://athena.ohdsi.org/search-terms/terms/4353936)   | no          | SNOMED     | Inspired oxygen concentration              | 250774007        | [Fraction of inspired oxygen (FiO2) (301)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=301) v1.1.1 |
|          | [42869590](https://athena.ohdsi.org/search-terms/terms/42869590) | no          | LOINC      | Oxygen/Gas total \[Pure volume fraction\]… | 71835-3          | [Fraction of inspired oxygen (FiO2) (301)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=301) v1.1.1 |
|          | [3026238](https://athena.ohdsi.org/search-terms/terms/3026238)   | no          | LOINC      | Oxygen/Inspired gas Respiratory system …   | 19996-8          | [Fraction of inspired oxygen (FiO2) (301)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=301) v1.1.1 |
|          | [3025408](https://athena.ohdsi.org/search-terms/terms/3025408)   | no          | LOINC      | Oxygen/Inspired gas Respiratory system …   | 19995-0          | [Fraction of inspired oxygen (FiO2) (301)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=301) v1.1.1 |
|          | [3024882](https://athena.ohdsi.org/search-terms/terms/3024882)   | no          | LOINC      | Oxygen/Total gas setting \[Volume Fracti…  | 19994-3          | [Fraction of inspired oxygen (FiO2) (301)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=301) v1.1.1 |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [4148972](https://athena.ohdsi.org/search-terms/terms/4148972)   | no          | SNOMED     | Extubation of trachea                      | 309812005        | [Extubation (303)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303) v1.1.0                         |
|          | [4231838](https://athena.ohdsi.org/search-terms/terms/4231838)   | no          | SNOMED     | Inadvertent tracheal extubation            | 405639008        | [Extubation (303)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303) v1.1.0                         |
|          | [4150627](https://athena.ohdsi.org/search-terms/terms/4150627)   | no          | SNOMED     | Removal of endotracheal tube               | 271280005        | [Extubation (303)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303) v1.1.0                         |
|          | [4012607](https://athena.ohdsi.org/search-terms/terms/4012607)   | no          | SNOMED     | Removal of tracheostomy tube               | 113153002        | [Extubation (303)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303) v1.1.0                         |
|          | [4195943](https://athena.ohdsi.org/search-terms/terms/4195943)   | no          | SNOMED     | Ventilating tube removal by another phy…   | 44482009         | [Extubation (303)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=303) v1.1.0                         |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [4119642](https://athena.ohdsi.org/search-terms/terms/4119642)   | no          | SNOMED     | Awake intubation                           | 304341005        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4337045](https://athena.ohdsi.org/search-terms/terms/4337045)   | no          | SNOMED     | Blind nasal intubation                     | 232681006        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4140765](https://athena.ohdsi.org/search-terms/terms/4140765)   | no          | SNOMED     | Digital assisted intubation                | 427331009        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4082243](https://athena.ohdsi.org/search-terms/terms/4082243)   | no          | SNOMED     | Emergency laryngeal intubation             | 182682004        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4335585](https://athena.ohdsi.org/search-terms/terms/4335585)   | no          | SNOMED     | Endobronchial intubation                   | 232687005        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4058031](https://athena.ohdsi.org/search-terms/terms/4058031)   | no          | SNOMED     | Endotracheal intubation, emergency proc…   | 16883004         | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [37116698](https://athena.ohdsi.org/search-terms/terms/37116698) | no          | SNOMED     | Insertion of double lumen tracheobronch…   | 733509002        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4013354](https://athena.ohdsi.org/search-terms/terms/4013354)   | no          | SNOMED     | Insertion of endotracheal tube             | 112798008        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4179373](https://athena.ohdsi.org/search-terms/terms/4179373)   | no          | SNOMED     | Insertion of endotracheal tube using la…   | 429161001        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4283807](https://athena.ohdsi.org/search-terms/terms/4283807)   | no          | SNOMED     | Intubation of larynx                       | 66861000         | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [40487536](https://athena.ohdsi.org/search-terms/terms/40487536) | no          | SNOMED     | Intubation of respiratory tract            | 447996002        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4056812](https://athena.ohdsi.org/search-terms/terms/4056812)   | no          | SNOMED     | Laryngeal intubation for inhalation        | 182709001        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4335584](https://athena.ohdsi.org/search-terms/terms/4335584)   | no          | SNOMED     | Nasal intubation awake                     | 232680007        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4337617](https://athena.ohdsi.org/search-terms/terms/4337617)   | no          | SNOMED     | Nasotracheal fiberoptic intubation         | 232682004        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4337616](https://athena.ohdsi.org/search-terms/terms/4337616)   | no          | SNOMED     | Nasotracheal intubation                    | 232679009        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4339623](https://athena.ohdsi.org/search-terms/terms/4339623)   | no          | SNOMED     | Oral intubation awake                      | 232675003        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4337615](https://athena.ohdsi.org/search-terms/terms/4337615)   | no          | SNOMED     | Orotracheal fiberoptic intubation          | 232678001        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4335481](https://athena.ohdsi.org/search-terms/terms/4335481)   | no          | SNOMED     | Orotracheal intubation                     | 232674004        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4287921](https://athena.ohdsi.org/search-terms/terms/4287921)   | no          | SNOMED     | Retrograde intubation                      | 397892004        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4303945](https://athena.ohdsi.org/search-terms/terms/4303945)   | no          | SNOMED     | Tracheal intubation through a laryngeal…   | 418613003        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|          | [4335583](https://athena.ohdsi.org/search-terms/terms/4335583)   | no          | SNOMED     | Tracheal intubation using rigid broncho…   | 232677006        | [Endotracheal intubation (305)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=305) v1.2.0            |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [37158404](https://athena.ohdsi.org/search-terms/terms/37158404) | no          | SNOMED     | Invasive mechanical ventilation            | 1258985005       | [Invasive mechanical ventilation (306)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=306) v1.1.0    |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [4072515](https://athena.ohdsi.org/search-terms/terms/4072515)   | no          | SNOMED     | Airway pressure release ventilation        | 243143008        | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152410](https://athena.ohdsi.org/search-terms/terms/37152410) | no          | SNOMED     | Assist control ventilation pressure con…   | 1186746005       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152412](https://athena.ohdsi.org/search-terms/terms/37152412) | no          | SNOMED     | Assist control ventilation pressure-con…   | 1186748006       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152409](https://athena.ohdsi.org/search-terms/terms/37152409) | no          | SNOMED     | Assist control ventilation volume-contr…   | 1186745009       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152411](https://athena.ohdsi.org/search-terms/terms/37152411) | no          | SNOMED     | Assist control ventilation volume-targe…   | 1186747001       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152408](https://athena.ohdsi.org/search-terms/terms/37152408) | no          | SNOMED     | Assist control ventilation volume-targe…   | 1186744008       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [4055375](https://athena.ohdsi.org/search-terms/terms/4055375)   | no          | SNOMED     | Assisted controlled mandatory ventilati…   | 243150007        | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [40491848](https://athena.ohdsi.org/search-terms/terms/40491848) | no          | SNOMED     | Bilevel positive airway pressure titrat…   | 447243000        | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37158487](https://athena.ohdsi.org/search-terms/terms/37158487) | no          | SNOMED     | Continuous flow apneic ventilation         | 1260411001       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37153603](https://athena.ohdsi.org/search-terms/terms/37153603) | no          | SNOMED     | Continuous mandatory ventilation           | 1222606000       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37151337](https://athena.ohdsi.org/search-terms/terms/37151337) | no          | SNOMED     | Continuous mandatory ventilation pressu…   | 1187023008       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37151338](https://athena.ohdsi.org/search-terms/terms/37151338) | no          | SNOMED     | Continuous mandatory ventilation pressu…   | 1187024002       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152413](https://athena.ohdsi.org/search-terms/terms/37152413) | no          | SNOMED     | Continuous mandatory ventilation volume…   | 1186749003       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37151336](https://athena.ohdsi.org/search-terms/terms/37151336) | no          | SNOMED     | Continuous mandatory ventilation volume…   | 1187022003       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37151339](https://athena.ohdsi.org/search-terms/terms/37151339) | no          | SNOMED     | Continuous mandatory ventilation volume…   | 1187025001       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37153604](https://athena.ohdsi.org/search-terms/terms/37153604) | no          | SNOMED     | Continuous mandatory ventilation with s…   | 1222607009       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [4165535](https://athena.ohdsi.org/search-terms/terms/4165535)   | no          | SNOMED     | Continuous positive airway pressure ven…   | 47545007         | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152383](https://athena.ohdsi.org/search-terms/terms/37152383) | no          | SNOMED     | Continuous positive airway pressure wit…   | 1186678006       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152402](https://athena.ohdsi.org/search-terms/terms/37152402) | no          | SNOMED     | Continuous spontaneous ventilation with…   | 1186733000       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152400](https://athena.ohdsi.org/search-terms/terms/37152400) | no          | SNOMED     | Continuous spontaneous ventilation with…   | 1186731003       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152401](https://athena.ohdsi.org/search-terms/terms/37152401) | no          | SNOMED     | Continuous spontaneous ventilation with…   | 1186732005       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [4055262](https://athena.ohdsi.org/search-terms/terms/4055262)   | no          | SNOMED     | Dual pressure spontaneous ventilation s…   | 243142003        | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [4055377](https://athena.ohdsi.org/search-terms/terms/4055377)   | no          | SNOMED     | High frequency jet ventilation             | 243154003        | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [4074666](https://athena.ohdsi.org/search-terms/terms/4074666)   | no          | SNOMED     | High frequency oscillatory ventilation     | 243155002        | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [4055376](https://athena.ohdsi.org/search-terms/terms/4055376)   | no          | SNOMED     | High frequency positive pressure ventil…   | 243153009        | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37157167](https://athena.ohdsi.org/search-terms/terms/37157167) | no          | SNOMED     | Intermittent mandatory ventilation         | 1197612007       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37157430](https://athena.ohdsi.org/search-terms/terms/37157430) | no          | SNOMED     | Intermittent mandatory ventilation with…   | 1217390002       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152407](https://athena.ohdsi.org/search-terms/terms/37152407) | no          | SNOMED     | Intermittent mandatory ventilation with…   | 1186742007       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [1243692](https://athena.ohdsi.org/search-terms/terms/1243692)   | no          | SNOMED     | Neurally adjusted ventilatory assist       | 1297240007       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [3661882](https://athena.ohdsi.org/search-terms/terms/3661882)   | no          | SNOMED     | Nocturnal continuous positive airway pr…   | 34281000175105   | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [3661883](https://athena.ohdsi.org/search-terms/terms/3661883)   | no          | SNOMED     | Nocturnal dual pressure spontaneous ven…   | 34291000175108   | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37154096](https://athena.ohdsi.org/search-terms/terms/37154096) | no          | SNOMED     | Pressure support ventilation               | 1259864003       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152791](https://athena.ohdsi.org/search-terms/terms/37152791) | no          | SNOMED     | Spontaneous and/or timed ventilation       | 1197780003       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152379](https://athena.ohdsi.org/search-terms/terms/37152379) | no          | SNOMED     | Spontaneous timed ventilation with pres…   | 1186672007       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152378](https://athena.ohdsi.org/search-terms/terms/37152378) | no          | SNOMED     | Spontaneous timed ventilation with pres…   | 1186658003       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152380](https://athena.ohdsi.org/search-terms/terms/37152380) | no          | SNOMED     | Spontaneous timed ventilation with volu…   | 1186674008       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [4245036](https://athena.ohdsi.org/search-terms/terms/4245036)   | no          | SNOMED     | Synchronized intermittent mandatory ven…   | 59427005         | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152364](https://athena.ohdsi.org/search-terms/terms/37152364) | no          | SNOMED     | Synchronized intermittent mandatory ven…   | 1186622005       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152363](https://athena.ohdsi.org/search-terms/terms/37152363) | no          | SNOMED     | Synchronized intermittent mandatory ven…   | 1186621003       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152384](https://athena.ohdsi.org/search-terms/terms/37152384) | no          | SNOMED     | Synchronized intermittent mandatory ven…   | 1186679003       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152385](https://athena.ohdsi.org/search-terms/terms/37152385) | no          | SNOMED     | Synchronized intermittent mandatory ven…   | 1186680000       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152388](https://athena.ohdsi.org/search-terms/terms/37152388) | no          | SNOMED     | Synchronized intermittent mandatory ven…   | 1186683003       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152387](https://athena.ohdsi.org/search-terms/terms/37152387) | no          | SNOMED     | Synchronized intermittent mandatory ven…   | 1186682008       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152386](https://athena.ohdsi.org/search-terms/terms/37152386) | no          | SNOMED     | Synchronized intermittent mandatory ven…   | 1186681001       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152389](https://athena.ohdsi.org/search-terms/terms/37152389) | no          | SNOMED     | Synchronized intermittent mandatory ven…   | 1186684009       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|          | [37152390](https://athena.ohdsi.org/search-terms/terms/37152390) | no          | SNOMED     | Synchronized intermittent mandatory ven…   | 1186685005       | [Ventilation mode (339)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) v1.2.0                   |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [3029268](https://athena.ohdsi.org/search-terms/terms/3029268)   | no          | LOINC      | Horowitz index adjusted to patients act…   | 50989-3          | [Horowitz index (PaO2/FiO2) (313)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313) v1.0.1         |
|          | [3029906](https://athena.ohdsi.org/search-terms/terms/3029906)   | no          | LOINC      | Horowitz index adjusted to patients act…   | 50987-7          | [Horowitz index (PaO2/FiO2) (313)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313) v1.0.1         |
|          | [3032208](https://athena.ohdsi.org/search-terms/terms/3032208)   | no          | LOINC      | Horowitz index adjusted to patients act…   | 50988-5          | [Horowitz index (PaO2/FiO2) (313)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313) v1.0.1         |
|          | [3029523](https://athena.ohdsi.org/search-terms/terms/3029523)   | no          | LOINC      | Horowitz index adjusted to patients act…   | 50990-1          | [Horowitz index (PaO2/FiO2) (313)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313) v1.0.1         |
|          | [3032443](https://athena.ohdsi.org/search-terms/terms/3032443)   | no          | LOINC      | Horowitz index adjusted to patients act…   | 50991-9          | [Horowitz index (PaO2/FiO2) (313)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313) v1.0.1         |
|          | [3029943](https://athena.ohdsi.org/search-terms/terms/3029943)   | no          | LOINC      | Horowitz index in Arterial blood           | 50984-4          | [Horowitz index (PaO2/FiO2) (313)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313) v1.0.1         |
|          | [3029880](https://athena.ohdsi.org/search-terms/terms/3029880)   | no          | LOINC      | Horowitz index in Blood                    | 50982-8          | [Horowitz index (PaO2/FiO2) (313)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313) v1.0.1         |
|          | [3030774](https://athena.ohdsi.org/search-terms/terms/3030774)   | no          | LOINC      | Horowitz index in Capillary blood          | 50983-6          | [Horowitz index (PaO2/FiO2) (313)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313) v1.0.1         |
|          | [3029599](https://athena.ohdsi.org/search-terms/terms/3029599)   | no          | LOINC      | Horowitz index in Mixed venous blood       | 50985-1          | [Horowitz index (PaO2/FiO2) (313)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313) v1.0.1         |
|          | [3029316](https://athena.ohdsi.org/search-terms/terms/3029316)   | no          | LOINC      | Horowitz index in Venous blood             | 50986-9          | [Horowitz index (PaO2/FiO2) (313)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313) v1.0.1         |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [42528516](https://athena.ohdsi.org/search-terms/terms/42528516) | no          | LOINC      | Extrinsic dynamic PEEP Respiratory syst…   | 83387-1          | [Applied Positive End-Expiratory P… (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.4.0 |
|          | [42528515](https://athena.ohdsi.org/search-terms/terms/42528515) | no          | LOINC      | Extrinsic PEEP Respiratory system          | 83386-3          | [Applied Positive End-Expiratory P… (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.4.0 |
|          | [3016226](https://athena.ohdsi.org/search-terms/terms/3016226)   | no          | LOINC      | PEEP Respiratory system                    | 20075-8          | [Applied Positive End-Expiratory P… (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.4.0 |
|          | [21490855](https://athena.ohdsi.org/search-terms/terms/21490855) | no          | LOINC      | PEEP Respiratory system --on ventilator    | 76248-4          | [Applied Positive End-Expiratory P… (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.4.0 |
|          | [3022875](https://athena.ohdsi.org/search-terms/terms/3022875)   | no          | LOINC      | Positive end expiratory pressure settin…   | 20077-4          | [Applied Positive End-Expiratory P… (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.4.0 |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [42528517](https://athena.ohdsi.org/search-terms/terms/42528517) | no          | LOINC      | Total dynamic PEEP Respiratory system      | 83388-9          | [Total Positive End-Expiratory Pre… (385)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=385) v1.0.0 |
|          | [42527140](https://athena.ohdsi.org/search-terms/terms/42527140) | no          | LOINC      | Total PEEP Respiratory system              | 76247-6          | [Total Positive End-Expiratory Pre… (385)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=385) v1.0.0 |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [42527139](https://athena.ohdsi.org/search-terms/terms/42527139) | no          | LOINC      | Intrinsic dynamic PEEP Respiratory syst…   | 76246-8          | [Intrinsic Positive End-Expiratory… (384)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=384) v1.0.0 |
|          | [3035822](https://athena.ohdsi.org/search-terms/terms/3035822)   | no          | LOINC      | Intrinsic PEEP Respiratory system          | 38199-6          | [Intrinsic Positive End-Expiratory… (384)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=384) v1.0.0 |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [4215838](https://athena.ohdsi.org/search-terms/terms/4215838)   | no          | SNOMED     | Inspiratory pressure setting               | 417071008        | [Inspiratory pressure setting (Pin… (314)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=314) v1.0.1 |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [4101694](https://athena.ohdsi.org/search-terms/terms/4101694)   | no          | SNOMED     | Peak inspiratory pressure                  | 27913002         | [Peak inspiratory pressure (PIP) (319)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=319) v1.0.1    |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | [44782825](https://athena.ohdsi.org/search-terms/terms/44782825) | no          | SNOMED     | Airway plateau pressure                    | 698822002        | [Plateau pressure (Pplat) (320)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320) v1.2.1           |
|          | [3006369](https://athena.ohdsi.org/search-terms/terms/3006369)   | no          | LOINC      | Airway pressure --at zero inspiratory f…   | 20060-0          | [Plateau pressure (Pplat) (320)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320) v1.2.1           |
|          | [3012810](https://athena.ohdsi.org/search-terms/terms/3012810)   | no          | LOINC      | Airway pressure by Airway pressure moni…   | 20059-2          | [Plateau pressure (Pplat) (320)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320) v1.2.1           |
|          | [21490565](https://athena.ohdsi.org/search-terms/terms/21490565) | no          | LOINC      | Dynamic plateau pressure                   | 60802-6          | [Plateau pressure (Pplat) (320)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320) v1.2.1           |
|          | [37040392](https://athena.ohdsi.org/search-terms/terms/37040392) | yes         | LOINC      | Pressure.plateau | Respiratory system a…   | LP409162-7       | [Plateau pressure (Pplat) (320)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320) v1.2.1           |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
|          | 2100000010                                                       | no          | INDICATE   | Driving pressure                           | driving-pressure | [Driving Pressure (ΔP) (386)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=386) v1.0.0              |
|---       |---                                                               |---          |---         |---                                         |---               |---                                                                                                                     |
| 1        | [44782826](https://athena.ohdsi.org/search-terms/terms/44782826) | no          | SNOMED     | Inspiratory tidal volume                   | 698823007        | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
| 2        | [4108448](https://athena.ohdsi.org/search-terms/terms/4108448)   | no          | SNOMED     | Spontaneous tidal volume                   | 250816009        | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
| 3        | [3012410](https://athena.ohdsi.org/search-terms/terms/3012410)   | no          | LOINC      | Tidal volume setting Ventilator            | 20112-9          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
| 4        | [4029625](https://athena.ohdsi.org/search-terms/terms/4029625)   | no          | SNOMED     | Tidal volume                               | 13621006         | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [44782827](https://athena.ohdsi.org/search-terms/terms/44782827) | no          | SNOMED     | Expiratory tidal volume                    | 698824001        | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [4353946](https://athena.ohdsi.org/search-terms/terms/4353946)   | no          | SNOMED     | Mandatory tidal volume                     | 250817000        | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [21490752](https://athena.ohdsi.org/search-terms/terms/21490752) | no          | LOINC      | Tidal volume expired Respiratory system…   | 75958-9          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [21490789](https://athena.ohdsi.org/search-terms/terms/21490789) | no          | LOINC      | Tidal volume expired Respiratory system…   | 76007-4          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3011767](https://athena.ohdsi.org/search-terms/terms/3011767)   | no          | LOINC      | Tidal volume expired spontaneous correc…   | 20106-1          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3020572](https://athena.ohdsi.org/search-terms/terms/3020572)   | no          | LOINC      | Tidal volume expired spontaneous uncorr…   | 20105-3          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3009097](https://athena.ohdsi.org/search-terms/terms/3009097)   | no          | LOINC      | Tidal volume expired spontaneous+mechan…   | 20108-7          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3015016](https://athena.ohdsi.org/search-terms/terms/3015016)   | no          | LOINC      | Tidal volume expired spontaneous+mechan…   | 20107-9          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3033780](https://athena.ohdsi.org/search-terms/terms/3033780)   | no          | LOINC      | Tidal volume inspired spontaneous+mecha…   | 20110-3          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3021470](https://athena.ohdsi.org/search-terms/terms/3021470)   | no          | LOINC      | Tidal volume inspired spontaneous+mecha…   | 20111-1          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3016166](https://athena.ohdsi.org/search-terms/terms/3016166)   | no          | LOINC      | Tidal volume inspired spontaneous+mecha…   | 20109-5          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3008805](https://athena.ohdsi.org/search-terms/terms/3008805)   | no          | LOINC      | Tidal volume sigh spontaneous+mechanica…   | 20114-5          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [21490854](https://athena.ohdsi.org/search-terms/terms/21490854) | no          | LOINC      | Tidal volume Ventilator --on ventilator    | 76222-9          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [36303816](https://athena.ohdsi.org/search-terms/terms/36303816) | no          | LOINC      | Tidal volume.inspired                      | 76221-1          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3017594](https://athena.ohdsi.org/search-terms/terms/3017594)   | no          | LOINC      | Tidal volume.spontaneous --on ventilator   | 20116-0          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3004732](https://athena.ohdsi.org/search-terms/terms/3004732)   | no          | LOINC      | Tidal volume.spontaneous+mechanical --o…   | 20118-6          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3007828](https://athena.ohdsi.org/search-terms/terms/3007828)   | no          | LOINC      | Tidal volume.spontaneous+mechanical cor…   | 20119-4          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |
|          | [3017707](https://athena.ohdsi.org/search-terms/terms/3017707)   | no          | LOINC      | Tidal volume.spontaneous+mechanical unc…   | 20121-0          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                  |

## Guidance

We assume that the ventilator settings and measurements are reported at least
hourly.

If the PaO2/FiO2 ratio is not available it has to be calculated as follows:

The PaO2 is measured irregularly in an arterial blood gas analysis.
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
        PaO2/FiO2 = 300 mmHg

    IF PaO2/FiO2 > 200 mmHg
        low PEEP table
    ELSE
        high PEEP table

recommended PEEP:
    lowest PEEP in PEEPtable listed for the highest FiO2 <= measured FiO2
```

## Initial Population

```
All critically ill patients that are 18 years or older
    AND are mechanically ventilated
    AND (are Intubated (Device Exposure)
         OR a period
            between Intubation (Procedure) and Extubation (Procedure)
            overlaps the period in question)
    AND (an ARDS is diagnosed
         OR PaO2/FiO2 < 200 mmHg)
during the observation period.
```

Notes:
* Intubation procedures that are recorded without an end time should be treated as occurring at a point in time given by the start time (the start time is mandatory according to OMOP CDM documentation). Accordingly, intubation procedures that are recorded with identical start and end times are acceptable.
* If there is no subsequent extubation procedure for a given intubation procedure, the intubated period should end at the start of the next intubation procedure, if any.
* An intubation procedure not followed by either an extubation procedure or another intubation procedure results in an unbounded intubated period so that the "intubated" criterion of the initial population is fulfilled from that point in time onward.
* When the initial population criterion is evaluated for a time `t`,
  * Any ARDS diagnoses are subject to the following constraints
    Let `t_as` be the recorded start time of an ARDS diagnosis which is considered for the criterion
    * If the diagnosis is recorded without an end time `t_ae` or the end time is the same as `t_as`, `t_ae` is assumed to be the end of the visit (observation period)
    * `t_as ≤ t ≤ t_ae` has to hold
    * At some point in time between `t_as` and `t_ae`, the patient has to be ventilated and intubated as defined above
  * The calculation of the PaO2/FiO2 fraction from PaO2 and FiO2 measurements is subject to several constraints.
    Let `t_p` be the time of the PaO2 measurement used in the calculation and let `t_f` be the time of the FiO2 measurement used in the calculation, the following conditions must hold
    * At time `t_p`, the patient has to be ventilated and intubated as defined above
    * For the selected PaO2 measurement `t_p ≤ t` and `t - t_p` is minimal among all PaO2 measurements
    * For the selected FiO2 measurement `t_f ≤ t` and `t - t_f` is minimal among all FiO2 measurements which also fulfill the next condition
    * `(t_p - 60 min) ≤ t_f ≤ t_p`

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
    Pplat <= 30 cmH2O
    AND
    Pdelta <= 14 cmH2O
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

- Fichtner et al. 2025
  "S3-Leitlinie Invasive Beatmung und Einsatz extrakorporaler Verfahren bei akuter respiratorischer Insuffizienz"


## Comments
