# 🎬 VeriSight AI: 90–150 Second Video Reel Teleprompter & Recording Guide
**Problem ID: C21 | Course: SCSE4041 — Prompt Engineering Mini-Project**  
**Target Video Duration**: **110 – 120 Seconds** *(Safely inside the mandatory 90–150s range)*

---

## 📌 Key Guidelines Reminders (Must Follow to Avoid 0 Marks)
1. **Length**: Strictly between **90 and 150 seconds** (e.g., 115s). A video shorter than 90s or longer than 150s loses marks.
2. **Order of Content** (Mandatory as per SCSE4041 Rubric):
   - **Part 1**: Problem (~10s)
   - **Part 2**: Prompt experiment (~30–40s) — Before-and-after old vs new prompt
   - **Part 3**: Working demo (~40–60s) — Real run on screen (mock-ups get 0 marks)
   - **Part 4**: Progress & Next Steps (~15–20s)
3. **Format**: Screen recording with voiceover or captions (faces optional). Vertical or horizontal both work.
4. **Hosting**: Upload to **Google Drive** or **YouTube (Unlisted)** set to **"Anyone with the link can view"**.

---

## 🖥️ Screen Assets Ready for Your Recording

| Asset | Link / File Location | How to Use |
| :--- | :--- | :--- |
| **Interactive HTML Slides** | [`presentation/reel_presentation.html`](file:///d:/Prompt-Project/C21-Data-Analysis-Report-Writer/presentation/reel_presentation.html) | Double-click to open in Chrome/Edge. Press **F11** for fullscreen. Use Arrow keys to navigate. Includes a live built-in timer! |
| **Live Working Streamlit App** | [https://adityasingh6533-c21-data-analysis-report-writer-app-bxvkvg.streamlit.app/](https://adityasingh6533-c21-data-analysis-report-writer-app-bxvkvg.streamlit.app/) | Open in a second browser tab for the live demo part. |
| **GitHub Repository** | [https://github.com/adityasingh6533/C21-Data-Analysis-Report-Writer](https://github.com/adityasingh6533/C21-Data-Analysis-Report-Writer) | Open to show commit history and changelog. |

---

## ⏱️ Second-by-Second Teleprompter Script

---

### [0:00 – 0:15] Part 1: The Problem & The LLM Math Trap (~15s)
* **What to Show on Screen**: Slide 1 of `presentation/reel_presentation.html` (Title & Problem Cards).
* **English Voiceover**:
  > *"If you paste a spreadsheet into ChatGPT and ask for the average, it won't calculate it—it guesses it. In quantitative data, probabilistic next-token prediction causes silent, dangerous mathematical hallucinations. We built **VeriSight AI** for Problem ID C21: a tool-assisted system that eliminates math hallucinations and translates raw CSV datasets into verified executive reports and charts."*
* **Hinglish Alternative (Agar Hindi me bolna ho)**:
  > *"Agar aap koi raw CSV spreadsheet directly ChatGPT me daal kar average ya trend poochenge, toh woh calculate nahi karta—guess karta hai. Tabular data me LLM mental math hallucination karta hai. Isi problem ko solve karne ke liye humne banaya **VeriSight AI** for Problem ID C21."*

---

### [0:15 – 0:50] Part 2: The Prompt Experiment — Before vs. After (~35s)
* **What to Show on Screen**: Slide 2 (Prompt Evolution v1 vs v2 vs v3) and Slide 3 (4-Stage Pipeline).
* **English Voiceover**:
  > *"In our prompt iteration experiment:
  > In **Version 1.0 Baseline**, naive zero-shot prompting scored only 41.5%. On a 35-row retail sales dataset, it completely missed an $18,750 enterprise outlier and hallucinated the average revenue as $340.50—a 63% calculation error!
  > In **Version 2.0 Structured**, we added a Senior Data Journalist persona and negative constraints. That lifted the score to 75.5%, but correlation estimation still drifted due to cognitive overload.
  > In **Version 3.0**, we decoupled arithmetic into a deterministic Python profiler and built a 4-stage chained pipeline. Stage 1 explores anomalies, Stage 2 writes executive prose, Stage 3 generates Grammar of Graphics chart JSON, and Stage 4 audits every single number against ground truth.
  > This lifted our benchmark score to **98.9% and achieved 100% numerical faithfulness with zero hallucinations**."*
* **Hinglish Alternative**:
  > *"Hamare prompt experiment me:
  > Version 1 baseline naive prompt ne average revenue $340 guess kiya jabki ground-truth $920 tha—ek 63% ka critical math hallucination!
  > Version 2 me role aur constraints dene par formatting sudhri, par cognitive overload raha.
  > Version 3 me humne calculation ko Python profiler me alag kiya aur 4-stage chained prompt pipeline banayi. Stage 4 har ek number ko ground truth se cross-check karta hai. Isse hamara score 41% se seedha **98.9% pahuch gaya with 100% accuracy**!"*

---

### [0:50 – 1:35] Part 3: Working Live Demo (~45s)
* **What to Show on Screen**: Switch tab to the live Streamlit Web App ([Deployed Streamlit Link](https://adityasingh6533-c21-data-analysis-report-writer-app-bxvkvg.streamlit.app/)).
* **Actions on Screen**:
  1. Show sidebar: Select *"Retail Sales & Bulk Outlier (35 rows)"* and click **"Run VeriSight Pipeline"**.
  2. Tab 1: Scroll through the **Verified Executive Narrative Report** and point cursor at the green badge: `100% Verified Against Ground Truth`. Show the interactive Plotly bar and scatter charts.
  3. Tab 2: Click **Tab 2 (Chain Inspector)** and expand Stage 4 Auditor to show `EXACT_MATCH` ledger.
  4. Tab 4: Click **Tab 4 (Evaluation)** and show the grouped comparison bar chart (v1 vs v2 vs v3).
* **English Voiceover**:
  > *"Here is VeriSight AI running live on Streamlit Cloud.
  > In Tab 1, we see the executive narrative: typical orders center around $360 median, while the $18,750 bulk outlier is cleanly flagged without distorting typical operations. Plotly charts render dynamically from Stage 3's JSON specifications.
  > In Tab 2, evaluators can inspect intermediate artifacts for all 4 stages live. Notice Stage 4: it audited 7 numerical claims and verified every single one with zero hallucinations.
  > In Tab 4, our empirical evaluation across 9 experiments proves the +57% performance lift across all 3 benchmark datasets."*
* **Hinglish Alternative**:
  > *"Yeh hamari live Streamlit application hai.
  > Tab 1 me executive report generate hui hai jisme 100% verified badge hai. Typical median $360 hai aur $18,750 ka outlier cleanly call out hua hai. Plotly charts dynamically render ho rahe hain.
  > Tab 2 me aap 4-stage pipeline ke saare intermediate JSON aur prompts dekh sakte hain. Stage 4 fact-checker ne saare numbers ko exact match verify kiya hai.
  > Aur Tab 4 me hamare 9 benchmark experiments ka quantitative comparison chart hai."*

---

### [1:35 – 1:55] Part 4: Progress & Milestone 3 Roadmap (~20s)
* **What to Show on Screen**: Switch back to Slide 6 (`reel_presentation.html` Slide 6: Milestone 2 Status & Roadmap).
* **English Voiceover**:
  > *"For Milestone 2, our deliverables are fully complete: a deployed cloud prototype, versioned prompts v1 to v3, a 12-case test suite with edge cases, and client-side PII privacy masking.
  > For Milestone 3, we plan to expand from single CSVs to multi-table relational SQL joins, add dynamic PowerPoint report export, and explore real-time conversational querying with the Gemini Live API.
  > VeriSight AI: Putting prompt engineering and deterministic verification at the heart of automated data analysis. Thank you!"*
* **Hinglish Alternative**:
  > *"Milestone 2 ke liye hamara live prototype, 4-stage prompt chain, 12 test cases aur PII masking fully complete hai. Milestone 3 me hum multi-table SQL joins aur Gemini Live voice querying add karenge. Thank you!"*

---

## ⏱️ Final Video Time Check
| Segment | Start Time | End Time | Duration |
| :--- | :---: | :---: | :---: |
| Part 1: Problem & Hook | 0:00 | 0:15 | **15 sec** |
| Part 2: Prompt Experiment | 0:15 | 0:50 | **35 sec** |
| Part 3: Live Working Demo | 0:50 | 1:35 | **45 sec** |
| Part 4: Progress & Roadmap | 1:35 | 1:55 | **20 sec** |
| **TOTAL RUNTIME** | | | **~115 Seconds** ✅ *(Perfect: 90s < 115s < 150s)* |

---

## 🎥 Recording Instructions (3 Easy Steps)
1. **Tool to Record**: Press **`Windows Key + Alt + R`** (built-in Windows Game Bar screen recorder) or use **OBS Studio** / **Loom**.
2. **Browser Setup**:
   - Tab 1: `presentation/reel_presentation.html` (Press **F11** for fullscreen).
   - Tab 2: Your deployed Streamlit app ([Link](https://adityasingh6533-c21-data-analysis-report-writer-app-bxvkvg.streamlit.app/)).
3. **Record & Upload**:
   - Click the timer button `▶` on the slide topbar to watch the elapsed seconds.
   - Speak clearly following the script above.
   - Upload the resulting `.mp4` file to **Google Drive** or **YouTube (Unlisted)**.
   - Verify sharing is set to **"Anyone with the link can view"**.
   - Enter the exact seconds (e.g. `115`) in Question 14 of the Microsoft Form!
