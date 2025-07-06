Sure! Here's the complete and well-structured **Java version** of the **Rotational Cipher** (variant of Caesar Cipher), including:

✅ Clean code
✅ Full explanation
✅ Example walkthrough
✅ Time & space complexity
✅ Edge cases

---

## ✅ Problem: Rotational Cipher (Caesar Cipher with Variable Rotation)

You are given:

* A string `s`
* An integer `rotationFactor`

### 🔁 Rules:

1. Rotate **letters** within `a-z` or `A-Z`, preserving case
2. Rotate **digits** within `0-9`
3. Leave **non-alphanumeric characters** unchanged

---

## ✅ Java Code (Clean & Easy to Memorize)

```java
public class RotationalCipher {

    public String rotationalCipher(String input, int rotationFactor) {
        StringBuilder result = new StringBuilder();

        for (char ch : input.toCharArray()) {
            if (Character.isLowerCase(ch)) {
                // Lowercase letter rotation (wrap around a-z)
                char shifted = (char) ((ch - 'a' + rotationFactor) % 26 + 'a');
                result.append(shifted);

            } else if (Character.isUpperCase(ch)) {
                // Uppercase letter rotation (wrap around A-Z)
                char shifted = (char) ((ch - 'A' + rotationFactor) % 26 + 'A');
                result.append(shifted);

            } else if (Character.isDigit(ch)) {
                // Digit rotation (wrap around 0-9)
                char shifted = (char) ((ch - '0' + rotationFactor) % 10 + '0');
                result.append(shifted);

            } else {
                // Non-alphanumeric characters remain the same
                result.append(ch);
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        RotationalCipher sol = new RotationalCipher();

        // ✅ Test Case 1
        String input1 = "All-convoYs-9-be:Alert1.";
        int rotationFactor1 = 4;
        System.out.println(sol.rotationalCipher(input1, rotationFactor1));
        // Expected: "Epp-gsrzsCw-3-fi:Epivx5."

        // ✅ Test Case 2
        String input2 = "abcdZXYzxy-999.@";
        int rotationFactor2 = 200;
        System.out.println(sol.rotationalCipher(input2, rotationFactor2));
        // Expected: "stuvRPQrpq-999.@"

        // ✅ Test Case 3 (Edge)
        System.out.println(sol.rotationalCipher("Zebra-493?", 3));
        // Expected: "Cheud-726?"

        // ✅ Test Case 4 (Wrap check)
        System.out.println(sol.rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39));
        // Expected: "nopqrstuvwxyzABCDEFGHIJKLM9012345678"
    }
}
```

---

## 🧠 Explanation

### 🔹 Logic

For each character:

* **Lowercase**: rotate within `'a'`–`'z'`
* **Uppercase**: rotate within `'A'`–`'Z'`
* **Digits**: rotate within `'0'`–`'9'`
* **Symbols/Punctuation**: leave unchanged

### 🔹 Formula (common pattern):

```java
shifted = (original - base + rotation) % range + base;
```

---

## 🔍 Dry Run

### Input:

```java
"Zebra-493?", rotationFactor = 3
```

### Output:

```java
"Cheud-726?"
```

How?

* `'Z'` → `'C'`
* `'e'` → `'h'`
* `'b'` → `'e'`
* `'r'` → `'u'`
* `'a'` → `'d'`
* `'4'` → `'7'`, `'9'` → `'2'`, `'3'` → `'6'`
* `'-'` and `'?'` → unchanged

---

## ✅ Time and Space Complexity

| Metric    | Value | Notes                             |
| --------- | ----- | --------------------------------- |
| **Time**  | O(n)  | `n` = input string length         |
| **Space** | O(n)  | New string builder of same length |

---

## ✅ Edge Case Tests

```java
assert rotationalCipher("Zebra-493?", 3).equals("Cheud-726?");
assert rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39)
       .equals("nopqrstuvwxyzABCDEFGHIJKLM9012345678");
```

* Tests full alphabet wrapping
* Handles large rotation values (`rotationFactor > 26 or > 10`)

---

## ✅ Real World Applications

* Caesar Cipher (historical cryptography)
* Obfuscation for emails/IDs
* Temporary token generation
* Entry-level security exercises

---

Let me know if you want:

* The **reverse/decryption** version
* A version that supports **Unicode emojis**
* Or adds word/phrase level rotation instead of char-by-char.
