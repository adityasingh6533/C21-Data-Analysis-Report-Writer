# Prompt Version 1.0: Naive Single-Shot Baseline Prompt

## 📋 Metadata
- **Version**: 1.0.0 (Baseline)
- **Architecture**: Single-shot, Zero-shot Monolithic Prompt
- **Input Modality**: Raw uncomputed CSV text directly injected into context
- **Target LLM Role**: None (Default assistant)
- **Primary Goal**: Establish an unoptimized baseline to measure hallucination rate, token saturation, and narrative inconsistency.

---

## 📝 Prompt Template

```text
You are a helpful data analyst assistant.

Here is a raw CSV dataset:
```csv
{{RAW_CSV_DATA}}
```

User Goal: {{USER_GOAL}}

Please analyze this dataset and do the following:
1. Give me the key findings and trends in plain language.
2. Calculate the averages, totals, and any interesting percentages or correlations.
3. Tell me what charts I should create to visualize this data.
4. Provide any recommendations based on your findings.
```

---

## 🔬 Parameter Settings
- **Temperature**: `0.7` (Default creative exploratory setting)
- **Top_P**: `0.95`
- **Max Output Tokens**: `2048`
- **Output Format**: Freeform Markdown

---

## ⚠️ Documented Weaknesses & Failure Modes of v1.0

Empirical testing of this naive baseline on our benchmark datasets reveals four critical failure modes:

### 1. Arithmetic & Aggregation Hallucinations
- **The Problem**: Language models are probabilistic next-token generators that lack internal state machines or arithmetic ALUs. When prompted to *"calculate averages, totals, and percentages"* across 30–50+ rows of numbers, the model hallucinates figures rather than computing them.
- **Observed Failures**:
  - In `test_1_retail_sales.csv`, the model routinely calculates average order revenue as ~$320–$350, completely ignoring the $18,750 enterprise outlier that drags the actual arithmetic mean up to ~$948.
  - In `test_3_cloud_server_logs.csv`, average CPU utilization was hallucinated as 48.2% when the true mean was 50.8%, and error counts were fabricated with arithmetic discrepancies exceeding 25%.

### 2. Context Window Saturation & Attention Degeneration
- **The Problem**: Dumping raw CSV rows wastes thousands of prompt tokens on punctuation, commas, repeated category strings, and formatted timestamps.
- **Observed Failures**:
  - Leads to the **"Lost-in-the-Middle"** phenomenon: The LLM pays attention to the first 5 rows and the last 3 rows of the CSV, ignoring trends, anomalies, or distribution shifts occurring in the middle 30 rows.
  - Fails to scale: Once a CSV exceeds 100 rows, token consumption explodes, increasing inference latency and risk of context truncation.

### 3. Vague, Unrenderable Chart Suggestions
- **The Problem**: Without visual taxonomy constraints or strict schema enforcement, chart recommendations are colloquial, ambiguous, and cannot be ingested by any visualization library (e.g., Chart.js, Vega-Lite, D3.js).
- **Observed Failures**:
  - Outputs vague statements like: *"You should make a pie chart showing sales by region and a line chart of ratings."*
  - Suggests anti-pattern visual encodings, such as pie charts with 15+ slices or plotting discrete categorical IDs along continuous line axes.
  - Missing field encodings: Omits exact column names for X-axis, Y-axis, aggregation methods (SUM, MEAN, COUNT), and grouping dimensions.

### 4. Zero Grounding & Absence of Fact-Checking
- **The Problem**: The prompt contains no closed-loop verification mechanism. If the model invents a finding (e.g., *"Region North had the lowest customer rating of 2.1"* when North actually had a 4.3 average), the human reader has no audit trail or verification badge to detect the falsehood without manually inspecting the spreadsheet.
