Great! You're sharing a clean and efficient implementation of **LeetCode 31: Next Permutation**.

Let’s break down the full logic of the code with **detailed Telugu-style comments**, and a **step-by-step explanation** of how it finds the next lexicographical permutation in-place.

---

## ✅ Problem Statement (Summary)

> Modify the given list of integers to produce the **next lexicographical permutation**. If such a permutation is not possible (i.e., it's the highest), rearrange to the **lowest possible (sorted in ascending)**.

---

## 🧠 Core Idea:

### Next Permutation Logic:

1. Traverse from **right to left** and find the **first decreasing element** (pivot).
2. Find the **smallest number greater than that pivot** to the right.
3. **Swap them**.
4. **Reverse** the part to the right of the pivot (to make it smallest possible).

---

## ✅ Python Code with Telugu Comments (Transliterated)

```python
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        valley = None

        # Step 1: End nunchi left ki iterate cheyyadam
        # First decreasing element ni identify cheyyali
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                valley = i - 1
                break

        # Step 2: Already highest permutation unte → reverse to lowest
        if valley is None:
            nums.reverse()
            return

        # Step 3: Right lo smallest number find cheyyali which is > nums[valley]
        next_higher = len(nums) - 1
        while nums[next_higher] <= nums[valley]:
            next_higher -= 1

        # Step 4: Swap them
        nums[valley], nums[next_higher] = nums[next_higher], nums[valley]

        # Step 5: Reverse the suffix (valley+1 to end)
        left = valley + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1



def main():
    solution = Solution()

    test_cases = [
        [1, 2, 3],         # Simple ascending: next is [1, 3, 2]
        [3, 2, 1],         # Descending (highest): next is [1, 2, 3]
        [1, 1, 5],         # Duplicate values: next is [1, 5, 1]
        [1, 3, 2],         # Mixed: next is [2, 1, 3]
        [2, 3, 1],         # next is [3, 1, 2]
        [1],               # Single element → same
        [1, 5, 1],         # next is [5, 1, 1]
        [2, 4, 3, 2, 1],   # next is [3, 1, 2, 2, 4]
        [1, 2, 3, 6, 5, 4] # next is [1, 2, 4, 3, 5, 6]
    ]

    for idx, nums in enumerate(test_cases, start=1):
        original = nums[:]
        print(f"Test Case {idx}: Input = {original}")
        solution.nextPermutation(nums)
        print(f"            Next Permutation = {nums}\n")

if __name__ == "__main__":
    main()

```

---

## 🧪 Example

```python
nums = [1, 2, 3]
→ Output: [1, 3, 2]

nums = [3, 2, 1]
→ Output: [1, 2, 3]

nums = [1, 1, 5]
→ Output: [1, 5, 1]
```

---

## 🔍 Step-by-step Visual

### Example: `[1, 2, 3, 6, 5, 4]`

1. Find pivot: `3` (first decreasing from right)
2. Find next higher: `4`
3. Swap: `1, 2, 4, 6, 5, 3`
4. Reverse after pivot: `1, 2, 4, 3, 5, 6`

---

## ✅ Time & Space Complexity

| Metric    | Complexity |
| --------- | ---------- |
| **Time**  | `O(n)`     |
| **Space** | `O(1)`     |

* Done **in-place**, as required by the problem.

---

Let me know if you’d like:

* A **recursive version**
* To generate the **k-th next permutation**
* A **generator** for all permutations in order
