Here’s the **Java version** of your C++ solution for **Leetcode 88: Merge Sorted Array** using the **three-pointer approach** (merging from the end):

---

## ✅ Java Code with Telugu-style Comments

```java
public class MergeSortedArray {

    // Merges nums2 into nums1 as one sorted array
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // 🟢 a: nums1 valid elements index
        int a = m - 1;

        // 🟢 b: nums2 index
        int b = n - 1;

        // 🟢 i: nums1 final position index (merged array end)
        int i = m + n - 1;

        // 🔁 Loop till all nums2 elements are merged
        while (b >= 0) {
            if (a >= 0 && nums1[a] >= nums2[b]) {
                nums1[i] = nums1[a];  // nums1 element is bigger
                a--;
            } else {
                nums1[i] = nums2[b];  // nums2 element is bigger
                b--;
            }
            i--;
        }
    }
}
```

---

## ✅ Example Test in `main()`

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        MergeSortedArray merger = new MergeSortedArray();

        int[] nums1 = {1, 2, 3, 0, 0, 0};
        int[] nums2 = {2, 5, 6};
        int m = 3, n = 3;

        merger.merge(nums1, m, nums2, n);
        System.out.println(Arrays.toString(nums1)); // Output: [1, 2, 2, 3, 5, 6]
    }
}
```

---

## ✅ Time and Space Complexity

| Metric           | Value           |
| ---------------- | --------------- |
| Time Complexity  | O(m + n)        |
| Space Complexity | O(1) — in-place |

---

## ✅ Interview Explanation Summary

> “I use three pointers: one at the end of the valid portion of `nums1`, one at the end of `nums2`, and one at the end of the full `nums1` array.
> I compare and insert elements from the back to avoid overwriting.
> This ensures an in-place `O(m + n)` merge in sorted order.”

---

Would you like a version that merges into a **new array** or handles edge cases like null/empty arrays?
