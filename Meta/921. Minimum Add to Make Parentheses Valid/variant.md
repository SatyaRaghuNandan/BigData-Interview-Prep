# // VARIANT: What if you had to return the parentheses string itself after the minimum adds?


Absolutely! Let's convert your **C++ variant** of Leetcode 921 — where we return the **corrected string** after adding the **minimum number of parentheses** — into **Java**, with:

✅ **Telugu-style comments**
✅ **Dry run walkthrough**
✅ **Test cases**
✅ **Explanation** of logic and edge handling

---

## ✅ Java Code (with Telugu-style Comments)

```java
public class MinimumAddToMakeValidString {

    public String minAddToMakeValid(String s) {
        StringBuilder result = new StringBuilder();
        int extraOpen = 0;  // ✅ '(' count chestham → match ayyaka inka pending unte

        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                // ✅ Open bracket dorikindi → pending ga unchadam
                extraOpen++;
                result.append(ch);
            } else if (ch == ')') {
                if (extraOpen == 0) {
                    // ✅ ')' ki match ledhu → mundu lo '(' add cheyyadam
                    result.append('(');
                    result.append(')');
                } else {
                    // ✅ match ayindi → '(' use chesi ')' add cheyyadam
                    extraOpen--;
                    result.append(ch);
                }
            } else {
                // ✅ Non-parenthesis character → direct ga add cheyyadam
                result.append(ch);
            }
        }

        // ✅ Loop ayyaka: leftover '(' ki closing ')' add cheyyadam
        while (extraOpen-- > 0) {
            result.append(')');
        }

        return result.toString();
    }

    // ✅ Test Runner with assert-style validation
    public static void main(String[] args) {
        MinimumAddToMakeValidString sol = new MinimumAddToMakeValidString();

        System.out.println(sol.minAddToMakeValid(")))").equals("()()()"));
        System.out.println(sol.minAddToMakeValid("(((").equals("((()))"));
        System.out.println(sol.minAddToMakeValid("").equals(""));
        System.out.println(sol.minAddToMakeValid("(())").equals("(())"));
        System.out.println(sol.minAddToMakeValid(")))(((").equals("()()()((()))"));
        System.out.println(sol.minAddToMakeValid("abcxyz").equals("abcxyz"));
        System.out.println(sol.minAddToMakeValid("(()()))((").equals("(()())()(())"));
        System.out.println(sol.minAddToMakeValid("((a)()))((xyz").equals("((a)())()((xyz))"));
    }
}
```

---

## ✅ Dry Run: `"(()()))(("`

Let’s simulate this string:

```
Input:  "(()()))(("
        ↑
        Step-by-step

Initial:
- extraOpen = 0
- result = ""

Walkthrough:

1. `(` → extraOpen = 1 → result = "("
2. `(` → extraOpen = 2 → result = "(("
3. `)` → match '(' → extraOpen = 1 → result = "(()"
4. `)` → match '(' → extraOpen = 0 → result = "(())"
5. `)` → no '(' → add '(', ')' → result = "(())()"
6. `)` → no '(' → add '(', ')' → result = "(())()()"
7. `(` → extraOpen = 1 → result = "(())()()("
8. `(` → extraOpen = 2 → result = "(())()()(("

Final append: extraOpen = 2 → add 2 `)` → result = "(())()()((()))"

✅ Output: `"(()())()(())"`

---

## ✅ Explanation (Meta-Style)

> “We’re not just counting unmatched parentheses, we’re also **building the corrected string**.
>
> - If we encounter an unmatched `)` (i.e., no `'('` before it), we insert a `'('` **before** it to fix the balance.
> - At the end, if we have unmatched `'('`, we insert closing `')'` at the end.
>
> The key is to always keep the current string **valid up to that point**, and fix mismatches on the go.”

---

## ✅ Time & Space Complexity

| Operation           | Complexity |
|---------------------|------------|
| Traversing input    | O(N)       |
| StringBuilder ops   | O(N)       |
| Final `while` loop  | O(N) worst |
| Final output        | O(N)       |

✅ **Time:** `O(N)`  
✅ **Space:** `O(N)` — output string + counters

---

## ✅ Edge Case Table

| Input            | Output              | Reason                                        |
|------------------|---------------------|-----------------------------------------------|
| `""`             | `""`                | Already valid, empty string                   |
| `"((("`          | `"((()))"`          | Add 3 `')'` to match                          |
| `")))"`          | `"()()()"`          | Add 3 `'('` before                            |
| `"(()()))(("`    | `"(()())()(())"`    | Balanced insertions                           |
| `"abcxyz"`       | `"abcxyz"`          | No brackets → already valid                   |
| `"((a)()))((xyz"`| `"((a)())()((xyz))"`| Mix of chars and parentheses handled cleanly  |

---

Would you like me to build a **stack-based visual version**, or generate **unit tests in JUnit format** next?
```

