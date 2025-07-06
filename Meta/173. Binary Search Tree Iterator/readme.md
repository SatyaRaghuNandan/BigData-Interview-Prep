## 🧭 LeetCode 173 – Binary Search Tree Iterator (Java Version)

---

### ✅ Problem Summary
> Design an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Implement the `BSTIterator` class:
- `BSTIterator(TreeNode root)` initializes the object.
- `int next()` returns the next smallest number.
- `boolean hasNext()` returns whether the next smallest number is available.

---

### ✅ Java Code (with Comments)

```java
import java.util.*;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class BSTIterator {
    private Stack<TreeNode> stack = new Stack<>();

    public BSTIterator(TreeNode root) {
        pushLeft(root); // Push all left nodes to the stack (in-order traversal)
    }

    // Returns the next smallest element
    public int next() {
        TreeNode node = stack.pop();

        // If node has a right subtree, process its left path
        if (node.right != null) {
            pushLeft(node.right);
        }

        return node.val;
    }

    // Returns true if there is a next element
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    // Helper method: Push all left children of a subtree to the stack
    private void pushLeft(TreeNode node) {
        while (node != null) {
            stack.push(node);
            node = node.left;
        }
    }
}
```

---

### ✅ Time and Space Complexity

| Method        | Time Complexity | Space Complexity |
|---------------|------------------|-------------------|
| `next()`      | `O(1)` amortized | `O(h)` where h = height of tree |
| `hasNext()`   | `O(1)`           | `O(h)`            |

- In total, each node is pushed and popped **once**, so total time across `n` calls is `O(n)`.
- Stack holds up to `h` elements, where `h` is the height of the BST.

---

### ✅ Sample Test Case

```java
TreeNode root = new TreeNode(7,
        new TreeNode(3),
        new TreeNode(15,
            new TreeNode(9),
            new TreeNode(20)));

BSTIterator iterator = new BSTIterator(root);
System.out.println(iterator.next());    // returns 3
System.out.println(iterator.next());    // returns 7
System.out.println(iterator.hasNext()); // returns true
System.out.println(iterator.next());    // returns 9
System.out.println(iterator.hasNext()); // returns true
System.out.println(iterator.next());    // returns 15
System.out.println(iterator.hasNext()); // returns true
System.out.println(iterator.next());    // returns 20
System.out.println(iterator.hasNext()); // returns false
```

---

### 🧠 How to Remember This Approach

- Think of **in-order traversal** (Left → Node → Right) = Sorted Order.
- Use a **stack** to simulate the recursive traversal.
- Always **push left nodes** first (simulate the in-order recursion).
- When `next()` is called, pop one node and process its right child.

✅ Tip: All left children are pushed until we reach the smallest node.

---

Let me know if you'd like the **reverse iterator** (for decreasing order) or **next-k smallest** extension!
