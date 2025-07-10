# // VARIANT: What if you could only consider a limited set of characters as a part of
# // a potential palindrome?

Here's the **Java conversion** for both:

---

## ✅ Original Problem (Leetcode 125): Valid Palindrome

### ✅ Java Code with Telugu-style Comments

```java
public class ValidPalindrome {

    // ✅ Check if input string is a valid palindrome (ignoring non-alphanumeric)
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        // 🧭 Two-pointer approach
        while (left < right) {

            // 🔁 Left pointer ni alphanumeric varaku move cheyyadam
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            // 🔁 Right pointer ni alphanumeric varaku move cheyyadam
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            // 🔍 Compare lower-cased characters
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
```

---

### ✅ Time and Space Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(N)       |
| Space  | O(1)       |

* `N = length of the string`
* We scan each character at most once with 2 pointers

---

## ✅ Variant: Valid Palindrome with Custom Inclusion Set

### ✅ Java Code with Telugu-style Comments

```java
import java.util.*;

public class ValidPalindromeVariant {

    // ✅ Only check characters in `includeSet` for palindrome check
    public boolean isPalindrome(String s, List<Character> include) {
        Set<Character> includeSet = new HashSet<>(include);
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {

            // 🔁 Left pointer ni included character varaku move cheyyadam
            while (left < right && !includeSet.contains(s.charAt(left))) {
                left++;
            }

            // 🔁 Right pointer ni included character varaku move cheyyadam
            while (left < right && !includeSet.contains(s.charAt(right))) {
                right--;
            }

            // ✅ Compare characters directly (case-sensitive)
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
```

---

### ✅ Time and Space Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(N)       |
| Space  | O(K)       |

* `N = length of string`
* `K = size of inclusion set` (stored in HashSet for O(1) lookup)

---

## ✅ Differences at a Glance

| Feature          | Original Leetcode 125 | Variant                   |
| ---------------- | --------------------- | ------------------------- |
| Char Filter      | Alphanumeric          | Custom set (`include[]`)  |
| Case Sensitivity | Case-insensitive      | Case-sensitive            |
| Empty string     | Returns `true`        | Returns `true`            |
| Optimization     | Two-pointer, linear   | Same (HashSet for lookup) |

---

Would you like a **case-insensitive version** of the variant as well? Or should we convert the `List<Character>` into a more efficient input like `String` or `char[]`?
