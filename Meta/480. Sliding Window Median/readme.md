Here’s how you can **memorize** and understand the **Sliding Window Median** problem (`Leetcode 480 – Hard`) with two heaps:

---

## ✅ Problem Summary

> You are given an array `nums` and a sliding window size `k`.
> For each window of size `k`, compute the **median** of the numbers inside the window.

---

## ✅ Java Code Summary

### 💡 Key Idea:

Use two heaps:

* `maxHeap` (for the smaller half)
* `minHeap` (for the larger half)

Maintain balance such that:

* `maxHeap` size == `minHeap` size (+1 when odd `k`)
* Median is:

  * top of `maxHeap` if odd size
  * average of tops if even size

```java
class Solution {
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    private PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

    public double[] medianSlidingWindow(int[] nums, int k) {
        double[] result = new double[nums.length - k + 1];

        for (int i = 0; i < nums.length; i++) {
            add(nums[i]);

            if (i >= k - 1) {
                result[i - k + 1] = findMedian();
                remove(nums[i - k + 1]);
            }
        }

        return result;
    }

    private void add(int num) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) maxHeap.offer(num);
        else minHeap.offer(num);

        rebalance();
    }

    private void remove(int num) {
        if (num <= maxHeap.peek()) maxHeap.remove(num);
        else minHeap.remove(num);

        rebalance();
    }

    private void rebalance() {
        while (maxHeap.size() > minHeap.size() + 1)
            minHeap.offer(maxHeap.poll());

        while (minHeap.size() > maxHeap.size())
            maxHeap.offer(minHeap.poll());
    }

    private double findMedian() {
        if (maxHeap.size() > minHeap.size())
            return maxHeap.peek();
        return ((double) maxHeap.peek() + minHeap.peek()) / 2;
    }
}
```

---

## ✅ Time and Space Complexity

| Operation    | Time            | Notes                                |
| ------------ | --------------- | ------------------------------------ |
| `add()`      | `O(log k)`      | Because of heap insert               |
| `remove()`   | `O(k)` *(Java)* | Java's `remove(obj)` is `O(k)`       |
| `findMedian` | `O(1)`          | Direct peek                          |
| **Total**    | ⚠️ `O(n * k)`   | Because of linear `remove()` in Java |
| Space        | `O(k)`          | Heap space                           |

> 🧠 Use **TreeMap or TreeSet** in Java to optimize remove to `O(log k)` (like C++ multiset).

---

## 🧠 Memory Tips — How to Remember

### 🔑 Think of this as “Balanced Tree Sliding Window”:

* You need two balanced parts:

  * One heap has smaller half
  * One heap has larger half

### 🎯 Triggers to Remember:

| Trigger        | Thought                                               |
| -------------- | ----------------------------------------------------- |
| Median         | “Two Heaps” → One maxHeap (left), one minHeap (right) |
| Sliding Window | Add + Remove per index                                |
| Rebalancing    | Make sure sizes differ by ≤ 1                         |

---

## ✅ Dry Run Example

### Input:

```java
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
```

### Output:

```java
[1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

**Explanation:**

```
[1,3,-1] → median = 1
[3,-1,-3] → median = -1
[-1,-3,5] → median = -1
[-3,5,3] → median = 3
[5,3,6] → median = 5
[3,6,7] → median = 6
```

---

## ✅ Interview Summary

> “We use two heaps to keep track of the sliding window values: maxHeap for the left half and minHeap for the right half. We balance both heaps so that median can be found in O(1). On every step, we add the current number, remove the outgoing number, rebalance the heaps, and take the top(s) to compute the median. This gives an overall O(n \* k) solution in Java.”

---

Would you like a **TreeMap version** that works in `O(n log k)` or a visual diagram for this heap balancing?
