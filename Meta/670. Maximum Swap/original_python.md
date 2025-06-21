Here's the **complete and detailed Python solution** for the **original problem** [LeetCode 670: Maximum Swap](https://leetcode.com/problems/maximum-swap/), including:

* ✅ Telugu comments (transliterated)
* ✅ Time and space complexity analysis
* ✅ Edge case handling
* ✅ A working `__main__` method with test cases

---

## ✅ Problem Summary

> Given a non-negative integer, you can swap two digits **at most once** to get the **maximum possible number**. Return the maximum number you can get.

---

## ✅ Final Python Code with Telugu Comments

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        # 📌 Step 1: Number ni list of characters ga convert cheyyadam
        n = list(str(num))

        # 🗺️ Step 2: Prati digit ki last/right-most index ni store cheyyadam
        right_most = [-1] * 10
        for i, digit in enumerate(n):
            right_most[int(digit)] = i

        # 🔁 Step 3: Left to right traverse cheyyadam
        for i, digit in enumerate(n):
            curr_digit = int(digit)

            # 💡 9 to curr_digit+1 varaku check cheyyadam — right side lo bigger digit vundha ani
            for d in range(9, curr_digit, -1):
                if right_most[d] > i:
                    # 🔄 Swap bigger digit with current digit
                    n[i], n[right_most[d]] = n[right_most[d]], n[i]

                    # 🔚 Final result ni int ga convert cheyyadam
                    return int("".join(n))

        # 😐 No beneficial swap possible → original number return cheyyadam
        return num
```

---

## ✅ Time and Space Complexity

| Metric              | Value  | Explanation                               |
| ------------------- | ------ | ----------------------------------------- |
| **Time Complexity** | `O(n)` | - One pass to build `right_most` → `O(n)` |

```
                               - Two nested loops → outer = `n`, inner = 10 → total = `O(n)` |
```

\| **Space Complexity**| `O(n)`       | - String to list conversion → `O(n)`
\- `right_most` array is fixed size → `O(1)` auxiliary |

> ✅ So overall:
> **Time:** `O(n)`
> **Space:** `O(n)` (due to digit list), but **`O(1)` auxiliary**

---

## ✅ Edge Cases

| Case | Input  | Output | Explanation      |
| ---- | ------ | ------ | ---------------- |
| 1    | `2736` | `7236` | Swap `2` and `7` |
| 2    | `9973` | `9973` | Already max      |
| 3    | `0`    | `0`    | Only one digit   |
| 4    | `9`    | `9`    | Already max      |
| 5    | `1993` | `9913` | Swap `1` and `9` |

---

## ✅ Testable `__main__` Method

```python
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (2736, 7236),
        (9973, 9973),
        (0, 0),
        (9, 9),
        (1993, 9913),
        (98368, 98863),  # Swap 3 and 8
        (123456, 623451),  # Swap 1 and 6
        (321, 321),  # Already max
    ]

    for i, (input_num, expected) in enumerate(test_cases):
        result = solution.maximumSwap(input_num)
        print(f"Test Case {i+1}: Input = {input_num}")
        print(f"Expected: {expected}")
        print(f"Result:   {result}")
        print("✅ Passed\n" if result == expected else "❌ Failed\n")
```

---

## 🧠 Summary

* Greedy logic: Always look for the **biggest digit on the right** of current digit to **swap** and maximize the result.
* One swap is allowed.
* Best case: Early swap.
* Worst case: No swap needed.

Let me know if you want to **visualize this as a dry run**, or convert this to **Java with Telugu comments**!
