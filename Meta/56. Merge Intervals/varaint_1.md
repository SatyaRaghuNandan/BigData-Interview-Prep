# // VARIANT: What if you had to merge two interval lists instead of one?

Excellent! You're now working on a powerful **variant** of the classic **Merge Intervals** problem:

> 🔁 **LeetCode 56 – Variant**:
> Merge **two sorted interval lists** `A` and `B` into a final merged list where overlapping intervals are combined.

---

## ✅ Variant Explanation

**Original LeetCode 56:** You’re given one list of possibly unsorted intervals and asked to merge overlapping intervals.

**✅ This Variant:**
You are given **two** sorted lists of intervals (A and B), and you must:

1. Combine the lists like merge-sort.
2. Merge overlapping intervals on-the-fly.

---

## ✅ Java Version with Telugu Comments

```java
import java.util.*;

public class MergeTwoIntervalLists {

    // ✅ Merge helper - merges current interval into result list if needed
    private static void tryMerge(List<int[]> result, int[] curr) {
        if (result.isEmpty() || curr[0] > result.get(result.size() - 1)[1]) {
            // ❌ Overlap ledu → Add directly
            result.add(curr);
        } else {
            // ✅ Overlap vunte → Merge with previous
            int[] last = result.get(result.size() - 1);
            last[1] = Math.max(last[1], curr[1]);
        }
    }

    public static List<int[]> mergeTwoIntervalLists(int[][] A, int[][] B) {
        List<int[]> result = new ArrayList<>();
        int i = 0, j = 0;

        // ✅ Merge-sort style merging based on start time
        while (i < A.length && j < B.length) {
            int[] curr;
            if (A[i][0] <= B[j][0]) {
                curr = A[i++];
            } else {
                curr = B[j++];
            }
            tryMerge(result, curr);
        }

        // ✅ Remaining intervals in A
        while (i < A.length) {
            tryMerge(result, A[i++]);
        }

        // ✅ Remaining intervals in B
        while (j < B.length) {
            tryMerge(result, B[j++]);
        }

        return result;
    }

    // ✅ Utility to convert 2D array to list
    public static List<int[]> toList(int[][] arr) {
        List<int[]> res = new ArrayList<>();
        for (int[] x : arr) res.add(x.clone());
        return res;
    }

    // ✅ Utility to check list equality
    public static boolean equal(List<int[]> a, List<int[]> b) {
        if (a.size() != b.size()) return false;
        for (int i = 0; i < a.size(); i++) {
            if (a.get(i)[0] != b.get(i)[0] || a.get(i)[1] != b.get(i)[1])
                return false;
        }
        return true;
    }

    // ✅ Test cases
    public static void main(String[] args) {
        runTests();
    }

    public static void runTests() {
        test(new int[][]{{3, 11}, {14, 15}, {18, 22}, {23, 24}, {25, 26}},
             new int[][]{{2, 8}, {13, 20}},
             new int[][]{{2, 11}, {13, 22}, {23, 24}, {25, 26}});

        test(new int[][]{},
             new int[][]{{2, 8}, {13, 20}},
             new int[][]{{2, 8}, {13, 20}});

        test(new int[][]{{1, 5}, {10, 15}, {20, 25}},
             new int[][]{{5, 10}, {15, 20}},
             new int[][]{{1, 25}});

        test(new int[][]{{1, 5}, {11, 15}, {21, 25}},
             new int[][]{{6, 10}, {16, 20}},
             new int[][]{{1, 5}, {6, 10}, {11, 15}, {16, 20}, {21, 25}});

        test(new int[][]{{1, 5}},
             new int[][]{{1, 5}},
             new int[][]{{1, 5}});

        test(new int[][]{{1, 5}, {10, 15}, {20, 25}},
             new int[][]{{2, 3}, {4, 5}, {12, 13}, {20, 27}},
             new int[][]{{1, 5}, {10, 15}, {20, 27}});
    }

    private static void test(int[][] A, int[][] B, int[][] expected) {
        List<int[]> result = mergeTwoIntervalLists(A, B);
        List<int[]> expectedList = toList(expected);
        boolean pass = equal(result, expectedList);

        System.out.println("Input A: " + Arrays.deepToString(A));
        System.out.println("Input B: " + Arrays.deepToString(B));
        System.out.println("Expected: " + Arrays.deepToString(expected));
        System.out.println("Output  : " + Arrays.deepToString(result.toArray(new int[0][])));
        System.out.println("✅ Pass? " + pass);
        System.out.println("-------------------------------------");
        assert pass;
    }
}
```

---

## ✅ Time & Space Complexity

| Metric           | Value      | Notes                                |
| ---------------- | ---------- | ------------------------------------ |
| Time Complexity  | `O(n + m)` | Like merge sort, scanning both lists |
| Space Complexity | `O(n + m)` | Final result in output list          |

---

## ✅ Key Ideas Recap

* Both input lists **A and B are sorted** by start time.
* We merge them **merge-sort style**, one interval at a time.
* Use a helper `tryMerge` to decide if:

  * A new interval should be added
  * Or **merged** with the last one

---

Would you like:

* ✅ A version that merges more than 2 sorted lists?
* ✅ A streaming or iterator-based version for large inputs?

Let me know — I’m ready to extend this!
