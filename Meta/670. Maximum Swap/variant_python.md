Absolutely! Let's walk through the **detailed Python implementation** for the `buildSecondLargestNumber` problem, just like your original idea.

---

## ✅ **Problem Summary**

Given a list of digits, build the **second-largest possible number** by:

1. Sorting the digits in descending order to get the **maximum number**.
2. Swapping the **last unequal adjacent pair** (from right to left) to get the **next lower permutation**.
3. If all digits are equal (no swap can help), return an empty list.

---

## ✅ Python Code with Telugu Comments + Main Method

```python
from typing import List

class Solution:
    def buildSecondLargestNumber(self, num: List[int]) -> List[int]:
        # 📌 Edge case: list empty or okkate digit unte, second-largest possible kaadu
        if not num or len(num) <= 1:
            return []

        # 🧮 Step 1: 0 to 9 digits yokka frequency count cheyyadam
        freqs = [0] * 10
        for digit in num:
            freqs[digit] += 1

        # 🏗️ Step 2: largest number ni form cheyyadam using frequency
        largest = []
        for d in range(9, -1, -1):
            largest.extend([d] * freqs[d])

        # 🔁 Step 3: right nunchi left ki move avthu unequal adjacent digits unte swap cheyyadam
        for i in range(len(largest) - 1, 0, -1):
            if largest[i] != largest[i - 1]:
                # 🔄 Swap chesi break cheyyadam
                largest[i], largest[i - 1] = largest[i - 1], largest[i]
                return largest

        # ❌ Swap valla change cheyyatam ledu ante second largest undadu
        return []

# ✅ Main method for testing
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([2, 7, 3, 6], [7, 6, 2, 3]),
        ([1, 2, 1, 1, 1], [1, 2, 1, 1, 1]),
        ([5, 5, 5, 5], []),                        # all same digits
        ([0, 0, 0], []),                           # all zeroes
        ([1], []),                                 # single digit
        ([], []),                                  # empty list
        ([2, 3, 4, 1, 8], [8, 4, 3, 1, 2]),
        ([5, 9, 7, 6, 6, 3, 9, 6, 6], [9, 9, 7, 6, 6, 6, 6, 3, 5]),
        ([4, 4, 4, 4, 9, 9, 9, 9, 9], [9, 9, 9, 9, 4, 9, 4, 4, 4]),
        ([0, 0, 8, 4, 9, 9, 6, 7], [9, 9, 8, 7, 6, 0, 4, 0])
    ]

    for i, (input_digits, expected) in enumerate(test_cases):
        result = solution.buildSecondLargestNumber(input_digits)
        print(f"Test Case {i+1}: Input = {input_digits}")
        print(f"Expected: {expected}")
        print(f"Result:   {result}")
        print("✅ Passed\n" if result == expected else "❌ Failed\n")
```

---

## ✅ Time and Space Complexity

| Metric           | Value  | Notes                                     |
| ---------------- | ------ | ----------------------------------------- |
| Time Complexity  | `O(n)` | Counting + building + scanning            |
| Space Complexity | `O(n)` | Result list stores `n` digits             |
| Auxiliary Space  | `O(1)` | Only `10` size frequency array (constant) |

---

## ✅ Edge Cases Covered

| Input         | Output            | Reason                                  |
| ------------- | ----------------- | --------------------------------------- |
| `[1]`, `[]`   | `[]`              | Can't make a second number with 1 digit |
| `[5,5,5,5]`   | `[]`              | All digits same, no unequal pair        |
| `[0, 0, 0]`   | `[]`              | All zeroes                              |
| `[2,3,4,1,8]` | `[8, 4, 3, 1, 2]` | Valid swap creates second largest       |
| `[]`          | `[]`              | Empty input                             |

---

Let me know if you want to:

* Add support for **returning the number instead of list**
* Handle **k-th permutation variants**
* Make the solution fully **in-place** for interview contexts
