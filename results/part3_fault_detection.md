# Part 3 – Fault Detection Check

## Problem 1 – longest_word (task6.py)

## Problem 1 – longest_word (task6.py)

- **Bug description:** I modified the implementation so that the regex only matches alphabetic characters (`[A-Za-z]+`) instead of alphanumeric (`[A-Za-z0-9]+`). As a result, digits are no longer treated as part of words, and words like `"c333"` are mis-handled.
- **Why realistic:** This is a common kind of bug where a developer forgets to include digits (or other characters) in tokenization logic. The function still works for many normal sentences, but fails on inputs with digits.
- **Result:** After introducing the bug and running `pytest -q`, the test `test_longest_word_with_digits_extra` (and any other digit-based tests) failed, because the function no longer returns `"c333"` as the longest word.
- **Conclusion (coverage ↔ fault detection):** The increased branch/edge coverage from Part 2 (especially tests targeting words with digits) directly enabled the test suite to catch this bug. With only the original three tests, this bug would likely have gone undetected, even though line coverage was already high.

---

## Problem 2 – matrix_transpose (task8.py)

- **Bug description:** I modified the implementation so that when the input matrix is `[]`, the function returns `[[]]` instead of `[]`. For all non-empty matrices, it still calls the normal transpose logic.
- **Why realistic:** Special-case handling for empty inputs is a common source of bugs: a developer might return the wrong shape or structure while trying to be “helpful.” The function continues to work for normal shapes (1xN, Nx1, rectangular), so the bug only appears on a specific edge case.
- **Result:** After introducing the bug and running `pytest -q`, the test `test_matrix_transpose_empty_matrix_extra` failed because it expected `[]` but received `[[]]`. All other transpose tests still passed, showing that the defect is localized to the empty-matrix branch.
- **Conclusion (coverage ↔ fault detection):** The original tests did not include an empty-matrix case, so this bug would not have been caught with only the baseline suite. The LLM-generated tests from Part 2 increased coverage on edge branches (including the empty-input path), which enabled the suite to detect this bug.
