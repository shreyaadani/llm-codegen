# 🧠 Prompting, Debugging, and Innovation for Code Generation with LLMs

**Author:** Shreyaa Jayant Dani
**Course:** COMPSCI 520 : Prompting, Debugging, and Innovation for Code Generation
**Date:** October 22, 2025
**Models:** GPT-4o (OpenAI) & Gemini 1.5 (Google DeepMind)

---

## 🎯 Overview

This project explores how **Large Language Models (LLMs)** generate and repair Python code when guided through structured prompting workflows.

Students were required to:

- Use **two distinct LLM families** (GPT vs Gemini),
- Generate solutions for **10 MBPP-style programming tasks**,
- Apply **Chain-of-Thought** and **Self-Repair** prompting,
- Evaluate correctness via automated **unit tests**, and
- Analyze improvements after debugging.

All experiments were run locally in VS Code using `pytest`.

---

## 🧩 Project Structure

```
llm-codegen/
├── tasks_gpt/           # GPT-4o generated code (10 tasks)
├── tasks_gemini/        # Gemini 1.5 generated code (10 tasks)
├── tests/               # Unit tests for each task (3 per file)
├── prompts/             # Prompt templates (CoT + Self-Repair)
├── scripts/
│   └── log_results.py   # Evaluation & CSV logger
├── results/
│   └── eval/
│       └── self_repair_results.csv
├── requirements.txt
└── README.md / report.pdf
```

---

## ⚙️ Environment Setup

```bash
# 1. Clone the repo
git clone https://github.com/shreyaadani/llm-codegen.git
cd llm-codegen

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # (Windows PowerShell)

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 📘 Dataset of Tasks

---

All ten programming tasks, their function contracts, and associated concepts are documented in 10tasks.csv

## 🧪 Running Evaluations

### ▶ Run GPT-4o results

```bash
pytest -q
```

### ▶ Run Gemini 1.5 results

```bash
$env:MODEL_DIR="tasks_gemini"
pytest -q
```

### ▶ Log overall results to CSV

```bash
python scripts/log_results.py
```

CSV output example:

```
ModelDir,Passed,Failed,Skipped,Errors,Total,PassPercent
tasks_gpt,30,0,0,0,30,100.0
tasks_gemini,30,0,0,0,30,100.0
```

---

## 🧠 Prompting Strategies

### **1️⃣ Chain-of-Thought (CoT)**

Used for initial code generation.

```
You are an expert Python developer.
Think step by step and then output the correct code.

Task:
<function contract here>

Rules:
- Output only valid Python code
- No markdown, comments, or prints
```

### **2️⃣ Self-Repair**

Used to fix failing unit tests.

```
You are an expert Python debugger.
Fix the function so the failing unit test passes.

Rules:
- Keep the same function name & signature
- Make minimal changes
- Output only valid Python code
```

---

## 📊 Results Summary

| Model      | Baseline Pass    | After Self-Repair | Δ Improvement |
| :--------- | :--------------- | :---------------- | :------------ |
| GPT-4o     | 93.3 % (28 / 30) | 100 % (30 / 30)   | + 3.3 %       |
| Gemini 1.5 | 90 % (27 / 30)   | 100 % (30 / 30)   | + 10 %        |

Both models reached **100 % accuracy** after self-repair.

---

## 🔍 Debugging Case Studies

### **Task 4 — `are_anagrams()`**

- **Issue:** punctuation and case differences ignored.
- **Fix:** normalized inputs to lowercase alphanumerics.

```python
def are_anagrams(s1, s2):
    s1 = ''.join(c.lower() for c in s1 if c.isalnum())
    s2 = ''.join(c.lower() for c in s2 if c.isalnum())
    return sorted(s1) == sorted(s2)
```

### **Task 6 — `longest_word()`**

- **Issue:** punctuation (“ccc!”) counted as part of the word.
- **Fix:** regex tokenization to isolate alphanumeric runs.

```python
import re
def longest_word(sentence):
    words = re.findall(r"[A-Za-z0-9]+", sentence)
    return max(words, key=len) if words else ""
```

---

## 💡 Innovation: Self-Repair Prompting Loop

**Workflow**

1. Generate code with CoT.
2. Run unit tests.
3. Feed failing test & error trace back into the model.
4. Accept minimal patch if tests pass.

**Benefits**

- No API keys required.
- Works across model families.
- Fully reproducible using open-source tools.

---

## 🧾 Deliverables Checklist

| Deliverable                 | Location                                |
| --------------------------- | --------------------------------------- |
| Prompts (CoT + Self-Repair) | `/prompts/`                             |
| Generated Code (LLMs)       | `/tasks_gpt/`, `/tasks_gemini/`         |
| Unit Tests                  | `/tests/`                               |
| Evaluation Script           | `/scripts/log_results.py`               |
| Results CSV                 | `/results/eval/self_repair_results.csv` |
| Report / README             | `/README.md` and `report.pdf`           |

---

## 🏁 Key Takeaways

- Structured prompting can drastically improve LLM code correctness.
- Explicit error-aware feedback is an effective substitute for retraining.
- The method generalizes across different LLM families.

---

**GitHub Repository:** [github.com/shreyaadani/llm-codegen](https://github.com/shreyaadani/llm-codegen)

---
