Here’s a detailed breakdown of your `maximumSwap` solution, including:

1. ✅ **Explanation in English and Telugu-style transliteration**
2. ✅ **Time & Space Complexity**
3. ✅ **Step-by-step dry run with example**
4. ✅ **When it returns original number**

---

## ✅ Problem

You’re allowed **one swap** between any two digits of the given number. Return the **maximum number** you can get.

---

## ✅ Code with Detailed Comments (Telugu-style in English)

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        right_most = [-1 for _ in range(10)]  # last occurrence of each digit 0–9
        n = list(str(num))  # number ni list of characters ga marchadam (easy to swap)

        for i, dig in enumerate(n):
            right_most[int(dig)] = i  # prathi digit ki, tana last index ni record chey

        for i, dig in enumerate(n):
            for j in range(9, int(dig), -1):  # check bigger digits than current
                if right_most[j] > i:
                    # manaki bigger digit dorikindhi which occurs later
                    n[right_most[j]], n[i] = n[i], n[right_most[j]]  # swap
                    return int("".join(n))  # final ga string ni integer ga marchi return chey

        return num  # if no better swap possible, return original number
```

---

## ✅ Time and Space Complexity

* **Time Complexity:** `O(n)`

  * One pass to record right-most indices `O(n)`
  * One nested loop of at most `9` per digit ⇒ still linear.
* **Space Complexity:** `O(n)` for converting the number into a list, plus `O(1)` for `right_most` (fixed size 10).

---

## ✅ Dry Run Example

### Input: `2736`

* `n = ['2', '7', '3', '6']`
* `right_most = [_, _, 0, 2, _, _, 3, 1, _, _]`

Now loop over digits:

* At `i = 0` (`digit = 2`), check if there's a higher digit after this.

  * `j = 9 → 8 → 7` → 7 is at index `1` → `1 > 0`
  * ✅ Swap `2` and `7` → becomes `7236`

Output: `7236`

---

## ✅ When It Returns Original Number

If the digits are in **descending order**, e.g., `9876`, there's **no better digit later** to swap with → it returns `num`.

---

## ✅ Example Test Cases

| Input   | Output  | Explanation     |
| ------- | ------- | --------------- |
| `2736`  | `7236`  | Swap 2 and 7    |
| `9973`  | `9973`  | Already max     |
| `98368` | `98863` | Swap 3 and 8    |
| `1234`  | `4231`  | Swap 1 and 4    |
| `1111`  | `1111`  | All digits same |

---

Let me know if you'd like a **variant** (e.g., two swaps allowed or apply to a string instead of number).
