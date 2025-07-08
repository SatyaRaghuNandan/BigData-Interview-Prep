You're exploring the **Kth Smallest Element** variant of Leetcode 215.
Let's implement both:

---

## ✅ Problem:

**"Find the Kth smallest number in an integer array"**

---

## ✅ Approach 1: Max Heap (Priority Queue)

We maintain a **max heap of size `k`**, so the largest among the smallest `k` elements is always at the top.

---

### ✅ Java Code (Max Heap)

```java
import java.util.PriorityQueue;
import java.util.Collections;

public class KthSmallestWithHeap {

    public static int findKthSmallest(int[] nums, int k) {
        // ✅ Max Heap to keep k smallest elements
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int num : nums) {
            maxHeap.add(num);
            if (maxHeap.size() > k) {
                maxHeap.poll(); // Remove largest of k+1 elements
            }
        }

        return maxHeap.peek(); // ✅ This is the kth smallest
    }

    public static void main(String[] args) {
        int[] nums = {3, 8, 4, 1, 10};
        System.out.println(findKthSmallest(nums, 3)); // 4
        System.out.println(findKthSmallest(nums, 1)); // 1
    }
}
```

---

### ✅ Time and Space

| Metric | Value      |
| ------ | ---------- |
| Time   | O(N log K) |
| Space  | O(K)       |

---

## ✅ Approach 2: QuickSelect

We use the **QuickSelect algorithm** to find the element at index `k - 1` (0-based index of the k-th smallest).

---

### ✅ Java Code (Quick Select)

```java
public class KthSmallestQuickSelect {

    public static int findKthSmallest(int[] nums, int k) {
        return quickSelect(nums, 0, nums.length - 1, k - 1);
    }

    private static int quickSelect(int[] nums, int left, int right, int kIndex) {
        if (left == right) return nums[left];

        int pivotIndex = partition(nums, left, right);

        if (pivotIndex == kIndex) {
            return nums[pivotIndex];
        } else if (pivotIndex < kIndex) {
            return quickSelect(nums, pivotIndex + 1, right, kIndex);
        } else {
            return quickSelect(nums, left, pivotIndex - 1, kIndex);
        }
    }

    private static int partition(int[] nums, int left, int right) {
        int pivot = nums[right];
        int i = left;

        for (int j = left; j < right; j++) {
            if (nums[j] < pivot) {
                swap(nums, i, j);
                i++;
            }
        }

        swap(nums, i, right);
        return i;
    }

    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        int[] nums = {3, 8, 4, 1, 10};
        System.out.println(findKthSmallest(nums, 3)); // 4
        System.out.println(findKthSmallest(nums, 1)); // 1
    }
}
```

---

### ✅ Time and Space

| Metric | Value                     |
| ------ | ------------------------- |
| Time   | O(N) average, O(N²) worst |
| Space  | O(1) (in-place)           |

---

## 🧠 Summary Table

| Approach    | Time       | Space | Best When...                         |
| ----------- | ---------- | ----- | ------------------------------------ |
| Max Heap    | O(N log K) | O(K)  | When `K` is small                    |
| QuickSelect | O(N) avg   | O(1)  | Optimal for large `K` and full array |

---

Let me know if you want:

* 🔁 Python versions
* 📉 Descending-order version
* 🎯 Kth smallest in a sorted matrix/grid (Leetcode 378)

Happy to help!
