# // VARIANT: What if you had to use reservoir sampling to pick an index of the maximum value in the array?




You're diving into an excellent **set of variants based on Leetcode 398: Random Pick Index**, and you're currently working on:

---

## ✅ Variant 2: **Randomly Pick One Index of the Maximum Value**

---

Let’s first summarize all **three versions** of the problem family, then provide:

1. ✅ Conceptual differences
2. ✅ Use-cases
3. ✅ Java implementation of **Variant 2**
4. ✅ Time and Space complexities
5. ✅ Explanation with examples

---

## ✅ 📦 Problem Family Overview

| Variant         | Description                                                                     | Space  | Time/Query | Use Case                                 |
| --------------- | ------------------------------------------------------------------------------- | ------ | ---------- | ---------------------------------------- |
| **Original**    | Pick a random index of a **target number** with duplicates (LC 398)             | `O(n)` | `O(1)`     | When you're asked to pick uniform target |
| **Variant 1**   | Use **Reservoir Sampling** to return a random index of a **target number**      | `O(1)` | `O(n)`     | Memory-constrained streaming scenarios   |
| ✅ **Variant 2** | Pick a random index of the **maximum number** (which may appear multiple times) | `O(1)` | `O(n)`     | Uniform sampling among max candidates    |

---

## ✅ Variant 2 – Explanation

> You're given an array of integers. Find the **maximum value**, and return a **random index** among all occurrences of that maximum value.

**Goal:** Every index where the max value occurs should be picked with **equal probability**.

---

### 🔍 Example

```text
nums = [1, 3, 3, 2, 3]
→ max = 3
→ max occurs at indices [1, 2, 4]

Randomly return 1, 2, or 4 (each with 1/3 probability)
```

---

### ✅ Why Reservoir Sampling?

You may not want to:

* store all indices where max occurs (especially for huge streams)
* make two passes (one to find max, one to collect indices)

Reservoir sampling solves this in **a single pass** with **constant space**.

---

## ✅ Java Code for Variant 2 — With Comments

```java
import java.util.Random;

public class RandomMaxIndexPicker {

    private Random rand = new Random();

    /**
     * Picks a random index where the maximum number occurs in the array.
     */
    public int pickMaxIndex(int[] nums) {
        int maxNumber = Integer.MIN_VALUE;
        int pickedIndex = -1;
        int count = 0; // number of times maxNumber has appeared

        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];

            if (current < maxNumber) {
                continue; // not interested
            }

            if (current > maxNumber) {
                // New maximum found
                maxNumber = current;
                pickedIndex = i;
                count = 1;
            } else if (current == maxNumber) {
                // Same max again, do reservoir sampling
                count++;
                int r = rand.nextInt(count); // random int in [0, count-1]
                if (r == 0) {
                    pickedIndex = i; // replace the previous selection
                }
            }
        }

        return pickedIndex;
    }
}
```

---

## ✅ Dry Run Example

### Input:

```java
nums = [4, 1, 5, 3, 5, 5]
```

* Max = 5
* Occurs at indices = \[2, 4, 5]

Let’s say we are at:

* i = 2 → first max → pickedIndex = 2
* i = 4 → second max → 50% chance to pick index 4
* i = 5 → third max → 1/3 chance to replace pickedIndex with 5

→ Final output: uniformly distributed across \[2, 4, 5]

---

## ✅ Time & Space Complexity

| Metric        | Value  | Explanation                     |
| ------------- | ------ | ------------------------------- |
| ⏱ Time        | `O(n)` | Single pass through array       |
| 🧠 Space      | `O(1)` | Only constant vars used         |
| 🧮 Uniformity | ✅ Yes  | Each max index has equal chance |

---

## ✅ Summary of Variants

| Variant     | What is being picked?                    | Space  | Key Algorithm      |
| ----------- | ---------------------------------------- | ------ | ------------------ |
| Original    | Index of a given `target` (preprocessed) | `O(n)` | HashMap + Random   |
| Variant 1   | Index of a given `target` (streaming)    | `O(1)` | Reservoir Sampling |
| ✅ Variant 2 | Index of the **maximum** value           | `O(1)` | Reservoir Sampling |

---

## ✅ Interview Summary

> “This problem requires picking an index of the **maximum value** with equal probability when there are duplicates. I used **reservoir sampling**, which allows us to solve it in a single pass without storing all indices. Every time we encounter the max again, we choose it with `1/count` chance, ensuring fairness.”

---

Would you like:

* 🧪 A test suite for this?
* ⚖️ A version that picks **weighted max**?
* 💡 A follow-up version that picks **min or median** index?

Just say the word!
