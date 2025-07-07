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




Absolutely! Below is the **Java version** of the **Previous Permutation** algorithm — the **reverse counterpart** of LeetCode 31's **Next Permutation** — with:

✅ Telugu-style inline comments (transliterated)
✅ `O(n)` time and `O(1)` space complexity
✅ Full main class with test cases for demonstration

---

## ✅ Java Implementation: Previous Permutation (with Telugu Comments)

```java
import java.util.Arrays;

public class Solution {
    public void previousPermutation(int[] nums) {
        int n = nums.length;
        int peak = -1;

        // Step 1: Right to Left lo chusi, first decreasing element ni identify cheyyali
        // Condition: nums[i-1] > nums[i]
        for (int i = n - 1; i > 0; i--) {
            if (nums[i - 1] > nums[i]) {
                peak = i - 1;
                break;
            }
        }

        // Step 2: If peak not found ante → already smallest permutation → reverse to get largest
        if (peak == -1) {
            reverse(nums, 0, n - 1);
            return;
        }

        // Step 3: Right side lo smallest element find cheyyali which is < nums[peak]
        int nextLower = n - 1;
        while (nums[nextLower] >= nums[peak]) {
            nextLower--;
        }

        // Step 4: Swap nums[peak] and nums[nextLower]
        swap(nums, peak, nextLower);

        // Step 5: Reverse the suffix (peak+1 to end) to get largest possible suffix
        reverse(nums, peak + 1, n - 1);
    }

    // Swap helper method
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    // Reverse helper method
    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start++, end--);
        }
    }

    // Main method with test cases
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] testCases = {
            {1, 2, 3},          // → [3, 2, 1]
            {3, 2, 1},          // → [3, 1, 2]
            {1, 1, 5},          // → [5, 1, 1]
            {1},                // → [1]
            {1, 5, 1},          // → [1, 1, 5]
            {3, 1, 2},          // → [2, 3, 1]
            {2, 3, 1},          // → [2, 1, 3]
            {1, 2, 3, 6, 5, 4}, // → [1, 2, 3, 6, 4, 5]
            {2, 4, 3, 2, 1}     // → [2, 4, 3, 1, 2]
        };

        for (int i = 0; i < testCases.length; i++) {
            int[] input = testCases[i];
            System.out.println("Test Case " + (i + 1) + ": Input = " + Arrays.toString(input));
            sol.previousPermutation(input);
            System.out.println("          Previous Permutation = " + Arrays.toString(input));
            System.out.println();
        }
    }
}
```

---

## ✅ Example Output (Expected)

```
Test Case 1: Input = [1, 2, 3]
          Previous Permutation = [3, 2, 1]

Test Case 2: Input = [3, 2, 1]
          Previous Permutation = [3, 1, 2]

Test Case 3: Input = [1, 1, 5]
          Previous Permutation = [5, 1, 1]

...
```

---

## ✅ Time & Space Complexity

| Metric             | Value  |
| ------------------ | ------ |
| Time Complexity    | `O(n)` |
| Space Complexity   | `O(1)` |
| In-place operation | ✅      |

---

## ✅ Summary: Previous vs. Next Permutation

| Feature             | Next Permutation        | Previous Permutation    |
| ------------------- | ----------------------- | ----------------------- |
| Pivot condition     | `nums[i-1] < nums[i]`   | `nums[i-1] > nums[i]`   |
| Swap candidate      | First element > pivot   | First element < pivot   |
| Post-swap operation | Reverse suffix (to min) | Reverse suffix (to max) |
| Goal                | Get next greater perm   | Get next smaller perm   |

---

Would you like:

* ✅ A version that **returns** the array instead of modifying in-place?
* ✅ A function to generate the **k-th previous permutation**?
* ✅ Full suite of **unit tests** with JUnit?

Let me know — I’ll help with the next step!
