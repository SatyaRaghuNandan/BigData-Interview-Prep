Great — you're now using the **iterative version of Exponentiation by Squaring** for `x^n`, which improves the **space complexity from O(log n) → O(1)**. This is a common **follow-up question** in interviews after solving the recursive version.

---

## ✅ Follow-Up: Iterative `myPow()` — Full Explanation with Telugu Comments

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # n negative unte, reciprocal teesukovali: x^-n = 1 / x^n
        if n < 0:
            x = 1 / x       # x ni 1/x ga marchadam
            n = abs(n)      # n ni positive ga teesukovadam

        result = 1.0         # Final result accumulator
        doubling_val = x     # Squaring kosam base ni track cheyyadam

        while n != 0:
            # Odd power unte, current doubling_val ni result lo include cheyyali
            if n % 2 == 1:
                result *= doubling_val

            # doubling_val ni square cheyyali → x, x^2, x^4, x^8 ...
            doubling_val *= doubling_val

            # n ni half cheyyadam (binary power reduction)
            n //= 2

        return result
```

---

## 🧠 Telugu Explanation (Line-by-Line)

```text
1. n negative unte, x ni 1/x ga marchadam and n ni positive cheyyadam.
2. result = 1.0 → idi accumulator, final answer ikkadey build avtadi.
3. doubling_val = x → idi power doubling ki upayogistharu.
4. while loop: n ni binary ga process cheyyadam.

    - n odd unte result *= doubling_val → a bit is set, so include that power.
    - doubling_val *= doubling_val → base ni square cheyyadam (x^1 → x^2 → x^4 ...)
    - n //= 2 → next binary digit process cheyyadam.
```

---

## ✅ Time and Space Complexity

| Metric           | Value                                               |
| ---------------- | --------------------------------------------------- |
| Time Complexity  | `O(log n)`                                          |
| Space Complexity | `O(1)`                                              |
| Why?             | Iterative, constant space, and halves `n` each time |

---

## ✅ Interview Comparison Table

| Version        | Time     | Space    | Notes                                              |
| -------------- | -------- | -------- | -------------------------------------------------- |
| Recursive DFS  | O(log n) | O(log n) | Elegant, intuitive; uses call stack                |
| Iterative Loop | O(log n) | O(1)     | Space-optimal; interviewer-preferred in follow-ups |

---

## 🔁 Bonus Interview Follow-Ups:

1. **What if n is `Integer.MIN_VALUE` (`-2^31`)?**
   👉 Use `long` to avoid overflow when converting `n = -n`.

2. **What if x is 0 or negative?**
   👉 Edge cases: return 0 for `x=0, n>0`; throw for `x=0, n<=0`.

3. **What if fractional powers?**
   👉 Not supported with this logic (only works for integer powers).

---

Let me know if you'd like to visualize the **bitwise interpretation** of how the powers are selected during iteration!
