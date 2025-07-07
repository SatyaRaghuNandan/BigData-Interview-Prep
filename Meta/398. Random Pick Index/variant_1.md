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

---

Would you like a **Java or Python** version of this?
Or the **weighted version** of reservoir sampling (for probabilities)?

Let me know!
