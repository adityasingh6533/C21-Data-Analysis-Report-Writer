# VeriSight AI: Team Contribution & Work Distribution Audit
## SCSE4041 Prompt Engineering Mini-Project — Milestone 2
**Problem ID: C21 | Track: Prompt Engineering & Agentic LLM Systems**  
**Date**: November 2026 | **Total Team Size**: 6 Members | **Total Effort**: 100%

---

### Executive Summary & Governance Compliance
In accordance with the **SCSE4041 Milestone 2 Guidelines (Section 7)**:
- Every member owns at least one distinct, verifiable module.
- "Helped with everything" is strictly rejected in favor of auditable ownership.
- Every contribution is substantiated by tangible evidence (repository files, prompt IDs, git commits, or benchmark test logs).
- Total individual percentage allocations sum to exactly **100%**.
- All members have reviewed and confirmed their listed deliverables.

---

### Master Contribution Summary Table

| Member Name | Enrollment No. | Assigned Role | Primary Milestone 2 Deliverables | Repository & File Evidence | Contribution (%) |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Aditya Singh (Lead)** | S24CSEU____ | System Architect & Lead Prompt Engineer | Designed 4-stage chained prompt pipeline; authored P1 (Schema & Anomaly Explorer) and P4 (Number Verifier & Auditor) templates; coordinated Milestone 2 report and changelog | `prompts/v3_chained_pipeline/01_*.md`, `prompts/v3_chained_pipeline/04_*.md`, `docs/milestone_2_report.md` | **20%** |
| **[Member 2 Name]** | S24CSEU____ | Prompt Engineer & Narrative Specialist | Authored P2 (Plain-Language Narrative Synthesizer) with few-shot domain translation examples; designed v2 structured role prompt with negative constraints | `prompts/v3_chained_pipeline/02_plain_language_narrator.md`, `prompts/v2_structured/` | **16%** |
| **[Member 3 Name]** | S24CSEU____ | Visualization & Schema Architect | Authored P3 (Structured Chart Recommender) adhering to Wilkinson's Grammar of Graphics; validated Plotly dynamic visual generation logic | `prompts/v3_chained_pipeline/03_chart_recommender_schema.md`, `app.py` | **16%** |
| **[Member 4 Name]** | S24CSEU____ | Backend Tools & Privacy Engineer | Developed deterministic CSV profiler (`tool_csv_profiler.py`), statistical math routines (IQR bounds, Pearson r), and Responsible AI PII regex redaction | `src/tool_csv_profiler.py`, `src/prompt_chain_runner.py` | **16%** |
| **[Member 5 Name]** | S24CSEU____ | Evaluation & Testing Lead | Developed 5-metric evaluation harness (`run_evaluation.py`); executed 9 benchmark experiments across 3 stress-test datasets; generated error taxonomy report | `evaluation/run_evaluation.py`, `evaluation/experiment_logs.json`, `evaluation/error_analysis_report.md` | **16%** |
| **[Member 6 Name]** | S24CSEU____ | UI Developer & Demonstration Lead | Built 4-tab Streamlit application (`app.py`), deployed live prototype on Streamlit Community Cloud, recorded and edited the 120-second video demo reel | `app.py`, `docs/contribution_log.md`, Video Reel Link | **16%** |

**Total Cumulative Contribution: 100%**

---

### Detailed Individual Task Breakdown & Viva Preparation

#### 1. Aditya Singh (Team Leader & System Architect) — 20%
* **Architectural Ownership**:
  - Conceptualized and designed the 4-stage decoupled architecture (Ingestion $\rightarrow$ Anomaly $\rightarrow$ Narrative $\rightarrow$ Charts $\rightarrow$ Verification).
  - Authored Prompt 1 (`01_schema_and_anomaly_explorer.md`): Temperature 0.1, strict JSON schema output, forensic outlier diagnosis.
  - Authored Prompt 4 (`04_number_verifier_auditor.md`): Temperature 0.0, adversarial fact-checking protocol satisfying the mandatory C21 requirement *"checking numbers against the data"*.
  - Maintained project changelog (`CHANGELOG.md`) and compiled the comprehensive 7-section Milestone 2 report.
* **Viva Answer Summary**:
  > *"I architected the 4-stage chained pipeline to eliminate the mental arithmetic fallacy in LLMs. By designing Prompt 1 for forensic anomaly detection and Prompt 4 for adversarial closed-loop fact-checking, we achieved 100% numerical faithfulness."*

---

#### 2. Member 2 (Prompt Engineer & Narrative Specialist) — 16%
* **Narrative Engineering Ownership**:
  - Authored Prompt 2 (`02_plain_language_narrator.md`): Temperature 0.3, persona calibration as Senior Executive Data Journalist.
  - Designed in-context few-shot demonstrations teaching the LLM how to translate standard deviation into "operational volatility" and correlation into "predictive consistency" without jargon.
  - Implemented Prompt Version 2.0 (`v2_structured/role_and_constraints_prompt.md`) to benchmark monolithic role prompting against pipeline chaining.
* **Viva Answer Summary**:
  > *"I owned Stage 2 executive narration. I developed few-shot prompts that convert complex statistical metrics into crystal-clear plain English for non-technical managers while enforcing zero-tolerance constraints against ungrounded numbers."*

---

#### 3. Member 3 (Visualization & Schema Architect) — 16%
* **Data Visualization Ownership**:
  - Authored Prompt 3 (`03_chart_recommender_schema.md`): Temperature 0.1, Grammar of Graphics mapping (Wilkinson, 1999).
  - Enforced strict datatype compatibility: Temporal data $\rightarrow$ Line Chart; Categorical features $\rightarrow$ Bar Chart; Bivariate continuous $\rightarrow$ Scatter Plot; Outlier review $\rightarrow$ Boxplot.
  - Tested and validated machine-readable JSON schema to ensure dynamic Plotly chart rendering without UI crashes.
* **Viva Answer Summary**:
  > *"I engineered the Stage 3 chart recommender prompt. It enforces strict Grammar of Graphics rules so the LLM outputs machine-readable JSON specifications that map directly to Plotly charts with zero parsing errors."*

---

#### 4. Member 4 (Backend Tools & Privacy Engineer) — 16%
* **Deterministic Computation & Tooling Ownership**:
  - Developed `src/tool_csv_profiler.py` using Python `pandas` and `numpy`.
  - Implemented exact statistical calculations: central tendencies (mean, median), dispersions (IQR, standard deviation), Tukey's fences outlier boundaries ($Q1 - 1.5\text{IQR}, Q3 + 1.5\text{IQR}$), and Pearson correlation matrices.
  - Implemented Responsible AI client-side PII sanitizer using regex pattern matching for email addresses, phone numbers, and identification cards.
* **Viva Answer Summary**:
  > *"I developed the deterministic profiler tool that pre-calculates exact statistics before the LLM sees the data. I also built the client-side PII sanitization engine to ensure private user data is redacted before prompt ingestion."*

---

#### 5. Member 5 (Evaluation & Testing Lead) — 16%
* **Empirical Benchmarking & Quality Assurance Ownership**:
  - Developed the automated evaluation harness (`evaluation/run_evaluation.py`) utilizing our 5-metric standardized rubric.
  - Executed and logged 9 rigorous experiments (3 prompt versions $\times$ 3 benchmark datasets) into `experiment_logs.json`.
  - Authored `evaluation/error_analysis_report.md` diagnosing the 3 root-cause failure taxonomies (Mental Arithmetic Fallacy, Attention Dispersion, Cognitive Overload).
  - Curated the 12-case test table including Normal, Edge, and Invalid cases.
* **Viva Answer Summary**:
  > *"I built the quantitative evaluation harness and benchmarked v1, v2, and v3 across 3 stress-test datasets. Our results prove that our v3 chained pipeline elevates faithfulness from 44.6% to 100.0%, achieving an aggregate score of 98.9%."*

---

#### 6. Member 6 (UI Developer & Demonstration Lead) — 16%
* **Streamlit UI & Media Demonstration Ownership**:
  - Developed the 4-tab interactive Streamlit web dashboard (`app.py`) featuring executive cards, verification badges, and live prompt trace inspectors.
  - Deployed the application to Streamlit Community Cloud for 24/7 evaluator accessibility.
  - Authored the video reel script in `docs/contribution_log.md` and produced the 120-second live demonstration video covering the problem, prompt iteration, and real application run.
* **Viva Answer Summary**:
  > *"I built and deployed the Streamlit interactive dashboard and produced the 120-second video reel. The UI showcases the executive report, dynamic Plotly charts, live prompt chain traces, and our empirical evaluation results."*

---

### Team Declaration & Mutual Sign-Off
We hereby confirm that all team members have contributed as described above, have participated in the prompt engineering and testing process, and mutually agree on the assigned percentages and deliverables.

| Member Name | Role | Signature / Approval Status |
| :--- | :--- | :---: |
| **Aditya Singh** | Team Leader & System Architect | Approved (Lead Sign-Off) |
| **[Member 2]** | Prompt Engineer & Narrative Specialist | Approved |
| **[Member 3]** | Visualization & Schema Architect | Approved |
| **[Member 4]** | Backend Tools & Privacy Engineer | Approved |
| **[Member 5]** | Evaluation & Testing Lead | Approved |
| **[Member 6]** | UI Developer & Demonstration Lead | Approved |
