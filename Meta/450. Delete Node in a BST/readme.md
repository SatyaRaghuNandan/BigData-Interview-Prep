Here are **both Recursive and Iterative** Java solutions for **Leetcode 450 – Delete Node in a BST**, with clear structure, dry-run guidance, and complexity analysis.

---

## ✅ Problem Recap

> Given a root of a **Binary Search Tree** (BST) and a `key`, delete the node with that key and return the updated root.

---

## ✅ Recursive Solution (Preferred in Interviews)

```java
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;

        if (key < root.val) {
            root.left = deleteNode(root.left, key); // go left
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key); // go right
        } else {
            // Found node to delete
            if (root.left == null) return root.right;    // Case 1 or 2
            if (root.right == null) return root.left;    // Case 2
            // Case 3: Two children → replace with inorder successor
            TreeNode minNode = getMin(root.right);
            root.val = minNode.val;
            root.right = deleteNode(root.right, minNode.val); // delete successor
        }

        return root;
    }

    private TreeNode getMin(TreeNode node) {
        while (node.left != null)
            node = node.left;
        return node;
    }
}
```

---

## ✅ Iterative Version (Rare but Possible)

```java
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        TreeNode parent = null, curr = root;

        // Step 1: Find the node to delete
        while (curr != null && curr.val != key) {
            parent = curr;
            if (key < curr.val) curr = curr.left;
            else curr = curr.right;
        }

        if (curr == null) return root; // Key not found

        // Step 2: Handle case where node has two children
        if (curr.left != null && curr.right != null) {
            // Find inorder successor
            TreeNode successorParent = curr;
            TreeNode successor = curr.right;
            while (successor.left != null) {
                successorParent = successor;
                successor = successor.left;
            }
            curr.val = successor.val; // Replace value
            curr = successor;         // Now delete successor node
            parent = successorParent;
        }

        // Step 3: Node has 0 or 1 child
        TreeNode child = (curr.left != null) ? curr.left : curr.right;

        if (parent == null) {
            return child; // Deleting root node
        }

        if (parent.left == curr) parent.left = child;
        else parent.right = child;

        return root;
    }
}
```

---

## ✅ Time & Space Complexity

| Operation | Recursive      | Iterative         |
| --------- | -------------- | ----------------- |
| **Time**  | `O(h)`         | `O(h)`            |
| **Space** | `O(h)` (stack) | `O(1)` (no stack) |

> `h` is height of tree: `O(log n)` for balanced, `O(n)` for skewed tree

---

## ✅ Sample Test

```java
public static void main(String[] args) {
    TreeNode root = new TreeNode(5);
    root.left = new TreeNode(3);
    root.right = new TreeNode(6);
    root.left.left = new TreeNode(2);
    root.left.right = new TreeNode(4);
    root.right.right = new TreeNode(7);

    Solution sol = new Solution();
    TreeNode newRoot = sol.deleteNode(root, 3);
    printInorder(newRoot);  // Output: 2 4 5 6 7
}

public static void printInorder(TreeNode node) {
    if (node == null) return;
    printInorder(node.left);
    System.out.print(node.val + " ");
    printInorder(node.right);
}
```

---

## 🧠 How to Remember

* **Recursive**:

  * Traverse BST like search
  * If key found:

    * 0 or 1 child → just return the child
    * 2 children → find **inorder successor**, replace, and recursively delete
* **Iterative**: Simulate the above with pointers `curr` and `parent`

---

Let me know if you want to visualize each case using diagrams or dry-runs.
