Here's a **detailed explanation with comments** for your solution to **"Custom Sort String"** (Leetcode 791):

---

### ✅ Problem Summary

Given:

* A custom order string `order` (a permutation of unique letters),
* A string `s` (can contain duplicates),

**Goal**: Reorder `s` so that the characters in `order` appear first (in the same order as `order`), followed by any leftover characters (in any order).

---

### ✅ Python Code with Detailed Comments

```python
from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Step 1: Count frequency of each character in s
        freq = Counter(s)

        # Step 2: Initialize result list
        result = []

        # Step 3: Add characters from s that are in the custom order
        for char in order:
            if char in freq:
                result.extend([char] * freq[char])  # Add char `freq[char]` times
                freq[char] = 0  # Mark it as used

        # Step 4: Add remaining characters not in `order`
        for remaining_char, f in freq.items():
            if f > 0:
                result.extend([remaining_char] * f)

        # Step 5: Return as a string
        return "".join(result)
```

---

### 🧠 Example Walkthrough

```python
order = "cba"
s = "abcdabc"
```

* Frequency of `s`: `{'a':2, 'b':2, 'c':2, 'd':1}`
* Output: All `c`, then all `b`, then all `a`, then the leftover `d`

👉 Result: `"ccbbaa" + "d"` → `"ccbbaad"`

---

### 🕰️ Time and Space Complexity

* **Time Complexity**: O(n + m)

  * n = length of `s`, for `Counter(s)`
  * m = length of `order`, for iteration
* **Space Complexity**: O(n) for `Counter` and result list

---

### ✅ Test Cases

```python
assert Solution().customSortString("cba", "abcdabc") in ["ccbbaad"]
assert Solution().customSortString("xyz", "abc") in ["abc"]  # None in order
assert Solution().customSortString("abc", "abcabc") == "aabbcc"
assert Solution().customSortString("bca", "aabbccdd") == "bbccaadd"
```

---

Would you like:

* A Java version?
* A version that preserves relative order for chars not in `order`?
* An in-place or streaming optimization?
