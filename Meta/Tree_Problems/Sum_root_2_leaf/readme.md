Absolutely! Let's convert all **three approaches (DFS, BFS, Morris Traversal)** for **Leetcode 129 - Sum Root to Leaf Numbers** into clean, well-commented **Java versions**.

We'll also include **time/space complexity** and **Telugu transliterated comments**.

---

## ✅ Approach 1: Recursive DFS (Top-down)

### 🔧 Logic:

* Root nunchi leaf varaku path follow cheyyadam.
* Each node lo current number ni `cur * 10 + node.val` laga build cheyyadam.
* Leaf ki reach aithe, a number ni sum lo add cheyyadam.

### ✅ Java Code:

```java
class Solution {
    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int curSum) {
        if (node == null) return 0;

        // Path number ni build cheyyadam
        curSum = curSum * 10 + node.val;

        // Leaf ayithe return cheyyadam
        if (node.left == null && node.right == null) {
            return curSum;
        }

        // Left + Right subpaths total
        return dfs(node.left, curSum) + dfs(node.right, curSum);
    }
}
```

### ⏱ Time: `O(N)` — every node once

### 📦 Space: `O(H)` — recursion stack

---

## ✅ Approach 2: BFS (Iterative with Queue)

### 🔧 Logic:

* Breadth-First Traversal
* Queue lo `(node, pathSum)` pairs store cheyyadam
* Leaf ki reach ayite total lo add cheyyadam

### ✅ Java Code:

```java
import java.util.*;

class Solution {
    public int sumNumbers(TreeNode root) {
        if (root == null) return 0;

        int total = 0;
        Queue<Pair<TreeNode, Integer>> queue = new LinkedList<>();
        queue.offer(new Pair<>(root, root.val));

        while (!queue.isEmpty()) {
            Pair<TreeNode, Integer> entry = queue.poll();
            TreeNode node = entry.getKey();
            int currentSum = entry.getValue();

            // Leaf node ayite total lo add cheyyadam
            if (node.left == null && node.right == null) {
                total += currentSum;
            }

            if (node.left != null) {
                queue.offer(new Pair<>(node.left, currentSum * 10 + node.left.val));
            }
            if (node.right != null) {
                queue.offer(new Pair<>(node.right, currentSum * 10 + node.right.val));
            }
        }

        return total;
    }
}
```

> 🔸 Use `javafx.util.Pair` or create your own `Pair` class if `javafx` not available.

### ⏱ Time: `O(N)`

### 📦 Space: `O(W)` — width of tree (max queue size)

---

## ✅ Approach 3: Morris Traversal (Constant Space)

### 🔧 Logic:

* Morris Preorder traversal with threading
* Path number build cheyyadam with rollback (backtrack) using digit count
* Leaf ayite sum lo add cheyyadam
* Tree ni restore cheyyadam

### ✅ Java Code:

```java
class Solution {
    public int sumNumbers(TreeNode root) {
        int totalSum = 0;
        int currentNumber = 0;
        int depth = 0;

        TreeNode current = root;

        while (current != null) {
            if (current.left != null) {
                TreeNode predecessor = current.left;
                depth = 1;

                // Find rightmost child in left subtree
                while (predecessor.right != null && predecessor.right != current) {
                    predecessor = predecessor.right;
                    depth++;
                }

                if (predecessor.right == null) {
                    // Threading: connect to root and go left
                    predecessor.right = current;
                    currentNumber = currentNumber * 10 + current.val;
                    current = current.left;
                } else {
                    // Unthreading
                    predecessor.right = null;
                    if (predecessor.left == null) {
                        totalSum += currentNumber;
                    }

                    // Backtrack → remove last 'depth' digits
                    currentNumber /= Math.pow(10, depth);
                    current = current.right;
                }
            } else {
                // No left → visit and go right
                currentNumber = currentNumber * 10 + current.val;
                if (current.right == null) {
                    totalSum += currentNumber;
                }
                current = current.right;
            }
        }

        return totalSum;
    }
}
```

> ✨ This version uses `Math.pow(10, depth)` to backtrack digits.

### ⏱ Time: `O(N)`

### 📦 Space: `O(1)` (No recursion or queue)

---

## ✅ Summary Table

| Approach         | Time   | Space  | Pros                 | Cons                   |
| ---------------- | ------ | ------ | -------------------- | ---------------------- |
| DFS (Recursive)  | `O(N)` | `O(H)` | Clean and easy       | Stack overflow if deep |
| BFS (Queue)      | `O(N)` | `O(W)` | Iterative            | Queue space needed     |
| Morris Traversal | `O(N)` | `O(1)` | Most space efficient | Harder to implement    |

---

Would you like:

* A **dry-run** on a sample tree?
* A **visual diagram** of Morris threading?
* Or a **unit test class** in Java to test all approaches?

Let me know!
