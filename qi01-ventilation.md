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

FiO2 | 0.3 | 0.5 | 0.6 | 0.8 | 1.0
----------------------------------
PEEP |   5 |   8 |  10 |  14 |  18

#### high PEEP table

FiO2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.9
----------------------------------
PEEP |   5 |  14 |  16 |  20 |  22


### Ideal Body Weight

We calculate the ideal body weight (IBW) based on the Devine formula:
- women: IBW = 45.5 [kg] + 0.91 [kg] * (body height [cm] - 152.4)
- men:   IBW = 50 [kg] + 0.91 [kg] * (body height [cm] - 152.4)

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

Plateau pressure is defined for VCV.
For PCV we will use the inspiratory pressure (Pinsp).

```
Pplat:
    IF ventilation mode IS VCV
        Pplat
    ELSE
        Pinsp
```

### Pressure difference

```
Pdelta = Pplat - PEEP
```


## Mapping

athena concept ids

body height [cm]:
- 607590

Gender:
- 4135376

IBW:
- 40308117

ARDS:
- 45552897

intubated (tube present):
- 4097216

invasive ventilation (invasive ventilation requires a tube)/mechanical ventilated:
- 37158404

ventilation mode:
- 37042784

PaO2/FiO2:
- 3029943

PaO2:
- 3027801

FiO2:
- 4353936

PEEP:
- 4353713

Pplat:
- 44782825

Pinsp:
- 4215838

VT:
- 4029625 (measurement)


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
    AND mechanical ventilated
    AND are intubated
    AND an ARDS is diagnosed
during the observation period.


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