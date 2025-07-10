// VARIANT: What if the sizes - m and n - weren't given? Instead, we're guaranteed
// that one list is double in size of the other. Merge them like you would in the original problem.


Here's the **Java version** of your **Leetcode 88 Variant**, where `listA` has **twice the size** of `listB`, with zero placeholders at the end.

---

### ✅ Java Code with Telugu-style Comments

```java
import java.util.*;

public class MergeVariant88 {

    // ✅ Variant: No m or n given. Just guaranteed: listA.length == 2 * listB.length
    public static void merge(int[] listA, int[] listB) {
        int a = (listA.length / 2) - 1;     // 🟢 listA lo valid part ending index
        int b = listB.length - 1;           // 🟢 listB ending index
        int i = listA.length - 1;           // 🟢 Final merge position from last

        while (b >= 0) {
            if (a >= 0 && listA[a] >= listB[b]) {
                listA[i] = listA[a];  // Bigger element from listA
                a--;
            } else {
                listA[i] = listB[b];  // Bigger element from listB
                b--;
            }
            i--; // Move to previous position
        }
    }
}
```

---

### ✅ Example Test Cases (Same as your `assert` tests)

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        test(new int[]{1, 3, 0, 0}, new int[]{4, 10}, new int[]{1, 3, 4, 10});
        test(new int[]{5, 6, 7, 8, 0, 0, 0, 0}, new int[]{1, 2, 3, 4}, new int[]{1, 2, 3, 4, 5, 6, 7, 8});
        test(new int[]{0}, new int[]{99}, new int[]{99});
        test(new int[]{1, 10, 0, 0}, new int[]{2, 11}, new int[]{1, 2, 10, 11});
    }

    private static void test(int[] listA, int[] listB, int[] expected) {
        MergeVariant88.merge(listA, listB);
        if (Arrays.equals(listA, expected)) {
            System.out.println("✅ Passed: " + Arrays.toString(listA));
        } else {
            System.out.println("❌ Failed: Expected " + Arrays.toString(expected) + ", but got " + Arrays.toString(listA));
        }
    }
}
```

---

### ⏱ Time and Space Complexity

| Metric           | Value                                             |
| ---------------- | ------------------------------------------------- |
| Time Complexity  | `O(m + n)` = O(n), since listA = 2n and listB = n |
| Space Complexity | `O(1)` — In-place merge, no extra space used      |

---

### 💡 Key Takeaway

This **variant** simplifies the merge logic because:

* We know listA has **2n total space** and **n valid elements**
* No need for `m` and `n` parameters — just derive from size

Let me know if you'd like a version using `List<Integer>` instead of arrays.
