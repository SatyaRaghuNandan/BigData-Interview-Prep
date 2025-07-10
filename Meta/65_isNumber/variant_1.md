# // VARIANT: What if you had to build the second largest number?

Here's the Java version of the C++ variant for:

> **Leetcode 670 Variant** – Build the **second largest number** from a list of digits by swapping any two **adjacent unequal digits once**.

---

## ✅ Java Code with Telugu Comments (Transliterated)

```java
import java.util.*;

public class SecondLargestNumberBuilder {

    public List<Integer> getSecondLargestNumber(List<Integer> digits) {
        if (digits == null || digits.size() <= 1)
            return new ArrayList<>(); // ❌ empty or single digit unda → no second largest

        // ✅ Frequency array create cheyyadam (0–9 digits)
        int[] freqs = new int[10];
        for (int digit : digits) {
            freqs[digit]++;
        }

        // ✅ Largest number build cheyyadam (descending order)
        List<Integer> largestNum = new ArrayList<>();
        for (int digit = 9; digit >= 0; digit--) {
            for (int i = 0; i < freqs[digit]; i++) {
                largestNum.add(digit);
            }
        }

        // ✅ Adjacent digits lo unequal pair kanipettadam
        //     → swap cheyyadam to make second largest
        for (int i = largestNum.size() - 1; i > 0; i--) {
            if (!Objects.equals(largestNum.get(i), largestNum.get(i - 1))) {
                // ✅ Swap cheyyadam
                Collections.swap(largestNum, i, i - 1);
                return largestNum; // 💥 Only one valid swap allowed
            }
        }

        return new ArrayList<>(); // ❌ All digits same → no second largest possible
    }
}
```

---

## ✅ Example Walkthrough

### Input:

```java
digits = [1, 2, 3]
```

### Step-by-step:

1. **Build largest number:**
   Sorted descending → `3 2 1`

2. **Find swap for second largest:**
   Swap rightmost unequal pair → `3 1 2`
   Return: `3 1 2` ✅

---

## ✅ Time and Space Complexity

| Metric           | Value                                        |
| ---------------- | -------------------------------------------- |
| Time Complexity  | `O(N + K)` = `O(N)`                          |
| Space Complexity | `O(1)` (digit count 0–9) + `O(N)` for result |

* `N` = number of digits
* `K = 10` → constant for digit frequency array

---

## ✅ When Will It Return Empty?

* If all digits are same → e.g., `[1, 1, 1]`
* There is no **adjacent unequal digit pair** to swap

---

## ✅ Interview Explanation (Plain English)

> “To build the second largest number, I first sort digits in descending order to form the largest number. Then, I scan from the right and find the first pair of **adjacent unequal digits**, and swap them. This guarantees the result is the closest smaller permutation. Time complexity is `O(N)` and space is `O(N)` for storing the output.”

---

## ✅ Want More?

Would you like to extend this logic to:

* ✅ **All permutations** to get Kth largest number?
* ✅ Handle string input like `"231"` instead of list?
* ✅ Use a custom comparator for descending string digits?

Let me know!



