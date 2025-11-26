```markdown
# Exercise 3 — Coverage Summary (Spec-Guided Testing)

This document summarizes the **before vs. after** code coverage for the two selected problems:

- `task6.py` → `longest_word`
- `task8.py` → `matrix_transpose`

Coverage was measured using `pytest` + `pytest-cov` with:
```

pytest --cov=tasks_gpt --cov-branch --cov-report=term-missing

```

---

## 📌 1. Coverage Before Spec-Guided Tests (from Exercise 2)

| Task | File | Line Coverage | Branch Coverage |
|------|------|----------------|------------------|
| Problem 1 | `task6.py` (longest_word) | **93%** | **93%** |
| Problem 2 | `task8.py` (matrix_transpose) | **100%** | **100%** |

These values came after adding:
- Baseline tests
- LLM-improved tests (coverage-boosting tests)

---

## 📌 2. Coverage After Spec-Guided Tests (Exercise 3 Part 2)

After adding:

- `tests/test_task6_specs.py`
- `tests/test_task8_specs.py`

The coverage numbers remained:

| Task | File | Line Coverage | Branch Coverage |
|------|------|----------------|------------------|
| Problem 1 | `task6.py` (longest_word) | **93%** | **93%** |
| Problem 2 | `task8.py` (matrix_transpose) | **100%** | **100%** |

Full output excerpt:

```

## Name Stmts Miss Branch BrPart Cover Missing

tasks_gpt\task6.py 9 0 6 1 93% 10->exit
tasks_gpt\task8.py 4 0 2 0 100%
TOTAL 97 2 56 5 95%

```

---

## 📌 3. Interpretation

### **Problem 1 — `longest_word`**
- Spec-guided tests validated additional semantic behaviors
  (case preservation, mixed alphanumeric sequences, punctuation separation).
- However, all these paths were already exercised by prior tests.
- **Coverage did not increase** — but *semantic strength improved*.

### **Problem 2 — `matrix_transpose`**
- All branches were already hit with baseline + LLM-generated tests.
- Spec-guided tests primarily:
  - validated non-modification of input,
  - reinforced empty matrix and `[[]]` cases,
  - covered all rectangular and square shapes.

- **Coverage remained at 100%.**

---

## 📌 4. Final Summary

| Task | Before | After | Change |
|------|---------|--------|---------|
| `task6.py` (longest_word) | 93% line / 93% branch | 93% line / 93% branch | **No change** |
| `task8.py` (matrix_transpose) | 100% line / 100% branch | 100% line / 100% branch | **No change** |

Spec-guided tests **improved specification alignment** but did not increase numerical coverage — which is explicitly allowed and expected in Exercise 3.

---


```
