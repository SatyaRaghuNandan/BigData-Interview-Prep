Here is the **Java version** of your C++ code for:

> 🔼 **Finding a peak element** in an array — Leetcode 162
> A peak is defined as an element that is **greater than its neighbors**

---

## ✅ Java Code with Telugu-style Comments

```java
public class PeakElementFinder {

    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        // 🔁 Binary search loop
        while (left <= right) {
            int mid = left + (right - left) / 2;

            // ✅ Mid element ni check cheyyadam if it is peak
            boolean isRightSmaller = (mid == nums.length - 1 || nums[mid] > nums[mid + 1]);
            boolean isLeftSmaller = (mid == 0 || nums[mid] > nums[mid - 1]);

            if (isLeftSmaller && isRightSmaller) {
                return mid; // 🏔️ Peak found
            }

            // 🔽 Right side slope → peak might be on right side
            if (mid < nums.length - 1 && nums[mid + 1] > nums[mid]) {
                left = mid + 1;
            }
            // 🔼 Left side slope → peak might be on left side
            else {
                right = mid - 1;
            }
        }

        return -1; // Should never reach here for valid input
    }
}
```

---

## ✅ Time and Space Complexity

| Metric | Value    |
| ------ | -------- |
| Time   | O(log N) |
| Space  | O(1)     |

Binary search ensures logarithmic time.

---

## ✅ How It Works (Dry Run)

```text
Example: [1, 2, 3, 1]

→ mid = 1 → nums[1] = 2 → nums[2] = 3 > 2 → go right
→ mid = 2 → nums[2] = 3 → nums[3] = 1 < 3, nums[1] = 2 < 3 → ✅ peak
```

---

## ✅ When to Use This

* Efficiently find **any peak** (doesn't guarantee the global max, just *a* peak)
* Perfect fit for **binary search reasoning interviews** (Meta, Google, Bloomberg)

---

Would you like the version that returns **all peaks** or that works on **2D matrix peaks** (Leetcode 1901)?


