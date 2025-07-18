To easily remember the solution for **Leetcode 249: Group Shifted Strings**, you can break it into **5 easy-to-remember steps**. This problem is like grouping anagrams — **but based on shift patterns** (e.g., `"abc" -> "bcd" -> "cde"` all have same relative character difference).

---

### ✅ Problem Summary

Group strings that belong to the **same shifting sequence**.
For example:
`["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]` → group strings that can be shifted to match each other.

---

### ✅ 5-Step Approach to Remember the Solution:

#### 1️⃣ **Understand the concept of "shifting group"**

* All strings in a group have the **same letter-to-letter difference** between characters.
* Example:

  * `"abc"` → `'b'-'a' = 1`, `'c'-'b' = 1`
  * `"bcd"` → `'c'-'b' = 1`, `'d'-'c' = 1`
  * They match.

#### 2️⃣ **Use normalization via shifting to 'a'**

* Convert every string so that its **first character becomes 'a'** by subtracting the shift.
* `"bcd"` becomes `"abc"`, `"xyz"` becomes `"abc"`, so they map to same normalized key.

#### 3️⃣ **Use a HashMap to group by the normalized key**

* Key: normalized string (e.g., `"abc"` for `"bcd"` and `"xyz"`)
* Value: list of original strings with same normalized key.

#### 4️⃣ **Edge case: shift wraps around**

* When subtracting, if the character goes before `'a'`, add 26.
* `'a' - 1 = '`'`→ needs fix →`'z' + 1`=`'a'\`.

#### 5️⃣ **Build final result from map values**

* Each list in map represents a valid group.

---

### 🔁 How to Memorize the Normalization Function (`getShiftKey`)

```java
int shift = input.charAt(0) - 'a'; // how much to shift to make first char 'a'
for (char c : input.toCharArray()) {
    int normalized = c - shift;
    if (normalized < 'a') normalized += 26;
    builder.append((char) normalized);
}
```

📌 **Trick**: Always shift first letter to `'a'`, adjust others accordingly.

---

### 🧠 Mnemonic to Remember:

> **"Group by shape after sliding to 'a'"**

* **"Shape"** = normalized form.
* **"Sliding to 'a'"** = make the first character of each string `'a'` by subtracting shift.

---

### ⏱ Time and Space Complexity

| Complexity | Value                                        |
| ---------- | -------------------------------------------- |
| Time       | `O(N * L)` — N = num strings, L = avg length |
| Space      | `O(N * L)` — storing groups in HashMap       |

---

Would you like a dry run example with this logic?
