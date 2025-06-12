Here's your `addStrings()` solution with **detailed Telugu comments**, as well as the **time and space complexity analysis** at the end.

---

## ✅ Python Code with Telugu Comments

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []        # result digits ni collect cheyyataniki list
        carry = 0       # addition lo carry ni maintain cheyyali
        p1 = len(num1) - 1  # num1 string last index
        p2 = len(num2) - 1  # num2 string last index

        # renditlo eedaina character unnapatike loop continue cheyyadam
        while p1 >= 0 or p2 >= 0:
            # p1 valid index ayithe dani digit ni theesukovali, lekapote 0
            x1 = ord(num1[p1]) - ord("0") if p1 >= 0 else 0
            # p2 valid index ayithe dani digit ni theesukovali, lekapote 0
            x2 = ord(num2[p2]) - ord("0") if p2 >= 0 else 0

            # current digit calculate cheyyadam (modulo 10 valla last digit)
            value = (x1 + x2 + carry) % 10

            # next iteration ki carry prepare cheyyadam
            carry = (x1 + x2 + carry) // 10

            # result list lo current digit ni add cheyyadam
            res.append(value)

            # indexes ni move cheyyadam (left side ki)
            p1 -= 1
            p2 -= 1

        # loop ayyaka final carry unte add cheyyadam
        if carry:
            res.append(carry)

        # digits reverse order lo unnayi (LSB to MSB), so reverse and convert to string
        return "".join(str(x) for x in res[::-1])
```

---

## 🧠 Time and Space Complexity (Telugu Explanation)

### ⏱ **Time Complexity**: `O(max(n, m))`

* `n = len(num1)`, `m = len(num2)`
* Prathi character ni once matrame process chestam.
* So loop runs `max(n, m)` times.

### 💾 **Space Complexity**: `O(max(n, m))`

* `res[]` list lo max(n, m) digits store cheyyadam jarugutundi.
* Final result string kooda roughly same length untundi.

---

## 🔍 Example:

```python
num1 = "456"
num2 = "77"

# Loop 1: 6 + 7 + 0 = 13 → digit = 3, carry = 1
# Loop 2: 5 + 7 + 1 = 13 → digit = 3, carry = 1
# Loop 3: 4 + 0 + 1 = 5  → digit = 5, carry = 0
# Result = [3, 3, 5] → reverse and join → "533"
```

---

Let me know if you'd like the **Java version**, or want to extend it to **support negative numbers or decimal points**.
