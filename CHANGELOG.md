# Changelog — VeriSight AI (Problem ID: C21)

All notable changes to this project are documented here.
Format: `[Date] — Summary of change`

---

## Milestone 2 Development (October–November 2026)

### [2026-11-22] Final Milestone 2 Submission Preparation
- Finalized all test cases across 3 benchmark datasets (12 test inputs including 4 edge cases)
- Created CHANGELOG.md for submission compliance
- Verified all links (prototype, repository, reel) are publicly accessible
- Confirmed zero API keys exposed in repository

### [2026-11-20] Evaluation Framework & Error Analysis Report
- Built automated 5-metric evaluation harness (`evaluation/run_evaluation.py`)
- Executed 9 benchmark experiments (3 versions × 3 datasets)
- Generated `experiment_logs.json` with full scoring data
- Authored empirical error analysis report documenting 3 failure taxonomies (Mental Arithmetic Fallacy, Token Attention Dispersion, Cognitive Overload & Schema Bleeding)
- Documented 3 concrete before/after case studies caught by Stage 4 Auditor

### [2026-11-18] Streamlit Interactive Dashboard (`app.py`)
- Built 4-tab Streamlit application:
  - Tab 1: Executive Report & Verified Interactive Plotly Charts
  - Tab 2: 4-Stage Prompt Chain Inspector (Live Trace)
  - Tab 3: Prompt Iteration Lab (v1 vs v2 vs v3 side-by-side comparison)
  - Tab 4: Quantitative Evaluation & Error Analysis with grouped bar chart
- Added custom CSS for verification badges, governance indicators, and executive card styling
- Implemented Demo Mode toggle for offline classroom demonstrations without API key
- Added custom CSV upload support alongside 3 benchmark datasets

### [2026-11-15] Technical Synopsis & Video Reel Script
- Authored `docs/technical_synopsis.md` — Milestone 2 Technical Report covering architecture, empirical evaluation (v1→41.5%, v2→75.5%, v3→98.9%), and Responsible AI guardrails
- Created team contribution log with detailed 120-second video reel script (`docs/contribution_log.md`)

### [2026-11-10] Prompt Chain Runner & LLM Integration (`src/prompt_chain_runner.py`)
- Implemented `VeriSightPipeline` class with Gemini 2.5 Flash API integration via `google-genai` SDK
- Built automatic prompt template loader that extracts System and User prompts from markdown files
- Developed comprehensive deterministic mock response generator for all 3 datasets × 4 stages
- Implemented v1 baseline, v2 structured, and v3 chained pipeline execution methods
- Added Python regex-based numerical claim auditor for independent Stage 4 verification

### [2026-11-05] Deterministic CSV Profiler Tool (`src/tool_csv_profiler.py`)
- Built pandas/numpy-based statistical profiler computing:
  - Central tendencies (mean, median), dispersion (std dev, IQR, min, max)
  - Tukey's fence outlier detection (Q1 − 1.5×IQR, Q3 + 1.5×IQR)
  - Pearson correlation matrices with strength classification
  - Column semantic type inference (numeric, temporal, categorical, text)
- Implemented Responsible AI PII scanner with regex-based detection for emails, phone numbers, SSN, Aadhaar
- Added automatic PII masking/redaction before LLM context injection
- Added sample size bias warnings (N < 30 alert)

### [2026-11-01] Prompt Engineering Lifecycle — 3-Version Iteration
- **v1.0 Baseline** (`prompts/v1_baseline/single_shot_prompt.md`): Naive zero-shot raw CSV ingestion — documented failure modes (41.5% aggregate score, 6 hallucinations)
- **v2.0 Structured** (`prompts/v2_structured/role_and_constraints_prompt.md`): Added Senior Data Journalist persona, negative constraints, 1-shot demo, dual output — improved to 75.5% but still hallucinated correlations
- **v3.0 Chained Pipeline** (`prompts/v3_chained_pipeline/`): 4-stage decomposed pipeline:
  - `01_schema_and_anomaly_explorer.md` (Temp 0.1, JSON output)
  - `02_plain_language_narrator.md` (Temp 0.3, 2 few-shot examples, Markdown output)
  - `03_chart_recommender_schema.md` (Temp 0.1, Grammar of Graphics, JSON array)
  - `04_number_verifier_auditor.md` (Temp 0.0, adversarial fact-checking, JSON output)
- Achieved 98.9% aggregate score and 100% Numerical Faithfulness with zero hallucinations

### [2026-10-25] Synthetic Benchmark Datasets
- Created `test_1_retail_sales.csv` — 35 rows, $18,750 outlier, 2 missing values
- Created `test_2_student_performance.csv` — 40 rows, r=0.941 attendance-CGPA correlation
- Created `test_3_cloud_server_logs.csv` — 36 rows, 620ms latency spike, error cascade

---

## Milestone 1 (October 2026)

### [2026-10-15] Project Proposal & Repository Setup
- Defined Problem ID C21 scope: "Data analysis report writer"
- Authored comprehensive Milestone 1 proposal (`docs/milestone_1_proposal.md`)
- Mapped project to 10-stage Prompt Engineering Lifecycle
- Identified target users: students, junior analysts, non-technical managers
- Designed initial 4-stage architecture concept
- Set up GitHub repository with README.md and project structure
