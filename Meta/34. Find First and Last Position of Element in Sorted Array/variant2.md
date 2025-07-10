

# // VARIANT: What if you had to return the number of unique elements in an integer array?
# // Note this must be done in K LOG N time complexity (unless the input has all unique integers)

Here is the **Java version** of your C++ code for:

> ✅ **Counting unique elements** in a sorted array using **binary search**
> ✅ Target **`O(K log N)`** time, where `K = number of unique elements`

---

## ✅ Java Code with Telugu-style Comments

```java
public class UniqueElementCounter {

    // ✅ Sorted array lo unique elements count cheyyadam
    public int countUniqueElements(int[] nums) {
        int count = 0;
        int i = 0;

        while (i < nums.length) {
            int target = nums[i]; // 🧭 Current element ni consider cheyyadam
            int left = i;
            int right = nums.length - 1;

            // 🔍 Binary search to find last index of current target
            while (left <= right) {
                int mid = left + (right - left) / 2;

                if (nums[mid] <= target) {
                    left = mid + 1; // Move right if mid value same or smaller
                } else {
                    right = mid - 1; // Move left if greater than target
                }
            }

            // 🔢 Unique element found → count increment cheyyadam
            count++;

            // 🧭 Next i = right + 1 ante → current target complete ayindi
            i = right + 1;
        }

        return count;
    }
}
```

---

## ✅ Dry Run Example

```java
Input: [1, 1, 2, 3, 3, 3, 4, 5, 5]

i = 0 → target = 1 → binary search gives right = 1 → i = 2 → count = 1  
i = 2 → target = 2 → right = 2 → i = 3 → count = 2  
i = 3 → target = 3 → right = 5 → i = 6 → count = 3  
i = 6 → target = 4 → right = 6 → i = 7 → count = 4  
i = 7 → target = 5 → right = 8 → i = 9 → count = 5  
```

Final `count = 5`

---

## ✅ Time and Space Complexity

| Metric | Value      |
| ------ | ---------- |
| Time   | O(K log N) |
| Space  | O(1)       |

* `K` = number of unique elements
* For each unique element, we binary search its last index → `log N`

---

## ✅ Interview Tip

> “To count unique elements in a sorted array in better than O(N) time, I perform a binary search to skip all duplicates. For each new unique value, I use binary search to jump directly to the last occurrence, making it `O(K log N)` where `K` is the number of distinct elements.”

---

Would you like a version for unsorted arrays or frequency maps too?
