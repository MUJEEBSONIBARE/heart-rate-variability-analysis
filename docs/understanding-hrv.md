# Understanding Heart Rate Variability

## What is Heart Rate Variability?

Heart Rate Variability (HRV) describes the variation in the time between successive heartbeats.

A healthy heart does not beat like a perfectly regular metronome. The interval between one heartbeat and the next changes over time. HRV analysis measures and describes these changes in beat-to-beat timing.

This project uses annotated ECG recordings to extract the timing of normal heartbeats and calculate several measures of heart rate and heart rate variability.

---

## 1. Understanding the ECG

An electrocardiogram (ECG) records the electrical activity associated with the heart's activity.

A typical ECG cycle contains three main components:

- **P-wave** — associated with atrial depolarisation.
- **QRS complex** — associated with ventricular depolarisation.
- **T-wave** — associated with ventricular repolarisation.

For HRV analysis, the important feature is the timing of successive heartbeats, particularly the timing of the R waves within the QRS complexes.

---

## 2. ECG Annotations

The recordings used in this project contain heartbeat annotations.

Each annotation records:

| Field | Meaning |
|---|---|
| `time` | Time of the annotated heartbeat in milliseconds |
| `type` | Classification of the heartbeat |

The annotation `N` represents a **normal sinus rhythm** heartbeat.

For HRV calculations, the project focuses on normal beats and uses the intervals between successive normal beats.

These intervals are commonly referred to as **NN intervals**.

---

## 3. From ECG Beats to NN Intervals

Suppose normal beats occur at:

```text
Beat 1       Beat 2       Beat 3       Beat 4
  |            |            |            |
  R            R            R            R
  |<-- NN 1 -->|
               |<-- NN 2 -->|
                            |<-- NN 3 -->|
```

If the normal beats occur at different times, the difference between consecutive beat times gives the NN interval.

For example:

```text
Beat 1 = 1000 ms
Beat 2 = 1800 ms

NN interval = 1800 - 1000 = 800 ms
```

The sequence of NN intervals is therefore the fundamental input for the HRV calculations in this project.

---

## 4. Why Do We Look at Variability?

HRV can be examined at different timescales.

### Long-term variability

The distribution of NN intervals across a recording provides information about variability over the recording as a whole.

One way of quantifying this is **SDNN**, the standard deviation of the NN intervals.

### Short-term variability

We can also compare consecutive NN intervals:

```text
NN1 → NN2
NN2 → NN3
NN3 → NN4
```

The differences between successive intervals capture beat-to-beat changes.

**RMSSD**, for example, is based on these successive differences and therefore represents short-term beat-to-beat variability.

---

## 5. HRV Metrics Used in This Project

### Mean NN

The average duration of all normal-to-normal (NN) intervals in the recording.

It provides a measure of the typical time between normal heartbeats.

### Mean BPM

Mean heart rate calculated from the NN intervals.

The project calculates this using:

```text
Mean BPM = (1000 / Mean NN) × 60
```

where Mean NN is measured in milliseconds.

### SDNN

**Standard Deviation of NN intervals.**

SDNN measures the overall variation in the set of NN intervals.

```text
SDNN = standard deviation of NN intervals
```

It reflects variability across the recording rather than focusing specifically on individual successive differences.

### RMSSD

**Root Mean Square of Successive Differences.**

RMSSD is calculated from the differences between successive NN intervals.

Conceptually:

```text
NN1 → NN2 → NN3 → NN4

Difference 1 = NN2 - NN1
Difference 2 = NN3 - NN2
Difference 3 = NN4 - NN3
```

The squared successive differences are averaged and the square root is taken.

RMSSD therefore focuses on short-term, beat-to-beat variability.

### pNN20

The proportion of successive NN interval differences whose absolute value is greater than 20 ms.

### pNN50

The proportion of successive NN interval differences whose absolute value is greater than 50 ms.

---

## 6. Visualising HRV with a Poincaré Plot

A Poincaré plot provides a visual representation of successive NN intervals.

For each pair of consecutive intervals:

```text
x-axis = NNₙ
y-axis = NNₙ₊₁
```

For example:

```text
NNₙ = 1.2 seconds
NNₙ₊₁ = 0.9 seconds
```

This produces a point at:

```text
(1.2, 0.9)
```

The plot therefore shows how one heartbeat interval relates to the interval immediately following it.

### Interpreting the diagonal

The diagonal line:

```text
x = y
```

represents consecutive intervals of equal length.

Points close to the diagonal correspond to relatively small beat-to-beat differences, while points farther from the diagonal represent larger successive differences.

Poincaré plots are useful because they allow the structure of beat-to-beat variability to be seen directly rather than represented only by a single numerical statistic.

---

## 7. The Fantasia Dataset

This project uses annotated ECG recordings associated with the Fantasia dataset.

The source material describes the dataset as containing healthy young and elderly participants who underwent approximately 120 minutes of continuous resting ECG recording. The groups include both men and women, and the ECG recordings were digitised at 250 Hz.

The heartbeat annotations were generated using an automated arrhythmia detection algorithm and subsequently verified by visual inspection.

The project uses the annotated heartbeat information rather than attempting to detect R-peaks directly from the raw ECG signal.

---

## 8. How This Connects to the Python Analysis

The project converts the conceptual HRV workflow into reusable Python functions:

```text
Annotated ECG files
        ↓
Read heartbeat annotations
        ↓
Select normal (N) beats
        ↓
Calculate NN intervals
        ↓
Calculate HRV metrics
        ↓
Create consolidated results
        ↓
Visualise HRV
        ↓
Compare younger and older groups
        ↓
Statistical analysis
```

The main implementation is contained in:

```text
hrv.py
```

The notebook:

```text
HRV_analysis.ipynb
```

then uses these functions for batch processing, visualisation and statistical analysis.

---

## 9. Why This Matters for the Project

The project is not simply calculating heart rate.

It investigates the **variation in the timing of heartbeats**.

Two people could have similar average heart rates while exhibiting substantially different patterns of beat-to-beat variability. HRV metrics and Poincaré plots provide different ways of quantifying and visualising these differences.

The analysis therefore combines:

- signal-derived timing information
- numerical HRV measures
- visual exploration
- statistical testing
- comparison between age groups

This provides the conceptual foundation for the technical analysis implemented in the project.

---

## Further Reading

The project background material refers to the Fantasia dataset hosted by PhysioNet:

https://physionet.org/content/fantasia/1.0.0/

The background material also uses ECG and HRV educational resources to explain ECG structure, beat annotations, interval variability and Poincaré plots.
