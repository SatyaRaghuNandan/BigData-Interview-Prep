Here’s a clean, interview-ready solution to **check if a binary tree is a valid Binary Search Tree (BST)**.

---

## ✅ Problem: Validate Binary Search Tree (Leetcode 98)

### ❓ Definition

A Binary Search Tree (BST) is valid if:

* For every node, **left subtree values < node value**, and
* **right subtree values > node value**

This must apply **recursively** to the entire tree.

---

## ✅ Approach: Recursive Min/Max Range Validation

* Use **DFS traversal**
* Pass down **valid range** (`min`, `max`) that each node must lie between
* A node’s value must be:

  * `> min`
  * `< max`

---

## ✅ Java Code

```java
class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class ValidateBST {
    
    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean validate(TreeNode node, long min, long max) {
        if (node == null) return true;

        if (node.val <= min || node.val >= max) return false;

        // Left subtree must be < node.val
        // Right subtree must be > node.val
        return validate(node.left, min, node.val) &&
               validate(node.right, node.val, max);
    }

    public static void main(String[] args) {
        ValidateBST validator = new ValidateBST();

        // ✅ Valid BST
        TreeNode root1 = new TreeNode(5);
        root1.left = new TreeNode(3);
        root1.right = new TreeNode(7);
        System.out.println("Valid BST: " + validator.isValidBST(root1)); // true

        // ❌ Invalid BST (left child > parent)
        TreeNode root2 = new TreeNode(5);
        root2.left = new TreeNode(6);
        root2.right = new TreeNode(7);
        System.out.println("Valid BST: " + validator.isValidBST(root2)); // false

        // ❌ Invalid BST (right child <= parent)
        TreeNode root3 = new TreeNode(10);
        root3.left = new TreeNode(5);
        root3.right = new TreeNode(10);
        System.out.println("Valid BST: " + validator.isValidBST(root3)); // false
    }
}
```

---

## 🧪 Test Cases

| Tree Structure           | Is Valid BST? |
| ------------------------ | ------------- |
| `5 → 3, 7`               | ✅ Yes         |
| `5 → 6, 7` (6 on left)   | ❌ No          |
| `10 → 5, 10` (duplicate) | ❌ No          |

---

## 🧠 Time & Space Complexity

| Metric | Value              |
| ------ | ------------------ |
| Time   | O(N)               |
| Space  | O(H) (stack)       |
| Notes  | H = height of tree |

---

Let me know if you want an iterative version using Stack, or want to validate **duplicate allowed** BSTs (e.g., on left only).
