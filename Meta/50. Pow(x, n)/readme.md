
Here’s your complete **Java implementation** of **Binary Exponentiation** (both Recursive and Iterative) for computing `x^n`, with:

✅ **Detailed Telugu-style comments**
✅ **Time & space complexity analysis**
✅ **Test cases with dry run explanations**
✅ **Walkthrough of how the code works**

---

## ✅ Java Code: Recursive Binary Exponentiation

```java
public class SolutionRecursive {

    // Recursive Binary Exponentiation function
    public double binaryExp(double base, int power) {
        // 👉 Base Case: power == 0 ayithe result always 1
        if (power == 0) return 1.0;

        // 👉 Negative exponent case: x^-n = 1 / x^n
        if (power < 0) return 1.0 / binaryExp(base, -power);

        // 👉 If power is odd: x^n = x * (x^2)^(n/2)
        if (power % 2 == 1) {
            return base * binaryExp(base * base, (power - 1) / 2);
        }

        // 👉 If power is even: x^n = (x^2)^(n/2)
        return binaryExp(base * base, power / 2);
    }

    public double myPow(double x, int n) {
        return binaryExp(x, n);
    }
}
```

---

## ✅ Java Code: Iterative Binary Exponentiation

```java
public class SolutionIterative {

    // Iterative Binary Exponentiation function
    public double binaryExp(double base, int power) {
        // 👉 If power < 0, take reciprocal of base and make power positive
        if (power < 0) {
            base = 1.0 / base;
            power = -power;
        }

        double result = 1.0;

        // 👉 While power > 0
        while (power > 0) {
            // 👉 If power is odd, result *= base
            if (power % 2 == 1) {
                result *= base;
            }

            // 👉 Base square cheyyi, power half cheyyi
            base *= base;
            power /= 2;
        }

        return result;
    }

    public double myPow(double x, int n) {
        return binaryExp(x, n);
    }
}
```

---

## ✅ Time and Space Complexity

| Approach  | Time Complexity | Space Complexity | Notes                         |
| --------- | --------------- | ---------------- | ----------------------------- |
| Recursive | `O(log n)`      | `O(log n)`       | Recursive stack memory usage  |
| Iterative | `O(log n)`      | `O(1)`           | Constant memory, better usage |

---

## 🧪 Test Cases with Expected Output

```java
public class TestBinaryExponentiation {

    public static void main(String[] args) {
        SolutionRecursive recur = new SolutionRecursive();
        SolutionIterative iter = new SolutionIterative();

        test(recur, iter, 2.0, 10);      // 1024.0
        test(recur, iter, 2.0, -3);      // 0.125
        test(recur, iter, 2.5, 3);       // 15.625
        test(recur, iter, 2.0, 0);       // 1.0
        test(recur, iter, 1.0, 1000);    // 1.0
        test(recur, iter, 0.5, 2);       // 0.25
        test(recur, iter, -2.0, 3);      // -8.0
        test(recur, iter, -2.0, 4);      // 16.0
    }

    private static void test(SolutionRecursive recur, SolutionIterative iter, double x, int n) {
        System.out.printf("x = %.2f, n = %d\n", x, n);
        System.out.println("Recursive Result : " + recur.myPow(x, n));
        System.out.println("Iterative Result : " + iter.myPow(x, n));
        System.out.println("--------------------------------------------------");
    }
}
```

---

## 🧠 Dry Run Example for `x = 2.0`, `n = 10`

### ✅ Recursive Stack Breakdown

```text
binaryExp(2.0, 10) 
-> even => binaryExp(4.0, 5)
    -> odd => 4.0 * binaryExp(16.0, 2)
        -> even => binaryExp(256.0, 1)
            -> odd => 256.0 * binaryExp(65536.0, 0)
                -> base case => 1.0
```

Backtrack:

* 256 × 1 = 256
* 4 × 256 = 1024
  ✅ Output: 1024.0

---

### ✅ Iterative Trace Table

| Step             | Power | Base  | Result       | Action (Telugu Comments)                    |
| ---------------- | ----- | ----- | ------------ | ------------------------------------------- |
| 1                | 10    | 2.0   | 1.0          | Even → base^2=4.0, power=5                  |
| 2                | 5     | 4.0   | 1×4=4.0      | Odd → result \*= base, base^2=16.0, power=2 |
| 3                | 2     | 16.0  | 4.0          | Even → base^2=256.0, power=1                |
| 4                | 1     | 256.0 | 4×256=1024.0 | Odd → result \*= base, power=0              |
| ✅ Output: 1024.0 |       |       |              |                                             |

---

## 🔚 Summary

* Recursive is clean and easier to reason for depth-based logic.
* Iterative is preferred in practice due to **constant space** and **no risk of stack overflow**.
* Both work well for positive, negative, decimal bases.

---

Let me know if you’d like:

* 📊 Java implementation with BigDecimal precision
* 📚 Explanation for integer overflow/edge cases in Java
* 💡 Application of this technique in matrix exponentiation or modular arithmetic
