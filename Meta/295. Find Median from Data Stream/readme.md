```text
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
```


Here’s a full explanation of the **MedianFinder** design with Telugu-style comments, approach, time/space complexity, and also answers your question — *is there a better way for O(1) `findMedian()`*?

---

### ✅ **Approach (in Plain English):**

1. We maintain **two heaps**:

   * A **Max Heap** (`small`) for the smaller half of numbers.
   * A **Min Heap** (`large`) for the larger half.
2. This helps us **balance** the two halves so we can fetch the median easily.
3. When adding a number:

   * If total count is even, we insert into `large`, then move the smallest from `large` to `small`.
   * If odd, we insert into `small`, then move the largest from `small` to `large`.
4. Median is either the top of `small` (odd size) or average of both tops (even size).
5. This ensures **O(log n)** for insertion and **O(1)** for median lookup.

---

### 💡 Telugu Comments Explanation Version

```java
class MedianFinder {

    // Small half numbers ni store cheyyadaniki Max Heap (largest element peek lo untadi)
    private PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());

    // Large half numbers ni store cheyyadaniki Min Heap (smallest element peek lo untadi)
    private PriorityQueue<Integer> large = new PriorityQueue<>();

    // Count even or odd ani cheyyataniki flag
    private boolean even = true;

    // Median ni direct ga calculate cheyyachu in O(1)
    public double findMedian() {
        if (even) {
            // Even count ayithe middle two numbers ni average cheyyali
            return (small.peek() + large.peek()) / 2.0;
        } else {
            // Odd count ayithe max heap top (middle element) return cheyyali
            return small.peek();
        }
    }

    public void addNum(int num) {
        if (even) {
            // Large heap lo add chesi, smallest ni small heap lo pumpinchali
            large.offer(num);
            small.offer(large.poll());
        } else {
            // Small heap lo add chesi, largest ni large heap lo pumpinchali
            small.offer(num);
            large.offer(small.poll());
        }
        // Toggle even/odd count
        even = !even;
    }
}
```

---

### ⏱️ Time and Space Complexity

| Operation      | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| `addNum()`     | O(log n)        | O(n)             |
| `findMedian()` | O(1)            | O(1)             |

---

### ❓ Is there a better way?

* ✅ **This is the optimal solution** for real-time streaming median problems.
* 🔁 You can’t do better than `O(log n)` insertion because **heaps require sorting** logic.
* ✅ But `findMedian()` is already **O(1)** — which is optimal.

---

### 📌 Summary

* Two Heaps → Balanced → Easy median.
* Always maintain: `small.size() == large.size()` or `small.size() == large.size() + 1`.
* `addNum()` → O(log n), `findMedian()` → O(1) ✅

Let me know if you want a **version with sorted array + binary insertion (TreeSet / AVL Tree)** for comparison!
