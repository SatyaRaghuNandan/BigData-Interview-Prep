Here’s the **Java version** of your Python solution for **Leetcode 227 - Basic Calculator II**, complete with:

✅ Clean structure
✅ Detailed **Telugu-style comments**
✅ Dry run and edge test cases
✅ Time and space complexity analysis

---

## ✅ Java Code with Telugu Comments (No Stack Needed)

```java
public class Solution {

    public int calculate(String s) {
        int currNum = 0;         // 🔢 Present number build cheyyadam digit by digit
        int prevNum = 0;         // 🔁 Previous number store cheyyadam (+/- lo result lo add cheyyali)
        int result = 0;          // 🧮 Final result accumulate cheyyadam kosam
        char op = '+';           // 🔣 Initial operator assume '+' (starting number ki)

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            // 🔢 Digit ayithe: multi-digit number ni build cheyyadam
            if (Character.isDigit(ch)) {
                currNum = currNum * 10 + (ch - '0');
            }

            // ⛔ Operator or last character vachinappudu, operation perform cheyyali
            if ((!Character.isDigit(ch) && ch != ' ') || i == s.length() - 1) {

                // 🔄 Based on previous operator, operation perform cheyyadam
                if (op == '+') {
                    result += prevNum;      // ✅ Previous number ni result lo add cheyyadam
                    prevNum = currNum;      // 🔄 Ee number ni store cheyyadam for next op
                } else if (op == '-') {
                    result += prevNum;
                    prevNum = -currNum;     // 🔻 Negative number ni consider cheyyadam
                } else if (op == '*') {
                    prevNum = prevNum * currNum;  // ➕ Multiply directly to prevNum
                } else if (op == '/') {
                    prevNum = prevNum / currNum;  // ➗ Integer division, truncate towards zero
                }

                // 🔁 Reset current number and update operator
                currNum = 0;
                op = ch;
            }
        }

        // 🔚 Last prevNum ni result lo add cheyyadam
        result += prevNum;
        return result;
    }
}
```

---

## ✅ Dry Run Example: `s = "3+2*2"`

```java
String s = "3+2*2";
```

**Step-by-step:**

| i | ch   | currNum | prevNum | result | op   | Action                                            |
| - | ---- | ------- | ------- | ------ | ---- | ------------------------------------------------- |
| 0 | '3'  | 3       | 0       | 0      | '+'  | digit build cheyyadam                             |
| 1 | '+'  | 0       | 3       | 0      | '+'  | '+' operation: result += prevNum (0), prevNum = 3 |
| 2 | '2'  | 2       | 3       | 0      | '+'  | digit build cheyyadam                             |
| 3 | '\*' | 0       | 2       | 3      | '\*' | '+' operation: result += 3, prevNum = 2           |
| 4 | '2'  | 2       | 2       | 3      | '\*' | digit build cheyyadam                             |
| 5 | end  | 0       | 4       | 3      | '\*' | '\*' operation: prevNum = 2 \* 2 = 4              |
|   |      |         |         | 7      |      | result += prevNum = 4 → final = 7                 |

✅ Final Answer = **7**

---

## ✅ Test Cases and Edge Handling

```java
public static void main(String[] args) {
    Solution sol = new Solution();

    System.out.println(sol.calculate("3+2*2"));           // ✅ 7
    System.out.println(sol.calculate(" 3/2 "));           // ✅ 1 (floor division)
    System.out.println(sol.calculate(" 3+5 / 2 "));       // ✅ 5
    System.out.println(sol.calculate("14-3/2"));          // ✅ 13
    System.out.println(sol.calculate("1+2*5/3+6/4*2"));   // ✅ 6
    System.out.println(sol.calculate("0"));               // ✅ 0
}
```

---

## 🧠 Time and Space Complexity

| Metric              | Value                                     |
| ------------------- | ----------------------------------------- |
| ⏱️ Time Complexity  | **O(N)** — One pass through the string    |
| 🧠 Space Complexity | **O(1)** — Only variables, no extra stack |

---

## ✅ Interview Summary

> “This is a **non-stack based solution** for parsing basic expressions.
> We use a `prevNum` to delay addition until multiplication/division is done.
> This gives us constant space and linear time performance — optimal for this restricted operator set.”

---

Let me know if you'd like:

* Stack-based solution (good for extending to parentheses)
* Recursive solution
* Leetcode-style JUnit tests

Would you also like the **Leetcode 772 (Basic Calculator III)** version next?
