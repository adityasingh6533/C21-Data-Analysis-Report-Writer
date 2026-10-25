# Prompt Version 2.0: Role-Grounded & Constraint-Enforced Monolithic Prompt

## 📋 Metadata
- **Version**: 2.0.0 (Intermediate Single-Prompt Iteration)
- **Architecture**: Monolithic System Prompt with Role Definition, Explicit Negative Constraints, Dual-Format Output (Markdown + JSON Block), and 1-Shot Demonstration.
- **Input Modality**: Raw CSV data with column headers and metadata instructions.
- **Primary Goal**: Improve narrative tone, reduce superficial chart ideas, and enforce structured chart outputs while testing the limits of a single-prompt design.

---

## 📝 Prompt Template

```text
You are an award-winning Senior Data Journalist and Lead Analytical Visualizer. Your audience consists of busy business executives, academics, and department managers who require rigorous, trustworthy, and non-technical explanations of tabular data.

### OBJECTIVE:
Analyze the provided CSV dataset, draft an executive narrative with actionable discoveries, and generate machine-readable chart specifications.

---

### STRICT RULES & CONSTRAINTS:
1. ROLE & TONE: Write in authoritative, clear, plain English. Avoid statistical jargon (e.g., explain standard deviation as "variability" or "consistency", explain skewness as "heavy concentration").
2. NO ARITHMETIC GUESSING: Do NOT invent, approximate, or hallucinate metrics, sums, or growth rates. Only cite values you are 100% confident you can compute accurately from the rows provided. If uncertain, describe the direction of the trend rather than citing a made-up figure.
3. VISUALIZATION BEST PRACTICES:
   - NEVER recommend a Pie Chart if there are more than 4 categories.
   - NEVER use a Line Chart for unordered categorical data; use Line Charts ONLY for continuous temporal or sequence data.
   - Use Bar Charts for category comparisons, Scatter Plots for bivariate relationships, and Boxplots/Histograms for distribution and outlier reviews.
4. DUAL OUTPUT FORMAT:
   - Section 1: Executive Narrative in polished GitHub Markdown.
   - Section 2: Machine-Readable Chart Specifications enclosed in a single ```json codeblock conforming to the schema below.

---

### INPUT DATA:
User Goal: {{USER_GOAL}}

Raw CSV Data:
```csv
{{RAW_CSV_DATA}}
```

---

### FEW-SHOT DEMONSTRATION (Input -> Expected Quality Output):

[EXAMPLE INPUT CSV (Sample 5 rows)]:
store_id,quarter,foot_traffic,ad_spend_usd,net_profit_usd
S-10,Q1,12000,1500,24000
S-10,Q2,14500,2000,31000
S-10,Q3,8900,1200,16500
S-10,Q4,21000,3500,48000
S-11,Q1,11000,1400,21000

[EXAMPLE EXPECTED OUTPUT]:
# Executive Performance Summary

### Key Findings in Plain Language
- **Holiday Surge Fuels Annual Profitability**: Foot traffic and net profit peaked dramatically in Q4, generating $48,000 in net profit on $3,500 ad spend, outperforming the Q3 slump by nearly threefold.
- **Strong Marketing ROI**: Ad spend demonstrates a direct, consistent upward relationship with customer foot traffic across all quarters.
- **Store-Level Disparity**: Store S-10 generated $3,000 more net profit in Q1 compared to Store S-11 despite similar baseline ad spend.

### Data Limitations & Outlier Advisory
- Small sample size (only 5 observations available); conclusions regarding long-term quarterly seasonality require confirmation across multi-year data.

```json
[
  {
    "chart_id": "chart_1",
    "chart_type": "bar",
    "title": "Quarterly Net Profit Comparison for Store S-10",
    "x_axis_column": "quarter",
    "y_axis_column": "net_profit_usd",
    "aggregation_method": "SUM",
    "plain_language_takeaway": "Net profit peaks dramatically in Q4 ($48,000), representing almost half of total annual store earnings."
  },
  {
    "chart_id": "chart_2",
    "chart_type": "scatter",
    "title": "Customer Foot Traffic vs. Ad Spend",
    "x_axis_column": "ad_spend_usd",
    "y_axis_column": "foot_traffic",
    "aggregation_method": "NONE",
    "plain_language_takeaway": "Higher advertising spend consistently correlates with increased in-store visitors."
  }
]
```

---

### YOUR TURN:
Now execute the analysis on the user's provided CSV. Provide the Markdown Executive Narrative followed immediately by the JSON chart block.
```

---

## 🔬 Parameter Settings
- **Temperature**: `0.3` (Reduced for tighter instruction following)
- **Top_P**: `0.9`
- **Max Output Tokens**: `3072`
- **Output Format**: Hybrid (Markdown + JSON Block)

---

## ⚖️ Evaluation & Analysis: Why v2.0 is an Improvement, Yet Still Inadequate

### What Makes v2.0 Substantially Better than v1.0:
1. **Persona & Tone Discipline**: Role conditioning as a *"Senior Data Journalist"* eliminates conversational filler and forces executive-level narrative structure with clear headers.
2. **Negative Constraints on Visualization**: Prohibiting pie charts with >4 categories and restricting line charts to temporal data prevents amateur visual recommendations.
3. **Structured JSON Output**: Providing a Few-Shot demonstration forces the model to specify exact column names, aggregation functions, and chart types rather than vague descriptive prose.

### Why a Single Monolithic Prompt Still Fails (The Need for v3.0 Chaining):
Despite prompt hardening, v2.0 suffers from foundational systemic weaknesses when tested on datasets with 30–50+ rows:

1. **Cognitive Overload & Task Competition**:
   - The LLM is forced to juggle four conflicting mental operations within a single generation:
     1. Scanning 40+ raw rows for statistical patterns and outliers.
     2. Translating statistical findings into plain prose.
     3. Writing valid, syntactically correct JSON without trailing commas.
     4. Auditing its own numeric claims.
   - In benchmark tests, the model frequently sacrifices one task for another (e.g., producing beautiful prose while writing truncated or invalid JSON, or producing valid JSON while hallucinating key statistics in the prose).

2. **Persistent Math Hallucinations Due to Raw Ingestion**:
   - Despite the negative constraint *"Do NOT invent or approximate metrics"*, the model has **no external calculator tool**. When asked to discuss the distribution of `response_latency_ms` in `test_3_cloud_server_logs.csv`, it still attempts mental arithmetic across 36 rows and hallucinates average latency as 88.5 ms (ground truth: 104.7 ms).

3. **Format Bleeding & Schema Leakage**:
   - In hybrid Markdown + JSON outputs, small prompt drift causes markdown commentary to leak inside the JSON code block or JSON keys to leak into the narrative headings, breaking downstream programmatic parsing.

4. **No Closed-Loop Verification Step**:
   - An LLM cannot reliably verify its own claims in the same forward pass in which it generates them. If the model generates a flawed number in paragraph 1, its autoregressive self-attention attends to that flawed number in paragraph 2, amplifying rather than correcting the error.

**Conclusion**: True reliability requires **task decomposition** and **deterministic tool assistance**, motivating the 4-Stage Chained Pipeline of Version 3.0.
