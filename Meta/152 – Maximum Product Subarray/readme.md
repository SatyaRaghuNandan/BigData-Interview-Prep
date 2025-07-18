Great! Let's now go through **Leetcode 152 – Maximum Product Subarray**, which is a **trickier version** of Maximum Sum Subarray.

---

## ✅ Approach in 5 Bullet Points (Plain English)

1. Keep track of **both the current max and min products** (since negative × negative = positive).
2. For each number in the array:

   * If the number is negative, **swap** the current max and min.
3. Update `currentMax` and `currentMin` by either:

   * Starting fresh with the current number, or
   * Extending previous product.
4. At each step, update the global `maxProduct`.
5. Return `maxProduct` at the end.

---

## 🧠 Easy Way to Remember

> "Keep max and min because negatives can flip results – like a double-edged sword."

---

## ✅ Java Code with Telugu Comments

```java
class Solution {
    public int maxProduct(int[] nums) {
        // Starting values – all point to first element
        int maxProduct = nums[0];
        int currentMax = nums[0]; // Ippati varaku maximum product
        int currentMin = nums[0]; // Ippati varaku minimum product (for negative support)

        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];

            // Negative number vachesindhi ante, max ↔ min swap cheyyali
            if (num < 0) {
                int temp = currentMax;
                currentMax = currentMin;
                currentMin = temp;
            }

            // current number tho start cheyyali? or extend cheyyali? choosukovali
            currentMax = Math.max(num, currentMax * num);
            currentMin = Math.min(num, currentMin * num);

            // maxProduct ni update cheyyadam
            maxProduct = Math.max(maxProduct, currentMax);
        }

        return maxProduct;
    }
}
```

---

## ⏱️ Time and Space Complexity

| Complexity | Value | Explanation                          |
| ---------- | ----- | ------------------------------------ |
| **Time**   | O(n)  | One pass through the array           |
| **Space**  | O(1)  | Only variables used, no extra arrays |

---

Let me know if you'd like:

* Dry run example (especially with negatives)
* Python version with Telugu comments
* Variant: Subarray with max product AND return subarray itself

Happy to walk you through it! 🚀
