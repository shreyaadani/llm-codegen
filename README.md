````markdown
# 🧠 Prompting, Debugging, and Automated Testing for Code Generation with LLMs

**Author:** Shreyaa Jayant Dani  
**Course:** COMPSCI 520 / Prompting, Debugging, and Innovation for Code Generation  
**Date:** November 2025  
**Models:** GPT-4o (OpenAI) & Gemini 1.5 (Google DeepMind)

---

## 🎯 Overview

This repository combines two major experiments:

1. **Exercise 1 — Prompting & Self-Repair**  
   Generation and debugging of Python programs using two LLMs (GPT-4o and Gemini 1.5) on 10 MBPP-style tasks.
2. **Exercise 2 — Automated Testing & Coverage**  
   Measurement, improvement, and analysis of code coverage using `pytest-cov`, followed by LLM-assisted test generation and seeded-bug fault detection.

Together, these experiments evaluate how LLMs can generate correct programs **and** enhance software reliability through automated testing.

---

## 🧩 Project Structure

```basg

llm-codegen/
├── tasks_gpt/ # GPT-4o generated code (10 tasks)
├── tasks_gemini/ # Gemini 1.5 generated code
├── tests/ # Baseline + LLM-added tests
├── prompts/
│ ├── cot_prompts/ # CoT prompts (Exercise 1)
│ ├── self_repair_prompts/ # Self-repair prompts (Exercise 1)
│ └── llm_test_prompts/ # Test-generation prompts (Exercise 2)
├── scripts/
│ └── log_results.py # Evaluation & CSV logger
├── results/
│ ├── eval/ # Self-repair results (Exercise 1)
│ ├── baseline_coverage_summary.md
│ ├── part2_llm_tests_and_coverage.md
│ └── part3_fault_detection.md
├── cov_tasks_gpt\*/ # HTML/XML coverage reports (pytest-cov)
├── requirements.txt
└── README.md / report.pdf / Exercise2_ShreyaaDani.docx
```
````

---

## ⚙️ Environment Setup

```bash
# 1️⃣ Clone the repo
git clone https://github.com/shreyaadani/llm-codegen.git
cd llm-codegen

# 2️⃣ Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Running Evaluations (Exercise 1)

### ▶ Run GPT-4o results

```bash
pytest -q
```

### ▶ Run Gemini 1.5 results

```bash
$env:MODEL_DIR="tasks_gemini"
pytest -q
```

### ▶ Log aggregate results

```bash
python scripts/log_results.py
```

**Example CSV Output →** `results/eval/self_repair_results.csv`

```
ModelDir,Passed,Failed,Skipped,Errors,Total,PassPercent
tasks_gpt,30,0,0,0,30,100.0
tasks_gemini,30,0,0,0,30,100.0
```

---

## 🧮 Automated Coverage Analysis (Exercise 2)

### ▶ Baseline Coverage

Collect baseline coverage (Exercise 1 tests only):

```bash
pytest --cov=tasks_gpt --cov-branch \
  --cov-report=term-missing \
  --cov-report=html:cov_tasks_gpt \
  --cov-report=xml:cov_tasks_gpt.xml
```

### ▶ After LLM-Added Tests (Iteration 1 & 2)

```bash
pytest --cov=tasks_gpt --cov-branch \
  --cov-report=term-missing \
  --cov-report=html:cov_tasks_gpt_iter1 \
  --cov-report=xml:cov_tasks_gpt_iter1.xml

pytest --cov=tasks_gpt --cov-branch \
  --cov-report=term-missing \
  --cov-report=html:cov_tasks_gpt_iter2 \
  --cov-report=xml:cov_tasks_gpt_iter2.xml
```

### 📊 Coverage Results Summary

| Task               | Baseline Line % | After LLM Tests % | Δ Improvement                            | Notes |
| :----------------- | :-------------- | :---------------- | :--------------------------------------- | :---- |
| `longest_word`     | 80 → 93         | +13               | Added punctuation, digit, spacing cases  |       |
| `matrix_transpose` | 67 → 100        | +33               | Added empty, 1×N, Nx1, rectangular cases |       |

HTML reports are located in:
`cov_tasks_gpt/`, `cov_tasks_gpt_iter1/`, `cov_tasks_gpt_iter2/`

---

## 🧠 LLM Test Prompts

### Example — `longest_word (task6.py)`

```
You are an expert Python developer and tester.
Generate pytest tests to increase branch coverage for:
  - Empty strings
  - Punctuation-only input
  - Words with digits
  - Irregular spacing
```

### Example — `matrix_transpose (task8.py)`

```
Generate pytest tests for:
  - Empty matrix []
  - 1×N and Nx1 matrices
  - Rectangular matrices
  - Negative and zero values
```

All prompt files are saved in `prompts/llm_test_prompts/`.

---

## 🧩 Fault Detection (Exercise 2 Part 3)

After coverage convergence, two realistic bugs were seeded:

| Problem            | Bug Injected                                     | Failing Test                               | Finding                                      |
| :----------------- | :----------------------------------------------- | :----------------------------------------- | :------------------------------------------- |
| `longest_word`     | Regex changed to `[A-Za-z]+` (digits ignored)    | `test_longest_word_with_digits_extra`      | Bug detected → digit case coverage critical  |
| `matrix_transpose` | Returned `[[]]` instead of `[]` for empty matrix | `test_matrix_transpose_empty_matrix_extra` | Bug detected → empty input coverage critical |

These failures demonstrated a direct correlation between **branch coverage** and **fault detection** effectiveness.

---

## 📘 Reports & Deliverables

| Deliverable               | Location                                  |
| :------------------------ | :---------------------------------------- |
| Baseline Coverage Summary | `results/baseline_coverage_summary.md`    |
| LLM Test Iterations       | `results/part2_llm_tests_and_coverage.md` |
| Fault Detection Analysis  | `results/part3_fault_detection.md`        |
| HTML Reports              | `cov_tasks_gpt*/index.html`               |

---

## 📊 Results Highlights

| Metric             | Exercise 1 | Exercise 2        |
| :----------------- | :--------- | :---------------- |
| Pass Rate (GPT-4o) | 100 %      | –                 |
| Avg Coverage       | 93 %       | 95 % (↑ 2 %)      |
| Faults Detected    | –          | 2 / 2 seeded bugs |

---

## 🧾 Key Insights

- LLMs can assist not only in code generation but also in **test generation**.
- Branch coverage is a stronger indicator of fault detection than line coverage.
- Combining coverage tools with LLM-driven test synthesis creates a feedback loop for more robust software.

---

**GitHub Repository:** [github.com/shreyaadani/llm-codegen](https://github.com/shreyaadani/llm-codegen)
