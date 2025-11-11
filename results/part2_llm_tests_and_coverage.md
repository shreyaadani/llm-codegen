# Part 2 – LLM-Assisted Test Generation & Coverage Improvement

## Problem 1 – longest_word (task6.py)

**Baseline coverage (iteration 0):**

- Line: 80%
- Branch: 80%

### Prompts Used

#### Prompt 1

````text
[### Prompt 1 (for longest_word tests)

```text
You are an expert Python developer and tester.

I have a Python function `longest_word(sentence: str) -> str` that returns the longest alphanumeric word in a sentence.
- Punctuation should be ignored (e.g., "word!" counts as "word").
- If the sentence has no words (empty string or only punctuation), it should return the empty string "".

Write additional `pytest` unit tests that increase **branch coverage** for this function. In particular, cover:
- Empty string input.
- String containing only punctuation.
- Sentences with multiple words tied for longest length (ensure behavior is consistent).
- Sentences containing words with digits.
- Sentences with irregular spacing (multiple spaces, leading/trailing spaces).

Constraints:
- Assume the function is imported as: `from tasks_gpt.task6 import longest_word`.
- Output only Python `pytest` test functions (no explanations, comments, or print statements).
- Use unique test function names that do not clash with existing tests.
]
````

##### Prompt 2

```text
[### Prompt 2 (for matrix_transpose)
You are an expert Python developer and tester.

I have a Python function `matrix_transpose(matrix)` that returns the transpose of a 2D list (matrix).
Each row in the input is a list. The function should:
- Correctly transpose rectangular matrices (more rows than columns and vice versa).
- Handle a single row and a single column.
- Handle an empty matrix [] and a matrix with empty rows like [ [] ] in a well-defined way.

Write additional `pytest` unit tests that increase branch coverage for this function by covering:
- Empty matrix input.
- 1xN and Nx1 matrices.
- Non-square rectangular matrices (e.g., 2x3, 3x2).
- Matrices containing negative numbers and zeros.

Constraints:
- Assume the function is loaded as:
    from conftest import load_func
    matrix_transpose = load_func(8, "matrix_transpose")
- Do NOT redefine `load_func` in the tests.
- Output only Python `pytest` test functions (no explanations, comments, or print statements).
- Use unique test names that do not clash with existing tests.
]

\# Part 2 – LLM-Assisted Test Generation & Coverage Improvement

## Problem 1 – longest_word (task6.py)

Baseline coverage (line 80 %, branch 80 %)

| Iteration | Description               | Line % | Branch % | Notes                                                   |
| --------- | ------------------------- | ------ | -------- | ------------------------------------------------------- |
| 0         | Baseline (original tests) | 80     | 80       | Only 3 instructor tests                                 |
| 1         | After LLM tests v1        | 93     | 93       | Added empty, punctuation-only, digit, and spacing cases |

Iteration 1 added five LLM-generated tests targeting empty input, punctuation-only strings,
words containing digits, and irregular spacing. This raised coverage from 80% to 93% by exercising
branches that were previously untested in edge-case handling.

## Problem 2 – matrix_transpose (task8.py)
Baseline coverage (line 67 %, branch 67 %)

| Iteration | Description                  | Line % | Branch % | Notes                                            |
|-----------|------------------------------|--------|----------|--------------------------------------------------|
| 0         | Baseline (original tests)    | 67     | 67       | Only 2 basic shape tests (square, rectangular)   |
| 1         | After LLM tests v1           | 100    | 100      | Added empty, 1xN, Nx1, rectangular, negatives/0s |

```

Iteration 1 added five LLM-generated tests that covered edge cases for the transpose:
empty matrix, single-row (1xN), single-column (Nx1), non-square rectangular matrices, and
matrices containing negative numbers and zeros. This raised coverage from 67% to 100% by
exercising all remaining branches in the implementation.

##### Redundancy and De-duplication

For both `longest_word` and `matrix_transpose`, the LLM sometimes produced tests that were
semantically similar to existing ones (e.g., additional cases with the same input pattern but
different test names). I kept tests that introduced new inputs, new shapes, or new edge cases,
and removed near-duplicates where the input and expected output were identical to existing tests.
This kept the suite compact while still improving branch coverage.

```

```
