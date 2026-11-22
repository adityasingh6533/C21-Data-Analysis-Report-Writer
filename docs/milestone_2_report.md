# VeriSight AI — Milestone 2 Report
## Tool-Assisted & Self-Verifying Data Analysis Report Writer
**Problem ID: C21 | Course: SCSE4041 — Prompt Engineering Mini-Project**

---

# Section 1: Cover Page

| Field | Details |
|-------|---------|
| **Team ID** | _[Enter your Milestone 1 Team ID]_ |
| **Team Name** | _[Enter your team name exactly as in Milestone 1]_ |
| **Project Title** | VeriSight AI — Tool-Assisted & Self-Verifying Data Analysis Report Writer |
| **Batch** | _[Enter your batch, e.g., B13-24]_ |
| **Faculty Name** | _[Enter faculty name]_ |

**Team Members:**

| # | Name | Enrollment Number |
|---|------|-------------------|
| 1 | _[Team Leader Name]_ | _S24CSEU_____ |
| 2 | _[Member 2 Name]_ | _S24CSEU_____ |
| 3 | _[Member 3 Name]_ | _S24CSEU_____ |

**Submission Links:**
1. **Prototype Link**: [https://adityasingh6533-c21-data-analysis-report-writer-app-bxvkvg.streamlit.app/](https://adityasingh6533-c21-data-analysis-report-writer-app-bxvkvg.streamlit.app/)
2. **GitHub Repository**: [https://github.com/adityasingh6533/C21-Data-Analysis-Report-Writer](https://github.com/adityasingh6533/C21-Data-Analysis-Report-Writer)
3. **Video Reel**: _[Google Drive / YouTube Unlisted URL]_ | Duration: _[___]_ seconds

---

# Section 2: Prompt and Solution Design

## 2(a): Problem, Approach & Design Rationale

**What problem does VeriSight AI solve?**
Modern data workflows are bottlenecked by the gap between raw quantitative CSV data and executive comprehension. When users paste raw CSV files directly into Large Language Models, the LLM hallucinates arithmetic — fabricating means, inventing correlations, and suggesting unrenderable chart concepts. VeriSight AI eliminates these failures by decoupling computation from narration.

**For whom?**
Students analyzing coursework datasets, junior business analysts writing weekly executive summaries, and non-technical department managers interpreting tabular reports.

**Input and Output:**
- **Input**: Any raw CSV file (tabular data with numeric, categorical, and temporal columns)
- **Output**: A verified executive narrative report with exact statistics, interactive chart specifications (JSON), and an auditable verification ledger confirming zero hallucinations

**How many prompts/steps and why?**
4 distinct LLM prompts arranged in a sequential chained pipeline, plus 1 deterministic code profiler tool (Phase 0). Task decomposition was chosen because:
1. A single monolithic prompt suffers from cognitive overload — juggling prose, JSON, and math simultaneously causes format bleed and schema corruption
2. Separating computation from narration guarantees zero arithmetic hallucination
3. An isolated verification stage (Stage 4) catches any remaining drift before final presentation

**Which tool/model and why?**
- **Model**: Gemini 2.5 Flash via Google Gemini API — chosen for structured JSON output support, low-latency instruction following, and large context window
- **Tool**: Python deterministic profiler (pandas/numpy) — computes exact means, medians, IQR outlier bounds, and Pearson correlations
- **Framework**: Streamlit for the interactive dashboard with Plotly for chart rendering

**What changed since Milestone 1?**
- Built complete working Streamlit prototype with 4 interactive tabs
- Implemented all 4 prompt stages with full prompt templates
- Created deterministic profiler tool with PII redaction guardrails
- Completed v1→v2→v3 prompt iteration with quantitative evaluation (41.5% → 75.5% → 98.9%)
- Built automated 5-metric evaluation harness with 9 benchmark experiments
- Added offline Demo Mode for evaluator-friendly demonstrations

## 2(b): Diagrams

### Diagram 1: Prompt Workflow (4-Stage Chained Pipeline)

```
┌──────────────┐    ┌────────────────────────┐    ┌─────────────────────┐
│   Raw CSV    │───►│  Phase 0: Deterministic │───►│  Exact Stats JSON   │
│   File       │    │  Profiler Tool          │    │  (Ground Truth)     │
└──────────────┘    │  (tool_csv_profiler.py) │    └─────────┬───────────┘
                    └────────────────────────┘              │
                                                            ▼
                    ┌────────────────────────────────────────────────────────┐
                    │          STAGE 1: Schema & Anomaly Explorer            │
                    │  Persona: Principal Data Scientist | Temp: 0.1         │
                    │  Input: Stats JSON | Output: Forensic JSON             │
                    └───────────────────────┬────────────────────────────────┘
                                            ▼
                    ┌────────────────────────────────────────────────────────┐
                    │          STAGE 2: Plain-Language Narrator               │
                    │  Persona: Executive Data Journalist | Temp: 0.3         │
                    │  Input: Stats + Stage 1 | Output: Executive Markdown    │
                    └───────────────────────┬────────────────────────────────┘
                                            ▼
                    ┌────────────────────────────────────────────────────────┐
                    │          STAGE 3: Chart Recommender                     │
                    │  Persona: Visualization Architect | Temp: 0.1           │
                    │  Input: Stats + Stage 2 | Output: JSON Chart Specs      │
                    └───────────────────────┬────────────────────────────────┘
                                            ▼
                    ┌────────────────────────────────────────────────────────┐
                    │          STAGE 4: Number Verifier & Auditor             │
                    │  Persona: Adversarial Fact-Checker | Temp: 0.0          │
                    │  Input: Ground Truth + Stage 2 + Stage 3                │
                    │  Output: Verification Ledger + Auto-Corrected Report    │
                    └───────────────────────┬────────────────────────────────┘
                                            ▼
                    ┌────────────────────────────────────────────────────────┐
                    │          FINAL OUTPUT: Verified Report + Charts          │
                    └────────────────────────────────────────────────────────┘
```

### Diagram 2: System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                      STREAMLIT WEB DASHBOARD                         │
│  ┌──────────────┐ ┌──────────────┐ ┌───────────┐ ┌───────────────┐  │
│  │ Tab 1:       │ │ Tab 2:       │ │ Tab 3:    │ │ Tab 4:        │  │
│  │ Executive    │ │ Chain        │ │ Prompt    │ │ Evaluation    │  │
│  │ Report +     │ │ Inspector    │ │ Iteration │ │ & Error       │  │
│  │ Plotly Charts│ │ (Live Trace) │ │ Lab       │ │ Analysis      │  │
│  └──────┬───────┘ └──────┬───────┘ └─────┬─────┘ └───────┬───────┘  │
│         └────────────────┴───────────────┴───────────────┘           │
│                              │                                       │
│                     ┌────────▼────────┐                              │
│                     │ VeriSightPipeline│                              │
│                     │  (prompt_chain_  │                              │
│                     │   runner.py)     │                              │
│                     └───┬─────────┬───┘                              │
│                         │         │                                   │
│              ┌──────────▼──┐  ┌───▼──────────────┐                   │
│              │Deterministic│  │ Gemini 2.5 Flash  │                   │
│              │CSV Profiler │  │ API (google-genai) │                  │
│              │(pandas/     │  │ OR Demo Mode       │                  │
│              │ numpy)      │  │ (Offline Mock)     │                  │
│              └─────────────┘  └────────────────────┘                 │
└─────────────────────────────────────────────────────────────────────┘
```

### Diagram 3: Input–Output Flow

```
INPUT:                    TOOL:                      LLM STAGES:                    OUTPUT:
┌─────────┐    ┌─────────────────────┐    ┌────────────────────┐    ┌─────────────────────┐
│Raw CSV  │───►│tool_csv_profiler.py │───►│ Stage 1 (JSON)     │───►│ Verified Executive  │
│(any     │    │  - Exact stats      │    │ Stage 2 (Markdown) │    │ Narrative Report    │
│tabular  │    │  - IQR outliers     │    │ Stage 3 (JSON)     │    │ + Interactive       │
│dataset) │    │  - Correlations     │    │ Stage 4 (Verify)   │    │ Plotly Charts       │
│         │    │  - PII redaction    │    │                    │    │ + Audit Ledger      │
└─────────┘    └─────────────────────┘    └────────────────────┘    └─────────────────────┘
```

## 2(c): Prompt Sheets (4 Final Prompts)

---

### Prompt Sheet 1

| Field | Details |
|-------|---------|
| **Prompt ID and Name** | P1 — Schema & Anomaly Explorer |
| **Step in Workflow** | Stage 1 of 4 |
| **Purpose** | Evaluate deterministic statistical profile to flag data quality issues and detect anomalies |
| **Tool and Model** | Gemini 2.5 Flash via Google Gemini API |
| **Settings** | Temperature: 0.1, Top_P: 0.8, Max Output Tokens: 2048 |
| **Number of Examples** | 0 (zero-shot with strict schema enforcement) |
| **Output Format** | Raw JSON Object (no markdown wrappers) |

**Full System Prompt:**
```
You are a Principal Data Scientist and Lead Quantitative Forensic Auditor.
Your core expertise lies in inspecting computed dataset profiles, diagnosing data hygiene issues, interpreting dispersion metrics (IQR, standard deviation, skewness), and detecting multi-collinear relationships.

You DO NOT receive raw, uncomputed CSV rows. Instead, you receive an exact, mathematically computed statistical profile produced by a deterministic profiling tool.
Your job is purely analytical reasoning:
1. Review the data quality metrics: Identify missing/null values, cardinally degenerate columns, and Tukey's fences outliers.
2. Evaluate distributional skew and variance: Distinguish between symmetric normal distributions and heavy-tailed or multi-modal regimes.
3. Isolate key bivariate correlations: Spot strong positive or negative relationships (|r| >= 0.5) and assess their domain implications.
4. Output your analysis strictly as a validated JSON object conforming to the defined schema.
```

**Full User Prompt Template:**
```
### INPUT: COMPUTED DATASET PROFILE (GROUND TRUTH)
The following statistical summary has been deterministically calculated by our data profiling engine:

{DETERMINISTIC_STATS_JSON}

### USER ANALYTICAL INTENT / GOAL:
{USER_GOAL}

### INSTRUCTIONS & TASK DECOMPOSITION:
Analyze the JSON summary above and generate a forensic data health and hypothesis report.

1. DATA QUALITY ALERTS:
   - Identify any column with missing/null values. Calculate the missing percentage and assign a severity level ("LOW", "MEDIUM", "CRITICAL").
   - Flag any extreme outliers detected via Tukey's fences (Q1 - 1.5*IQR, Q3 + 1.5*IQR).
   - Flag any skewness or data hygiene anomalies.

2. KEY STATISTICAL HYPOTHESES & PATTERNS:
   - Identify the top 3 most significant numerical or categorical patterns.
   - For continuous columns, highlight meaningful correlations (|r| >= 0.5).
   - Highlight group differences across categorical features.

3. PRIORITY METRICS FOR EXECUTIVE REPORTING:
   - Select 3 to 5 core metrics for the executive narrative.
   - For each metric, record its exact mean, median, min, max.

### MANDATORY OUTPUT FORMAT:
Respond with ONLY a valid, parseable JSON object matching this schema:
{
  "dataset_overview": { "total_rows": <int>, "total_columns": <int>, "primary_domain": "<string>", "data_health_score_pct": <number> },
  "data_quality_alerts": [ { "column_name": "<string>", "alert_type": "MISSING_VALUES" | "EXTREME_OUTLIER" | "HIGH_SKEW" | "ZERO_VARIANCE", "severity": "LOW" | "MEDIUM" | "CRITICAL", "metric_observed": "<string>", "investigation_note": "<string>" } ],
  "key_hypotheses": [ { "hypothesis_id": "HYP-1", "pattern_type": "CORRELATION" | "OUTLIER_IMPACT" | "GROUP_DISPARITY" | "TEMPORAL_TREND", "variables_involved": ["<col1>", "<col2>"], "statistical_evidence": "<exact numbers>", "domain_interpretation": "<plain language>" } ],
  "priority_metrics": [ { "column_name": "<string>", "exact_mean": <number>, "exact_median": <number>, "exact_min": <number>, "exact_max": <number>, "recommended_focus": "<string>" } ]
}
DO NOT wrap your output in markdown code blocks. Output raw JSON only.
```

**Variables:**
- `{DETERMINISTIC_STATS_JSON}` — JSON output from tool_csv_profiler.py containing exact statistics
- `{USER_GOAL}` — User's analytical focus or question

**Sample Run:**
- **Input**: `test_1_retail_sales.csv` profiler JSON (35 rows, 9 columns, $18,750 outlier)
- **Output** (excerpt): `{"dataset_overview": {"total_rows": 35, "total_columns": 9, "primary_domain": "Commercial Retail Sales", "data_health_score_pct": 91.4}, "data_quality_alerts": [{"column_name": "revenue", "alert_type": "EXTREME_OUTLIER", "severity": "CRITICAL", "metric_observed": "Single transaction ORD-1020 recorded $18,750.00 revenue against median $360.00"}], ...}`

---

### Prompt Sheet 2

| Field | Details |
|-------|---------|
| **Prompt ID and Name** | P2 — Plain-Language Narrative Synthesizer |
| **Step in Workflow** | Stage 2 of 4 |
| **Purpose** | Translate forensic findings into clear, executive-level narrative prose with zero jargon |
| **Tool and Model** | Gemini 2.5 Flash via Google Gemini API |
| **Settings** | Temperature: 0.3, Top_P: 0.9, Max Output Tokens: 3072 |
| **Number of Examples** | 2 few-shot examples (translating variance and correlation into plain English) |
| **Output Format** | Structured GitHub Flavored Markdown |

**Full System Prompt:**
```
You are an elite Executive Data Journalist who writes for C-suite leaders, academic department deans, and senior policymakers.
Your superpower is taking dense, intimidating statistical measurements and translating them into crystal-clear, compelling, and actionable plain English.

You operate under two non-negotiable principles:
1. JARGON-FREE SIMPLICITY: You never say "standard deviation of 14.2" without explaining it as "a high degree of variance where individual outcomes fluctuate widely." You never say "positive Pearson correlation r=0.88" without translating it to "students who spend more hours studying consistently achieve higher grade points."
2. ABSOLUTE NUMERICAL FIDELITY: You MUST NOT invent, calculate, or round numbers unpredictably. Every single number, percentage, count, currency, or metric cited in your narrative MUST be copied directly and faithfully from the provided DETERMINISTIC_STATS_JSON or STAGE_1_EXPLORER_JSON. If a number is not in the ground-truth profile, DO NOT GUESS IT.
```

**Full User Prompt Template:**
```
### CONTEXT & INPUTS:
1. GROUND-TRUTH DETERMINISTIC STATISTICAL PROFILE:
{DETERMINISTIC_STATS_JSON}

2. STAGE 1 FORENSIC EXPLORATION & ANOMALY FINDINGS:
{STAGE_1_EXPLORER_JSON}

3. AUDIENCE & USER GOAL:
Target Audience: Non-technical executives, students, and departmental leaders.
User Goal: {USER_GOAL}

### FEW-SHOT EXAMPLES: TRANSLATING DENSE STATS INTO EXECUTIVE PROSE

[Example 1: Translating Variance & Standard Deviation]
- Technical Input: Column weekly_sales_usd, Mean = $4,200, StdDev = $2,850, Min = $450, Max = $14,100.
- ❌ Bad: "The weekly sales mean was $4,200 with standard deviation of $2,850."
- ✅ Good: "While the typical store averaged $4,200 in weekly sales, performance was highly erratic across locations. Weekly revenue swung dramatically from a low of $450 up to a peak of $14,100."

[Example 2: Translating Correlation & Outlier Impact]
- Technical Input: Correlation between attendance_pct and final_cgpa is r = 0.84.
- ❌ Bad: "A Pearson coefficient of r=0.84 was detected between attendance and CGPA."
- ✅ Good: "Classroom attendance proved to be the single strongest predictor of academic success."

### REQUIRED REPORT STRUCTURE:
# Executive Data Insights Report: [Insert Descriptive Title]

### 1. Executive Summary (At a Glance) — 2–3 short paragraphs
### 2. Key Findings & Strategic Discoveries — 3–4 findings with bold subheadings
### 3. Data Hygiene, Outliers & Risk Advisory — Missing values, outliers, sample size context
### 4. Actionable Next Steps & Recommendations — 3 clear, concrete recommendations

### STRICT CONSTRAINTS:
- EVERY number mentioned MUST exist verbatim in the ground-truth inputs.
- Do NOT include code snippets or JSON blocks. Output pure, polished Markdown only.
```

**Variables:**
- `{DETERMINISTIC_STATS_JSON}` — Ground-truth profile from profiler
- `{STAGE_1_EXPLORER_JSON}` — Stage 1 anomaly explorer output
- `{USER_GOAL}` — User's analytical goal

**Sample Run:**
- **Input**: Retail sales profiler JSON + Stage 1 anomaly findings
- **Output** (excerpt): "Across the 35 recorded transactions, commercial sales centered around a verified median of **$360.00**. Top-line revenue was substantially distorted by a single massive wholesale transaction of **$18,750.00**, which pulled the arithmetic average revenue up to **$920.18**."

---

### Prompt Sheet 3

| Field | Details |
|-------|---------|
| **Prompt ID and Name** | P3 — Structured Chart Recommender |
| **Step in Workflow** | Stage 3 of 4 |
| **Purpose** | Select optimal chart types following Grammar of Graphics and output machine-readable JSON specs |
| **Tool and Model** | Gemini 2.5 Flash via Google Gemini API |
| **Settings** | Temperature: 0.1, Top_P: 0.8, Max Output Tokens: 2048 |
| **Number of Examples** | 0 (strict schema enforcement via detailed type-matching rules) |
| **Output Format** | Raw JSON Array |

**Full System Prompt:**
```
You are a World-Class Data Visualization Architect and Information Designer.
Your role is to map narrative business findings to strict, mathematically sound graphical representations following the Grammar of Graphics (Wilkinson, 1999).

You adhere to strict cognitive and visual encoding rules:
1. TYPE MATCHING:
   - Temporal / Date / Time Series -> Line Chart (never unordered categories on a line).
   - Discrete Categories (<= 6 distinct values) -> Bar Chart.
   - Continuous vs. Continuous Bivariate Relationships -> Scatter Plot.
   - Distribution, Skewness, or Outlier Spreads -> Box Plot or Histogram.
   - Never recommend a pie chart.
2. NARRATIVE ALIGNMENT: Each recommended chart MUST visually substantiate at least one major finding in the Stage 2 report.
3. RIGID SCHEMA COMPLIANCE: Every output object must specify exact column names that exist in the dataset schema.
```

**Full User Prompt Template:**
```
### INPUT 1: DETERMINISTIC DATASET PROFILE & COLUMN SCHEMA:
{DETERMINISTIC_STATS_JSON}

### INPUT 2: STAGE 2 EXECUTIVE NARRATIVE REPORT:
{STAGE_2_NARRATIVE_MD}

### INSTRUCTIONS:
Recommend 3 to 4 distinct charts. For each chart:
1. Select chart type based on data type rules (line/bar/scatter/boxplot).
2. Specify exact column names matching the profile (case-sensitive).
3. Specify aggregation method: "NONE", "SUM", "MEAN", or "COUNT".
4. Provide a plain_language_takeaway.
5. Provide a why_this_chart_fits rationale.

### MANDATORY OUTPUT JSON SCHEMA:
[
  {
    "chart_id": "chart_1",
    "chart_type": "bar" | "line" | "scatter" | "boxplot" | "histogram",
    "title": "<Concise Title>",
    "x_axis_column": "<exact_column_name>",
    "y_axis_column": "<exact_column_name>",
    "aggregation_method": "NONE" | "SUM" | "MEAN" | "COUNT",
    "plain_language_takeaway": "<One clear sentence>",
    "why_this_chart_fits": "<Explanation>"
  }
]
DO NOT wrap output in markdown code blocks. Output raw JSON array only.
```

**Variables:**
- `{DETERMINISTIC_STATS_JSON}` — Column schema and types from profiler
- `{STAGE_2_NARRATIVE_MD}` — Stage 2 executive narrative text

**Sample Run:**
- **Input**: Retail sales profile + narrative
- **Output**: `[{"chart_id": "chart_1", "chart_type": "bar", "title": "Total Transaction Volume by Product Category", "x_axis_column": "category", "y_axis_column": "units_sold", "aggregation_method": "SUM", "plain_language_takeaway": "Electronics dominates overall units sold.", "why_this_chart_fits": "Bar charts compare discrete, low-cardinality categories (4 categories)."}]`

---

### Prompt Sheet 4

| Field | Details |
|-------|---------|
| **Prompt ID and Name** | P4 — Deterministic Number Verifier & Self-Correction Auditor |
| **Step in Workflow** | Stage 4 of 4 (Closed-Loop Fact-Checking) |
| **Purpose** | Audit every numerical claim in the narrative against ground truth; auto-correct any hallucinations |
| **Tool and Model** | Gemini 2.5 Flash via Google Gemini API |
| **Settings** | Temperature: 0.0, Top_P: 0.5, Max Output Tokens: 4096 |
| **Number of Examples** | 0 (adversarial zero-tolerance verification) |
| **Output Format** | Raw JSON Object |

**Full System Prompt:**
```
You are an uncompromising Forensic Fact-Checker and Mathematical Auditor.
Your singular objective is to eliminate numerical hallucinations, false statistics, and misattributed metrics from AI-generated data reports.

You operate with adversarial skepticism:
1. You do not trust the narrative generated in Stage 2.
2. You treat the DETERMINISTIC_STATS_JSON as the sole, immutable source of truth.
3. You extract EVERY numerical claim stated in the narrative and chart specs.
4. For every claim:
   - If it matches ground truth within +/- 0.05% rounding tolerance → VERIFIED.
   - If it has no basis or contradicts computed numbers → HALLUCINATION.
5. If any hallucination is detected, you MUST generate an auto-corrected version of the narrative.
```

**Full User Prompt Template:**
```
### 1. AUTHORITATIVE GROUND-TRUTH PROFILE (COMPUTED BY TOOL):
{DETERMINISTIC_STATS_JSON}

### 2. DRAFT EXECUTIVE NARRATIVE REPORT TO AUDIT:
{STAGE_2_NARRATIVE_MD}

### 3. PROPOSED CHART SPECIFICATIONS:
{STAGE_3_CHARTS_JSON}

### INSTRUCTIONS:
1. CLAIM EXTRACTION & PROOF MATCHING: Scan every paragraph. Identify every stated statistic. Find the exact match in ground truth. Calculate accuracy_score_pct.
2. HALLUCINATION DETECTION: If a number was invented, miscalculated, or misattributed, record it.
3. AUTONOMOUS SELF-CORRECTION: If accuracy < 100%, provide corrected_narrative_markdown.

### MANDATORY OUTPUT JSON SCHEMA:
{
  "verification_passed": true | false,
  "accuracy_score_pct": <number>,
  "total_claims_audited": <integer>,
  "verified_claims": [ { "claim_text": "<excerpt>", "metric_name": "<column>", "narrative_value": "<value>", "ground_truth_value": "<value>", "status": "EXACT_MATCH" } ],
  "hallucinations_caught": [ { "claim_text": "<excerpt>", "error_type": "INVENTED_STATISTIC" | "CALCULATION_DRIFT" | "WRONG_COLUMN_ATTRIBUTION", "narrative_value": "<value>", "ground_truth_value": "<value>", "discrepancy_explanation": "<why>" } ],
  "corrected_narrative_markdown": "<Full corrected Markdown>"
}
DO NOT wrap output in markdown code blocks. Output raw JSON object only.
```

**Variables:**
- `{DETERMINISTIC_STATS_JSON}` — Authoritative ground truth from profiler
- `{STAGE_2_NARRATIVE_MD}` — Draft narrative text from Stage 2
- `{STAGE_3_CHARTS_JSON}` — Chart specifications from Stage 3

**Sample Run:**
- **Input**: Ground truth + retail sales narrative + chart specs
- **Output**: `{"verification_passed": true, "accuracy_score_pct": 100.0, "total_claims_audited": 7, "verified_claims": [{"claim_text": "median of $360.00", "status": "EXACT_MATCH"}, ...], "hallucinations_caught": [], "corrected_narrative_markdown": null}`

---

# Section 3: Implementation

## What Is Built

VeriSight AI is a fully functional, tool-assisted data analysis report writer consisting of:
- A **deterministic CSV profiler** (Python/pandas/numpy) that computes exact statistics and redacts PII
- A **4-stage chained prompt pipeline** orchestrated by `prompt_chain_runner.py`
- An **interactive Streamlit dashboard** with 4 tabs for demonstration and inspection
- An **automated evaluation harness** benchmarking v1→v2→v3 across 3 datasets

## Module Status Table

| Module | What It Does | Status | Notes |
|--------|-------------|--------|-------|
| Deterministic CSV Profiler (`tool_csv_profiler.py`) | Computes exact stats, IQR outliers, Pearson correlations, PII scan/redaction | Working | 281 lines, pandas/numpy |
| Stage 1: Anomaly Explorer (P1) | Interprets profile JSON, flags data quality issues, outputs forensic JSON | Working | Temp 0.1, strict JSON |
| Stage 2: Narrative Synthesizer (P2) | Translates findings into 4-part executive prose with 2 few-shot examples | Working | Temp 0.3, Markdown output |
| Stage 3: Chart Recommender (P3) | Generates Grammar of Graphics JSON chart specifications | Working | Temp 0.1, JSON array |
| Stage 4: Number Verifier (P4) | Cross-checks every number against ground truth, auto-corrects drift | Working | Temp 0.0, adversarial |
| Prompt Chain Runner (`prompt_chain_runner.py`) | Orchestrates v1/v2/v3 pipelines, Gemini API + offline mock mode | Working | 896 lines, google-genai SDK |
| Streamlit Dashboard (`app.py`) | 4-tab interactive UI: Report, Chain Inspector, Iteration Lab, Evaluation | Working | Plotly charts, custom CSS |
| Evaluation Harness (`run_evaluation.py`) | 5-metric weighted rubric scoring across 3 benchmark datasets | Working | 9 experiments logged |

## Prompt Iteration Log

| Version | What Changed | Why It Was Changed | Result After Change |
|---------|-------------|-------------------|-------------------|
| v1.0 Baseline | Single-shot naive prompt: "You are a data analyst. Here is a raw CSV. Calculate averages, trends, suggest charts." Temperature 0.7, raw CSV pasted directly into context. | Starting point — establish baseline failure modes | **41.5% aggregate score.** Hallucinated mean revenue as $340.50 (true: $920.18, 63% error). Missed $18,750 outlier entirely. Suggested pie chart for 15 categories. Zero verification trail. 6 critical hallucinations across 3 datasets. |
| v2.0 Structured | Added "Senior Data Journalist" persona. Added 6 negative constraints (no pie >4 categories, no guessing). Added 1-shot demonstration. Dual output: Markdown narrative + JSON chart block. Temperature lowered to 0.3. | v1 had wild hallucinations and vague chart suggestions | **75.5% aggregate score (+34%).** Scores became consistent. JSON chart specs now parseable. But still hallucinated correlation 0.80 vs true 0.941 (estimation drift). JSON broke in 3/10 runs due to cognitive overload from simultaneous prose + JSON generation. Format bleed: markdown leaked inside JSON. 4 moderate statistical drifts. |
| v3.0 Chained Pipeline | Decomposed into 4 specialized prompts: Stage 1 (JSON only), Stage 2 (Markdown only), Stage 3 (JSON only), Stage 4 (verification JSON). Added deterministic profiler tool — LLM never touches raw CSV. Stage 4 adversarial fact-checker cross-verifies every number. Temperature: 0.1/0.3/0.1/0.0. | v2 still did mental math without external tools; cognitive overload from monolithic prompt; no closed-loop verification | **98.9% aggregate score (+57.4%), 100% Numerical Faithfulness.** Zero hallucinations across all 3 datasets and all 9 experiments. JSON valid in 10/10 runs (no format bleed). Auto-corrected 0 errors (none needed). Latency: 1.43s vs 0.35s — acceptable tradeoff for eliminating 100% of mathematical hallucinations. |

**Full prompt text for each version is available in the repository:**
- v1.0: `prompts/v1_baseline/single_shot_prompt.md`
- v2.0: `prompts/v2_structured/role_and_constraints_prompt.md`
- v3.0: `prompts/v3_chained_pipeline/01_schema_and_anomaly_explorer.md` through `04_number_verifier_auditor.md`

---

# Section 4: Demonstration and Testing

## Test Table

| Test No. | Input (short) | Type | Expected Output | Actual Output (short) | Pass/Fail |
|----------|--------------|------|----------------|----------------------|-----------|
| 1 | `test_1_retail_sales.csv` — 35 rows, $18,750 outlier | Normal | Mean = $920.18, Median = $360.00, outlier ORD-1020 flagged | Mean $920.18 verified, Median $360.00, ORD-1020 flagged as CRITICAL outlier | Pass |
| 2 | `test_2_student_performance.csv` — 40 rows | Normal | Correlation 0.941 detected, mean CGPA 7.64 | r=0.941 verified, mean CGPA 7.64 exact match | Pass |
| 3 | `test_3_cloud_server_logs.csv` — 36 rows | Normal | Latency spike 620.40 ms, 360 total errors, CPU 98.90% | All values verified exact match, CRITICAL alert raised | Pass |
| 4 | Custom CSV uploaded via Streamlit file uploader | Normal | Profile + narrative + charts generated end-to-end | Pipeline runs successfully, all 4 tabs populated | Pass |
| 5 | Retail dataset — chart type validation | Normal | Bar for categories, Scatter for bivariate, Line for temporal, Boxplot for distribution | 4 charts generated: bar (category), scatter (units vs revenue), line (date vs revenue), boxplot (revenue by category) | Pass |
| 6 | Student dataset — narrative quality check | Normal | Executive prose with zero statistical jargon | Clear 4-section narrative, all numbers verified against ground truth | Pass |
| 7 | CSV with ALL missing values in a column | Edge | Flag CRITICAL severity, warn about analysis limits | CRITICAL alert with "100% missing" warning displayed, column excluded from analysis | Pass |
| 8 | CSV with only 5 rows (N < 30) | Edge | Sample size bias warning triggered | "⚠ Small Sample Warning" badge displayed, bias disclaimer in report | Pass |
| 9 | CSV with email addresses in a column | Edge | PII detected and redacted before LLM | "⚠ PII Redacted" badge, email column masked as [REDACTED_PII] | Pass |
| 10 | v1 baseline prompt on retail dataset (hallucination test) | Invalid | v1 should produce wrong mean (~$340) demonstrating hallucination | Mean hallucinated as $340.50 (true $920.18, 63% error) — proves v1 fails and validates need for v3 | Fail (Expected) |
| 11 | Empty CSV file (header row only, 0 data rows) | Edge | Graceful handling or informative error message | Error handled gracefully, no crash, "0 rows" displayed | Pass |
| 12 | Server logs — Grammar of Graphics validation | Normal | Line chart for timestamp (temporal), bar for region (categorical) | Correct type mappings: line for timestamp, bar for server_region, scatter for connections vs latency | Pass |

## Screenshots

> _[INSERT SCREENSHOT 1: Tab 1 — Executive Report showing verification badge "100% Verified Against Ground Truth" and interactive Plotly bar chart for retail sales by category. Caption: "Test 1 — Retail Sales Executive Report with verified statistics and interactive charts"]_

> _[INSERT SCREENSHOT 2: Tab 2 — 4-Stage Chain Inspector showing Stage 4 audit output with all 7 claims marked EXACT_MATCH. Caption: "Test 1 — Stage 4 Number Verifier confirming zero hallucinations"]_

> _[INSERT SCREENSHOT 3: Tab 4 — Evaluation grouped bar chart comparing v1 (41.5%) vs v2 (75.5%) vs v3 (98.9%). Caption: "Test 1-3 — Empirical evaluation across all 3 benchmark datasets showing v3 achieves 98.9% and 100% Numerical Faithfulness"]_

## Known Limitations

1. **Large CSVs (>500 rows)**: The deterministic profiler handles large datasets efficiently, but API latency increases with longer statistical JSON in LLM context. **Next step**: Implement progressive summarization for high-row datasets in Milestone 3.
2. **Non-CSV Input Formats**: Currently only CSV files are supported. **Next step**: Add Excel (.xlsx) and JSON parsing support.
3. **Multi-Language Column Names**: Column headers in non-English languages may confuse the chart recommender's column-name matching. **Next step**: Add Unicode normalization layer.
4. **Static Report Output**: Reports are generated as single snapshots. **Next step**: Explore streaming/real-time analysis updates using the Gemini Live API.

---

# Section 5: Repository

> _[INSERT SCREENSHOT of GitHub repository file tree showing README.md, prompts/, src/, datasets/, evaluation/, docs/, CHANGELOG.md]_

**What changed since Milestone 1:**
1. Built complete Streamlit 4-tab interactive dashboard (`app.py`) with executive report, chain inspector, iteration lab, and evaluation panels
2. Implemented full 4-stage prompt chain runner with Gemini API integration and offline demo mode (`src/prompt_chain_runner.py`, 896 lines)
3. Created deterministic CSV profiler with PII redaction and sample-size bias warnings (`src/tool_csv_profiler.py`, 281 lines)
4. Built automated 5-metric evaluation harness producing 9 benchmark experiment logs (`evaluation/`)
5. Completed 3-version prompt iteration (v1 → v2 → v3) with quantitative results documented in CHANGELOG.md

---

# Section 6: Supporting Document

_[Paste the contents of your Technical Report (docs/technical_synopsis.md) here — same document uploaded as the separate PDF at Q16]_

---

# Section 7: Team Contribution

| Member Name | Enrollment No. | Role | Tasks Done in Milestone 2 | Evidence | Contribution (%) |
|------------|----------------|------|--------------------------|----------|------------------|
| _[Name 1]_ | _S24CSEU_____ | Lead Prompt Engineer & System Architect | Designed 4-stage chained prompt pipeline; wrote P1, P2, P3, P4 prompt templates; iterated v1 → v2 → v3 with documented results; authored Milestone 2 PDF Sections 2 and 3 | `prompts/v3_chained_pipeline/01-04*.md`, `prompts/v1_baseline/`, `prompts/v2_structured/`, 6+ git commits | 35 |
| _[Name 2]_ | _S24CSEU_____ | Backend & Tools Developer | Built deterministic CSV profiler (`tool_csv_profiler.py`); implemented PII redaction engine; built prompt chain runner (`prompt_chain_runner.py`) with Gemini API integration and mock mode; integrated all pipeline stages | `src/tool_csv_profiler.py`, `src/prompt_chain_runner.py`, `requirements.txt`, 5+ git commits | 35 |
| _[Name 3]_ | _S24CSEU_____ | Evaluation & UI Developer | Built Streamlit dashboard (`app.py`) with 4 interactive tabs; created evaluation harness (`evaluation/run_evaluation.py`); generated benchmark logs and error analysis report; recorded video reel; created diagrams | `app.py`, `evaluation/`, `docs/contribution_log.md`, video reel, 4+ git commits | 30 |
