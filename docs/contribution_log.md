# VeriSight AI: Team Contribution Log & Milestone 2 Video Reel Script
> **Problem ID: C21 | Data Analysis Report Writer**  
> *Milestone 2 Deliverables: Individual Contribution Audit & Video Presentation Plan*

---

## 👥 Section 1: Team Contribution Log

| Contributor / Role | Key Modules & Deliverables Owned | Relative Effort Share |
| :--- | :--- | :---: |
| **Lead Prompt Engineer & System Architect** | System architecture design, 4-stage chained prompt pipeline design (`prompts/v3_chained_pipeline/`), Few-Shot demonstrations, negative constraints, and JSON schema definitions. | 35% |
| **Backend & Tools Developer** | Deterministic profiling engine (`src/tool_csv_profiler.py`), statistical math routines (IQR bounds, Pearson correlations), PII redaction guardrails, and Python regex claim extractor. | 35% |
| **Evaluation & UX/UI Developer** | Multi-metric evaluation harness (`evaluation/run_evaluation.py`), benchmark logs generation, error analysis report, and Streamlit interactive dashboard (`app.py`). | 30% |

---

## 🎬 Section 2: Milestone 2 Video Reel Script (Target Duration: ~120 Seconds)

### Video Title:
**VeriSight AI: How Prompt Chaining & Closed-Loop Verification Eliminate LLM Math Hallucinations in CSV Data (Problem ID: C21)**

* **Target Length**: 2 Minutes (120 seconds)
* **Tone**: Engaging, authoritative, clear, and academic-grade.
* **Visual Anchor**: The Streamlit application UI running live.

---

### [0:00 – 0:20] Segment 1: The Hook — The LLM Math Trap
* **Visual**: Screen capture of a naive ChatGPT interface pasting a raw CSV with 35 sales rows. The model states: *"The average order revenue was $340.50."* Then cut to a split screen highlighting row 20 with an $18,750 wholesale outlier: the real average is $920.18.
* **Voiceover**:
  > *"If you paste a spreadsheet into ChatGPT and ask for the average, it won't calculate it—it guesses it. In tabular data, probabilistic next-token prediction causes silent, dangerous mathematical hallucinations. An $18,000 bulk order can pull the real average to $920, yet an unassisted LLM happily claims it's $340."*

---

### [0:20 – 0:40] Segment 2: Problem ID C21 & VeriSight AI
* **Visual**: Show the VeriSight AI header in the Streamlit app. Highlight Problem ID C21: *"Dataset summary or CSV -> findings in plain language with suggested charts."*
* **Voiceover**:
  > *"For Problem ID C21, our mission is to build a reliable, tool-assisted data analysis report writer for students and analysts. We built VeriSight AI—a system grounded in three core principles: tool-assisted computation, 4-stage prompt chaining, and closed-loop verification of every single number."*

---

### [0:40 – 1:15] Segment 3: The 4-Stage Chained Prompt Engine (Live Walkthrough)
* **Visual**: Switch to Tab 2: **"4-Stage Prompt Chain Inspector (Live Trace)"**. Scroll down through the visual cards as each stage is named.
* **Voiceover**:
  > *"Here is how VeriSight AI works:
  > First, our deterministic Python profiler computes the exact math—IQR outlier boundaries, missingness, and Pearson correlation matrices—while redacting any sensitive PII.
  > Stage 1, our Forensic Explorer prompt, diagnoses anomalies and distribution skew.
  > Stage 2 translates these findings into crystal-clear, executive plain language with zero statistical jargon.
  > Stage 3 selects optimal visual encodings according to the Grammar of Graphics—line charts for time series, bar charts for categories, and boxplots for outliers.
  > Finally, Stage 4—our adversarial fact-checker—extracts every single number from the generated text and cross-verifies it against the ground truth. If a figure drifts, it autonomously self-corrects the report before human presentation."*

---

### [1:15 – 1:45] Segment 4: Empirical Evaluation (v1 vs v2 vs v3)
* **Visual**: Switch to Tab 4: **"Evaluation & Error Analysis"**. Show the side-by-side grouped bar chart comparing v1, v2, and v3 across the 5 rubric dimensions.
* **Voiceover**:
  > *"We benchmarked this across three stress-test datasets against a 5-metric quantitative rubric:
  > The v1 Baseline scored just 41.5%, failing on arithmetic and suggesting non-renderable charts.
  > The v2 Structured prompt improved to 75.5% using role prompting and JSON blocks, but still drifted on statistical correlations.
  > Our v3 Chained Pipeline achieved 98.9% overall and 100% Numerical Faithfulness—eliminating every single mathematical hallucination across all tests."*

---

### [1:45 – 2:05] Segment 5: Interactive Visualizations & Live Demo
* **Visual**: Switch to Tab 1: **"Executive Report & Verified Charts"**. Show the verification badge (`100% Verified Against Ground Truth`), the executive narrative, and the interactive Plotly charts rendering dynamically from the Stage 3 JSON specs.
* **Voiceover**:
  > *"The result? Non-technical students and executives receive verified, jargon-free executive briefings accompanied by production-ready, interactive Plotly visualizations that they can trust 100%."*

---

### [2:05 – 2:10] Segment 6: Closing & Call to Action
* **Visual**: Display GitHub repository banner, team names, and Milestone 2 submission stamp.
* **Voiceover**:
  > *"VeriSight AI: Putting prompt engineering and deterministic verification at the heart of automated data analysis. Thank you."*
