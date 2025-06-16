
Great! Let's rewrite all three approaches for the **Top K Frequent Elements** problem in **Python**, ensuring:

* ✅ Correctness
* ✅ Clean code
* ✅ In-line Telugu comments
* ✅ Time and Space complexity
* ✅ Easy-to-compare format

---

## ✅ Approach 1: Using Min Heap (`heapq.nlargest`)

```python
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k == len(nums) aithe, anni return cheyyali (optimization)
        if k == len(nums):
            return nums

        # Step 1: Frequency count using Counter
        frequency_map = Counter(nums)  # num: count

        # Step 2: Heap lo top-k keys ni based on frequency teesukovali
        # heapq.nlargest() valla O(N log k) lo vastundi
        return heapq.nlargest(k, frequency_map.keys(), key=frequency_map.get)
```

### ⏱ Time Complexity:

* Build Counter: O(N)
* heapq.nlargest: O(N log k)

### 🧠 Space Complexity:

* O(N) for frequency map and heap

---

## ✅ Approach 2: QuickSelect (Hoare’s Selection Algorithm)

```python
from collections import Counter
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Frequency count
        freq = Counter(nums)  # {num: frequency}

        # Step 2: Convert to list of tuples (frequency, num)
        items = [(count, num) for num, count in freq.items()]

        def quickSelect(left, right, k):
            if left >= right:
                return

            # Random pivot to avoid worst-case
            pivot_idx = random.randint(left, right)
            items[pivot_idx], items[right] = items[right], items[pivot_idx]
            pivot_freq = items[right][0]

            # Partition by frequency
            store_idx = left
            for i in range(left, right):
                if items[i][0] <= pivot_freq:
                    items[i], items[store_idx] = items[store_idx], items[i]
                    store_idx += 1

            # Move pivot to final place
            items[store_idx], items[right] = items[right], items[store_idx]

            # Decide which side to recurse
            if store_idx == len(items) - k:
                return
            elif store_idx > len(items) - k:
                quickSelect(left, store_idx - 1, k)
            else:
                quickSelect(store_idx + 1, right, k)

        # Step 3: Run QuickSelect
        quickSelect(0, len(items) - 1, k)

        # Step 4: Extract top-k elements
        return [num for freq, num in items[-k:]]
```

### ⏱ Time Complexity:

* Average: O(N)
* Worst-case: O(N²) (rare with random pivot)

### 🧠 Space Complexity:

* O(N) for frequency list

---

## ✅ Approach 3: Bucket Sort (Optimal for bounded frequencies)

```python
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq_map = Counter(nums)

        # Step 2: Bucket creation, index = frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        # Step 3: Collect top-k elements from bucket in reverse order
        result = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
```

### ⏱ Time Complexity:

* O(N)

  * Counting: O(N)
  * Bucket build + traverse: O(N)

### 🧠 Space Complexity:

* O(N) for buckets and result

---

## 🔁 Comparison Table

| Approach    | Time Complexity       | Space Complexity | Best Use Case                     |
| ----------- | --------------------- | ---------------- | --------------------------------- |
| Min Heap    | O(N log k)            | O(N)             | General top-k frequency           |
| QuickSelect | O(N) avg, O(N²) worst | O(N)             | Interview-optimized, no extra lib |
| Bucket Sort | O(N)                  | O(N)             | When values repeat significantly  |

---

Let me know if you’d like:

* Dry runs for each approach
* Java/C++ equivalents
* Additional interview-style test cases or edge cases
