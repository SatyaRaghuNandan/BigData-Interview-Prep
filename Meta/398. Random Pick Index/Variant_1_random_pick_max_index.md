# // VARIANT: What if you had to use reservoir sampling to randomly sample K numbers without replacement probability?

Great! You're tackling an excellent interview problem that combines **array traversal**, **randomization**, and **reservoir sampling** — a popular technique in large data streaming scenarios.

---

## 🔁 Problem Statement (Variant Recap)

> Given an array `nums`, randomly return **one index** where the **maximum value** occurs. All such indices should have **equal probability** of being returned.

---

# ✅ Approach 1: Reservoir Sampling (Recommended in Interviews)

### ✅ Java Implementation with Telugu Comments

```java
import java.util.Random;

public class RandomMaxPicker {
    private final Random rand = new Random();

    public int pickMaxIndex(int[] nums) {
        int maxValue = Integer.MIN_VALUE;  // 🧠 Starting point for max
        int pickedIndex = -1;              // ✅ Randomly selected index of max
        int count = 0;                     // 👍 Max value ochina count ni track cheyyadam

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < maxValue) {
                continue; // 🧪 Max kanna thakkuva vunte skip cheyyali
            }

            if (nums[i] > maxValue) {
                // 🆕 Kotha max value vachesindi. Reset cheyyali
                maxValue = nums[i];
                pickedIndex = i;
                count = 1;
            } else if (nums[i] == maxValue) {
                // 🎲 Equal probability tho pick cheyyadam using Reservoir Sampling
                count++;
                if (rand.nextInt(count) == 0) {
                    pickedIndex = i;
                }
            }
        }

        return pickedIndex;
    }

    public static void main(String[] args) {
        RandomMaxPicker picker = new RandomMaxPicker();
        int[] nums = {1, 3, 5, 5, 2, 5};

        // 🔁 Try multiple times to verify randomness
        for (int i = 0; i < 10; i++) {
            System.out.println("Picked max index: " + picker.pickMaxIndex(nums));
        }
    }
}
```

---

## 🧠 Logic Summary (Reservoir Sampling Variant)

* Max values can repeat, and we need to choose one randomly.
* Maintain count of how many times max has occurred (`count`).
* Replace the current selection with **probability 1/count**.

---

## 📊 Time & Space Complexity

| Metric              | Value  | Reason                    |
| ------------------- | ------ | ------------------------- |
| ⏱️ Time Complexity  | `O(n)` | One pass over array       |
| 🧠 Space Complexity | `O(1)` | Only constant extra space |

---

# ✅ Approach 2: Two-Pass with List of Indices

> 🔍 First find the max value, then collect all indices and randomly pick one.

### Java Code:

```java
import java.util.*;

public class MaxIndexPickerTwoPass {

    private final Random rand = new Random();

    public int pickMaxIndex(int[] nums) {
        int max = Integer.MIN_VALUE;

        // 🔍 1st Pass: Find max value
        for (int num : nums) {
            max = Math.max(max, num);
        }

        // 🧺 2nd Pass: Collect all indices of max value
        List<Integer> indices = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == max) {
                indices.add(i);
            }
        }

        // 🎲 Random ga oka index select cheyyali
        int randomIndex = rand.nextInt(indices.size());
        return indices.get(randomIndex);
    }
}
```

---

## 🔁 Two Approaches Comparison

| Feature                 | **Reservoir Sampling**           | **Two-Pass with List**               |
| ----------------------- | -------------------------------- | ------------------------------------ |
| ✅ **Time Complexity**   | `O(n)`                           | `O(n)` (2 passes)                    |
| 💾 **Space Complexity** | `O(1)`                           | `O(k)` (for storing `k` max indices) |
| 🎯 Use Case             | Streaming or Memory Efficient    | Simple implementation, small arrays  |
| ⚙️ Probability Logic    | Inline during traversal (1-pass) | Simple random choice from a list     |

---

## ✅ What to Say in an Interview

> “I’ll start with a **Reservoir Sampling** approach to ensure uniform randomness in one pass. But if memory isn’t a concern and the dataset is small, a simpler **two-pass solution** with a list of max indices can also work well.”

---

Would you also like:

* ✅ Extension for minimum element?
* ✅ Return **all max indices** instead of one?
* ✅ Implementation using a streaming interface for large inputs?

Let me know and I’ll guide you accordingly!
