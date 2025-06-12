Great! You're working on **LeetCode 50 – Pow(x, n)** using **recursive exponentiation by squaring**, which is both optimal and elegant.

---

## ✅ Goal:

Implement `x^n` (x raised to the power n) **efficiently**.

---

## ✅ Python Code with Telugu Comments

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Negative power unte, reciprocal teesukuntam (x^-n = 1 / x^n)
        if n < 0:
            return 1.0 / self.myPow(x, abs(n))

        # n = 0 aithe, x^0 = 1
        if n == 0:
            return 1

        # Half power ni recursive ga call chestunnam (Exponentiation by squaring)
        result = self.myPow(x, n // 2)

        # Odd power unte, extra x multiply cheyyali (ex: x^5 = x * (x^2)^2)
        if n % 2 == 1:
            return x * result * result

        # Even power aithe, just square result (x^4 = (x^2)^2)
        return result * result
```

---

## 🧠 Step-by-Step Logic (Telugu Transliteration):

```text
1. n negative unte, reciprocal use chestam (1 / x^|n|).
2. n = 0 unte, return 1 (identity for exponentiation).
3. n > 0 unte, half power ni recursive ga calculate chestam.
4. n odd unte, final result lo oka additional x multiply cheyyali.
5. n even unte, result ni square cheyadam chalu.
```

---

## ⏱ Time and Space Complexity

| Metric           | Value                               |
| ---------------- | ----------------------------------- |
| Time Complexity  | `O(log n)`                          |
| Space Complexity | `O(log n)` (due to recursion stack) |

### 📌 Why `O(log n)`?

* Each recursive step divides `n` by 2 → log₂(n) steps.

---

## ✅ Iterative Version (if you want `O(1)` space):

Use a **while loop** and avoid recursion — often asked in follow-ups.

Let me know if you want that version or a dry run with a sample input like `x=2.0, n=10`.
