Here's a full breakdown of **Leetcode 215 – Find Kth Largest Element in an Array** with the **Top 4 Approaches**, each explained with:

* ✅ Python Code
* ✅ Detailed Telugu Comments
* ✅ Time & Space Complexity

---

## ✅ Problem:

Find the **kth largest element** in an unsorted list.

---

## ✅ Approach 1: Sorting

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Array ni sort chestunnam (ascending order)
        nums.sort()
        # kth largest ante right side nunchi k-th index (N - k)
        return nums[-k]
```

### 🧠 Telugu Comments:

```text
- nums.sort(): Complete ga sort chesestham
- nums[-k]: Right side nunchi k-th element return cheyyadam
```

### ⏱ Complexity:

* Time: `O(N log N)`
* Space: `O(1)` (in-place sort if allowed)

---

## ✅ Approach 2: Min-Heap (Best for streaming/online input)

```python
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # First k elements ni heap lo petti, heap maintain chestunnam
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # Next elements process cheyyadam
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]
```

### 🧠 Telugu Comments:

```text
- First k elements min-heap lo petti, smallest maintain chestunnam
- Tharuvatha elements check chesi, heap update cheyyadam
- Final ga heap[0] contains kth largest
```

### ⏱ Complexity:

* Time: `O(N log k)`
* Space: `O(k)`

---

## ✅ Approach 3: Quickselect (Randomized)

```python
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Kth largest ni kth smallest ga convert chestunnam
        target_idx = len(nums) - k

        def quickSelect(left, right):
            # Random pivot pick cheyyadam
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            pivot = nums[right]

            # Partition: pivot kanna takkuva elements left side ki
            store_idx = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1

            # Pivot ni correct position lo petadam
            nums[store_idx], nums[right] = nums[right], nums[store_idx]

            # Left, right lo recursive ga search cheyyadam
            if store_idx < target_idx:
                return quickSelect(store_idx + 1, right)
            elif store_idx > target_idx:
                return quickSelect(left, store_idx - 1)
            else:
                return nums[store_idx]

        return quickSelect(0, len(nums) - 1)
```

### 🧠 Telugu Comments:

```text
- target_idx = N - k (kth largest → index)
- quickSelect() lo pivot random ga pick cheyyadam
- Partition logic tho left, right adjust cheyyadam
- store_idx == target ante answer dorikindi
```

### ⏱ Complexity:

* Average Time: `O(N)`
* Worst Case: `O(N^2)` (rare)
* Space: `O(1)` (in-place)

---

## ✅ Approach 4: Counting Sort (If numbers are within known range)

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Range lo max and min values ni find cheyyadam
        min_val = min(nums)
        max_val = max(nums)

        # Counting array prepare cheyyadam
        count = [0] * (max_val - min_val + 1)
        for num in nums:
            count[num - min_val] += 1

        # Backward iterate cheyyadam (largest to smallest)
        for i in range(len(count) - 1, -1, -1):
            k -= count[i]
            if k <= 0:
                return i + min_val
```

### 🧠 Telugu Comments:

```text
- Count array lo each number yentha sarlu vacchindo track chestunnam
- Reverse lo iterate chesi k reduce chestunnam
- k == 0 or less aithe answer found
```

### ⏱ Complexity:

* Time: `O(N + R)` where R = range of numbers
* Space: `O(R)`

---

## 🏁 Summary Table

| Approach      | Time Complexity  | Space Complexity | Notes                            |
| ------------- | ---------------- | ---------------- | -------------------------------- |
| Sort          | O(N log N)       | O(1)             | Easiest, not optimal             |
| Min-Heap      | O(N log k)       | O(k)             | Ideal when `k` is small          |
| Quickselect   | O(N) avg / O(N²) | O(1)             | Optimal, interview-preferred     |
| Counting Sort | O(N + R)         | O(R)             | Best when range is small/integer |

---

Let me know if you'd like to visualize the **Quickselect recursion** or see a **Java version** with same annotations.
