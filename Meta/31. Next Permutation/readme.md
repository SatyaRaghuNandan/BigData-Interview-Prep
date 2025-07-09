
Here is your exact requested **Java version of Leetcode 31: Next Permutation** based on the Python version you shared, including:

✅ Telugu-style comments (transliterated)
✅ Clean helper methods (`swap`, `reverse`)
✅ Dry run test cases
✅ Time & space complexity
✅ Interview explanation

---

### ✅ Java Code: `nextPermutation` with Detailed Comments

```java
import java.util.Arrays;

public class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int valley = -1;

        // ✅ Step 1: Right nunchi left ki check cheyyadam
        // First decreasing index ni identify cheyyali (valley)
        for (int i = n - 1; i > 0; i--) {
            if (nums[i - 1] < nums[i]) {
                valley = i - 1;
                break;
            }
        }

        // 🛑 If no valley found ante array is in descending → highest permutation
        // So, just reverse the entire array to get the smallest permutation
        if (valley == -1) {
            reverse(nums, 0, n - 1);
            return;
        }

        // ✅ Step 2: Right side lo smallest number ni find cheyyali which is > nums[valley]
        int nextHigher = n - 1;
        while (nums[nextHigher] <= nums[valley]) {
            nextHigher--;
        }

        // ✅ Step 3: Swap valley and nextHigher
        swap(nums, valley, nextHigher);

        // ✅ Step 4: Reverse the suffix starting from valley + 1 to end
        reverse(nums, valley + 1, n - 1);
    }

    // Swap helper method
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    // Reverse helper method
    private void reverse(int[] nums, int left, int right) {
        while (left < right) {
            swap(nums, left++, right--);
        }
    }

    // --- Test Driver ---
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] testCases = {
            {1, 2, 3},         // ✅ Output: [1, 3, 2]
            {3, 2, 1},         // ✅ Output: [1, 2, 3]
            {1, 1, 5},         // ✅ Output: [1, 5, 1]
            {1, 3, 2},         // ✅ Output: [2, 1, 3]
            {2, 3, 1},         // ✅ Output: [3, 1, 2]
            {1},               // ✅ Output: [1]
            {1, 5, 1},         // ✅ Output: [5, 1, 1]
            {2, 4, 3, 2, 1},   // ✅ Output: [3, 1, 2, 2, 4]
            {1, 2, 3, 6, 5, 4} // ✅ Output: [1, 2, 4, 3, 5, 6]
        };

        for (int i = 0; i < testCases.length; i++) {
            int[] input = testCases[i];
            int[] copy = Arrays.copyOf(input, input.length);
            System.out.println("Test Case " + (i + 1) + ": Input = " + Arrays.toString(copy));
            sol.nextPermutation(copy);
            System.out.println("            Next Permutation = " + Arrays.toString(copy));
            System.out.println();
        }
    }
}
```

---

### 🔁 Example Dry Run

#### Input: `[1, 2, 3, 6, 5, 4]`

```
1. Find valley: 3 < 6 → valley = 2
2. Find nextHigher: 4 > 3 → nextHigher = 5
3. Swap(2, 5): → [1, 2, 4, 6, 5, 3]
4. Reverse(3, 5): → [1, 2, 4, 3, 5, 6]
```

✅ Final output: `[1, 2, 4, 3, 5, 6]`

---

### ⏱ Time and Space Complexity

| Metric | Complexity | Explanation                                |
| ------ | ---------- | ------------------------------------------ |
| Time   | O(n)       | 1 scan for valley + 1 reverse = 2 passes   |
| Space  | O(1)       | Done in-place using swap and reverse logic |

---

### 🧠 Interview Recap

> “We scan from the end to find the first decreasing point, then swap it with the next higher number to the right and reverse the suffix. This generates the next lexicographical permutation in-place.”

---

Let me know if you'd like:

* ✅ Recursive implementation
* ✅ Generator for all permutations
* ✅ `k`-th next permutation logic

I’m here to help.





Absolutely! Let’s walk through **5 dry-run examples** of the `nextPermutation()` logic — step by step — so you can deeply understand how it works.

---

## 🔁 **Overview of Logic**

To find the **next permutation** in lexicographical order:

1. 🔍 Find the first index `i` from right such that `nums[i] < nums[i+1]`. Call it `valley`.
2. 🔍 From the right end again, find the first number > `nums[valley]`. Call it `nextHigher`.
3. 🔄 Swap `nums[valley]` and `nums[nextHigher]`.
4. 🔁 Reverse the suffix from `valley + 1` to end of array.

---

## ✅ Example 1: `nums = [1, 2, 3]`

```
Step 1: Find first decreasing pair from right → 2 < 3 at index 1 → valley = 1
Step 2: Find number > 2 from end → 3 at index 2
Step 3: Swap(1,2): [1, 3, 2]
Step 4: Reverse from index 2 to end → already one element → [1, 3, 2]
```

✅ **Output: \[1, 3, 2]**

---

## ✅ Example 2: `nums = [3, 2, 1]`

```
Step 1: No decreasing pair found → valley = -1
→ Reverse whole array → [1, 2, 3]
```

✅ **Output: \[1, 2, 3]** (It was the last permutation, so we go back to the first one)

---

## ✅ Example 3: `nums = [1, 1, 5]`

```
Step 1: 1 < 5 at index 1 → valley = 1
Step 2: Find nextHigher > 1 → 5 at index 2
Step 3: Swap(1,5) → [1, 5, 1]
Step 4: Reverse from 2 to end → [1] → final → [1, 5, 1]
```

✅ **Output: \[1, 5, 1]**

---

## ✅ Example 4: `nums = [1, 3, 2]`

```
Step 1: 1 < 3 → valley = 0
Step 2: From end → find > 1 → 2 at index 2
Step 3: Swap(1,2) → [2, 3, 1]
Step 4: Reverse from index 1 to 2 → [3,1] → [1,3]
Final: [2, 1, 3]
```

✅ **Output: \[2, 1, 3]**

---

## ✅ Example 5: `nums = [2, 3, 1]`

```
Step 1: 2 < 3 → valley = 0
Step 2: Find nextHigher > 2 → 3 at index 1
Step 3: Swap(2,3) → [3, 2, 1]
Step 4: Reverse from 1 to 2 → [2,1] → [1,2]
Final: [3, 1, 2]
```

✅ **Output: \[3, 1, 2]**

---

## 🧠 Summary Table:

| Input     | Valley Index | Next Higher | Swap      | Reversed Suffix | Final Output |
| --------- | ------------ | ----------- | --------- | --------------- | ------------ |
| `[1,2,3]` | 1            | 2           | `[1,3,2]` | -               | `[1,3,2]`    |
| `[3,2,1]` | -1           | -           | -         | `[1,2,3]`       | `[1,2,3]`    |
| `[1,1,5]` | 1            | 2           | `[1,5,1]` | -               | `[1,5,1]`    |
| `[1,3,2]` | 0            | 2           | `[2,3,1]` | `[1,3]`         | `[2,1,3]`    |
| `[2,3,1]` | 0            | 1           | `[3,2,1]` | `[1,2]`         | `[3,1,2]`    |

---

If you want me to **simulate custom input** or give you a **visual dry run for interview preparation**, I can help you with that too.



To **easily remember the `nextPermutation()` algorithm**, especially in interviews, associate each step with a **visual and logical metaphor**. Here’s a structured memory guide that breaks the process into an intuitive 3-step pattern, along with a mnemonic and visual reasoning:

---

## 🧠 High-Level Intuition

You're trying to **find the next lexicographical permutation** (i.e., the "next bigger number"). If the current arrangement is the **last permutation**, return the **first permutation** (sorted in ascending order).

---

## ✅ Memory Framework: “**V-S-R**”

(Like: **Valley, Swap, Reverse**)

| Step | Name        | What to Do                                             | Why?                                             |
| ---- | ----------- | ------------------------------------------------------ | ------------------------------------------------ |
| 1️⃣  | **V**alley  | Find the first index going *down* from the end         | This is the "pivot" where the next change starts |
| 2️⃣  | **S**wap    | Find the smallest number > pivot on the right and swap | To make it just bigger                           |
| 3️⃣  | **R**everse | Reverse the suffix after pivot                         | To make it the lowest possible next number       |

---

## 🧩 Detailed Steps (with variable names)

### 🔹 Step 1: **Find the Valley**

```python
for i in range(len(nums) - 1, 0, -1):
    if nums[i - 1] < nums[i]:
        valley = i - 1
        break
```

* Go from the **right end**, find the first pair where **nums\[i - 1] < nums\[i]**
* This is the **pivot (valley)** — the point where things start going *down*.
* If **not found**, array is in descending order → reverse to get smallest permutation.

---

### 🔹 Step 2: **Find Next Higher and Swap**

```python
while nums[next_higher] <= nums[valley]:
    next_higher -= 1

nums[valley], nums[next_higher] = nums[next_higher], nums[valley]
```

* From the end, find **just larger** element than `nums[valley]`
* Swap it — this gives you a number *just bigger* than the current one

---

### 🔹 Step 3: **Reverse the Right Side**

```python
left = valley + 1
right = len(nums) - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
```

* After the valley, the right half is in decreasing order
* Reversing it gives the **smallest** arrangement (i.e., next lexicographical order)

---

## 🧠 Mnemonic:

> "**V-S-R** → Valley, Swap, Reverse"

Repeat it in your head like a chant — just 3 actions.

---

## 📝 Interview Summary to Say:

> “To compute the next permutation in-place:
>
> 1. I scan from the end to find the first decreasing element — the *pivot*.
> 2. I then find the next larger element to its right and swap them.
> 3. Finally, I reverse the suffix to get the lowest order after the pivot.
>    If no pivot is found, I reverse the entire array, which gives the smallest permutation.”

---

## 📌 Real-World Analogy

> Imagine you’re trying to get the next bigger lottery number using the same digits.
> You:

1. Find where the digits start decreasing → the last *upward slope*
2. Swap the turning point with the next bigger one
3. Reorder everything after that to be the **smallest possible** (ascending)

---

Let me know if you want a **diagram or animation-style explanation** or a **Java version** to match your dual-language prep!
