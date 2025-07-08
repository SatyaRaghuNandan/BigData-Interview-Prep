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



Absolutely! Here's the **QuickSelect version** to find the **(k + 1)-th largest element** in an array.

---

## ✅ Variant: Return (k+1)th Largest Element Using QuickSelect

QuickSelect is a selection algorithm based on the **partitioning logic of QuickSort**.
To find the (k+1)th largest, we look for the **(n - (k+1))th smallest** element by index.

---

## ✅ Java Code with Telugu Comments

```java
public class KthPlusOneLargestQuickSelect {

    // ✅ Main function to find (k+1)th largest
    public static int findKPlusOneLargest(int[] nums, int k) {
        int n = nums.length;

        // k+1 largest → (n - k - 1)th smallest in 0-based indexing
        int targetIndex = n - (k + 1);

        return quickSelect(nums, 0, n - 1, targetIndex);
    }

    // 🔁 QuickSelect Function
    private static int quickSelect(int[] nums, int left, int right, int targetIndex) {
        if (left == right) return nums[left];

        int pivotIndex = partition(nums, left, right);

        if (pivotIndex == targetIndex) {
            return nums[pivotIndex]; // ✅ Found our (k+1)th largest
        } else if (pivotIndex < targetIndex) {
            return quickSelect(nums, pivotIndex + 1, right, targetIndex); // 🔁 Right side
        } else {
            return quickSelect(nums, left, pivotIndex - 1, targetIndex); // 🔁 Left side
        }
    }

    // 🔁 Partition using Lomuto scheme
    private static int partition(int[] nums, int left, int right) {
        int pivot = nums[right];
        int i = left;

        for (int j = left; j < right; j++) {
            if (nums[j] <= pivot) {
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

    // ✅ Test Driver
    public static void main(String[] args) {
        int[] nums = {3, 2, 1, 5, 6, 4};
        int k = 2; // → We want 3rd largest = 4

        System.out.println(findKPlusOneLargest(nums, k)); // Output: 4
    }
}
```

---

## ✅ Time and Space Complexity

| Metric | Value                          |
| ------ | ------------------------------ |
| Time   | `O(N)` average, `O(N^2)` worst |
| Space  | `O(1)` (in-place)              |

---

## 🧠 Dry Run (Example)

```java
nums = [3, 2, 1, 5, 6, 4], k = 2
targetIndex = 6 - 3 = 3
```

Sorted: `[1, 2, 3, 4, 5, 6]`

* 3rd index = `4` → ✅ the (k+1)-th largest

---

Let me know if you'd like a **descending variant**, or to apply **Randomized QuickSelect** for better average case performance!
