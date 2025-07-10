# // VARIANT: What if you had to optimize the time complexity of your solution?
Great! You're working with a **variant of the "Custom Sort String"** problem where:

✅ The input `s` and `order` are guaranteed to contain only **lowercase English letters**, and
✅ We use a **fixed-size array (length 26)** to optimize both time and space.

---

Here’s the **Java version** of this **efficient variant** with:

* 🧠 Optimized logic using frequency array
* 📌 Telugu + English comments
* ⏱️ Time and Space complexity analysis
* ✅ Clean code structure and sample test case

---

## ✅ Java Code with Detailed Telugu Comments

```java
public class Solution {
    public String customSortString(String order, String s) {
        // Step 1: Frequency array create cheddam (a-z = 26 letters)
        // Telugu: a-z characters ki occurrence count store cheyyadam
        int[] freq = new int[26];

        // Step 2: Count frequency of each character in 's'
        for (char ch : s.toCharArray()) {
            freq[ch - 'a']++; // Telugu: 'a' base index calculate cheyyadam
        }

        // Step 3: Result build cheyyadam using StringBuilder
        StringBuilder result = new StringBuilder();

        // Step 4: 'order' lo unna characters ni correct order lo add cheyyadam
        for (char ch : order.toCharArray()) {
            int index = ch - 'a';
            while (freq[index] > 0) {
                result.append(ch);
                freq[index]--; // Telugu: used character ni decrease cheyyadam
            }
        }

        // Step 5: Remaining characters (not in 'order') ni add cheyyadam
        for (int i = 0; i < 26; i++) {
            while (freq[i] > 0) {
                result.append((char) ('a' + i));
                freq[i]--;
            }
        }

        return result.toString();
    }

    // ✅ Sample Test Case
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.customSortString("cba", "abcdabc")); // Output: "ccbbaad"
    }
}
```

---

## 🕰️ Time & Space Complexity

### ✅ Time Complexity: `O(n + m)`

* `n = s.length()` → Frequency count
* `m = order.length()` → Order character loop
* Final loop is constant 26 → total still linear

### ✅ Space Complexity: `O(1)`

* Frequency array is **fixed-size (26 elements)** → constant space
* Result uses extra space proportional to `s.length()` but it’s required for output

---

## 🔍 Example Walkthrough

```java
order = "cba"
s = "abcdabc"
```

1. Frequencies: `{a=2, b=2, c=2, d=1}`
2. Output:

   * From order: `cc`, `bb`, `aa` → `"ccbbaa"`
   * Remaining: `d` → `"ccbbaad"`

---

Would you like:

* ☑️ A version that supports **uppercase / Unicode**?
* ☑️ A version that **preserves relative order** of the characters not in `order`?
* ☑️ A version that is **stream-optimized**?

Let me know what to explore next!
