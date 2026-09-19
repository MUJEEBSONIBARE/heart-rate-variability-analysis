# Heart Rate Variability (HRV) Analysis

Python-based analysis of annotated ECG heartbeat recordings to calculate heart rate and heart rate variability (HRV) metrics, visualise beat-to-beat dynamics with Poincaré plots, and investigate differences between young and older adult groups.

The project was originally completed as an **ECMM443 Introduction to Data Science** investigation and has been organised here as a portfolio project demonstrating data processing, statistical analysis, visualisation, and scientific interpretation.

> **Note:** This is an academic data-analysis project and is not a clinical diagnostic tool.

---

## Project Overview

Heart Rate Variability (HRV) describes variation in the time interval between successive heartbeats. Rather than treating the heart as a metronome, HRV analysis examines the natural variation between consecutive normal sinus beats.

This project analyses annotated ECG recordings from **20 individuals**:

- 10 younger participants
- 10 older participants
- 5 males and 5 females in each age group
- Approximately 120 minutes of ECG annotation data per recording

The analysis focuses on the relationship between age group, heart rate, and HRV.

---

## Objectives

The project had six main objectives:

1. Build reusable Python functions to calculate HRV metrics from annotated ECG recordings.
2. Process multiple recordings and consolidate the calculated metrics into a structured dataset.
3. Visualise beat-to-beat relationships using Poincaré plots.
4. Compare heart rate and HRV between younger and older participants using statistical tests.
5. Assess the assumptions underlying the statistical analysis.
6. Critically discuss the findings in the context of existing research on age, gender, heart rate, and HRV.

---

## Dataset

The dataset contains annotated heartbeat recordings stored as CSV files.

Each recording contains:

| Column | Description |
|---|---|
| `time` | Timing of the identified heartbeat |
| `type` | Heartbeat annotation/type |

`N` represents a normal sinus rhythm beat. Other labels identify non-normal or ectopic beat types.

The recordings are divided into:

```text
y01.csv – y10.csv    # younger group
o01.csv – o10.csv    # older group
```

The recordings contain thousands of annotated heartbeats and represent approximately two hours of data per participant.

---

## Data Processing Pipeline

The analysis follows this general workflow:

```text
Annotated ECG recordings
          │
          ▼
Load CSV files with Pandas
          │
          ▼
Identify consecutive heartbeat intervals
          │
          ▼
Filter for NN intervals
          │
          ▼
Calculate HRV metrics
          │
          ▼
Process all recordings
          │
          ▼
Combine with participant metadata
          │
          ▼
Exploratory visualisation
          │
          ▼
Statistical comparison
          │
          ▼
Interpretation and critical evaluation
```

---

# HRV Metrics

The project calculates six main measures.

### Mean NN

Average duration of all consecutive normal-to-normal heartbeat intervals.

Reported in milliseconds.

### Mean BPM

Average heart rate calculated from the mean NN interval:

```text
Mean BPM = (1000 / Mean NN) × 60
```

### SDNN

Standard deviation of the NN intervals.

This provides a measure of overall variability in the NN interval series.

### RMSSD

Root Mean Square of Successive Differences:

```text
RMSSD = sqrt(mean(successive NN interval differences²))
```

RMSSD was used as the primary indicator of heart rate variability in the age-group comparison.

### pNN20

Percentage of successive NN interval differences with an absolute magnitude greater than 20 ms.

### pNN50

Percentage of successive NN interval differences with an absolute magnitude greater than 50 ms.

---

# Implementation

## `hrv.py`

The main reusable processing functions are:

### `calculate_HRV_metrics(file_in)`

Loads an annotated ECG CSV file and calculates:

- Number of NN intervals
- Mean NN
- Mean BPM
- SDNN
- RMSSD
- pNN20
- pNN50

The implementation constructs intermediate variables representing:

- next heartbeat time
- next heartbeat type
- RR interval
- RR interval type
- next RR interval
- successive interval difference
- squared interval difference

A minimum valid-data threshold is also used before calculating the metrics.

### `process_HRV_files(file_list_in, file_out)`

Processes a list of ECG recording files, applies `calculate_HRV_metrics()` to each recording, and saves the consolidated results as CSV.

The function also handles missing input files by reporting the problem while continuing to process the remaining valid files.

---

# Exploratory Analysis

The notebook investigates the recordings at both the individual-recording and group levels.

## Poincaré Plots

A 4 × 5 grid of Poincaré plots is generated for the 20 recordings.

Each plot compares:

```text
NN(i)       vs       NN(i+1)
```

This provides a visual representation of beat-to-beat variability.

The plots allow the recordings from the younger and older groups to be visually compared. The completed analysis observed generally broader distributions for many younger recordings and more concentrated patterns in several older recordings.

---

# Statistical Analysis

The analysis compares the younger and older groups for:

1. Mean BPM
2. RMSSD

Independent-samples t-tests were initially used to assess whether the group means differed.

### Mean BPM

The completed analysis reported:

```text
t = 0.802
p = 0.433
```

The analysis therefore did not identify statistical evidence of a difference in mean BPM between the two groups at the 0.05 significance level.

Group means calculated in the notebook were approximately:

| Group | Mean BPM |
|---|---:|
| Young | 60.32 |
| Old | 57.22 |

### RMSSD

The completed analysis reported:

```text
t = 2.499
p = 0.022
```

At the 0.05 significance level, the analysis found statistical evidence of a difference in RMSSD between the two age groups.

The corresponding group means were approximately:

| Group | Mean RMSSD |
|---|---:|
| Young | 70.42 ms |
| Old | 34.21 ms |

These results describe this particular sample and analysis; they should not be interpreted as a clinical conclusion about HRV in the general population.

---

# Statistical Assumption Checking

Because the sample sizes are small, the notebook also investigates the assumptions behind the t-test.

The analysis uses:

- Q-Q plots
- Shapiro-Wilk normality tests

### Mean BPM

The Shapiro-Wilk results were:

| Group | Shapiro-Wilk p-value |
|---|---:|
| Young | 0.655 |
| Old | 0.705 |

The analysis found no evidence against normality for either group's mean BPM distribution.

### RMSSD

The Shapiro-Wilk results were:

| Group | Shapiro-Wilk p-value |
|---|---:|
| Young | 0.275 |
| Old | 0.000318 |

The older-group RMSSD distribution showed evidence of non-normality.

The project therefore discusses the limitations of applying a parametric t-test to the RMSSD comparison and identifies the **Mann-Whitney U test** as an appropriate non-parametric alternative for independent samples when the normality assumption is not satisfied.

---

# Data Quality Investigation

The analysis also examines the heartbeat annotations before interpreting the group-level results.

For example, the `y01.csv` recording contained:

```text
Normal (N) beats: 8708
Non-normal beats: 2
```

The notebook visualises heartbeat-type frequencies to assess whether recordings contain unusually large numbers of non-normal annotations that could influence the analysis.

This provides an additional quality-control step before comparing participants.

---

# Key Findings

The completed analysis produced several main observations:

- Heart rate showed no statistically significant difference between the young and old groups in the independent-samples t-test.
- RMSSD showed a statistically significant group difference in the completed t-test.
- The younger group had a higher mean RMSSD than the older group in this dataset.
- Poincaré plots provided a visual representation consistent with greater beat-to-beat variation in many of the younger recordings.
- Normality checks indicated that the t-test assumptions were more problematic for RMSSD than for mean BPM.
- The analysis therefore highlighted the importance of checking statistical assumptions rather than relying solely on the output of a statistical test.

---

# Visualisations

The notebook contains several forms of visual analysis:

### Poincaré plots

A 4 × 5 grid covering all 20 recordings.

### Group dot plots

Group-level mean values with standard-error bars for:

- Mean BPM
- RMSSD

### Box plots

Distribution comparisons between young and old groups for:

- Mean BPM
- RMSSD

### Q-Q plots

Normality assessment for:

- Young mean BPM
- Old mean BPM
- Young RMSSD
- Old RMSSD

### Heartbeat-type frequency plot

A bar chart showing the distribution of heartbeat annotations for an individual recording.

---

# Technologies

The project uses:

- **Python**
- **Pandas** — data loading, transformation and tabular analysis
- **NumPy** — numerical calculations
- **SciPy** — statistical testing
- **Matplotlib** — visualisation
- **Jupyter Notebook** — analysis workflow and documentation

---

# Repository Structure

The recommended portfolio structure is:

```text
HRV-analysis/
│
├── README.md
│
├── hrv.py
│
├── HRV_analysis.ipynb
│
├── data/
│   ├── o01.csv
│   ├── o02.csv
│   ├── ...
│   ├── o10.csv
│   ├── y01.csv
│   ├── y02.csv
│   ├── ...
│   └── y10.csv
│
└── outputs/
    └── fantasia.csv
```

If the participant metadata file is available, it should also be included in the `data/` directory:

```text
data/
└── fantasia_individuals.csv
```

---

# Reproducing the Analysis

## 1. Clone the repository

```bash
git clone https://github.com/MUJEEBSONIBARE/HRV-analysis.git
cd HRV-analysis
```

## 2. Install dependencies

```bash
pip install pandas numpy matplotlib scipy jupyter
```

## 3. Run the Python functions

The reusable functions are contained in:

```text
hrv.py
```

They can be imported into Python or used from the notebook.

## 4. Open the notebook

```bash
jupyter notebook HRV_analysis.ipynb
```

Run the notebook cells in sequence to reproduce the data processing, visualisations and statistical analysis.

---

# Reproducibility Note

The original coursework archive contains the 20 ECG annotation files used in the analysis.

The completed notebook also references a participant metadata file named:

```text
fantasia_individuals.csv
```

This metadata file is **not present in the supplied project archive used to create this repository**. It was nevertheless available to the original notebook when the analysis was performed, as demonstrated by the completed notebook output containing age, sex and group information.

Therefore, the participant-level age/sex merge cannot be reproduced from the supplied archive alone unless the metadata file is added.

For a fully reproducible repository, `fantasia_individuals.csv` should be placed in the `data/` directory.

---

# Portfolio Value

This project demonstrates a complete small-scale data science workflow:

```text
Raw data
   ↓
Data ingestion
   ↓
Feature engineering
   ↓
Domain-specific metric calculation
   ↓
Data aggregation
   ↓
Exploratory visualisation
   ↓
Statistical testing
   ↓
Assumption checking
   ↓
Critical interpretation
```

It demonstrates practical experience with:

- Data cleaning and transformation
- Reusable Python functions
- Batch processing
- Statistical feature engineering
- Exploratory data analysis
- Scientific visualisation
- Hypothesis testing
- Normality assessment
- Parametric vs non-parametric methods
- Interpretation of statistical results
- Reproducible analytical workflows

---

# Limitations

Several limitations should be considered when interpreting the results:

- The analysis uses a relatively small sample of 20 recordings.
- The age comparison contains only 10 participants per group.
- RMSSD for the older group did not satisfy the normality assumption according to the Shapiro-Wilk test.
- The analysis focuses primarily on age-group comparisons rather than modelling the independent effects of age and gender simultaneously.
- The results describe this dataset and should not be generalised to a wider population without further evidence.
- The participant metadata required for complete reproduction is missing from the supplied project archive.

---

# Further Development

Potential extensions include:

- Applying the Mann-Whitney U test to the RMSSD comparison.
- Comparing additional HRV metrics between groups.
- Investigating gender alongside age.
- Examining the relationship between continuous age and HRV.
- Adding automated data-quality checks for abnormal heartbeat annotations.
- Creating a reusable analysis pipeline for additional ECG datasets.
- Improving visualisation and automated reporting.
- Adding unit tests for the HRV metric calculation functions.

---

## Author

**Mujeeb Sonibare**

GitHub: `MUJEEBSONIBARE`

---

## Academic Context

Originally completed as an **ECMM443 — Introduction to Data Science** investigation at the University of Exeter.

The original coursework focused on designing a data science pipeline, investigating an ECG-derived dataset using mathematical and visualisation techniques, applying statistical pattern-recognition methods, and critically evaluating research relating to heart rate and heart rate variability.
