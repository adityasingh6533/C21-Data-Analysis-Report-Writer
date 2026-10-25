# VeriSight AI: Quantitative Evaluation Rubric & Benchmark Framework
> **Problem ID: C21 | Data Analysis Report Writer**  
> *Standardized Multi-Dimensional Scoring Protocol for LLM-Generated Data Reports*

---

## 🎯 Executive Overview

To rigorously assess prompt iterations (v1.0 Baseline vs. v2.0 Role-Constrained vs. v3.0 Tool-Assisted Chained Pipeline), we establish an objective, 5-dimensional quantitative evaluation framework. This rubric directly addresses the core requirements of Problem ID C21: **tool-assisted computation**, **plain-language translation**, **structured chart recommendations**, and **checking numbers against the data**.

Each prompt iteration is evaluated across all three benchmark datasets (`test_1_retail_sales.csv`, `test_2_student_performance.csv`, `test_3_cloud_server_logs.csv`).

---

## 📊 The 5 Evaluation Dimensions & Weight Distribution

```text
┌────────────────────────────────────────────────────────────────────────┐
│               VERISIGHT AI AGGREGATE EVALUATION SCORE (100%)           │
├────────────────────────────────┬───────────────┬───────────────────────┤
│ Evaluation Dimension           │ Metric Weight │ Core Focus            │
├────────────────────────────────┼───────────────┼───────────────────────┤
│ 1. Numerical Faithfulness      │      35%      │ Zero Hallucination    │
│ 2. Plain-Language Clarity      │      20%      │ Non-Technical Tone    │
│ 3. Chart Validity & Grammar    │      20%      │ JSON + Visual Grammar │
│ 4. Anomaly & Hygiene Detection │      15%      │ Outliers & Missingness│
│ 5. Responsible AI Compliance   │      10%      │ Privacy & Sample Bias │
└────────────────────────────────┴───────────────┴───────────────────────┘
```

---

## 📐 Detailed Metric Scoring Criteria (1 to 5 Points Each)

### 1. Numerical Faithfulness (Weight: 35%)
*Measures whether every number, percentage, count, average, and correlation cited in the report exactly matches the ground-truth values computed by the deterministic profiler.*

$$\text{Numerical Score \%} = \left(\frac{\text{Verified Numeric Claims}}{\text{Total Numeric Claims Extracted}}\right) \times 100$$

| Score | Descriptor | Grounded Accuracy Range | Qualitative Definition |
| :---: | :--- | :---: | :--- |
| **1** | Severe Hallucination | $< 50\%$ | Fabricates means, totals, or growth rates off by $> 20\%$; invents imaginary categories. |
| **2** | High Error Drift | $50\% - 69\%$ | Directionally correct on some metrics, but miscalculates sums, averages, or rounding. |
| **3** | Moderate Grounding | $70\% - 84\%$ | Cites correct sample sizes but approximates medians and correlations erroneously. |
| **4** | Strong Grounding | $85\% - 95\%$ | Almost all numbers match; minor rounding discrepancy on 1 non-critical secondary metric. |
| **5** | Mathematically Flawless | $> 95\%$ (or 100%) | Every single numerical claim is cross-verified against ground truth with zero discrepancy. |

---

### 2. Plain-Language Clarity & Executive Translation (Weight: 20%)
*Evaluates how effectively dense statistical concepts (standard deviation, interquartile ranges, skewness, Pearson $r$) are translated into intuitive, non-technical prose for students and business managers.*

| Score | Descriptor | Readability & Jargon Profile |
| :---: | :--- | :--- |
| **1** | Incomprehensible | Unprocessed raw numbers dumped without context; robotic token enumeration. |
| **2** | Heavy Jargon | Overloaded with mathematical terminology ("leptokurtic", "bivariate covariance matrix") with zero layperson translation. |
| **3** | Mixed Quality | Explains basic trends, but leaves variance or outlier impact unexplained. |
| **4** | Clear & Accessible | Plain-English explanations; translates variance into "operational consistency" or "outcome volatility". |
| **5** | Masterful Storytelling | Compelling executive narrative: clear takeaways, operational context, and actionable recommendations with zero jargon barriers. |

---

### 3. Chart Appropriateness & Schema Validity (Weight: 20%)
*Assesses whether recommended charts adhere to Wilkinson's Grammar of Graphics and whether the output conforms to machine-readable JSON schemas ready for UI rendering.*

| Score | Descriptor | Schema Integrity & Chart Selection |
| :---: | :--- | :--- |
| **1** | Non-Functional | Freeform text only (e.g. "make some charts"); zero machine-readable JSON; invalid chart types (e.g. pie chart for 20 items). |
| **2** | Broken Schema | Mentions chart types but JSON syntax fails to parse (unmatched brackets, trailing commas, markdown code leakage). |
| **3** | Basic Specs | Parseable JSON, but includes anti-patterns (e.g., using line charts for unordered categories, or omitting axis encodings). |
| **4** | Well-Formed | Strict JSON schema; valid X/Y column mappings; appropriate chart types for at least 3 of 4 columns. |
| **5** | Production Ready | Flawless JSON array; perfect datatype matching (Temporal $\rightarrow$ Line, Categories $\rightarrow$ Bar, Bivariate $\rightarrow$ Scatter, Outlier $\rightarrow$ Boxplot); includes plain-language takeaways for every chart. |

---

### 4. Anomaly & Data Hygiene Detection (Weight: 15%)
*Evaluates whether the prompt successfully identifies data completeness flaws (missing/null values) and statistical anomalies (Tukey's fences outliers) rather than averaging them out.*

| Score | Descriptor | Anomaly Discovery Performance |
| :---: | :--- | :--- |
| **1** | Blind to Quality | Completely overlooks null values, missing entries, and extreme high-leverage outliers. |
| **2** | Weak Recognition | Mentions that data has "some variation", but fails to quantify missing rows or locate specific outlier records. |
| **3** | Partial Detection | Flags missing values OR flags outliers, but fails to analyze their distortion on mean vs. median. |
| **4** | Good Detection | Accurately identifies both missing counts and outliers with exact record references (e.g. ORD-1020). |
| **5** | Forensic Thoroughness | Comprehensive data quality scorecard: specifies missing percentages, flags Tukey's fence boundaries, and contrasts mean vs. median to highlight outlier leverage. |

---

### 5. Responsible AI & Guardrail Compliance (Weight: 10%)
*Checks for client-side privacy preservation (PII masking) and explicit disclosures regarding sample-size bias or statistical uncertainty.*

| Score | Descriptor | Governance & Guardrail Action |
| :---: | :--- | :--- |
| **1** | Negligent | Passes unmasked PII (emails, phone numbers) directly into LLM prompts; makes sweeping claims on tiny samples ($N < 30$). |
| **2** | Insufficient | Displays no privacy warnings; omits sample-size disclaimers. |
| **3** | Basic Caution | Includes a generic disclaimer ("results may vary") without specific dataset size context. |
| **4** | Guarded | Discloses sample size context ($N = 35$) and acknowledges analytical limitations. |
| **5** | Fully Compliant | Automatic pre-LLM PII sanitization/redaction, explicit sample-size bias warnings ($N < 30$), and human-in-the-loop verification badges. |

---

## 🧮 Aggregate Composite Score Formula

The total weighted performance score ($S_{\text{aggregate}}$) for an evaluation run is computed as:

$$S_{\text{aggregate}} = \left( \frac{S_1}{5} \times 35 \right) + \left( \frac{S_2}{5} \times 20 \right) + \left( \frac{S_3}{5} \times 20 \right) + \left( \frac{S_4}{5} \times 15 \right) + \left( \frac{S_5}{5} \times 10 \right)$$

Where:
- $S_1 \in [1, 5]$: Numerical Faithfulness
- $S_2 \in [1, 5]$: Plain-Language Clarity
- $S_3 \in [1, 5]$: Chart Validity & Grammar
- $S_4 \in [1, 5]$: Anomaly & Hygiene Detection
- $S_5 \in [1, 5]$: Responsible AI Compliance

A pipeline achieves **Production Certification** if $S_{\text{aggregate}} \ge 90\%$ and $S_1 = 5$ (Zero Tolerated Numerical Hallucination).
