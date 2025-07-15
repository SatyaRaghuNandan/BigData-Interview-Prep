
---

### 🔁 Interview Framing (How to Speak):

> “The brute force approach checks each element and its neighbors in O(n) time.
> But we can optimize it using binary search.
> The insight is: if the slope is rising (`nums[mid] < nums[mid+1]`), then a peak must exist on the right.
> If the slope is falling, then a peak must be on the left or at mid.
> We shrink the window accordingly until `left == right`, which is guaranteed to be a peak.
> This gives us O(log n) time and constant space.”

---

Absolutely! Below is the **Java implementation** of the **`findPeakElement`** problem (Leetcode 162) using the optimal **binary search approach**.

---

## ✅ Problem Summary

> Given an array `nums`, find a **peak element** and return its index.
> A peak is an element strictly greater than its neighbors.
> You may assume that `nums[-1] = nums[n] = -∞` (virtual boundary).

---

## ✅ Java Code (Binary Search) with Telugu + English Comments

```java
class Solution {
    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        // Telugu: Binary Search apply cheyyadam
        while (left < right) {
            int mid = left + (right - left) / 2; // Overflow avoid cheyyadam kosam

            // Telugu: mid value kanna right side value ekkuva undi ante → peak right lo untundi
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1; // Telugu: right side search continue cheyyadam
            } else {
                // Telugu: mid peak kaani possibility undi. So include left side
                right = mid;
            }
        }

        // Telugu: Left == right ayyaka loop break avutundi → Peak found
        return left; // Or right (same)
    }
}
```

---

## ✅ Time & Space Complexity

| Metric               | Value      | Explanation                    |
| -------------------- | ---------- | ------------------------------ |
| **Time Complexity**  | `O(log n)` | Binary Search halves each step |
| **Space Complexity** | `O(1)`     | No extra memory used           |

---

## ✅ Sample Input/Output

```java
Input: [1, 2, 3, 1]
Output: 2  // nums[2] = 3 is a peak

Input: [1, 2, 1, 3, 5, 6, 4]
Output: 1 or 5  // nums[1]=2 and nums[5]=6 are both valid peaks
```

---

## 🧠 Why Does This Work?

* If `nums[mid] < nums[mid + 1]`, then peak must lie **to the right**
* Else, a peak lies **on the left or at mid**
* Eventually, `left == right` → that index is a peak (guaranteed by the problem)

---

## ✅ Edge Cases Covered

| Input             | Output | Explanation                              |
| ----------------- | ------ | ---------------------------------------- |
| `[1]`             | `0`    | Single element is a peak                 |
| `[2, 1]`          | `0`    | First element is a peak                  |
| `[1, 2]`          | `1`    | Last element is a peak                   |
| `[1, 2, 3, 4, 5]` | `4`    | Monotonically increasing → last is peak  |
| `[5, 4, 3, 2, 1]` | `0`    | Monotonically decreasing → first is peak |

---

## 📌 Optional Variation: Safer Version with Bounds

```java
if (mid < nums.length - 1 && nums[mid] < nums[mid + 1]) {
    left = mid + 1;
} else {
    right = mid;
}
```

This ensures you never go out of bounds. But in this exact implementation, `mid + 1` is safe because the loop always maintains `left < right`.

---

## ✅ Final Thought

This is **Meta-level efficient**:

* Optimal `O(log n)` solution
* Clean and boundary-safe
* No extra space

Would you like the:

* 🔁 **Recursive version** of this approach?
* 🔄 **2D Peak Element** variant using Divide and Conquer (`O(m log n)`)?
* 🧪 JUnit test cases for verification?

Let me know and I’ll walk you through them!
