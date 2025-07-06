Here’s a **detailed Java solution** for **LeetCode 701 – Insert into a Binary Search Tree**, covering both **recursive** and **iterative** approaches.

---

## ✅ Problem Summary

> You are given the `root` of a binary search tree (BST) and an integer `val`. Insert `val` into the BST such that the BST property is maintained. Return the root of the modified tree.

---

## ✅ Approach 1: Recursive Solution

### 🔁 Idea

* Traverse the tree recursively.
* If `val < node.val`, insert into the **left subtree**.
* Else, insert into the **right subtree**.
* Create a new node when you reach `null`.

### ✅ Code

```java
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        // Base case: insert at the null position
        if (root == null) {
            return new TreeNode(val);
        }

        if (val < root.val) {
            // Go left
            root.left = insertIntoBST(root.left, val);
        } else {
            // Go right
            root.right = insertIntoBST(root.right, val);
        }

        return root;
    }
}
```

### 🧠 Time and Space Complexity

| Metric           | Value                                                                            |
| ---------------- | -------------------------------------------------------------------------------- |
| Time Complexity  | `O(h)` where `h` is tree height (`O(log n)` for balanced BST, `O(n)` for skewed) |
| Space Complexity | `O(h)` recursion stack                                                           |

---

## ✅ Approach 2: Iterative Solution

### 🔁 Idea

* Traverse the tree using a loop instead of recursion.
* Track the current node.
* When we find the null spot where `val` should go, attach the new node.

### ✅ Code

```java
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        // If tree is empty
        if (root == null) {
            return new TreeNode(val);
        }

        TreeNode current = root;

        while (true) {
            if (val < current.val) {
                if (current.left == null) {
                    current.left = new TreeNode(val);
                    break;
                }
                current = current.left;
            } else {
                if (current.right == null) {
                    current.right = new TreeNode(val);
                    break;
                }
                current = current.right;
            }
        }

        return root;
    }
}
```

### 🧠 Time and Space Complexity

| Metric           | Value                 |
| ---------------- | --------------------- |
| Time Complexity  | `O(h)`                |
| Space Complexity | `O(1)` (no recursion) |

---

## ✅ Sample Usage

```java
public static void main(String[] args) {
    TreeNode root = new TreeNode(4);
    root.left = new TreeNode(2);
    root.right = new TreeNode(7);

    Solution sol = new Solution();
    TreeNode updatedRoot = sol.insertIntoBST(root, 5);

    // Perform inorder traversal to see if 5 is inserted
    inorder(updatedRoot); // Should print: 2 4 5 7
}

private static void inorder(TreeNode root) {
    if (root == null) return;
    inorder(root.left);
    System.out.print(root.val + " ");
    inorder(root.right);
}
```

---

Would you like:

* A **visual walkthrough** of how insertion works step-by-step?
* This in **Python** or **C++**?
* The **unit tests or JUnit** setup?

Let me know!
