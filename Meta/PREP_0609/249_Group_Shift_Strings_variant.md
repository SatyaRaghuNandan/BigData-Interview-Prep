Great — you're sharing a **variant of LeetCode 249**, inspired by **"rotational ciphers"** like the **Caesar Cipher**.

---

## 🔁 Problem Variant:

> Right shift every letter or digit in the string by a given **rotation factor**:

* Lowercase letters `a-z` wrap within `a-z`
* Uppercase letters `A-Z` wrap within `A-Z`
* Digits `0-9` wrap within `0-9`
* Non-alphanumeric characters remain unchanged

This is known as a **Rotational Cipher** or **Caesar Cipher with variable rotation**.

---

## ✅ Python Version with Detailed Telugu Comments

```python
class Solution:
    def rotationalCipher(self, s: str, rotation_factor: int) -> str:
        # Final result store cheyyadam kosam
        result = []

        for ch in s:
            # Lowercase character unte
            if ch.islower():
                # ASCII lo 'a' ni base ga teesukoni right shift apply cheyyadam
                shifted = (ord(ch) - ord('a') + rotation_factor) % 26 + ord('a')
                result.append(chr(shifted))

            # Uppercase character unte
            elif ch.isupper():
                # ASCII lo 'A' ni base ga teesukoni right shift
                shifted = (ord(ch) - ord('A') + rotation_factor) % 26 + ord('A')
                result.append(chr(shifted))

            # Digit unte
            elif ch.isdigit():
                # 0-9 range lo rotate cheyyadam
                shifted = (ord(ch) - ord('0') + rotation_factor) % 10 + ord('0')
                result.append(chr(shifted))

            # Special character or symbol → unchanged
            else:
                result.append(ch)

        return ''.join(result)
```

---

## 🧪 Example

```python
sol = Solution()
print(sol.rotationalCipher("All-convoYs-9-be:Alert1.", 4))
# Output: "Epp-gsrzsCw-3-fi:Epivx5."

print(sol.rotationalCipher("abcdZXYzxy-999.@", 200))
# Output: "stuvRPQrpq-999.@"
```

---

## 🔍 How It Works:

### For each character:

* If **lowercase**: `'a' → 'z'` stays within that range
* If **uppercase**: `'A' → 'Z'`
* If **digit**: `'0' → '9'`
* Else: keep it unchanged (punctuation, symbols)

All use this formula:

```python
(ord(ch) - base + rotation_factor) % length + base
```

---

## ✅ Time & Space Complexity:

| Metric    | Value  |
| --------- | ------ |
| **Time**  | `O(n)` |
| **Space** | `O(n)` |

* Each character is processed once

---

## 📦 Use Cases:

* Data obfuscation
* Lightweight encryption
* Time-based token generation
* Interview question (similar to Caesar Cipher / ROT13)

---

Let me know if you want to:

* Decode the message (reverse rotation)
* Extend it to rotate **Unicode or emoji** characters
* Handle rotation on words instead of characters



```text
Edge Case Test Results
You've tested:

python
Copy
Edit
assert rotationalCipher("Zebra-493?", 3) == "Cheud-726?"
assert rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39) == "nopqrstuvwxyzABCDEFGHIJKLM9012345678"
These are perfect tests:

The first checks lowercase, uppercase, digits, and special characters.

The second checks rotation factor > 26 (modulo logic correctness) for both alphabets and digits.


```
