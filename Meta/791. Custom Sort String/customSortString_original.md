Absolutely! Here's the **Java version** of the `customSortString` problem (Leetcode 791) with:

* ✅ Clean structure
* ✅ Telugu-style comments (transliterated in English)
* ✅ Time and Space Complexity analysis
* ✅ Edge case-friendly logic
* ✅ Sample test cases (as a main method)

---

## ✅ Java Code with Detailed Telugu Comments

```java
import java.util.*;

public class Solution {
    public String customSortString(String order, String s) {
        // Step 1: Frequency map ni build cheddam for 's' string
        Map<Character, Integer> freq = new HashMap<>();
        for (char ch : s.toCharArray()) {
            freq.put(ch, freq.getOrDefault(ch, 0) + 1);
        }

        // Step 2: Result build cheyyadam ki StringBuilder use cheddam
        StringBuilder result = new StringBuilder();

        // Step 3: 'order' lo unna characters ni order lo result lo add cheddam
        for (char ch : order.toCharArray()) {
            if (freq.containsKey(ch)) {
                int count = freq.get(ch);
                // ch ni count times append cheyyadam
                for (int i = 0; i < count; i++) {
                    result.append(ch);
                }
                freq.remove(ch); // already used characters remove cheyyadam
            }
        }

        // Step 4: 'order' lo leni remaining characters ni append cheyyadam
        for (Map.Entry<Character, Integer> entry : freq.entrySet()) {
            char ch = entry.getKey();
            int count = entry.getValue();
            for (int i = 0; i < count; i++) {
                result.append(ch);
            }
        }

        return result.toString();
    }

    // ✅ Sample Test Cases
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.customSortString("cba", "abcdabc")); // Example: ccbbaad
        System.out.println(sol.customSortString("xyz", "abc"));     // Output: abc (order lo characters ledu)
        System.out.println(sol.customSortString("abc", "abcabc"));  // Output: aabbcc
        System.out.println(sol.customSortString("bca", "aabbccdd")); // Output: bbccaadd
    }
}
```

---

## 🧠 Example Walkthrough

```java
order = "cba"
s = "abcdabc"
```

* Frequency map of `s`: `{a=2, b=2, c=2, d=1}`
* First append c → "cc"
* Then b → "ccb"
* Then a → "ccbb"
* Remaining: d → "ccbbaad"

---

## 🕰️ Time and Space Complexity

### ✅ Time Complexity: `O(n + m)`

* `n = length of s` → building frequency map
* `m = length of order` → iterating through custom order
* Remaining characters loop → `O(n)` worst case

### ✅ Space Complexity: `O(n)`

* HashMap for `s` frequencies → O(n)
* Result StringBuilder → O(n) characters

---

Would you like:

* 🔄 A version that preserves the relative order for characters not in `order`?
* 🔧 An optimized streaming approach without HashMap?
* 📦 JUnit-based unit tests for the same problem?

Let me know!
