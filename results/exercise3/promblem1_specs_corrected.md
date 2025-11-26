# Problem 1 – longest_word Specification Analysis

## Raw LLM-Generated Assertions

Stored in: `results/exercise3/problem1_specs_raw.txt`

---

## Correctness Review

| #   | Assertion Summary                       | Correct?  | Notes / Corrections |
| --- | --------------------------------------- | --------- | ------------------- |
| 1   | Function takes str → returns str        | ✔ Correct | –                   |
| 2   | Word = contiguous run of letters/digits | ✔ Correct | –                   |
| 3   | Non-alphanumeric characters break words | ✔ Correct | –                   |
| 4   | Must return a longest alphanumeric word | ✔ Correct | –                   |
| 5   | Tie-breaking: any longest allowed       | ✔ Correct | –                   |
| 6   | Returned word length = max word length  | ✔ Correct | –                   |
| 7   | Word must appear contiguously in input  | ✔ Correct | –                   |
| 8   | Empty sentence → return ""              | ✔ Correct | –                   |
| 9   | No alphanumeric chars → return ""       | ✔ Correct | –                   |
| 10  | One alphanumeric word → return that     | ✔ Correct | –                   |
| 11  | No non-alphanumeric chars in result     | ✔ Correct | –                   |
| 12  | Case preserved                          | ✔ Correct | –                   |
| 13  | Digits allowed in words                 | ✔ Correct | –                   |
| 14  | Mixed alphanumeric sequences allowed    | ✔ Correct | –                   |

---

## Accuracy Score

- **Correct:** 14
- **Incorrect:** 0
- **Accuracy:** **100%**

All LLM-generated assertions were consistent with the original specification. No corrections were required.

---
