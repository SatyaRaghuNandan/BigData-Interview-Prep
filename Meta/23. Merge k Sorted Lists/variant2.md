

# // VARIANT: What if you had to merge K sorted integer arrays an an iterator?


Here’s the **Java version** of **Leetcode 23 - Variant 2**, where you're asked to **merge K sorted arrays using an iterator interface**.

This means:

* Instead of returning the full merged list at once,
* You call `hasNext()` and `next()` to **iterate** through the merged values.

---

## ✅ Java Code for Variant 2 – With Telugu Comments

```java
import java.util.*;

// Telugu: K sorted arrays ni merge cheyyadam iterator model lo chestham
public class MergedKArraysIterator implements Iterator<Integer> {

    // Telugu: listIndex, elementIndex, and value store cheyyadam kosam class
    static class Element {
        int listIndex; // Edi e array nunchi vachindo
        int index;     // Array lo current position
        int val;       // Current value

        Element(int listIndex, int index, int val) {
            this.listIndex = listIndex;
            this.index = index;
            this.val = val;
        }
    }

    // Telugu: minHeap lo current smallest elements maintain chestham
    private PriorityQueue<Element> minHeap;
    private List<List<Integer>> lists;

    // Constructor lo first elements ni heap lo add cheyyadam
    public MergedKArraysIterator(List<List<Integer>> lists) {
        this.lists = lists;

        minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a.val, b.val));

        for (int i = 0; i < lists.size(); i++) {
            if (!lists.get(i).isEmpty()) {
                minHeap.offer(new Element(i, 0, lists.get(i).get(0)));
            }
        }
    }

    // Telugu: Heap lo elements unte → next element untadi
    @Override
    public boolean hasNext() {
        return !minHeap.isEmpty();
    }

    // Telugu: Next smallest element return cheyyadam and heap ni update cheyyadam
    @Override
    public Integer next() {
        if (!hasNext()) {
            throw new NoSuchElementException("No more elements to return.");
        }

        Element current = minHeap.poll();  // Telugu: current min value pop cheyyadam
        int nextIndex = current.index + 1;

        // Telugu: Same list lo next element unte heap lo add cheyyadam
        if (nextIndex < lists.get(current.listIndex).size()) {
            int nextVal = lists.get(current.listIndex).get(nextIndex);
            minHeap.offer(new Element(current.listIndex, nextIndex, nextVal));
        }

        return current.val;
    }

    // Telugu: remove() optional ga unchavachu, not required for our use case
    @Override
    public void remove() {
        throw new UnsupportedOperationException("Remove not supported.");
    }

    // ✅ Test case for the iterator
    public static void main(String[] args) {
        List<List<Integer>> arrays = Arrays.asList(
            Arrays.asList(1, 4, 5),
            Arrays.asList(1, 3, 4),
            Arrays.asList(2, 6)
        );

        MergedKArraysIterator iterator = new MergedKArraysIterator(arrays);

        System.out.println("Flattened Merged Output using Iterator:");
        while (iterator.hasNext()) {
            System.out.print(iterator.next() + " ");
        }
        // ✅ Output: 1 1 2 3 4 4 5 6
    }
}
```

---

## ✅ Time & Space Complexity

Let `k` = number of arrays, `n` = total number of elements.

| Operation            | Time         | Space  | Notes                              |
| -------------------- | ------------ | ------ | ---------------------------------- |
| Constructor Setup    | `O(k log k)` | `O(k)` | Inserting first elements into heap |
| `next()` per element | `O(log k)`   | `O(k)` | Heap insert/pop                    |
| All `next()` calls   | `O(n log k)` | `O(n)` | Worst case total                   |

✅ **Better than sorting all values upfront**
✅ **Great for streaming/large datasets**

---

## ✅ Interview-Ready Summary

> "Instead of merging K arrays at once, I implemented an iterator with `hasNext()` and `next()` methods. I use a Min Heap to track the next smallest element across all K arrays. This gives O(log K) time per `next()` call and allows on-demand processing of the merged result, which is memory-efficient and supports streaming."

---

Would you like:

* `int[][]` version instead of `List<List<Integer>>`?
* Bidirectional iterator (`previous()`, `peek()`)?
* Lazy evaluation or memory-efficient version for disk-based arrays?

Let me know — happy to provide!
