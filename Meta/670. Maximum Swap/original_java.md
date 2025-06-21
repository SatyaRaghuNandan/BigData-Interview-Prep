Here's the **detailed Java implementation** of the `maximumSwap` problem, including:

* ✅ Full logic explanation
* ✅ Transliteration of **Telugu comments**
* ✅ Time and space complexity

---

## ✅ Problem: [Leetcode 670 - Maximum Swap](https://leetcode.com/problems/maximum-swap/)

**Given** a non-negative integer, you can swap two digits **at most once** to get the maximum valued number.
Return the maximum number you can get.

---

## ✅ Java Code with Telugu Comments

```java
class Solution {
    public int maximumSwap(int num) {
        // 🧮 Step 1: Number ni string ga convert cheyyadam
        char[] digits = Integer.toString(num).toCharArray();

        // 🗺️ Step 2: Prati digit (0 to 9) yokka last occurrence ni store cheyyadam
        int[] rightMostIndex = new int[10];
        for (int i = 0; i < digits.length; i++) {
            rightMostIndex[digits[i] - '0'] = i;
        }

        // 🔁 Step 3: Left nunchi iterate cheyyadam, bigger digit right side lo vunte swap cheyyadam
        for (int i = 0; i < digits.length; i++) {
            // 9 nunchi current digit kanna pedda digit vunte adi check cheyyali
            for (int d = 9; d > digits[i] - '0'; d--) {
                // Right lo (i ki taruvata) d digit vunte swap cheyyadam
                if (rightMostIndex[d] > i) {
                    // ↔️ Swap cheyyadam
                    char temp = digits[i];
                    digits[i] = digits[rightMostIndex[d]];
                    digits[rightMostIndex[d]] = temp;

                    // 📦 Final ga, swapped array ni number ga convert cheyyadam
                    return Integer.parseInt(new String(digits));
                }
            }
        }

        // 😐 Swap chesina use lekapote, original number return cheyyadam
        return num;
    }
}
```

---

## 🧠 Dry Run Example

Input: `2736`

* `rightMostIndex = [0,0,...,3,2,1,...]`
* Start with `2` → check if `9`, `8`, `7` exist after position `0`
* `7` exists at index 1 → **swap 2 and 7** → `7236`

---

## ✅ Time and Space Complexity

| Operation               | Complexity                                  |
| ----------------------- | ------------------------------------------- |
| String conversion       | `O(n)`                                      |
| Build `rightMostIndex`  | `O(n)`                                      |
| Swap scan (nested loop) | `O(n * 10)` ⇒ `O(n)` (constant digit space) |
| Space (array + chars)   | `O(1)` (constant space for digits)          |

---

## ✅ Final Complexity:

* **Time:** `O(n)`
* **Space:** `O(1)` (since digits max = 10)

---

Let me know if you want to add test cases, optimize further, or explore a recursive variant!
