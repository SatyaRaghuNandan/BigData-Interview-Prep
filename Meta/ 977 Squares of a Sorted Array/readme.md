Here's a full breakdown of your Java solution to Leetcode **977. Squares of a Sorted Array**:

---

### ✅ **Problem Statement (Simplified):**

You're given a **sorted** array (may contain negatives). Return a **new array** of the squares of each number, also **sorted in non-decreasing order**.

---

### ✅ **Approach: Two Pointer + Fill from End**

#### 🔑 5-Step Strategy (Plain English):

1. The input array is sorted, but negative numbers become large when squared.
2. Use **two pointers**: one at the leftmost number, and one at the rightmost number.
3. Compare their absolute values and square the larger one.
4. Place the square at the **end** of the result array (since largest values go at the end).
5. Continue until you fill the entire array from back to front.

---

### ✅ Java Code with Telugu Comments

```java
class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] result = new int[n]; // Final array to return
        int left = 0;              // Left pointer
        int right = n - 1;         // Right pointer

        // Ika loop back nunchi forward ki chestham, ekkuva value ni end lo pettali kabatti
        for (int i = n - 1; i >= 0; i--) {
            int square;
            // Compare absolute values and move pointers
            if (Math.abs(nums[left]) < Math.abs(nums[right])) {
                square = nums[right]; // Right side value ekkuva unte
                right--;              // Right pointer ni back ki move cheyyi
            } else {
                square = nums[left];  // Left value ekkuva lekapote equal unte
                left++;               // Left pointer ni mundu ki move cheyyi
            }
            result[i] = square * square; // Square ni end position lo pettu
        }

        return result;
    }
}
```

---

### ✅ Time and Space Complexity

| Type             | Complexity |
| ---------------- | ---------- |
| ⏱ Time           | `O(n)`     |
| 🧠 Space (Extra) | `O(n)`     |

* **Time**: We scan the entire array once — `O(n)`
* **Space**: We use a new array of the same size for the result — `O(n)`

---

### 🧠 Easy Way to Remember

* Two ends → Compare absolute values.
* Large square goes to the end of result.
* Move inwards, shrinking window.
* Fill `result[]` **backwards**.

---

If you want the same implementation in **Python**, or want to explore a solution using **sorting directly**, let me know!
