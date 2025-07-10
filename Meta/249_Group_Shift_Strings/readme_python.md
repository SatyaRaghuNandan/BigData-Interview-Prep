# // VARIANT: What if you had to right shift a given string by a given rotational factor?

Absolutely! You're comparing two different but **related string manipulation problems** — the **original Group Shifted Strings** vs this **Rotational Cipher variant**. Let's break down the differences and explain what *Rotational Cipher* means.

---

## ✅ Rotational Cipher – What Is It?

A **Rotational Cipher (Caesar Cipher)** is a basic encryption method where:

* Each **letter or digit** is "rotated" (i.e., shifted) by a fixed number of positions.
* For example, if `rotationFactor = 3`, then:

  * `'a' → 'd'`, `'z' → 'c'`
  * `'7' → '0'` (wraps around 0-9)
  * Non-alphanumeric characters stay the same

This problem focuses on **rotating the entire string's characters** by a given rotation factor.

---

## ✅ Group Shifted Strings – Original Problem (Leetcode 249)

In contrast, **Group Shifted Strings** is about grouping multiple strings that have the same **relative character shifts**.

For example:

```java
Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
Output: [["abc","bcd","xyz"],["az","ba"],["acef"],["a","z"]]
```

🔁 Here, you're not rotating a string by a number.
Instead, you’re checking if strings have the **same shifting pattern**.

---

## ✅ 🔄 Core Differences

| Feature                   | Group Shifted Strings                  | Rotational Cipher (Variant)                     |
| ------------------------- | -------------------------------------- | ----------------------------------------------- |
| **Input**                 | List of strings                        | One string + one rotation factor                |
| **Goal**                  | Group strings with same char shifts    | Shift individual letters/digits by rotation     |
| **Rotation factor**       | Not given, inferred from pairs         | Given directly as an input                      |
| **Application**           | Pattern classification/grouping        | Encryption/obfuscation                          |
| **Example logic**         | "abc" → "bcd" is shift by +1 all chars | "Zebra" + 3 → "Cheud"                           |
| **Letters/digits/others** | Focuses only on lowercase letters      | Handles letters, digits, and symbols separately |

---

## ✅ Recap: What’s Rotational Cipher?

* A rotational cipher is a type of **monoalphabetic cipher**.
* It's **not** dependent on comparing strings.
* Just **rotate each character individually**.
* Often used in puzzles and beginner encryption problems.

---

## ✅ When to Use Each?

| Use Case                             | Choose This Approach      |
| ------------------------------------ | ------------------------- |
| Grouping words with similar patterns | **Group Shifted Strings** |
| Encoding/Obfuscation of data         | **Rotational Cipher**     |
| Input is a list of words             | Group Shifted Strings     |
| Input is a string + a number         | Rotational Cipher         |

---

## ✅ Summary

* **Group Shifted Strings** → pattern-based grouping across **multiple words**
* **Rotational Cipher** → transform **one string** using a fixed `rotationFactor`

---

Would you like:

* 🔁 The **decryption** logic for Rotational Cipher?
* 🧩 Rotational Cipher with only digits or only uppercase?
* 🎯 Group Shifted String implemented with **hashing** and **grouping** logic?

Let me know how you'd like to explore further!


Absolutely! Below is your **Rotational Cipher Java code** with detailed **Telugu-style comments (transliterated in English)** to help you understand and memorize it better.

---

## ✅ Final Code with Telugu Comments

```java
public class RotationalCipher {

    // ✅ Idi main function that takes input string and rotation factor
    public String rotationalCipher(String input, int rotationFactor) {
        // Result store cheyyadaniki
        StringBuilder result = new StringBuilder();

        // ✅ String ni oka character-by-character process cheddam
        for (char ch : input.toCharArray()) {
            
            if (Character.isLowerCase(ch)) {
                // 👉 Idi lowercase letter (a-z)
                // ch - 'a' → position lo convert chesthundi (0 to 25)
                // +rotationFactor apply chesi wrap cheyyali using % 26
                // Final ga, 'a' add chesi ASCII lo convert cheyyadam
                char shifted = (char) ((ch - 'a' + rotationFactor) % 26 + 'a');
                result.append(shifted);

            } else if (Character.isUpperCase(ch)) {
                // 👉 Idi uppercase letter (A-Z)
                // Similar logic with base as 'A'
                char shifted = (char) ((ch - 'A' + rotationFactor) % 26 + 'A');
                result.append(shifted);

            } else if (Character.isDigit(ch)) {
                // 👉 Idi digit (0-9)
                // Use % 10 to wrap around 0-9
                char shifted = (char) ((ch - '0' + rotationFactor) % 10 + '0');
                result.append(shifted);

            } else {
                // 👉 Idi alphanumeric kaadhu (symbols, punctuation, etc.)
                // Avi unchanged ga unchali
                result.append(ch);
            }
        }

        // ✅ Final rotated string return cheyyadam
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

        // ✅ Test Case 3 (Edge case: special characters and digits)
        System.out.println(sol.rotationalCipher("Zebra-493?", 3));
        // Expected: "Cheud-726?"

        // ✅ Test Case 4 (Wrap check: max wrap of characters)
        System.out.println(sol.rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39));
        // Expected: "nopqrstuvwxyzABCDEFGHIJKLM9012345678"
    }
}
```

---

## ✅ Summary of Logic

| Type of Char | Base  | Modulo | Formula                     |
| ------------ | ----- | ------ | --------------------------- |
| Lowercase    | `'a'` | `% 26` | `(ch - 'a' + r) % 26 + 'a'` |
| Uppercase    | `'A'` | `% 26` | `(ch - 'A' + r) % 26 + 'A'` |
| Digit        | `'0'` | `% 10` | `(ch - '0' + r) % 10 + '0'` |
| Other        | —     | —      | No change                   |

---

## ✅ Time & Space Complexity

| Metric    | Value                           |
| --------- | ------------------------------- |
| Time      | O(n)                            |
| Space     | O(n)                            |
| In-place? | ❌ (Creates a new result string) |

---

Let me know if you want:

* 🔁 Reverse (decryption) logic
* 🧪 JUnit test cases
* 📜 Rotation with different factors for letters vs digits

Would you like to implement this in Python next or optimize for stream-based input?




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
