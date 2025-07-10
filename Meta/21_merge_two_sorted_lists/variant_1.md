// VARIANT: What if you had to merge 3 sorted integer lists? Duplicates in the merged list is allowed.


Here’s the **Java version** of the variant of Leetcode 21:
✅ **Merging 3 sorted integer lists** (duplicates allowed)
✅ Includes **Telugu-style comments**
✅ Clean and intuitive logic

---

## ✅ Java Code with Telugu Comments

```java
import java.util.*;

public class MergeThreeSortedLists {

    public List<Integer> mergeThreeSortedLists(List<Integer> listA, List<Integer> listB, List<Integer> listC) {
        List<Integer> result = new ArrayList<>();

        // 🟢 3 pointers maintain cheyyadam for 3 lists
        int i = 0, j = 0, k = 0;

        // 🔁 Loop run cheyyadam until all 3 lists are exhausted
        while (i < listA.size() || j < listB.size() || k < listC.size()) {

            // ✅ If index valid unte value fetch cheyyadam, else → Integer.MAX_VALUE fix cheyyadam
            int aVal = (i < listA.size()) ? listA.get(i) : Integer.MAX_VALUE;
            int bVal = (j < listB.size()) ? listB.get(j) : Integer.MAX_VALUE;
            int cVal = (k < listC.size()) ? listC.get(k) : Integer.MAX_VALUE;

            // 🧠 Smallest value choose cheyyadam
            int minVal = Math.min(aVal, Math.min(bVal, cVal));

            // ➕ Add to result
            result.add(minVal);

            // ☝️ Yekkada match ayindo aa pointer ni move cheyyadam
            if (aVal == minVal) i++;
            else if (bVal == minVal) j++;
            else if (cVal == minVal) k++;
        }

        return result;
    }
}
```

---

## ✅ Time and Space Complexity

| Metric | Value           |
| ------ | --------------- |
| Time   | O(n1 + n2 + n3) |
| Space  | O(n1 + n2 + n3) |

* Where `n1`, `n2`, `n3` are lengths of the input lists
* Each element is processed once → linear merge

---

## ✅ Sample Test in `main()`

```java
public class Main {
    public static void main(String[] args) {
        MergeThreeSortedLists merger = new MergeThreeSortedLists();

        List<Integer> a = Arrays.asList(1, 1, 1, 3, 4, 5);
        List<Integer> b = Arrays.asList(3, 3, 4, 5, 6);
        List<Integer> c = Arrays.asList(1, 1, 3, 3, 8, 8, 8, 10);

        List<Integer> expected = Arrays.asList(1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6, 8, 8, 8, 10);
        List<Integer> result = merger.mergeThreeSortedLists(a, b, c);

        System.out.println("Output:   " + result);
        System.out.println("Expected: " + expected);
        System.out.println("Match:    " + result.equals(expected));
    }
}
```

---

## ✅ Summary

This approach is:

* 🔁 **Iterative** and **efficient** (linear scan)
* ✅ Duplicates allowed
* ✅ Easy to extend to `K` sorted lists using **Min Heap**

Would you like to see how this logic generalizes to `K` sorted lists using a **priority queue (min-heap)**?
