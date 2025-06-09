Here’s a breakdown of what this `Solution_227_Variant` does and its clean **Python equivalent**.

---

## ✅ Problem Statement

Given a string `s` containing **non-negative integers** and **operators `+` and `*` only**, evaluate the **expression**.

> ⚠️ No parentheses, no subtraction or division. Only `+` and `*`.

---

## 🔍 C++ Explanation (Line-by-line)

```cpp
int curr_num = 0;      // Parse current number being built (multi-digit)
int prev_num = 0;      // Last number before operator is applied
int result = 0;        // Final cumulative result
char op = '+';         // Previous operator seen (initialized to '+')
```

### Main Loop:

```cpp
if (std::isdigit(s[i]))
    curr_num = curr_num * 10 + (s[i] - '0'); // Build number like 23, 245, etc.

if ((!std::isdigit(s[i]) && s[i] != ' ') || i == s.size() - 1)
```

* If we hit an operator or the last character, we apply the **previous operator** to `prev_num` and `curr_num`.

### Only `+` and `*` Handling:

```cpp
if (op == '+') {
    result += prev_num;
    prev_num = curr_num;
} else if (op == '*') {
    prev_num = prev_num * curr_num;
}
```

---

## ✅ Final Step

At the end of the loop, we still have one last `prev_num` left → add it to result.

---

## ✅ Python Version

```python
class Solution:
    def calculate(self, s: str) -> int:
        curr_num = 0
        prev_num = 0
        result = 0
        op = '+'

        for i, ch in enumerate(s):
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            # If ch is an operator or last char
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if op == '+':
                    result += prev_num
                    prev_num = curr_num
                elif op == '*':
                    prev_num *= curr_num

                curr_num = 0
                op = ch

        result += prev_num
        return result
```

---

## 🧪 Test Example:

```python
sol = Solution()
print(sol.calculate("3+2*2"))     # Output: 7
print(sol.calculate("4*5+3"))     # Output: 23
print(sol.calculate("10+2*3"))    # Output: 16
```

Let me know if you want to extend this to support `-`, `/`, or parentheses like in the original \[Leetcode 227: Basic Calculator II].
