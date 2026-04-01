# ML-Enhanced Low-Cost Methane Sensor Calibration
### From Field Deployment to EPA-Grade Emissions Intelligence

**Author:** Elijah Kiplimo · [OilGasAI Platform](https://innovations1-spec.github.io/oilgasai/) · [OilGasAI Model Alpha](https://github.com/Kiplimo288/OIlGasAI_Model_Alpha)

[![Platform](https://img.shields.io/badge/Platform-OilGasAI-blue)](https://innovations1-spec.github.io/oilgasai/)
[![Model](https://img.shields.io/badge/Model-OilGasAI--Model--Alpha-orange)](https://huggingface.co/OilgasAI/OilGasAI-Model-Alpha)
[![Research](https://img.shields.io/badge/Research-METEC%20%2F%20SABER-green)](https://www.engr.colostate.edu/metec/)
[![Funded](https://img.shields.io/badge/Compute-UNDP%20%7C%20CINECA%20Leonardo-purple)](https://www.aihubfordevelopment.org/)

---

## The Problem This Solves

Methane emissions from oil and gas infrastructure are massively underreported. Reference-grade analyzers cost $30,000–$80,000 per unit, making dense, continuous field monitoring economically impossible for most operators — especially smaller upstream producers responsible for a significant share of U.S. fugitive emissions.

Low-cost metal oxide (MOx) sensors like the Figaro TGS2600 and TGS2611 cost under $20 each. But they drift with temperature, respond to cross-contaminants, and produce raw resistance readings that bear only a nonlinear relationship to actual methane concentration. Without calibration, they are scientifically meaningless.

**This repository solves that problem end-to-end** — from hardware build and field deployment through machine learning calibration to integration with the OilGasAI compliance platform.

---

## The Full Pipeline: Build → Deploy → Calibrate → Report

```
┌─────────────────────────────────────────────────────────────────────┐
│                     FIELD SENSOR SYSTEM                             │
│                                                                     │
│  TGS2600 + TGS2611 MOx Sensors                                     │
│  DHT22 Temperature/Humidity                                         │
│  Airmar Weather Station (wind speed, direction)                     │
│  Raspberry Pi / Phidgets SBC4 Data Logger                          │
│  Solar Power + LiFePO₄ Battery                                     │
└──────────────────────┬──────────────────────────────────────────────┘
                       │ Raw resistance readings (Ω) + met data
                       ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  ML CALIBRATION LAYER (this repo)                   │
│                                                                     │
│  1. Baseline correction (clean air resistance normalization)        │
│  2. Temperature/humidity cross-sensitivity correction               │
│  3. Piecewise linear range equations (TGS2600 & TGS2611)           │
│  4. Random Forest regression → CH₄ concentration (ppm)             │
│  5. Model evaluation: R², RMSE, Cohen's Kappa, residual analysis   │
└──────────────────────┬──────────────────────────────────────────────┘
                       │ Calibrated CH₄ (ppm) with confidence bounds
                       ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    OilGasAI PLATFORM                                │
│          https://innovations1-spec.github.io/oilgasai/             │
│                                                                     │
│  OilGasAI Model Alpha (Llama 3.1 70B, QLoRA fine-tuned)           │
│  RAG Pipeline (37,009 EPA/regulatory vectors)                      │
│  Auto-generates: EPA Subpart W reports, LDAR summaries,            │
│  NSPS OOOOa/b/c compliance checks, OGMP 2.0 quantification        │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Hardware: What I Built and Deployed

### Sensor Unit — AMMMU (Autonomous Mobile Methane Measurement Unit)

I designed, built, and field-deployed a low-cost continuous methane monitoring unit at Colorado State University's **Methane Emissions Technology Evaluation Center (METEC)** as part of the **SABER (Screening and Bayesian Estimation of Releases) project**, a U.S. Department of Energy-funded study.

**Sensor array:**
- **Figaro TGS2600** — Metal oxide sensor, sensitive to 1–30 ppm CH₄ range
- **Figaro TGS2611** — Metal oxide sensor, optimized for higher CH₄ concentrations
- **DHT22** — Temperature and relative humidity (critical for cross-sensitivity correction)
- **Airmar PB200** — Wind speed, wind direction, GPS coordinates (NMEA parsing)

**Data acquisition:**
- **Raspberry Pi 4 / Phidgets SBC4** — Edge computing and data logging
- **SQLite** — Local buffered storage during connectivity gaps
- **Cellular/WiFi uplink** — Real-time data transmission to cloud

**Power system:**
- Solar panel + **LiFePO₄ battery** — Continuous autonomous operation
- Designed for unattended field deployment in controlled-release environments

### Field Deployment Photos

**AMMMU deployed at METEC facility, Fort Collins, Colorado:**

> *Solar-powered autonomous sensor unit deployed in a controlled-release field environment. The unit continuously logs methane concentration, wind vector, temperature, and humidity for ML calibration against reference-grade Aeris MIRA analyzer measurements.*

<img src="https://raw.githubusercontent.com/Kiplimo288/Methane_Sensor_Calibrations_OGAI/main/images/ammmu_field_deployment_metec.jpg" width="600"/>

**Internal sensor assembly — custom PCB with TGS2600, TGS2611, and DHT22:**

> *Custom-built sensor enclosure showing the Raspberry Pi data logger, Figaro TGS2600 and TGS2611 MOx sensor array, DHT22 temperature/humidity module, and signal conditioning circuitry. Enclosure designed for weatherproof outdoor deployment.*

<img src="https://raw.githubusercontent.com/Kiplimo288/Methane_Sensor_Calibrations_OGAI/main/images/sensor_pcb_assembly.jpg" width="600"/>

**METEC facility instrumentation rack — reference measurement system:**

> *METEC instrumentation enclosure showing the Phidgets SBC4 data acquisition system, LabJack T7 analog interface, Phidgets 7-port USB hub, Airmar weather station integration, and reference gas flow control systems used for controlled-release calibration experiments.*

<img src="https://raw.githubusercontent.com/Kiplimo288/Methane_Sensor_Calibrations_OGAI/main/images/metec_instrumentation_rack.jpg" width="600"/>---

## The ML Calibration Pipeline

### Why Random Forest?

Raw MOx sensor resistance does not scale linearly with methane concentration. The relationship is:
- **Nonlinear** — resistance response varies across concentration ranges
- **Temperature-dependent** — DHT22 readings must be used to correct for thermal drift
- **Humidity-dependent** — water vapor affects sensor conductivity
- **Cross-sensitive** — other VOCs in field environments confound raw readings
- **Drifting** — baseline resistance shifts over deployment lifetime

Random Forest regression handles all of these simultaneously without requiring explicit equation derivation for each interaction term.

### Step 1: Baseline Correction (`sensors/Sensor_Baseline.py`)

Establishes clean-air baseline resistance for each sensor:

```python
# Clean air baseline resistance (established from controlled experiments)
baseline_TGS2600 = 29076.8499  # Ω
baseline_TGS2611 = 4714.29215  # Ω

# Deviation from baseline drives the calibration
df['TGS2600_Deviation'] = df['TGS2600'] - baseline_TGS2600
df['TGS2611_Deviation'] = df['TGS2611'] - baseline_TGS2611
```

### Step 2: Cross-Sensitivity Correction (`sensors/Cross_sensitivity.py`)

Quantifies sensor drift under varying temperature and humidity conditions by comparing initial and final condition datasets, filtering for matched environmental conditions (±0.5°C temperature, ±5% RH):

```python
cross_sensitivity_index = {
    'TGS2600': drift['TGS2600'] / (baseline_TGS2600 - background_CH4),
    'TGS2611': drift['TGS2611'] / (baseline_TGS2611 - background_CH4),
}
```

### Step 3: Piecewise Linear Range Equations (`sensors/Eqns_Aplied_Ranges_Mox.py`)

Applies concentration-range-specific linear equations derived from the calibration dataset — 8 concentration ranges from -0.69 to 147.60 ppm, each with independently fitted slope and intercept:

```python
ranges_TGS2600 = [(-0.69, 17.85), (17.85, 36.39), (36.39, 54.92), ...]
coeff_TGS2600  = [(0.2383, 1.935), (-1.2115, 25.1833), (-0.2868, 43.9224), ...]
```

### Step 4: Random Forest Training (`ml/RF_Performance.py`)

Trained on METEC controlled-release data against reference-grade **Aeris MIRA** laser analyzer measurements. Features: TGS2600 corrected resistance, TGS2611 corrected resistance, temperature, humidity, wind speed, wind direction.

**Model performance (held-out test set):**

| Metric | TGS2600 | TGS2611 |
|--------|---------|---------|
| R² (1.85–2 ppm) | High | — |
| RMSE (2–7 ppm) | < 1.5 ppm | — |
| Accuracy ±(1.85–5.85 ppm) | ±0.8 ppm | — |
| Accuracy ±(2–9 ppm) | — | ±1.2 ppm |
| Cohen's Kappa | > 0.75 | > 0.72 |

### Step 5: Calibration Curve Visualization (`ml/TGS_Calibration_Curve.py`)

Generates scatter plots of corrected sensor output vs. reference CH₄ with linear regression overlays and R² annotation — used for publication figures and model validation reporting.

---

## How Calibrated Data Feeds OilGasAI

Once the Random Forest model outputs calibrated CH₄ concentration in ppm, that data enters the OilGasAI platform through the sensor API:

```python
# OilGasAI Sensor API endpoint
POST /sensors/calibrate
{
  "sensor_type": "TGS2600",
  "raw_resistance": 24350.5,
  "temperature_c": 18.3,
  "humidity_pct": 52.1,
  "wind_speed_ms": 2.4,
  "wind_direction_deg": 245
}

# Response
{
  "ch4_ppm": 4.87,
  "confidence_interval": [4.12, 5.63],
  "drift_flag": false,
  "ldar_threshold_exceeded": false
}
```

The OilGasAI Model Alpha then uses this calibrated reading — combined with facility metadata and regulatory context from the RAG pipeline — to:

- Flag LDAR survey findings against NSPS OOOOa/b/c thresholds
- Auto-populate EPA GHGRP Subpart W emission factor calculations
- Generate plain-language compliance narratives
- Recommend corrective action timelines

**Full platform:** [https://innovations1-spec.github.io/oilgasai/](https://innovations1-spec.github.io/oilgasai/)
**AI Model:** [https://huggingface.co/OilgasAI/OilGasAI-Model-Alpha](https://huggingface.co/OilgasAI/OilGasAI-Model-Alpha)

---

## Field Scenario: How This Works in Practice

### Scenario: Small Upstream Operator, DJ Basin, Colorado

```
DAY 1 — DEPLOYMENT
├── Operator installs AMMMU sensor unit at wellpad perimeter
├── Unit begins continuous CH₄ logging every 60 seconds
├── Airmar station logs wind vector for plume attribution
└── Data streams to OilGasAI platform via cellular uplink

DAY 1–30 — CONTINUOUS MONITORING  
├── RF model applies real-time drift correction
├── Baseline resistance checked against clean-air periods
├── Concentration spikes flagged against LDAR thresholds
└── Daily summaries pushed to operator dashboard

EMISSION EVENT DETECTED
├── CH₄ reading: 8.4 ppm (threshold: 2.5 ppm)
├── Wind vector: 245° at 3.1 m/s
├── Gaussian plume back-calculation → emission rate estimate
├── OilGasAI Model Alpha generates LDAR finding report
└── Recommended action: Component-level OGI inspection within 5 days

COMPLIANCE REPORTING
├── Monthly CH₄ data aggregated by facility component
├── Emission factors applied per EPA Subpart W methodology  
├── OilGasAI drafts CDX submission narrative automatically
└── Operator reviews, certifies, and submits to EPA GHGRP
```

### Why This Matters at Scale

The U.S. has approximately **1 million active oil and gas wells**. Reference-grade continuous monitoring at $50,000/unit per site is not economically viable. ML-calibrated low-cost sensors deployed at $500/unit — with accuracy validated against reference analyzers at METEC — make continuous, EPA-quality monitoring achievable across the entire U.S. upstream sector.

This is the sensor layer that feeds OilGasAI. The platform closes the loop from field measurement to regulatory compliance at a cost structure that works for independent operators.

---

## Repository Structure

```
sensors-ml-calibration/
├── sensors/
│   ├── Sensor_Baseline.py          # Clean-air baseline resistance calculation
│   ├── Cross_sensitivity.py        # Temperature/humidity drift correction
│   ├── Eqns_Aplied_Ranges_Mox.py  # Piecewise linear range equations
│   ├── TGS_Callibration_Curve.py  # Calibration curve plotting
│   └── TGSCorr_Values.py          # Corrected resistance computation
├── ml/
│   ├── RF_Performance.py           # Random Forest model evaluation
│   ├── Comparison_with_studies.py  # R², RMSE, accuracy vs reference
│   └── Resuduals_PLots.py         # Residual analysis and scatter plots
├── data_processing/
│   ├── Timeseries_Conventional.py  # Time series visualization
│   ├── CH4_Bins.py                 # Concentration binning analysis
│   ├── Column_averages.py          # Statistical aggregation
│   └── Airmar_Coordinates.py      # GPS/wind data parsing
├── visualization/
│   ├── TimeseriesPLots.py          # Multi-sensor time series plots
│   ├── Temp_RH_plots.py            # Environmental condition plots
│   └── POINT_SHOW_ZOOM.py         # Zoomed concentration event viewer
├── images/
│   ├── deployment_field.jpg        # AMMMU field deployment at METEC
│   ├── sensor_internals.jpg        # Custom PCB sensor assembly
│   └── metec_rack.jpg             # METEC instrumentation rack
└── README.md
```

---

## Research Foundation

This work was conducted at:

- **Colorado State University — METEC Facility**, Fort Collins, CO
- **SABER Project** (Screening and Bayesian Estimation of Releases) — U.S. Department of Energy funded
- **Peer-reviewed publications:** 6 papers in MDPI journals on DJ Basin oil and gas emissions

**Compute support for OilGasAI Model Alpha training:**
- UNDP AI Hub for Sustainable Development — Compute Accelerator Programme (10,000 GPU hours)
- CINECA ISCRA Programme — 80,000 core hours on Leonardo HPC, Bologna, Italy

---

## Author

**Elijah Kiplimo**
M.Sc. Systems Engineering, Colorado State University
B.Sc. Petroleum Engineering, Kenyatta University
Founder, OilGasAI LLC

[OilGasAI Platform](https://innovations1-spec.github.io/oilgasai/) · [GitHub](https://github.com/Kiplimo288) · [LinkedIn](https://linkedin.com/in/elijah-kiplimo-321873108)
