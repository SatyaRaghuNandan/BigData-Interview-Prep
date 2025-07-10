

# // VARIANT: What if you had to merge 3 sorted integer lists into a resulting list without duplicates?


Here’s the **Java version** of your second variant of Leetcode 21:

> ✅ **Merge 3 sorted integer lists**, but this time:
>
> * ❌ **No duplicates** in the final merged list
> * ✅ Use **three pointers**
> * ✅ Keep it clean and efficient

---

## ✅ Java Code with Telugu-style Comments

```java
import java.util.*;

public class MergeThreeSortedListsNoDuplicates {

    public List<Integer> mergeThreeSortedLists(List<Integer> listA, List<Integer> listB, List<Integer> listC) {
        List<Integer> result = new ArrayList<>();
        int i = 0, j = 0, k = 0;

        // 🔁 Loop run cheyyadam until all lists are processed
        while (i < listA.size() || j < listB.size() || k < listC.size()) {

            // ✅ Valid index unte value fetch cheyyadam, else Integer.MAX_VALUE fix cheyyadam
            int aVal = (i < listA.size()) ? listA.get(i) : Integer.MAX_VALUE;
            int bVal = (j < listB.size()) ? listB.get(j) : Integer.MAX_VALUE;
            int cVal = (k < listC.size()) ? listC.get(k) : Integer.MAX_VALUE;

            // 🔽 Smallest among aVal, bVal, cVal choose cheyyadam
            int minVal = Math.min(aVal, Math.min(bVal, cVal));

            // ✅ result lo last value same kaakapothe add cheyyadam
            if (result.isEmpty() || result.get(result.size() - 1) != minVal) {
                result.add(minVal);
            }

            // ➕ Same minVal match aina list lo pointer move cheyyadam
            if (aVal == minVal) i++;
            if (bVal == minVal) j++;
            if (cVal == minVal) k++;
        }

        return result;
    }
}
```

---

## ✅ Time and Space Complexity

| Metric | Value                                    |
| ------ | ---------------------------------------- |
| Time   | O(n1 + n2 + n3)                          |
| Space  | O(n1 + n2 + n3) (worst case: all unique) |

---

## ✅ Sample `main()` Test Case

```java
public class Main {
    public static void main(String[] args) {
        MergeThreeSortedListsNoDuplicates merger = new MergeThreeSortedListsNoDuplicates();

        List<Integer> a = Arrays.asList(1, 1, 1, 3, 4, 5);
        List<Integer> b = Arrays.asList(3, 3, 4, 5, 6);
        List<Integer> c = Arrays.asList(1, 1, 3, 3, 8, 8, 8, 10);

        List<Integer> expected = Arrays.asList(1, 3, 4, 5, 6, 8, 10);
        List<Integer> result = merger.mergeThreeSortedLists(a, b, c);

        System.out.println("Output:   " + result);
        System.out.println("Expected: " + expected);
        System.out.println("Match:    " + result.equals(expected));
    }
}
```

---

## ✅ How to Explain in Interview

> “I use a **three-pointer scan** with default `Integer.MAX_VALUE` padding to avoid boundary errors.
> At each step, I select the smallest value and push it to the result only if it is **not a duplicate** of the last added element.
> I increment **all pointers** whose value matches the current minimum.
> Time complexity is O(n) and works efficiently without using sets.”

---

Would you like to extend this to:

* ✅ K sorted lists (with or without duplicates)?
* ✅ Streams or Iterators?
* ✅ Using MinHeap-based merging?
