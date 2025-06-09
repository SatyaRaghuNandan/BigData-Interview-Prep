Excellent! You're implementing the **Previous Permutation** algorithm — a reverse counterpart of LeetCode 31’s **Next Permutation**, and it’s perfectly structured.

Below is a **fully annotated version** with:

1. ✅ Telugu-style comments (transliterated in English)
2. ✅ Time and space complexity breakdown
3. ✅ Summary of differences between next and previous permutation

---

## ✅ Annotated Python Code with Telugu Comments

```python
class Solution:
    def previousPermutation(self, nums: list[int]) -> None:
        peak = None  # Index of the first 'peak' from the right

        # Step 1: Identify first element from right where nums[i-1] > nums[i]
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] > nums[i]:
                peak = i - 1
                break  # idi manaki swap cheyyalsina index

        # Step 2: If no peak found, ante current permutation is smallest → reverse to get largest
        if peak is None:
            nums.reverse()
            return

        # Step 3: Find the next smaller element to the right of peak
        next_lower = len(nums) - 1
        while nums[next_lower] >= nums[peak]:
            next_lower -= 1

        # Step 4: Swap nums[peak] and nums[next_lower]
        nums[peak], nums[next_lower] = nums[next_lower], nums[peak]

        # Step 5: Reverse the suffix after peak to get largest possible suffix
        left = peak + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

---

## 🧠 Telugu Explanation (Transliterated)

```text
- manaki previous permutation ante lexicographically mundu ochche arrangement kavali.
- So, last nunchi munde chusthu, first break (nums[i-1] > nums[i]) ni identify cheyyali.
- Daaniki right side lo immediate smaller value ni find chesi swap cheyyali.
- Tarvata aa peak ki right lo unna part ni reverse cheyyadam valla manaki biggest suffix vastadi.
```

---

## 🧪 Sample Walkthrough

```python
nums = [1, 2, 3] 
→ previousPermutation → [3, 2, 1]

nums = [3, 2, 1] 
→ previousPermutation → [3, 1, 2]
```

---

## ⏱️ Time and Space Complexity

| Metric               | Value  |
| -------------------- | ------ |
| **Time Complexity**  | `O(n)` |
| **Space Complexity** | `O(1)` |

* One backward scan to find peak → `O(n)`
* One scan to find next lower → `O(n)` worst case
* One in-place reverse → `O(n)` worst case
* Total: **Linear time, constant space**

---

## 🔄 Difference vs Next Permutation

| Feature              | Next Permutation           | Previous Permutation           |
| -------------------- | -------------------------- | ------------------------------ |
| Condition            | `nums[i-1] < nums[i]`      | `nums[i-1] > nums[i]`          |
| Find element to swap | Next greater than pivot    | Next smaller than pivot        |
| Reverse suffix       | To get **smallest** suffix | To get **largest** suffix      |
| Lexicographic goal   | Next permutation (larger)  | Previous permutation (smaller) |

---

Let me know if you'd like:

* A generator to get **all permutations in reverse order**
* Extension to **k-th previous permutation**
* A **visual representation** of step-by-step transformation
