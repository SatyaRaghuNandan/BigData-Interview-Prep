This Python code correctly checks whether a list of integers is **monotonic**, i.e., whether it is either:

* **Monotonically increasing** (non-decreasing), or
* **Monotonically decreasing** (non-increasing)

---

## ✅ Code Explanation (Line by Line)

```python
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_inc = True  # ✅ Assume list is increasing
        is_dec = True  # ✅ Also assume list is decreasing

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                is_dec = False  # ❌ Found an increasing pair — not decreasing
            if nums[i] < nums[i - 1]:
                is_inc = False  # ❌ Found a decreasing pair — not increasing

            if not is_inc and not is_dec:
                return False  # ❌ Violates both increasing and decreasing

        return True  # ✅ Passed all checks
```

---

## ✅ Time and Space Complexity

| Aspect              | Complexity | Reason                       |
| ------------------- | ---------- | ---------------------------- |
| ⏱ Time Complexity   | `O(N)`     | One pass through the array   |
| 🧠 Space Complexity | `O(1)`     | Constant space for two flags |

---

## ✅ Examples and Dry Run

### Example 1:

```python
nums = [1, 2, 2, 3]
→ is_inc = True, is_dec = False
→ Output: True
```

### Example 2:

```python
nums = [6, 5, 4, 4]
→ is_inc = False, is_dec = True
→ Output: True
```

### Example 3:

```python
nums = [1, 3, 2]
→ is_inc = False, is_dec = False
→ Output: False
```

### Example 4 (Edge case):

```python
nums = [1]
→ Single element → trivially monotonic
→ Output: True
```

---

## ✅ How to Explain in an Interview

> “I use two flags to track whether the list is non-decreasing or non-increasing. As I iterate, if I find a pair that violates either condition, I update the corresponding flag. If both flags are false at any point, the list is not monotonic. This runs in `O(N)` time and uses `O(1)` space.”

---

Let me know if you want:

* A Java version
* A follow-up that returns **which type** of monotonicity (increasing/decreasing/constant)
* Or a stricter variant (strictly increasing/decreasing only)
