
Here's the detailed breakdown for **Leetcode 53 – Maximum Subarray** using **Kadane's Algorithm**.

---

## ✅ Approach in 5 Bullet Points (Plain English)

1. Initialize `maxSum` with smallest value (`-∞`) and `tempSum` with 0.
2. Iterate through each number in the array:
3. Add current number to `tempSum`.
4. Update `maxSum` if `tempSum` is greater than current `maxSum`.
5. If `tempSum` becomes negative, **reset it to 0** (discard that subarray and start fresh).

---

## 🧠 Easy Way to Remember

* **Kadane’s Rule**: "If your running total becomes negative – drop it."
* Think of **building a subarray** as long as it's beneficial.
* If it hurts (i.e., sum < 0), restart from next element.

---

## ✅ Java Code with Telugu Comments

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int length = nums.length;
        
        // maxSum ni -infinity to initialize chesthunnam, ante ekkuva minimum
        int maxSum = Integer.MIN_VALUE;
        
        // tempSum lo current subarray sum ni track chestham
        int tempSum = 0;

        for (int num : nums) {
            // Current number ni tempSum lo add cheyyadam
            tempSum += num;

            // maxSum ni update cheyyali if tempSum is better
            maxSum = Math.max(maxSum, tempSum);

            // tempSum negative ayite, discard cheyyali → next subarray start cheyyali
            if (tempSum < 0) {
                tempSum = 0;
            }
        }

        return maxSum; // final maximum subarray sum
    }
}
```

---

## ⏱️ Time and Space Complexity

| Complexity | Value | Explanation                    |
| ---------- | ----- | ------------------------------ |
| **Time**   | O(n)  | One pass through the array     |
| **Space**  | O(1)  | No extra space, only variables |

---

Let me know if you want:

* Visual dry run
* Negative-only array version
* Variant like **Maximum Product Subarray**

Ready to help 🚀
