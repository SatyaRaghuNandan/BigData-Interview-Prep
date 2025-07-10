# // VARIANT: What if you had to find the valley element, no longer a peak element?

Here’s the **Java version** of your C++ code for the **valley element** variant of Leetcode 162:

---

## ✅ Problem: Find Valley Element

A **valley element** is an index `i` where:

```
nums[i] < nums[i-1] && nums[i] < nums[i+1]
```

We treat boundaries (`nums[-1]`, `nums[n]`) as **positive infinity** (`+∞`), so even the edge elements may qualify as valleys.

---

## ✅ Java Code with Telugu-style Comments

```java
public class ValleyElementFinder {

    public int findValleyElement(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // ✅ Left check: nums[mid - 1] > nums[mid] OR mid == 0 (left edge treated as +∞)
            boolean isLeftGreater = (mid == 0 || nums[mid - 1] > nums[mid]);

            // ✅ Right check: nums[mid + 1] > nums[mid] OR mid == n-1 (right edge treated as +∞)
            boolean isRightGreater = (mid == nums.length - 1 || nums[mid + 1] > nums[mid]);

            // 🏞️ If both sides > mid → valley found
            if (isLeftGreater && isRightGreater) {
                return mid;
            }

            // 🔽 Right slope → move right
            if (mid < nums.length - 1 && nums[mid + 1] < nums[mid]) {
                left = mid + 1;
            } else {
                // 🔼 Left slope → move left
                right = mid - 1;
            }
        }

        return -1; // Should never reach here for valid input
    }
}
```

---

## ✅ Time & Space Complexity

| Metric | Value    |
| ------ | -------- |
| Time   | O(log N) |
| Space  | O(1)     |

Same as peak search — binary search on terrain.

---

## ✅ Difference from Peak Element

| Feature        | Peak Element                       | Valley Element                     |
| -------------- | ---------------------------------- | ---------------------------------- |
| Definition     | `nums[i] > nums[i-1] && nums[i+1]` | `nums[i] < nums[i-1] && nums[i+1]` |
| Goal           | Find a local maximum               | Find a local minimum               |
| Slope Movement | Go **toward rising slope**         | Go **toward falling slope**        |
| Edge Behavior  | Edge can be a peak                 | Edge can be a valley               |

---

## ✅ Example Test Cases in `main()`

```java
public class Main {
    public static void main(String[] args) {
        ValleyElementFinder finder = new ValleyElementFinder();

        int[] nums1 = {1, 2, 3, 1}; // valley at start
        int[] nums2 = {1, 2, 3, 5, 3, 4, 3, 1, 6}; // valley at index 4
        int[] nums3 = {3, 2, 3, 4, 3, 2}; // valley at 1
        int[] nums4 = {1, 2, 3, 4, 3, 2}; // valley at 0
        int[] nums5 = {1, 2, 3, 2, 1, 0}; // valley at 5
        int[] nums6 = {1, 2, 3, 2, 1, 6}; // valley at 4

        System.out.println(finder.findValleyElement(nums1)); // 0
        System.out.println(finder.findValleyElement(nums2)); // 4
        System.out.println(finder.findValleyElement(nums3)); // 1
        System.out.println(finder.findValleyElement(nums4)); // 0
        System.out.println(finder.findValleyElement(nums5)); // 5
        System.out.println(finder.findValleyElement(nums6)); // 4
    }
}
```

---

## ✅ Interview Explanation Summary

> “This is the reverse of the peak element problem. We use the same binary search logic, but look for the opposite condition: `nums[i] < neighbors`. We treat boundaries as +∞ so the edge values can still qualify. Like the peak problem, time complexity is O(log N) and we always move in the direction of descent to find a local valley.”

---

Would you like to combine **both peak and valley detection** into one reusable method or build a **terrain analyzer** utility for such problems?
