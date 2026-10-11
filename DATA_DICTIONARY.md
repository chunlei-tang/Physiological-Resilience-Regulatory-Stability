# Data Dictionary

## Physiological Resilience as System-Level Regulatory Stability

**Associated manuscript:**  
*Quantifying Physiological Resilience as System-Level Regulatory Stability in Longitudinal Multi-System Dynamics*

## 1. Overview

This document describes selected variables and data structures relevant to the study of physiological resilience and longitudinal multi-system regulatory stability.

The original study drew on community health assessments conducted in Pengpu Town, Shanghai, China, during 2013–2023.

The original reported analytic cohort comprised:

- **6,671 adults**
- **10,141 longitudinal assessment records**
- **Nine predefined regulatory patterns**
- **29 selected clinical and physiological features** used in exploratory predictive modeling
- **430 participants** in a historical movement-exposure subgroup

These sample sizes are drawn from the original study documentation. The complete cohort selection and feature-extraction procedures have not been independently reconstructed from the currently available data export.

This dictionary is descriptive documentation, not a downloadable dataset or a complete machine-readable schema.

## 2. Source Data Structure

The available source-data export is an Excel workbook containing 141 columns and 20,282 data rows in its primary worksheet.

The export contains demographic information, health examination measurements, laboratory results, lifestyle information, and recorded health assessment categories.

Some columns contain composite text fields, repeated examination identifiers, or incomplete information. The source export should not be treated as equivalent to the final analytic cohort without further validation.

No individual-level data are included in this repository.

## 3. Selected Variables

The following table provides a descriptive mapping of selected source variables and analytical concepts. Standardized names are proposed for documentation purposes and do not necessarily correspond to columns in a released analysis dataset.

| Standardized name | Source variable or concept | Data type | Physiological domain | Interpretation and limitations |
|---|---|---|---|---|
| `exam_date` | Examination date (体检日期) | Date | Longitudinal timing | Records the examination date where available |
| `age` | Age or age derived from demographic information | Numeric | Demographic | Requires consistent definition at examination |
| `sex` | Recorded sex | Categorical | Demographic | Coding requires verification |
| `bmi` | Body mass index (体质指数) | Numeric | Metabolic | Candidate anthropometric feature |
| `tbil` | Total bilirubin (总胆红素) | Numeric | Hepatic / metabolic | Candidate biochemical feature |
| `hct` | Hematocrit (红细胞压积) | Numeric or extracted value | Hematologic / circulatory | May require extraction from composite laboratory text |
| `pulse_rate` | Pulse rate | Numeric, if available | Circulatory / autonomic | Reported historical model feature; a corresponding independent numeric source field has not been confirmed |
| `lymphocyte_count` | Lymphocyte count | Numeric or extracted value | Immune | May require extraction from composite laboratory text |
| `death_status` | Recorded death indicator (死亡) | Categorical | Outcome status | Static status field; not a verified time-to-event outcome |
| `regulatory_pattern` | Structured constitution assessment category | Categorical, 1–9 | Multidimensional assessment | Assigned using predefined assessment criteria, not unsupervised clustering |
| `exercise_frequency` | Exercise frequency (锻炼频率名称) | Categorical | Lifestyle / behavior | Does not independently establish participation in the structured movement program |
| `movement_exposure` | Historical structured movement-exposure classification | Binary | Behavioral exposure | Subgroup-specific analytical classification; not independently reconstructable from the available source export |

## 4. Regulatory Pattern Categories

The nine regulatory patterns correspond to predefined constitution categories from the original structured multidimensional assessment.

| Pattern | Original category | English designation |
|---|---|---|
| 1 | 平和质 | Balanced Constitution |
| 2 | 气虚质 | Qi-Deficiency |
| 3 | 阳虚质 | Yang-Deficiency |
| 4 | 阴虚质 | Yin-Deficiency |
| 5 | 痰湿质 | Phlegm-Dampness |
| 6 | 湿热质 | Damp-Heat |
| 7 | 血瘀质 | Blood-Stasis |
| 8 | 气郁质 | Qi-Stagnation |
| 9 | 特禀质 | Inherited Constitution |

Pattern 1 was designated as the reference category for longitudinal analyses.

Attainment of Pattern 1 at follow-up includes both maintenance of Pattern 1 and transitions from other patterns. It is used as an operational indicator of regulatory stability, not as an independently validated measure of physiological resilience.

The 29 clinical and physiological features used for exploratory predictive modeling were analytically distinct from the predefined criteria used to assign these categories.

## 5. Clinical Feature Selection

The original study documentation describes a reduction from a broader candidate feature set to 29 selected clinical and physiological features.

The original feature-importance analysis reported the following among its leading candidate contributors:

- Body mass index
- Total bilirubin
- Hematocrit
- Pulse rate
- Lymphocyte count

The complete feature-selection pipeline and extraction rules have not yet been independently reproduced.

The variables listed above should not be interpreted as validated diagnostic criteria for any individual regulatory pattern.

## 6. Longitudinal Data Considerations

Multiple examination records may be associated with the same individual.

The available source export does not provide a confirmed, consistent pseudonymized participant identifier sufficient to reconstruct the original longitudinal analytic cohort without additional validation.

Record linkage based solely on names is not considered a reliable or privacy-preserving solution.

The available export also contains incomplete records and possible duplicate entries. Exact exclusion and deduplication rules must be established before any new analysis is represented as a reproduction of the original study.

## 7. Mortality Outcome Limitations

The source export includes a recorded death-status field but does not provide verified death dates, event ascertainment times, or censoring dates.

Consequently, the available export alone does not support a validated time-to-event analysis or independent verification of mortality-discrimination performance.

Historical regulatory-pattern classification results should not be interpreted as mortality-prediction results.

## 8. Movement-Exposure Subgroup

The original study documentation reports a subgroup of 430 participants:

- 303 with structured movement exposure
- 127 without structured movement exposure

Follow-up Pattern 1 attainment was reported for 247 participants (57.4%).

The available source export does not contain a verified participant-level program-enrollment and adherence dataset sufficient to independently reconstruct this subgroup.

General exercise-frequency variables should not be used as substitutes for verified program exposure.

## 9. Privacy and Data Access

The underlying health examination records contain sensitive personal and medical information.

Names, examination identifiers, individual-level clinical measurements, and other potentially identifying information are not distributed through this public repository.

Access to source records is subject to institutional authorization, applicable ethical requirements, and data-governance restrictions.

## 10. Reproducibility Status

This dictionary documents the current understanding of the available source-data structure and the original study's reported analytical variables.

It does not establish that the original analytic cohort, all 29 model features, regulatory-pattern assignment procedures, or predictive analyses have been independently reproduced.

Any future public analysis scripts will be documented separately, with their inputs, outputs, assumptions, and verification status clearly identified.
