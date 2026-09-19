# Heart Rate Variability Analysis

Python-based analysis of annotated ECG recordings to calculate heart rate and heart rate variability (HRV) metrics, visualise beat-to-beat dynamics with Poincaré plots, and investigate differences between younger and older adult groups.

## Project Overview

This project analyses annotated ECG heartbeat recordings to investigate **heart rate variability (HRV)** — the variation in timing between successive heartbeats.

The analysis covers the complete workflow from heartbeat annotations through to HRV metrics, visualisation and statistical comparison.

### Key questions

- How can annotated ECG heartbeat data be converted into NN intervals?
- How can heart rate and HRV be quantified using standard metrics?
- How can beat-to-beat variability be visualised?
- How do HRV measures differ between younger and older participant groups?
- What statistical tests are appropriate when comparing the groups?

For readers unfamiliar with HRV, see:

**[Understanding HRV](docs/understanding-hrv.md)**

---

## Dataset

The project uses annotated ECG recordings associated with the **Fantasia dataset**.

The source material describes recordings from healthy young and elderly participants during approximately 120 minutes of resting ECG recording. The dataset includes both male and female participants in each age group.

The supplied annotation files contain two main fields:

| Field | Description |
|---|---|
| `time` | Time of each annotated heartbeat in milliseconds |
| `type` | Heartbeat type; `N` represents normal sinus rhythm |

The analysis focuses on normal (`N`) beats and uses the intervals between successive normal beats as the basis for HRV calculations.

> **Data note:** The repository should contain the dataset files only where redistribution is permitted. If the original data cannot be redistributed, the README should retain the expected file structure and provide instructions for obtaining the data from the original source.

---

## Analytical Workflow

```text
ECG heartbeat annotations
          ↓
Identify normal (N) beats
          ↓
Calculate NN intervals
          ↓
Calculate heart rate and HRV metrics
          ↓
Consolidate participant results
          ↓
Generate Poincaré plots
          ↓
Explore group differences
          ↓
Check statistical assumptions
          ↓
Apply statistical tests
```

---

## HRV Metrics

The project calculates:

| Metric | Description |
|---|---|
| **Mean NN** | Mean duration of normal-to-normal intervals |
| **Mean BPM** | Mean heart rate calculated from NN intervals |
| **SDNN** | Standard deviation of NN intervals |
| **RMSSD** | Root mean square of successive NN interval differences |
| **pNN20** | Percentage of successive differences greater than 20 ms |
| **pNN50** | Percentage of successive differences greater than 50 ms |

These metrics capture different aspects of heart rate variability, including overall and short-term beat-to-beat variation.

---

## Poincaré Visualisation

Poincaré plots are used to visualise the relationship between successive NN intervals.

For each observation:

```text
X = NNₙ
Y = NNₙ₊₁
```

This provides a direct visual representation of beat-to-beat dynamics.

The notebook generates Poincaré plots for the participant recordings and uses them alongside numerical HRV measures to explore variability patterns.

---

## Implementation

### `hrv.py`

Contains reusable functions for HRV analysis:

```python
calculate_HRV_metrics(file_in)
```

Calculates HRV metrics from an annotated recording.

```python
process_HRV_files(file_list_in, file_out)
```

Processes multiple recordings and creates a consolidated results dataset.

The implementation performs the intermediate calculations required to derive NN intervals, successive differences and the final HRV metrics.

### `HRV_analysis.ipynb`

The notebook provides the end-to-end analysis, including:

- loading and exploring the data
- batch HRV calculation
- data consolidation
- Poincaré plots
- group-level visualisation
- descriptive statistics
- assumption checking
- statistical comparison
- interpretation of results

---

## Statistical Analysis

The project compares younger and older participant groups.

### Mean BPM

The analysis found:

- Younger group mean BPM: **60.32**
- Older group mean BPM: **57.22**
- t-test: **t = 0.802, p = 0.433**

### RMSSD

The analysis found:

- Younger group mean RMSSD: **70.42 ms**
- Older group mean RMSSD: **34.21 ms**
- t-test: **t = 2.499, p = 0.022**

The project also checks assumptions before selecting statistical tests.

For RMSSD, the older group showed evidence of non-normality, so a non-parametric alternative such as the Mann–Whitney U test is considered appropriate.

---

## Visualisations

The project includes:

- Poincaré plots
- group comparison dot plots
- box plots
- Q-Q plots
- heartbeat-type frequency plots
- exploratory HRV visualisations

These visualisations complement the numerical metrics and statistical analysis.

---

## Project Structure

```text
heart-rate-variability-analysis/
│
├── README.md
├── hrv.py
├── HRV_analysis.ipynb
│
├── data/
│   ├── y01.csv
│   ├── ...
│   ├── y10.csv
│   ├── o01.csv
│   ├── ...
│   └── o10.csv
│
├── outputs/
│   └── fantasia.csv
│
└── docs/
    └── understanding-hrv.md
```

If the dataset is not redistributed with the repository, the `data/` directory can instead contain a short README explaining where the permitted source data should be placed.

---

## Technologies

- **Python**
- **Pandas**
- **NumPy**
- **SciPy**
- **Matplotlib**
- **Jupyter Notebook**

---

## Reproducibility

1. Obtain the permitted Fantasia/annotation data.
2. Place the annotation files in the expected `data/` directory.
3. Install the required Python packages.
4. Run `HRV_analysis.ipynb`.
5. The notebook processes the recordings, calculates HRV metrics, generates visualisations and performs the statistical analysis.

Example environment setup:

```bash
pip install pandas numpy scipy matplotlib jupyter
```

Then launch Jupyter:

```bash
jupyter notebook
```

and open:

```text
HRV_analysis.ipynb
```

---

## Key Skills Demonstrated

### Data Analysis
- Data loading and validation
- Data transformation
- Batch processing
- Feature calculation
- Descriptive statistics

### Statistical Analysis
- Distribution and assumption checking
- t-tests
- Non-parametric statistical testing
- Group comparison
- Interpretation of statistical results

### Data Visualisation
- Poincaré plots
- Box plots
- Q-Q plots
- Group comparison plots
- Exploratory visualisation

### Python Development
- Reusable functions
- Modular analysis
- Pandas-based data processing
- NumPy numerical computation
- SciPy statistical analysis
- Matplotlib visualisation

---

## Limitations

- The analysis is based on annotated heartbeat data rather than direct processing of the raw ECG waveform.
- The project focuses on a selected set of HRV metrics.
- Group comparisons are based on the available participant sample.
- HRV is influenced by multiple physiological and experimental factors, so group differences should be interpreted within the context of the study design.
- Statistical conclusions depend on the assumptions and sample characteristics of the analysis.

---

## Future Improvements

Potential extensions include:

- Add additional time-domain HRV measures.
- Add frequency-domain HRV analysis.
- Analyse raw ECG signals and implement R-peak detection.
- Add automated data-quality checks.
- Build a more comprehensive participant-level reporting pipeline.
- Extend the visualisation layer with interactive plots.
- Add automated statistical test selection based on validated assumptions.

---

## Project Context

Academic data science project focused on applying Python-based data processing, statistical analysis and visualisation techniques to physiological time-series data.

The repository has been organised as a portfolio project so that both technical and non-technical readers can understand the analytical problem, methodology and results without needing the original coursework material.
