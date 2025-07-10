# // VARIANT: What if you had to return the parentheses string itself after the minimum adds?

Absolutely! Let's convert the **Python code of Leetcode 921 - Minimum Add to Make Parentheses Valid** into **Java**, and add:

* ✅ **Telugu-style comments** (in English script)
* ✅ Full Java implementation
* ✅ Best explanation
* ✅ Time & Space complexity
* ✅ Test cases

---

## ✅ Java Code with Telugu Comments

```java
public class Solution {
    public int minAddToMakeValid(String s) {
        int leftOpen = 0;     // ✅ '(' undi kani inka match kaledu → closing ')' kavali
        int extraRight = 0;   // ✅ ')' ki matching '(' ledu → extra '(' add cheyyali

        for (char c : s.toCharArray()) {
            if (c == '(') {
                leftOpen++;   // '(' ochindi ante oka ')' kavali future lo
            } else if (c == ')') {
                if (leftOpen == 0) {
                    // '(' lekapote → ee ')' ki pair ledu, so oka '(' add cheyyali
                    extraRight++;
                } else {
                    // matching '(' undi → match cheyyadam
                    leftOpen--;
                }
            }
        }

        // Total add cheyyali: unmatched '(' + extra ')' ni match cheyyadaniki
        return leftOpen + extraRight;
    }

    // ✅ Simple test runner
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.minAddToMakeValid("()))(("));  // Output: 4
        System.out.println(sol.minAddToMakeValid(""));        // Output: 0
        System.out.println(sol.minAddToMakeValid("((("));     // Output: 3
        System.out.println(sol.minAddToMakeValid(")))"));     // Output: 3
        System.out.println(sol.minAddToMakeValid("()()"));    // Output: 0
        System.out.println(sol.minAddToMakeValid("(()))"));   // Output: 1
    }
}
```

---

## ✅ Meta-style Explanation (Interview Ready)

> I keep track of:
>
> * How many `'('` are still open (need closing `')'`)
> * How many `')'` are unmatched (no `'('` available to close)
>
> While scanning:
>
> * For `'('`, I increase the `leftOpen` counter.
> * For `')'`, if a `'('` is available, I pair it; otherwise, I increment `extraRight`.
>
> Final answer is the sum of both: how many opening or closing brackets need to be added.

---

## ✅ Time & Space Complexity

| Part                     | Complexity |
| ------------------------ | ---------- |
| Traversing the string    | `O(N)`     |
| Using only two counters  | `O(1)`     |
| Overall Time Complexity  | ✅ `O(N)`   |
| Overall Space Complexity | ✅ `O(1)`   |

---

## ✅ Dry Run Example: `s = "()))(("`

| Char | Action                             | leftOpen | extraRight |
| ---- | ---------------------------------- | -------- | ---------- |
| `(`  | Open bracket → expect a ')'        | 1        | 0          |
| `)`  | Matches open → decrease open count | 0        | 0          |
| `)`  | No open → needs new '('            | 0        | 1          |
| `)`  | No open → needs new '('            | 0        | 2          |
| `(`  | Open bracket → expect a ')'        | 1        | 2          |
| `(`  | Open bracket → expect a ')'        | 2        | 2          |

**Final:**

* `leftOpen = 2` → Need 2 `')'`
* `extraRight = 2` → Need 2 `'('`

**Result:** `2 + 2 = 4`

---

## ✅ Edge Cases Summary

| Input     | Output | Why                           |
| --------- | ------ | ----------------------------- |
| `""`      | 0      | Empty string is already valid |
| `"((("`   | 3      | 3 `')'` needed to close       |
| `")))"`   | 3      | 3 `'('` needed to open        |
| `"()"`    | 0      | Already valid                 |
| `"(()))"` | 1      | One `'('` needed              |

---

Would you like a **stack-based simulation** or **graphical walkthrough** next?


Great! Let's now generate:

---

## ✅ **JUnit Test Cases** for the Java solution

We'll use the same class (`MinimumAddToMakeValidString`) and add a proper **JUnit 5 test suite** using `@Test` annotations.

---

### ✅ `MinimumAddToMakeValidStringTest.java`

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class MinimumAddToMakeValidStringTest {

    MinimumAddToMakeValidString sol = new MinimumAddToMakeValidString();

    @Test
    public void testOnlyClosingBrackets() {
        assertEquals("()()()", sol.minAddToMakeValid(")))"));
    }

    @Test
    public void testOnlyOpeningBrackets() {
        assertEquals("((()))", sol.minAddToMakeValid("((("));
    }

    @Test
    public void testEmptyString() {
        assertEquals("", sol.minAddToMakeValid(""));
    }

    @Test
    public void testAlreadyValid() {
        assertEquals("(())", sol.minAddToMakeValid("(())"));
    }

    @Test
    public void testUnmatchedStartAndEnd() {
        assertEquals("()()()((()))", sol.minAddToMakeValid(")))((("));
    }

    @Test
    public void testNoParenthesesCharacters() {
        assertEquals("abcxyz", sol.minAddToMakeValid("abcxyz"));
    }

    @Test
    public void testComplexCase1() {
        assertEquals("(()())()(())", sol.minAddToMakeValid("(()()))(("));
    }

    @Test
    public void testComplexCaseWithLetters() {
        assertEquals("((a)())()((xyz))", sol.minAddToMakeValid("((a)()))((xyz"));
    }
}
```

---

## ✅ How to Run

1. Make sure you're using **JUnit 5** in your Java project (`org.junit.jupiter`).
2. Include both classes:

   * `MinimumAddToMakeValidString.java`
   * `MinimumAddToMakeValidStringTest.java`
3. Run with your favorite IDE or from CLI:
   `mvn test` or use `gradle test` if you're using Gradle.

---

Would you like me to show a **JUnit 4 compatible version** or convert this into **TestNG** format?
