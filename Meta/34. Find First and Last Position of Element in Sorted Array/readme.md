


Here's the **refactored and well-commented version** of your `searchRange()` Java solution (Leetcode 34: Find First and Last Position of Element in Sorted Array), including:

* ✅ **Telugu-style comments (transliterated)**
* ✅ **Edge cases**
* ✅ **Test driver**
* ✅ **Time and Space complexity analysis**

---

## ✅ Final Java Code with Comments

```java
import java.util.Arrays;

public class Solution {

    // Main function to find first and last position
    public int[] searchRange(int[] nums, int target) {
        // First occurrence ni find cheyyadam (left bound)
        int firstOccurrence = findBound(nums, target, true);

        // If target not found, return [-1, -1]
        if (firstOccurrence == -1) {
            return new int[]{-1, -1};
        }

        // Last occurrence ni find cheyyadam (right bound)
        int lastOccurrence = findBound(nums, target, false);

        return new int[]{firstOccurrence, lastOccurrence};
    }

    // Helper method to find either first or last bound
    private int findBound(int[] nums, int target, boolean isFirst) {
        int n = nums.length;
        int left = 0, right = n - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // ✅ Match found
            if (nums[mid] == target) {
                if (isFirst) {
                    // Check if this is the first occurrence
                    if (mid == left || nums[mid - 1] != target)
                        return mid;
                    // Continue searching left side
                    right = mid - 1;
                } else {
                    // Check if this is the last occurrence
                    if (mid == right || nums[mid + 1] != target)
                        return mid;
                    // Continue searching right side
                    left = mid + 1;
                }
            } else if (nums[mid] > target) {
                // Target lies on left side
                right = mid - 1;
            } else {
                // Target lies on right side
                left = mid + 1;
            }
        }

        return -1; // Target not found
    }

    // --- Test Driver ---
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] testArrays = {
            {5, 7, 7, 8, 8, 10},  // target = 8 → [3, 4]
            {5, 7, 7, 8, 8, 10},  // target = 6 → [-1, -1]
            {},                   // empty array → [-1, -1]
            {1},                  // single element = target → [0, 0]
            {1},                  // single element ≠ target → [-1, -1]
            {2, 2, 2, 2, 2},      // all same elements = target → [0, 4]
            {2, 2, 2, 2, 2},      // all same elements ≠ target → [-1, -1]
            {1, 3, 5, 7, 9, 11},  // no duplicates, target in middle → [2, 2]
            {1, 3, 5, 7, 9, 11},  // target not present → [-1, -1]
        };

        int[] targets = {8, 6, 0, 1, 2, 2, 1, 5, 4};

        for (int i = 0; i < testArrays.length; i++) {
            int[] nums = testArrays[i];
            int target = targets[i];
            System.out.println("Input: " + Arrays.toString(nums) + ", Target: " + target);
            int[] result = sol.searchRange(nums, target);
            System.out.println("Output: " + Arrays.toString(result));
            System.out.println();
        }
    }
}
```

---

## ✅ Dry Run: Example Input `[5, 7, 7, 8, 8, 10]`, Target = `8`

### Step 1: Find First Occurrence

* mid = 2 → nums\[2] = 7 < 8 → move right
* mid = 4 → nums\[4] = 8 (match) → check left → nums\[3] = 8 → move left
* mid = 3 → nums\[3] = 8 and nums\[2] = 7 → ✅ First occurrence = 3

### Step 2: Find Last Occurrence

* mid = 4 → nums\[4] = 8 and nums\[5] = 10 → ✅ Last occurrence = 4

✅ Output: `[3, 4]`

---

## ⏱ Time and Space Complexity

| Metric    | Value      | Explanation                   |
| --------- | ---------- | ----------------------------- |
| **Time**  | `O(log n)` | Binary search runs twice      |
| **Space** | `O(1)`     | No extra space, done in-place |

---

## ✅ Interview Summary

> “I used binary search twice — once to find the first occurrence and once for the last. I handle both bounds by tweaking the logic inside the loop. If no match is found, I return \[-1, -1]. The time complexity is O(log n), making it efficient even for large arrays.”

Let me know if you want:

* A **recursive binary search version**
* To extend this to **count occurrences**
* Or return **indices of all occurrences**

I can help with those too.



