Perfect. Meta often uses this pattern:
✅ First, test your knowledge of **sliding window templates** (like Leetcode 346: Moving Average from Data Stream)
✅ Then, test your ability to **adapt the pattern** to **batch-based** or **offline array-based** variants.

Let’s now break it down clearly:

---

## ✅ PART 1: Original Problem – Leetcode 346 (Streaming API)

### 🔁 Problem Summary:

You're designing a **class** that receives a stream of integers and returns the average of the last `size` elements.

### 🔍 Key Points:

* It needs to **maintain state** across calls to `.next()`.
* FIFO structure → **queue**
* Track **rolling sum** → subtract oldest, add newest.

### ✅ Time & Space Complexity

* Time: `O(1)` per `.next()` call
* Space: `O(size)`

---

## ✅ PART 2: Variant – Array Based

### 🔁 Problem Summary:

You’re given a **static list of integers** and a **window size**. Compute the average over **each window** of size `k`.

### 🔍 Key Points:

* This is a **fixed-size sliding window**, not streaming.
* The result is a list of `n - k + 1` averages (integer division).

### ✅ Time & Space Complexity

* Time: `O(n)` – single pass, each element visited once.
* Space: `O(n - k + 1)` – one average per window

---

## ✅ 🔥 Interviewer Intent at Meta

### What they want to test:

| Skill                      | What They Look For                                                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Template understanding** | Can you apply and tweak the **sliding window** pattern for both streaming and static input?                                    |
| **Optimization**           | Can you avoid recomputing sums each time?                                                                                      |
| **Robustness**             | Does your solution handle edge cases (`k=1`, `nums.length == k`)?                                                              |
| **Language fluency**       | For Python: Do you understand built-in types (list, deque, queue)? For Java: Do you pick the right interface (Deque vs Queue)? |

---

## ✅ Optimized Template Summary (With Telugu-style English Comments)

### 🎯 Python Streaming Variant:

```python
from collections import deque

class MovingAverageStream:
    def __init__(self, size: int):
        self.size = size             # Window size ni store cheyyadam
        self.queue = deque()         # FIFO Queue ni maintain cheyyadam
        self.window_sum = 0          # Sum of elements inside window

    def next(self, val: int) -> float:
        self.window_sum += val      # New value add cheyyadam
        self.queue.append(val)      

        if len(self.queue) > self.size:
            removed = self.queue.popleft()  # Oldest value remove cheyyadam
            self.window_sum -= removed

        return self.window_sum / len(self.queue)  # Current average return cheyyadam
```

---

### 🎯 Python Static Array Variant:

```python
from typing import List

def compute_moving_average(nums: List[int], size: int) -> List[int]:
    result = []                   # Final result ni store cheyyadam
    window_sum = 0                # Current window lo sum ni track cheyyadam

    for right in range(len(nums)):
        window_sum += nums[right]

        left = right - size
        if left >= 0:
            window_sum -= nums[left]  # Window size ni maintain cheyyadam

        if right >= size - 1:
            result.append(window_sum // size)

    return result
```

---

## ✅ Meta Preference:

| Scenario                  | Preferred                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Online / Streaming**    | Class-based Streaming API (Queue + Rolling Sum)                                            |
| **Offline / Batch Input** | Fixed-size Sliding Window (prefix sum, sliding window)                                     |
| **Follow-up**             | Often asks: What if values come in very fast? Use **Deque**, **Heap**, or **Prefix Sums**? |

---

If you're preparing for **Meta E5**, mastering both and explaining trade-offs (streaming vs offline, space constraints, latency) shows senior-level thinking.

Would you like the **Java versions** with comments next? Or a **heap-based variant** for exponential-weighted moving average (EWMA)?
