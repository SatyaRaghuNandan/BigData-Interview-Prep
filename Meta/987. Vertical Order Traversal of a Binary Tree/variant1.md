# // VARIANT: What if you had to print the order of nodes?

Thanks! Since you're analyzing a **printing variant** of Leetcode 987, let me now give you the **C++ → Java conversion** for this variant where the output is **printed column by column** instead of returning a nested list.

We'll use:

* ✅ `TreeMap<Integer, List<Pair>>` → auto-sorts by column
* ✅ BFS traversal (tracks row, col)
* ✅ Custom sorting by `(row, value)`
* ✅ Print column-by-column instead of returning a list

---

## ✅ Java Code (Print Variant) with Telugu Comments

```java
import java.util.*;

// Binary Tree Node structure
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

public class VerticalOrderPrinter {

    // Helper class to hold (row, value) for sorting
    static class Pair {
        int row;
        int val;
        Pair(int row, int val) {
            this.row = row;
            this.val = val;
        }
    }

    // NodeInfo → BFS ki required meta info: node + row + col
    static class NodeInfo {
        TreeNode node;
        int row, col;

        NodeInfo(TreeNode node, int row, int col) {
            this.node = node;
            this.row = row;
            this.col = col;
        }
    }

    // Main function that prints vertical order column-wise
    public void printVerticalOrder(TreeNode root) {
        // TreeMap use chestham: column-wise sort automatic
        TreeMap<Integer, List<Pair>> colMap = new TreeMap<>();

        // Queue for BFS: node + row + col
        Queue<NodeInfo> queue = new LinkedList<>();
        queue.offer(new NodeInfo(root, 0, 0));

        while (!queue.isEmpty()) {
            NodeInfo current = queue.poll();

            // Column lo (row, val) add cheyyadam
            colMap
                .computeIfAbsent(current.col, k -> new ArrayList<>())
                .add(new Pair(current.row, current.node.val));

            // Left ki move ayina → row + 1, col - 1
            if (current.node.left != null)
                queue.offer(new NodeInfo(current.node.left, current.row + 1, current.col - 1));

            // Right ki move ayina → row + 1, col + 1
            if (current.node.right != null)
                queue.offer(new NodeInfo(current.node.right, current.row + 1, current.col + 1));
        }

        // Each column ni print cheyyadam, sorted by row then value
        for (Map.Entry<Integer, List<Pair>> entry : colMap.entrySet()) {
            List<Pair> colList = entry.getValue();

            // Sort by row, then by val
            Collections.sort(colList, (a, b) -> {
                if (a.row != b.row) return Integer.compare(a.row, b.row);
                return Integer.compare(a.val, b.val);
            });

            // Print this column
            for (Pair p : colList) {
                System.out.print(p.val + " ");
            }
            System.out.println(); // New line for each column
        }
    }

    // ✅ Test code
    public static void main(String[] args) {
        /*
              6
            /   \
           8     7
          / \   / \
         3  15 10  9
             /
            1
        */

        TreeNode root = new TreeNode(6);
        root.left = new TreeNode(8);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(15);
        root.right.left = new TreeNode(10);
        root.right.right = new TreeNode(9);
        root.left.right.left = new TreeNode(1);

        VerticalOrderPrinter printer = new VerticalOrderPrinter();
        printer.printVerticalOrder(root);
    }
}
```

---

## ✅ Output for Above Tree

```
3 
8 1 
6 10 15 
7 
9 
```

---

## ✅ Time & Space Complexity

Let `N` be total number of nodes.

| Operation                | Time         | Explanation                      |
| ------------------------ | ------------ | -------------------------------- |
| BFS traversal            | `O(N)`       | One pass over all nodes          |
| Grouping into map        | `O(N)`       | One insert per node              |
| Sorting each column list | `O(N log N)` | Due to tie-breaking (row, value) |
| Printing all values      | `O(N)`       | Linear traversal                 |
| **Total Time**           | `O(N log N)` | Sorting dominates                |
| **Space**                | `O(N)`       | Map, queue, result               |

---

## ✅ Summary for Interviews

> “This is a **print-only variant** of vertical order traversal. Instead of returning a nested structure, I use a **BFS traversal** to capture each node’s `(row, col)` and group nodes into a `TreeMap`. Each column’s node list is sorted by `(row, value)` before printing. This method is ideal for debugging tree structure visually, and the time complexity is `O(N log N)` due to per-column sorting.”

---

Would you like:

✅ Side-by-side comparison of **return vs print** code?
✅ Java version with `List<List<Integer>>` return?
✅ Dry run for a custom tree?

Let me know!


Great point — let’s **explicitly list the differences** between the **original Leetcode 987 problem** and the **print-based variant** you’re analyzing. We'll break it down clearly across **input/output, purpose, structure, and usage**.

---

## ✅ Difference Between Original (Leetcode 987) and Print Variant

| Feature / Aspect       | 🔷 Original Problem (Leetcode 987)                       | ✅ Variant (Your Code)                              |
| ---------------------- | -------------------------------------------------------- | -------------------------------------------------- |
| **Problem Goal**       | Return `List<List<Integer>>` for vertical order          | **Print** each vertical column to console          |
| **Output Format**      | Structured, nested list: `[[col1], [col2], ..., [coln]]` | Flat console output: one column per line           |
| **Return Value**       | Returns result to caller for further use or testing      | No return value – side effect is printing          |
| **Usage Scenario**     | Integration into other logic / test harness              | Visualization, debugging, manual inspection        |
| **Testability**        | Can be unit-tested with assertions                       | Requires output capture (e.g., stdout) for testing |
| **Consumer of Output** | Programmatic → function/method calls                     | Human → console reader or log file                 |
| **Language Construct** | Uses data structures (lists/maps) for return             | Uses `System.out.print` or `std::cout`             |
| **Performance Intent** | Return result as efficiently as possible                 | Visual clarity more important than efficiency      |
| **Common Use Case**    | Production-grade solution                                | Debugging or interview whiteboard version          |
| **Sorting Behavior**   | Explicit `(row, value)` sorting required                 | Same sorting logic used but directly printed       |
| **Final Step**         | Aggregate into a list                                    | Iterate and print each column directly             |

---

## 🧠 Why This Difference Matters

| Context                       | Original Version                              | Print Variant                                    |
| ----------------------------- | --------------------------------------------- | ------------------------------------------------ |
| ✅ Leetcode/Test Cases         | Needs return format → list of lists           | ❌ Will fail if only `System.out.print` is used   |
| 🧪 Unit Testing               | Easy to write `assertEquals(...)` tests       | Needs capturing console output or mock print     |
| 🧑‍🏫 Interviews (Whiteboard) | Return version preferred for clean API design | Print version acceptable for "show the result"   |
| 🛠️ Debugging                 | Less useful unless you manually inspect list  | More helpful to visually verify column alignment |

---

## 🏁 Summary

> The **core traversal and grouping logic is the same** between Leetcode 987 and your variant.
> The key difference is: **one returns structured data**, while the other **prints output for visual debugging or console-based interpretation**.

---

Let me know if you’d like:

* A **side-by-side code comparison**
* A **return-based version** of the print variant
* How to **unit test** a print-based implementation

Happy to provide all!

