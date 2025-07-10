// VARIANT: What if you had to return the number of occurrences of a target number?

Here’s the **Java implementation** of your **Leetcode 34 – First Variant**, where the **goal is to return the number of occurrences** of a given target in a sorted array.

We’ll use **two binary searches**:

* One to find the **first occurrence**
* Another to find the **last occurrence**

---

## ✅ Java Code with Telugu Comments (Transliterated)

```java
public class TargetOccurrencesCounter {

    public int countOccurrences(int[] nums, int target) {
        int n = nums.length;

        // ✅ Edge case: empty array
        if (n == 0) return 0;

        // ✅ Target bound check: target out of range
        if (target < nums[0] || target > nums[n - 1]) return 0;

        // 🔍 First occurrence find cheyyadam
        int first = findFirst(nums, target);

        // ⚠️ If first occurrence not found, then no target
        if (first == -1) return 0;

        // 🔍 Last occurrence find cheyyadam
        int last = findLast(nums, target);

        // 🧮 Total count = last - first + 1
        return last - first + 1;
    }

    // 🔍 First occurrence binary search (left bound)
    private int findFirst(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        int first = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] >= target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        // Validate target match
        if (left < nums.length && nums[left] == target) {
            return left;
        }

        return -1;
    }

    // 🔍 Last occurrence binary search (right bound)
    private int findLast(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        int last = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return right;
    }
}
```

---

## ✅ Sample Test Driver

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        TargetOccurrencesCounter counter = new TargetOccurrencesCounter();

        int[][] testArrays = {
            {5, 7, 7, 8, 8, 10},
            {5, 7, 7, 8, 8, 10},
            {},
            {1},
            {1},
            {2, 2, 2, 2, 2},
            {2, 2, 2, 2, 2},
            {1, 3, 5, 7, 9, 11},
            {1, 3, 5, 7, 9, 11}
        };

        int[] targets = {8, 6, 0, 1, 2, 2, 1, 5, 4};

        for (int i = 0; i < testArrays.length; i++) {
            int[] nums = testArrays[i];
            int target = targets[i];
            int result = counter.countOccurrences(nums, target);
            System.out.println("Input: " + Arrays.toString(nums) + ", Target: " + target);
            System.out.println("Count of Occurrences: " + result);
            System.out.println();
        }
    }
}
```

---

## ✅ Time & Space Complexity

| Metric | Value    |
| ------ | -------- |
| Time   | O(log N) |
| Space  | O(1)     |

Because we’re performing **two binary searches** independently.

---

## ✅ Interview Tip

> “To count target occurrences in a sorted array, I apply binary search to find the **leftmost** and **rightmost** positions. Their difference + 1 gives the total count. The logic ensures edge cases like no match, all same elements, or single occurrences are handled cleanly in O(log N) time.”

---

Would you like to combine this into a single reusable method that returns both `[first, last, count]`?

Absolutely! The **easiest and most efficient way** to **remember and implement** this kind of binary search problem — like Leetcode 34 and its variants — is to follow a simple, repeatable **pattern-based structure**.

---

## ✅ GOAL: Count Occurrences of a Target in Sorted Array

We do this by:

> 🔢 `count = findLast() - findFirst() + 1`

---

## ✅ Memorization Strategy: “Left Bias” and “Right Bias” Binary Search

Instead of writing two completely different binary searches, use a **unified binary template** with a **directional flag**.

---

### ✅ Template Function

```java
// Reusable binary search that finds either the left or right bound
private int findBound(int[] nums, int target, boolean findFirst) {
    int left = 0, right = nums.length - 1;
    int bound = -1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            bound = mid; // Potential answer

            // Directional bias
            if (findFirst) {
                right = mid - 1; // go left
            } else {
                left = mid + 1;  // go right
            }
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return bound;
}
```

---

### ✅ Main Function Using Template

```java
public int countOccurrences(int[] nums, int target) {
    int first = findBound(nums, target, true);
    if (first == -1) return 0; // target not found

    int last = findBound(nums, target, false);
    return last - first + 1;
}
```

---

### ✅ Key to Remember

Just **one function**:

* If `findFirst == true`: keep moving `right = mid - 1`
* If `findFirst == false`: keep moving `left = mid + 1`

🔁 Only the **direction changes**, logic is the same.

---

### 🔁 Why This Is Efficient to Memorize

* ✅ No code repetition
* ✅ Only one function to learn
* ✅ Reusable for multiple variants:

  * First/Last occurrence
  * Count of duplicates
  * Find insert position

---

## ✅ Time & Space Complexity

| Operation          | Complexity              |
| ------------------ | ----------------------- |
| `findBound`        | O(log N)                |
| `countOccurrences` | O(log N) × 2 = O(log N) |
| Space              | O(1)                    |

---

## ✅ Interview One-Liner

> “I use two binary searches: one for the left bound and one for the right bound, both using a shared function with a directional flag. This ensures consistent logic and gives me O(log N) time complexity with minimal space.”

---

Would you like a reusable utility class for this binary search with even more variants?


