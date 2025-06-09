Here is the **Python version** of your C++ code (`Leetcode 227 - Basic Calculator II`) with **detailed comments** in **English and Telugu (transliterated)**:

---

### ✅ Python Translation with Telugu Comments

```python
class Solution:
    def calculate(self, s: str) -> int:
        curr_num = 0        # Telugu: current number ni build chesthunnam
        prev_num = 0        # Telugu: previous number ni multiplication/division kosam store chestham
        result = 0          # Telugu: final result ikkadiki accumulate chestham
        op = '+'            # Telugu: default ga first number ki '+' operation apply avutundi
        s = s.replace(" ", "")  # Telugu: whitespace remove cheyyadam

        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)  # Telugu: multi-digit numbers ni build cheyyadam

            # Telugu: character operator aithe or last index aithe, operation execute cheyyali
            if not char.isdigit() or i == len(s) - 1:
                if op == '+':
                    result += prev_num       # Telugu: previous value ni result lo add cheyyadam
                    prev_num = curr_num      # Telugu: current value ni store cheyyadam
                elif op == '-':
                    result += prev_num
                    prev_num = -curr_num     # Telugu: subtraction ki negative ga store cheyyadam
                elif op == '*':
                    prev_num *= curr_num     # Telugu: multiplication directly cheyyadam
                elif op == '/':
                    prev_num = int(prev_num / curr_num)  # Telugu: truncate toward zero

                curr_num = 0     # Telugu: current number reset cheyyadam
                op = char        # Telugu: next operator store cheyyadam

        result += prev_num       # Telugu: last pending value ni result lo add cheyyadam
        return result
```

---

### ✅ Example Usage:

```python
solution = Solution()
print(solution.calculate("3+2*2"))       # Output: 7
print(solution.calculate(" 3/2 "))       # Output: 1
print(solution.calculate(" 3+5 / 2 "))   # Output: 5
```

---

Let me know if you want to support parentheses (`(`, `)`) or handle floating point numbers as well.
