# Physiological Resilience as System-Level Regulatory Stability

## About this study

This repository accompanies the manuscript:

**Quantifying Physiological Resilience as System-Level Regulatory Stability in Longitudinal Multi-System Dynamics**

*Manuscript submitted to Discover Aging.*

The study investigates physiological resilience as system-level regulatory stability within longitudinal multi-system health assessments, with a focus on regulatory organization across metabolic, immune, circulatory, and other physiological domains during aging.

## Study population

The original analytic cohort comprised:

- **6,671** community-dwelling adults
- **10,141** longitudinal health assessment records
- **Study period:** 2013–2023
- **Study location:** Pengpu Town, Shanghai, China

These figures describe the original analytic cohort and have not been independently reconstructed from the currently available source-data export.

## Regulatory pattern framework

The study uses nine predefined regulatory patterns (Patterns 1–9), corresponding to categories established through a structured 33-item multidimensional health assessment.

The patterns were **not discovered through unsupervised machine learning**.

**Pattern 1 (Balanced Constitution)** serves as the reference category for longitudinal analyses. Follow-up attainment of Pattern 1 is used as an operational indicator of regulatory stability, rather than an independently validated measure of physiological resilience.

## Clinical and physiological features

The original analysis selected 29 clinical and physiological features from a broader set of candidate variables for exploratory predictive modeling.

These features are analytically distinct from the structured assessment criteria used to assign the nine regulatory patterns.

The original feature-importance analysis identified body mass index, total bilirubin, hematocrit, pulse rate, and lymphocyte count among the leading candidate contributors.

Potential relationships between individual regulatory patterns and clinical biomarkers remain exploratory and should not be interpreted as validated pattern-specific biological associations.

## Movement-exposure analysis

A historical subgroup analysis included 430 participants, comprising 303 individuals with structured movement exposure and 127 without such exposure.

Follow-up Pattern 1 attainment was observed in 247 participants (57.4%). No statistically significant association between movement exposure and follow-up Pattern 1 attainment was identified in the reported adjusted analysis.

These findings do not establish equivalence between exposure groups or rule out potential intervention effects.

## Predictive modeling

Exploratory machine-learning analyses evaluated regulatory-pattern classification using models including XGBoost, LightGBM, random forest, logistic regression, and k-nearest neighbors.

The reported XGBoost AUC was 0.7245 for regulatory-pattern classification.

This result
