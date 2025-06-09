Here’s the **detailed explanation** of your `findKthLargest` function with **line-by-line comments** in **English + Telugu (transliterated)**:

---

### ✅ Final Code with Comments

```python
from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Telugu: Minimum Heap ni initialize chesthunna
        # Idea: Heap lo top (index 0) lo k-th largest value untundi final ga
        min_heap = []

        # Telugu: List lo prathi number ni loop chesthunna
        for num in nums:
            heappush(min_heap, num)  # Telugu: number ni min_heap lo push chesthunna
            
            # Telugu: Heap size k kanna ekkuva aithe, smallest element pop cheyyadam
            if len(min_heap) > k:
                heappop(min_heap)

        # Telugu: Heap lo k elements untayi, and top element is k-th largest
        return min_heap[0]
```

---

### ✅ How It Works

* You **maintain a min-heap of size `k`**.
* Only the **k largest elements** remain in the heap.
* The smallest of those `k` (i.e., the root) is the **k-th largest overall**.

---

### ✅ Example

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2

# Output: 5
# Explanation: [6, 5] are the top 2 largest. So 5 is the 2nd largest.
```

---

### ✅ Time and Space Complexity

* **Time Complexity**: `O(n log k)`
  → Because each `heappush` and `heappop` takes `O(log k)`, and we do this `n` times.

* **Space Complexity**: `O(k)`
  → Because heap size is maintained at most `k`.

---

### 🔄 Alternate Follow-ups You Can Practice

1. **Find k-th smallest**: Use max-heap or modify logic.
2. **Stream version**: Process one element at a time.
3. **QuickSelect version**: Average `O(n)` time.

---

Would you like the **QuickSelect (non-heap) solution** for this too? It's often asked in Meta interviews for optimized version.
