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





Great follow-up. Yes — your understanding is **mostly correct**, and let’s make it **crystal clear**.

---

## ✅ Question Recap (LeetCode 670 – Maximum Swap)

> You are given an integer `num`.
> You can **swap two digits at most once** to get the maximum valued number.
> Return the maximum valued number you can get.

---

## 🤔 Why TWO `return` statements?

### ✅ Return #1 (inside loop):

```java
return Integer.parseInt(new String(digits));
```

* If a valid **swap is found**, do the swap and **return immediately**.
* This is the **only swap you're allowed** (since problem says: *at most once*).
* You **don't need to continue** — the greedy approach guarantees the best answer.

---

### ✅ Return #2 (at end):

```java
return num;
```

* This happens **only when no swap is ever made**.
* Which means: the digits are already in the best order possible (e.g. `9876` or `9973`)
* So, in that case, **no swap is needed**, and you just return the original number.

---

## ✅ Example 1: `2736`

* First digit = `2`
* You see `7` later → Swap to get `7236` → return immediately

✅ Early return after **one valid swap**

---

## ✅ Example 2: `9973`

* Already in maximum form — no digit after a smaller one
* Inner loop **never finds a swap**
* No `return` happens inside loop
* So fallback is: `return num` → returns `9973`

✅ No return inside loop → hits the final return

---

## ✅ Why Not Just One Return?

You **can** technically write it with one return like this:

```java
boolean swapped = false;

... // loop and swap if needed

if (swapped) return new number;
else return original;
```

But in this optimized version:

* We **exit early** as soon as we find the best possible result (greedy)
* We **avoid unnecessary tracking (e.g. boolean flags)**
* It's simpler and more efficient

---

## 🔁 Summary

| Situation           | What Happens                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------- |
| Valid swap found    | Swap → return new number                                                                    |
| No valid swap found | Just return original number                                                                 |
| Why two returns?    | Because only **one swap** is allowed, and if we don't use it, we return the original number |

---

Would you like to refactor this to a version with **one return**, or visualize this with a dry-run stack trace?



