You're implementing a **variant of Reservoir Sampling**, specifically:

---

### ✅ Problem:

> Given a stream (or array) `nums` and a value `k`, randomly select `k` items **without replacement**, such that every item in the input has equal probability of being selected.

---

## 🔁 Reservoir Sampling (k-sample Variant)

This variant is useful when:

* Input size is unknown or very large.
* You want to randomly pick `k` distinct elements from the stream/array **uniformly**.

---

## ✅ Python Version with Telugu Comments

```python
import random
from typing import List

def reservoir_sampling_k(nums: List[int], k: int) -> List[int]:
    # First k elements ni direct ga sample lo pettaali
    result = nums[:k]

    # Rest of the elements ni consider cheyyali from index k
    for i in range(k, len(nums)):
        # i+1 varaku total elements vachesayi
        n = i + 1
        r = random.randint(0, n - 1)  # randint is inclusive

        # r value < k unte, existing sample lo replace cheyyali
        if r < k:
            result[r] = nums[i]

    return result
```

---

### 🧪 Example:

```python
nums = [10, 20, 30, 40, 50, 60, 70, 80]
sample = reservoir_sampling_k(nums, 3)
print(sample)  # Random 3 values without replacement, each equally likely
```

---

### 📊 Time & Space Complexity:

| Operation | Complexity |
| --------- | ---------- |
| Time      | O(n)       |
| Space     | O(k)       |

---

### 🎯 Use Cases:

* When you cannot store entire dataset in memory (e.g., streaming APIs, log analysis).
* Efficient in memory and CPU for large data.

---

Would you like the **LeetCode 398 original** problem implemented using **Reservoir Sampling for just 1 value** (k=1)? That's the true optimization for huge data without storing all indices.
