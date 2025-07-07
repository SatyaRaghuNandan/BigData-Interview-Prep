You're implementing a **variant of Reservoir Sampling**, where instead of selecting **one** random element (as in Leetcode 398), you want to select **`k` distinct elements** from a stream or array **without replacement**, such that:

> Every element from the original array has **equal probability** of being included in the final `k` sample, and no duplicates occur in the output.

This is the **Reservoir Sampling of size `k`** algorithm.

---

## ✅ Cleaned & Annotated C++ Version (with Explanation)

```cpp
#pragma once
#include <vector>
#include <cstdlib> // for rand()

// ✅ Reservoir Sampling to select k random elements from nums[] (without replacement)
std::vector<int> randomPickIndices_first_variant_398(std::vector<int>& nums, int k) {
    int n = nums.size();
    std::vector<int> result(k);

    // ✅ Step 1: Initialize the reservoir with first k elements
    for (int i = 0; i < k; i++) {
        result[i] = nums[i];
    }

    // ✅ Step 2: Process remaining elements (index k to n - 1)
    for (int i = k; i < n; i++) {
        // 🔀 Total elements seen so far = i + 1
        int r = rand() % (i + 1); // Random index in range [0, i]

        // 🧠 Replace an element in reservoir with current element with probability k/i
        if (r < k) {
            result[r] = nums[i]; // Replace r-th element in reservoir
        }
    }

    return result; // 🎯 Final k-sized uniform sample
}
```

---

## ✅ Time and Space Complexity

| Metric       | Complexity | Notes                                 |
| ------------ | ---------- | ------------------------------------- |
| ⏱ Time       | `O(n)`     | Scans the array once                  |
| 🧠 Space     | `O(k)`     | Only stores `k` samples               |
| ✅ Uniformity | Guaranteed | Each item has k/n chance of inclusion |

---

## ✅ Dry Run Example

### Input:

```cpp
nums = [10, 20, 30, 40, 50], k = 2
```

### Possible Outputs (randomized):

* \[10, 50]
* \[20, 30]
* \[40, 50]
* \[10, 20]

Every element has equal probability of being in the result set.

---

## ✅ When to Use

* ✅ Input is a **stream** or large dataset (can't store all in memory)
* ✅ Need a **uniform random sample of size `k`**
* ✅ **Space efficient** solution is required (just `O(k)`)

---

## ✅ Interview Summary

> “Reservoir Sampling allows you to select `k` items from a list or stream of unknown size in a single pass and with constant space `O(k)`. Each item has an equal probability `k/n` of being included, and no duplicates appear in the result.”


Here is the **Java version** of the `Reservoir Sampling` algorithm for selecting **`k` distinct elements uniformly at random** from a list (or stream), without replacement.

---

## ✅ Java Implementation with Telugu-style Comments

```java
import java.util.*;

public class ReservoirSampler {
    private Random rand = new Random();

    /**
     * Returns a random sample of k elements from the input array.
     * Uniform probability for each element. No duplicates.
     */
    public int[] sample(int[] nums, int k) {
        int n = nums.length;
        int[] reservoir = new int[k];

        // ✅ Step 1: First k elements → directly copy to reservoir
        for (int i = 0; i < k; i++) {
            reservoir[i] = nums[i];
        }

        // ✅ Step 2: Process remaining elements one by one
        for (int i = k; i < n; i++) {
            int r = rand.nextInt(i + 1); // Random int in [0, i]

            // ✅ Replace with probability k / (i + 1)
            if (r < k) {
                reservoir[r] = nums[i]; // Replace one element in reservoir
            }
        }

        return reservoir;
    }
}
```

---

## ✅ Example Usage

```java
public class Main {
    public static void main(String[] args) {
        ReservoirSampler sampler = new ReservoirSampler();
        int[] nums = {10, 20, 30, 40, 50, 60};

        // Sample 3 elements from nums[]
        int[] result = sampler.sample(nums, 3);

        System.out.println("Random Sample: " + Arrays.toString(result));
    }
}
```

---

## ✅ Time and Space Complexity

| Metric            | Value  | Notes                                    |
| ----------------- | ------ | ---------------------------------------- |
| ⏱ Time            | `O(n)` | Scans the array once                     |
| 🧠 Space          | `O(k)` | Only stores k items in the reservoir     |
| Uniform Sampling? | ✅ Yes  | Each item has k/n chance of being chosen |

---

## ✅ Dry Run

### Input:

```java
nums = [1, 2, 3, 4, 5], k = 2
```

* Step 1: reservoir = \[1, 2]
* Step 2: for `i = 2 to 4`:

  * Randomly decide whether to replace any of the existing 2
  * Ensures uniform probability for all 5 elements

---

## ✅ Interview Tip

> “Reservoir Sampling is useful when we deal with **huge data streams** or **memory constraints**, and we want a **uniform random sample of k elements** without knowing the total size ahead of time.”

---

Would you like a:

* ✅ Version for `List<T>` generic types?
* ✅ Streaming API version?
* ✅ Weighted/biased reservoir sampling version?

Let me know — happy to help!



---

Would you like a **Java or Python** version of this?
Or the **weighted version** of reservoir sampling (for probabilities)?

Let me know!
