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
- SIMV, synchronized intermittent mandatory ventilation (pressure cycled, if not explicitly given assume VCV)
- SIMV+PS, synchronized intermittent mandatory ventilation plus pressure support (pressure cycled, if not explicitly given assume VCV)
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
* If more than one concepts are available at a specific time points the one with the highest priority (lowest number) should be used.
* ARDS Changed from 45552897 (ICD10 Code J80 which is a non-standard OMOP code) to 4195694
* Gender is encoded in `person` table, see [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
* Identify intensive care episodes using the Intensive Care concept (32037).
  See [INDICATE Mapping recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations).
  In CDM, ICU stays should be represented as a [`VISIT_OCCURRENCE`](https://ohdsi.github.io/CommonDataModel/cdm54.html#visit_occurrence)) with `visit_type_concept_id = 32037`.


| Category                        | Priority | Concept ID | Vocabulary | Concept Name                                                     | Concept Code | DD Concept Set                                                                                                  |
|---------------------------------|----------|------------|------------|------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Intensive Care                  |          | 32037      | Visit      | Intensive care                                                   | OMOP4822460  | N/A                                                                                                             |
| Gender                          |          | 8532       |            | Female                                                           |              | [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations)     |
| Gender                          |          | 8507       |            | Male                                                             |              | [INDICATE Mapping Recommendations](https://indicate-eu.github.io/data-dictionary/#/mapping-recommendations)     |
|---------------------------------|----------|------------|------------|------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Body height                     |          | 3036277    | LOINC      | Body height                                                      | 8302-2       | [Body height](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=274)                              |
| IBW                             |          | 4062985    | SNOMED     | Ideal body weight                                                | 170804003    | [Ideal body weight](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284)                        |
| ARDS                            |          | 4195694    | SNOMED     | Acute respiratory distress syndrome                              | 67782005     | [ARDS](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=26)                                      |
| Intubated (tube present)        |          | 4097216    | SNOMED     | Endotracheal tube                                                | 26412008     | [Endotracheal tube](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=299)                        |
| Invasive mechanical ventilation |          | 37158404   | SNOMED     | Invasive mechanical ventilation                                  | 1258985005   | [Invasive mechanical ventilation](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=306)          |
| Ventilation mode (PCV)          |          |            |            | see [Ventilation Modes](ventilation-modes.md)                    |              | [Ventilation mode - Pressure driven (PCV)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=339) |
| Ventilation mode (VCV)          |          |            |            | see [Ventilation Modes](ventilation-modes.md)                    |              | [Ventilation mode - Volume driven (VCV)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=340)   |
| PaO2/FiO2 (Horowitz index)      |          | 3029943    | LOINC      | Horowitz index in Arterial blood                                 | 50984-4      | [Horowitz index](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=313)                           |
| PaO2                            | 1        | 3027801    | LOINC      | Oxygen [Partial pressure] in Arterial blood (default)            | 2703-7       | [ABG PaO2](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=152)                                 |
| PaO2                            | 2        | 3022803    | LOINC      | Oxygen [Partial pressure] adjusted to patient's actu…            | 19255-9      | [ABG PaO2](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=152)                                 |
| FiO2                            |          | 4353936    | SNOMED     | Inspired oxygen concentration                                    | 250774007    | [FiO2](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=301)                                     |
|---------------------------------|----------|------------|------------|------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| PEEP                            | 1        | 42527140   | LOINC      | Total PEEP Respiratory system (total, measured)                  | 76247-6      | [PEEP](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318)                                     |
| PEEP                            | 2        | 4216746    | SNOMED     | Positive end expiratory pressure setting                         | 416595007    | [PEEP](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318)                                     |
| PEEP                            | 3        | 4353713    | SNOMED     | Positive end expiratory pressure (general, no inform…            | 250854009    | [PEEP](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318)                                     |
|---------------------------------|----------|------------|------------|------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Pplat                           |          | 44782825   | SNOMED     | Airway plateau pressure                                          | 698822002    | [Plateau pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=320)                         |
| Pinsp                           | 1        | 4215838    | SNOMED     | Inspiratory pressure setting [cmH2O]                             | 417071008    | [Inspiratory pressure setting](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=314)             |
| Pinsp                           | 2        | 4101694    | SNOMED     | Peak inspiratory pressure [mmHg], CAVE different uni…            | 27913002     | [Peak inspiration pressure](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=319)                |
|---------------------------------|----------|------------|------------|------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| VT                              | 1        | 44782826   | SNOMED     | Inspiratory tidal volume                                         | 698823007    | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                             |
| VT                              | 2        | 4108448    | SNOMED     | Spontaneous tidal volume                                         | 250816009    | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                             |
| VT                              | 3        | 3012410    | LOINC      | Tidal volume setting Ventilator                                  | 20112-9      | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                             |
| VT                              | 4        | 4029625    | SNOMED     | Tidal volume (general, no information about setting/measurement) | 13621006     | [Tidal volume](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322)                             |

<!-- inject:BodyHeight,IdealBodyWeight,EndotrachealTube,InvasiveMechanicalVentilation,PEEPMeasurements,TidalVolumeMeasurements -->
| Concept ID                                                       | Concept Name                             | Descendants | DD Concept Set                                                                                                              |
|---                                                               |---                                       |---          |---                                                                                                                          |
| [607590](https://athena.ohdsi.org/search-terms/terms/607590)     | Body height                              | no          | [Body height (274)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=274) v1.1.0                             |
| [3036277](https://athena.ohdsi.org/search-terms/terms/3036277)   | Body height                              | no          | [Body height (274)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=274) v1.1.0                             |
| [600652](https://athena.ohdsi.org/search-terms/terms/600652)     | Recumbent body height                    | no          | [Body height (274)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=274) v1.1.0                             |
| [4093975](https://athena.ohdsi.org/search-terms/terms/4093975)   | Standing height                          | no          | [Body height (274)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=274) v1.1.0                             |
|---                                                               |---                                       |---          |---                                                                                                                          |
| [1073500](https://athena.ohdsi.org/search-terms/terms/1073500)   | Adjusted ideal body weight               | no          | [Ideal body weight (284)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284) v1.1.0                       |
| [4062985](https://athena.ohdsi.org/search-terms/terms/4062985)   | Ideal body weight                        | no          | [Ideal body weight (284)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284) v1.1.0                       |
| [3032445](https://athena.ohdsi.org/search-terms/terms/3032445)   | Ideal body weight                        | no          | [Ideal body weight (284)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=284) v1.1.0                       |
|---                                                               |---                                       |---          |---                                                                                                                          |
| [4097216](https://athena.ohdsi.org/search-terms/terms/4097216)   | Endotracheal tube                        | yes         | [Endotracheal tube (299)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=299) v1.1.0                       |
|---                                                               |---                                       |---          |---                                                                                                                          |
| [37158404](https://athena.ohdsi.org/search-terms/terms/37158404) | Invasive mechanical ventilation          | no          | [Invasive mechanical ventilation (306)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=306) v1.1.0         |
|---                                                               |---                                       |---          |---                                                                                                                          |
| [4160171](https://athena.ohdsi.org/search-terms/terms/4160171)   | Best positive end expiratory pressure    | no          | [Positive End-Expiratory Pressure (PEEP) (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.1.2 |
| [42528515](https://athena.ohdsi.org/search-terms/terms/42528515) | Extrinsic PEEP Respiratory system        | no          | [Positive End-Expiratory Pressure (PEEP) (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.1.2 |
| [3035822](https://athena.ohdsi.org/search-terms/terms/3035822)   | Intrinsic PEEP Respiratory system        | no          | [Positive End-Expiratory Pressure (PEEP) (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.1.2 |
| [4353713](https://athena.ohdsi.org/search-terms/terms/4353713)   | Positive end expiratory pressure         | no          | [Positive End-Expiratory Pressure (PEEP) (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.1.2 |
| [4216746](https://athena.ohdsi.org/search-terms/terms/4216746)   | Positive end expiratory pressure setting | no          | [Positive End-Expiratory Pressure (PEEP) (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.1.2 |
| [3022875](https://athena.ohdsi.org/search-terms/terms/3022875)   | Positive end expiratory pressure settin… | no          | [Positive End-Expiratory Pressure (PEEP) (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.1.2 |
| [42527140](https://athena.ohdsi.org/search-terms/terms/42527140) | Total PEEP Respiratory system            | no          | [Positive End-Expiratory Pressure (PEEP) (318)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=318) v1.1.2 |
|---                                                               |---                                       |---          |---                                                                                                                          |
| [44782827](https://athena.ohdsi.org/search-terms/terms/44782827) | Expiratory tidal volume                  | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [44782826](https://athena.ohdsi.org/search-terms/terms/44782826) | Inspiratory tidal volume                 | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [4353946](https://athena.ohdsi.org/search-terms/terms/4353946)   | Mandatory tidal volume                   | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [4108448](https://athena.ohdsi.org/search-terms/terms/4108448)   | Spontaneous tidal volume                 | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [4029625](https://athena.ohdsi.org/search-terms/terms/4029625)   | Tidal volume                             | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [21490752](https://athena.ohdsi.org/search-terms/terms/21490752) | Tidal volume expired Respiratory system… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [21490789](https://athena.ohdsi.org/search-terms/terms/21490789) | Tidal volume expired Respiratory system… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3011767](https://athena.ohdsi.org/search-terms/terms/3011767)   | Tidal volume expired spontaneous correc… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3020572](https://athena.ohdsi.org/search-terms/terms/3020572)   | Tidal volume expired spontaneous uncorr… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3009097](https://athena.ohdsi.org/search-terms/terms/3009097)   | Tidal volume expired spontaneous+mechan… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3015016](https://athena.ohdsi.org/search-terms/terms/3015016)   | Tidal volume expired spontaneous+mechan… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3033780](https://athena.ohdsi.org/search-terms/terms/3033780)   | Tidal volume inspired spontaneous+mecha… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3021470](https://athena.ohdsi.org/search-terms/terms/3021470)   | Tidal volume inspired spontaneous+mecha… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3016166](https://athena.ohdsi.org/search-terms/terms/3016166)   | Tidal volume inspired spontaneous+mecha… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3012410](https://athena.ohdsi.org/search-terms/terms/3012410)   | Tidal volume setting Ventilator          | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3008805](https://athena.ohdsi.org/search-terms/terms/3008805)   | Tidal volume sigh spontaneous+mechanica… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [21490854](https://athena.ohdsi.org/search-terms/terms/21490854) | Tidal volume Ventilator --on ventilator  | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [36303816](https://athena.ohdsi.org/search-terms/terms/36303816) | Tidal volume.inspired                    | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3017594](https://athena.ohdsi.org/search-terms/terms/3017594)   | Tidal volume.spontaneous --on ventilator | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3004732](https://athena.ohdsi.org/search-terms/terms/3004732)   | Tidal volume.spontaneous+mechanical --o… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3007828](https://athena.ohdsi.org/search-terms/terms/3007828)   | Tidal volume.spontaneous+mechanical cor… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |
| [3017707](https://athena.ohdsi.org/search-terms/terms/3017707)   | Tidal volume.spontaneous+mechanical unc… | no          | [Tidal volume (Vt) (322)](https://indicate-eu.github.io/data-dictionary/#/concept-sets?id=322) v1.1.1                       |

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
    AND ventilation mode IN (VCV OR PCV from ventilation-modes.md)
    AND are intubated
    AND an ARDS is diagnosed
during the observation period.
```

Note: (ventilation mode IN (VCV OR PCV)) is false if no mechanical ventilation is performed.
temporal proximity of pa02 and fio2 (how close temporally, does one have to preceed the other) -> create issue @sebastian

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
