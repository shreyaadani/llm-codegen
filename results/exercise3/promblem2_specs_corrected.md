# Problem 2 – matrix_transpose Specification Analysis

## Raw LLM-Generated Assertions

Stored in: `results/exercise3/problem2_specs_raw.txt`

---

## Correctness Review

| #   | Assertion Summary                                                  | Correct? | Notes / Corrections                                                     |
| --- | ------------------------------------------------------------------ | -------- |----------------------------------------------------------------------- |
| 1   | Takes list of lists and returns list of lists                      | ✔        | –                                                                       |
| 2   | Each returned row represents one column of the input               | ✔        | –                                                                       |
| 3   | Value at (i, j) in input appears at (j, i) in output               | ✔        | Core transpose definition                                               |
| 4   | #rows(out) = #cols(in), assuming equal-length rows                 | ✔        | –                                                                       |
| 5   | #cols(out) = #rows(in)                                             | ✔        | –                                                                       |
| 6   | [] → []                                                            | ✔        | –                                                                       |
| 7   | One row of n elements → n rows of length 1                         | ✔        | –                                                                       |
| 8   | n rows of length 1 → one row of n elements                         | ✔        | –                                                                       |
| 9   | Rectangular matrices transpose to swapped rectangular dimensions   | ✔        | –                                                                       |
| 10  | Order within each returned row preserves the original column order | ✔        | –                                                                       |
| 11  | Must not modify input; all returned rows newly constructed         | ✖        | Over-specifies “newly constructed sequences”. See corrected spec below. |
| 12  | `[[]]` → [] via Python’s standard transpose semantics              | ✔        | –                                                                       |
| 13  | Jagged rows → `zip`-style truncation to shortest row               | ✖        | Behavior for ragged rows is not specified in the original problem.      |
| 14  | No additional elements beyond those in the input                   | ✔        | –                                                                       |
| 15  | Elements appear in an order consistent with row/column swap        | ✔        | –                                                                       |

---

## Corrected Versions for Incorrect Assertions

### Assertion 11 – Corrected

**Original:**

> The function must not modify the input matrix; all returned rows must be newly constructed sequences.

**Corrected:**

> The function must not modify the contents of `matrix` in place; it should return a separate matrix representing the transpose.

---

### Assertion 13 – Corrected

**Original:**

> If any row in the input matrix differs in length from others, the function’s behavior is consistent with Python's handling of such structures when transposing via `zip`, producing rows only up to the shortest row length.

**Corrected:**

> The intended inputs are well-formed matrices where all non-empty rows have the same length; behavior for ragged (unequal-length) rows is unspecified.

---

## Accuracy Score

- **Correct as written:** 13
- **Incorrect / over-specified:** 2
- **Accuracy:** **13 / 15 ≈ 86.7%**

The LLM produced mostly accurate specifications, but added some assumptions about implementation details (newly constructed rows, behavior on ragged matrices) that were not explicitly guaranteed by the original problem description.
