This updated version of `isNumber` is a **simplified validator** that handles only **integers and decimals**, **without supporting scientific notation (`e`, `E`)**. Here's a breakdown with full comments and analysis.

---

### ✅ What This Version Supports:

It accepts:

* Pure **integers**: `"0089"`, `"+3"`, `"-10"`
* **Decimals** (with or without leading digits): `"4."`, `"-.9"`, `"+3.14"`

It rejects:

* Scientific notation like `"3e+7"`, `"53.5e93"`
* Any alphabets or special characters
* Invalid formats like `"7.."`, `"."`, `"+7e5"`

---

### ✅ Code With Detailed Comments (Telugu-style, English transliterated)

```python
class Solution(object):
    def isNumber(self, s: str):
        # flags to check digits and dot
        seen_digit, seen_dot = [False, False]

        for i in range(len(s)):
            if s[i].isdigit():
                seen_digit = True  # digit ochindhi, so far valid
            elif s[i] in {"+", "-"}:
                # sign only at start allowed
                if i != 0:
                    return False
            elif s[i] == ".":
                # dot should not repeat
                if seen_dot:
                    return False
                seen_dot = True
            else:
                # vere character unte invalid
                return False

        # final validation lo at least 1 digit compulsory
        return seen_digit
```

---

### ✅ Time & Space Complexity

* **Time Complexity**: `O(n)` — full string scan
* **Space Complexity**: `O(1)` — constant flags

---

### ✅ Output Table Comparison

| Input      | Result | Reason                          |
| ---------- | ------ | ------------------------------- |
| `"0089"`   | ✅      | Valid integer                   |
| `"-0.1"`   | ✅      | Valid negative decimal          |
| `"4."`     | ✅      | Valid decimal with dot          |
| `".9"`     | ✅      | Valid decimal                   |
| `"3e+7"`   | ❌      | `e` not allowed in this version |
| `"abc"`    | ❌      | Letters not allowed             |
| `"1e"`     | ❌      | `e` not handled                 |
| `"7.."`    | ❌      | Multiple dots                   |
| `"."`      | ❌      | No digits at all                |
| `"+20e-5"` | ❌      | Exponent not supported          |

---

### 🆚 Difference from Full `isNumber()` Version:

| Feature                    | Full Version | This Version       |
| -------------------------- | ------------ | ------------------ |
| Supports `e`, `E`          | ✅ Yes        | ❌ No               |
| Supports sign at any place | ✅ (if valid) | ❌ Only start       |
| Supports decimals          | ✅            | ✅                  |
| Complex format checks      | ✅ DFA-like   | ❌ Simple scan only |

---

Let me know if you want a **regular expression (regex)** version or a **state machine (DFA)** version for completeness.
