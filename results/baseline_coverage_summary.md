# Baseline Coverage Summary (Assignment 2 – Part 1)

| Problem ID | Problem Name     | File                | Tests Passed | Line % | Branch % | Notes                                     |
| ---------- | ---------------- | ------------------- | ------------ | ------ | -------- | ----------------------------------------- |
| 1          | min_cost_path    | tasks_gpt/task1.py  | 3/3          | 86%    | 86%      | A few DP path branches untested           |
| 2          | reverse_words    | tasks_gpt/task2.py  | 3/3          | 100%   | 100%     | Fully covered                             |
| 3          | sum_digits       | tasks_gpt/task3.py  | 3/3          | 100%   | 100%     | Fully covered                             |
| 4          | are_anagrams     | tasks_gpt/task4.py  | 3/3          | 100%   | 100%     | Fully covered                             |
| 5          | intersection     | tasks_gpt/task5.py  | 3/3          | 95%    | 95%      | One conditional branch partially covered  |
| 6          | longest_word     | tasks_gpt/task6.py  | 3/3          | 80%    | 80%      | Missing branch for empty-string edge case |
| 7          | is_subsequence   | tasks_gpt/task7.py  | 3/3          | 95%    | 95%      | Not all subsequence outcomes hit          |
| 8          | matrix_transpose | tasks_gpt/task8.py  | 3/3          | 67%    | 67%      | One main branch untested                  |
| 9          | unique_elements  | tasks_gpt/task9.py  | 3/3          | 100%   | 100%     | Fully covered                             |
| 10         | count_primes     | tasks_gpt/task10.py | 3/3          | 100%   | 100%     | Fully covered                             |

**Interpretation:**  
Average line coverage = 93 %. Branch coverage varied per problem.  
The weakest tasks (6 and 8) will be used in Part 2 for LLM-assisted test improvement.
