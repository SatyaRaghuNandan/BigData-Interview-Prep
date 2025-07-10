# // VARIANT: What if you had to merge K sorted integer arrays, no longer linked lists?

Here’s the **Java version** of the **variant of Leetcode 23**, where instead of merging **K sorted linked lists**, we merge **K sorted integer arrays** using a **Min Heap** (`PriorityQueue` in Java).

---

### ✅ What Changed in the Variant?

| Feature             | Original Leetcode 23                    | Variant (This Code)                             |
| ------------------- | --------------------------------------- | ----------------------------------------------- |
| Input Type          | `ListNode[]` (Linked lists)             | `int[][]` or `List<List<Integer>>` (Arrays)     |
| Output Type         | Merged linked list                      | Flat merged array `List<Integer>`               |
| Data Access Pattern | Use `ListNode.next` pointer traversal   | Use `(array index + 1)` for next element        |
| Use Case            | Leetcode problem + production pipelines | Array merges: sorted partitions, search engines |
| Algorithm Used      | Min Heap on head of each list           | ✅ Same approach used → generalized for arrays   |

---

## ✅ Java Code (with Telugu Comments)

```java
import java.util.*;

// Solution to merge K sorted integer arrays using Min Heap
public class MergeKSortedArrays {

    // Telugu: heap lo petadaniki element info class (list index, value index, value)
    static class Element {
        int listIndex; // Edi e array nundi vachindo
        int index;     // Array lo position
        int val;       // Actual value

        Element(int listIndex, int index, int val) {
            this.listIndex = listIndex;
            this.index = index;
            this.val = val;
        }
    }

    public List<Integer> mergeKArrays(List<List<Integer>> lists) {
        List<Integer> result = new ArrayList<>();

        // Telugu: Min Heap ni define chestham → value basis lo sort avutundi
        PriorityQueue<Element> minHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.val, b.val)
        );

        // Telugu: Prathi array lo first element ni heap lo petadam
        for (int i = 0; i < lists.size(); i++) {
            if (!lists.get(i).isEmpty()) {
                minHeap.offer(new Element(i, 0, lists.get(i).get(0)));
            }
        }

        // Telugu: Heap empty kakapoyetvaraku process cheyyadam
        while (!minHeap.isEmpty()) {
            Element current = minHeap.poll(); // Min value pop cheyyadam
            result.add(current.val);          // Result lo add cheyyadam

            int nextIndex = current.index + 1;

            // Telugu: A array lo next element unda chuddam
            if (nextIndex < lists.get(current.listIndex).size()) {
                int nextVal = lists.get(current.listIndex).get(nextIndex);
                minHeap.offer(new Element(current.listIndex, nextIndex, nextVal));
            }
        }

        return result;
    }

    // ✅ Test Case
    public static void main(String[] args) {
        MergeKSortedArrays solution = new MergeKSortedArrays();

        List<List<Integer>> arrays = Arrays.asList(
            Arrays.asList(1, 4, 5),
            Arrays.asList(1, 3, 4),
            Arrays.asList(2, 6)
        );

        List<Integer> merged = solution.mergeKArrays(arrays);
        System.out.println("Merged Sorted Array:");
        System.out.println(merged); // ✅ Expected: [1, 1, 2, 3, 4, 4, 5, 6]
    }
}
```

---

## ✅ Time & Space Complexity

Let:

* `k` = number of arrays
* `n` = total number of elements across all arrays

| Operation                 | Time Complexity    | Space Complexity |
| ------------------------- | ------------------ | ---------------- |
| Heap insertions           | `O(log k)` per op  | `O(k)`           |
| Processing `n` elements   | `O(n log k)` total | `O(n + k)`       |
| Final result construction | `O(n)`             | `O(n)`           |

✅ So final:
**Time:** `O(n log k)`
**Space:** `O(n + k)`

---

## ✅ Why Is This Approach Better?

| Approach                          | Time         | Pros                           | Cons                     |
| --------------------------------- | ------------ | ------------------------------ | ------------------------ |
| **Min Heap (used here)**          | `O(n log k)` | Efficient, scalable to large K | Needs extra heap memory  |
| Brute force (merge all then sort) | `O(n log n)` | Simple to code                 | Slower for large K       |
| Pairwise merging                  | `O(n log k)` | Same time, harder to manage    | Higher constant overhead |

✅ Min Heap approach:

* Only keeps `k` elements in the heap
* Avoids sorting entire array at once
* Works **even if arrays are of unequal size**

---

## ✅ Interview Summary

> “To merge K sorted arrays efficiently, I use a **Min Heap** to always pick the smallest current element across all arrays. I insert the first element of each array into the heap, and each time I extract one, I push the next element from that array if available. This gives a total runtime of `O(n log k)`, where `n` is total elements. This method generalizes Leetcode 23 (K linked lists) to integer arrays.”

---

Let me know if you want:

* ✅ Linked list to array conversion helper
* ✅ Version using `int[][]` instead of `List<List<Integer>>`
* ✅ Tracing/print statements for step-by-step debug

Happy to extend!
