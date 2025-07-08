Sure! Here's the **Java version** of your **C++ variant** for:

> 🔁 **"Return the (K+1)th largest element"** in an integer array using a **min-heap approach**.

---

### ✅ Java Translation with Comments

```java
import java.util.PriorityQueue;

public class KthPlusOneLargest {

    // ✅ Find (k+1)th largest element
    public static int findKPlusOneLargest(int[] nums, int k) {
        if (k + 1 > nums.length) {
            throw new IllegalArgumentException("k + 1 cannot exceed array size.");
        }

        int heapSize = k + 1;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int num : nums) {
            minHeap.add(num);

            // ❗ Keep heap size at most k+1
            if (minHeap.size() > heapSize) {
                minHeap.poll(); // Remove the smallest to keep only top k+1 largest elements
            }
        }

        return minHeap.peek(); // ✅ This is the (k+1)th largest
    }

    public static void main(String[] args) {
        int[] nums = {3, 2, 1, 5, 6, 4};
        int k = 2;

        System.out.println(findKPlusOneLargest(nums, k)); // Output: 4 → (3rd largest)
    }
}
```

---

### ✅ Explanation

This is a small variant of the original Leetcode 215:

* Instead of keeping a **min-heap of k elements** (to get k-th largest),
* We keep a **min-heap of (k+1) elements**
* So the root of the heap is the **(k+1)th largest** value

---

### ✅ Time and Space Complexity

| Metric | Value            |
| ------ | ---------------- |
| Time   | `O(N log (k+1))` |
| Space  | `O(k+1)`         |

---

### 🧠 Example

Input: `nums = [3, 2, 1, 5, 6, 4], k = 2`
We want the **3rd largest** number (since `k+1 = 3`)

* Largest: `6`
* 2nd largest: `5`
* 3rd largest: `4` ✅

Output: `4`

---

Let me know if you want the **QuickSelect variant** for this `(k+1)` use case as well!
