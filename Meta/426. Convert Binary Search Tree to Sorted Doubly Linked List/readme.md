You're solving the classic **Leetcode 426 – Convert Binary Search Tree to a Sorted Circular Doubly Linked List**.
Let’s walk through it **line-by-line** with:

✅ Detailed \*\*Telugu-style comments (in English script)
✅ Time & Space Complexity
✅ Edge cases
✅ Test Cases

---

### ✅ Problem Statement (in short)

Given a **BST**, convert it to a **sorted, circular, doubly linked list** **in-place**.
Each node should have `.left` and `.right` pointing to **previous** and **next** nodes respectively.

---

### ✅ Clean Java Code with Detailed Telugu Comments

```java


/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/


class Solution {

  // Global variables to track smallest (first) and last visited node
  Node first = null;
  Node last = null;

  // In-order traversal to build the doubly linked list
  public void helper(Node node) {
    if (node != null) {

      // Telugu: Mundu left subtree ki veltham
      helper(node.left);

      // Telugu: Present node ni process chestam
      if (last != null) {
        // Telugu: Previous node (last) right = current
        last.right = node;

        // Telugu: Current node left = last
        node.left = last;
      } else {
        // Telugu: Idi first time visit ayye node. Smallest element.
        first = node;
      }

      // Telugu: Last pointer ni update cheyyali current node ki
      last = node;

      // Telugu: Now right subtree ki veltham
      helper(node.right);
    }
  }

  public Node treeToDoublyList(Node root) {
    if (root == null) return null; // Telugu: Empty tree ante return null

    helper(root); // Telugu: In-order traversal call

    // Telugu: First and last node ni connect cheyyadam (circular DLL)
    last.right = first;
    first.left = last;

    // Telugu: Return head of DLL
    return first;
  }
}
```

---

### ✅ Time and Space Complexity

| Metric              | Value                                                        |
| ------------------- | ------------------------------------------------------------ |
| ⏱ Time Complexity   | **O(n)** → We visit each node once during in-order traversal |
| 🧠 Space Complexity | **O(h)** → h = height of the tree (due to recursion stack)   |

> If the BST is balanced, `h = log n`, so space is `O(log n)`.
> If it’s skewed, `h = n`, so worst case `O(n)`.

---

### ✅ Edge Cases

1. ✅ Empty Tree → Return `null`
2. ✅ Only 1 Node → Point it to itself → `node.left = node; node.right = node`
3. ✅ Already sorted structure → Output should still be circular DLL
4. ✅ Skewed tree (e.g., all right children or all left children) → Should still work

---

### ✅ Sample Test Cases

#### 🔹 Test Case 1: Empty Tree

```java
Input: root = null
Output: null
```

#### 🔹 Test Case 2: Single Node

```java
Input: root = Node(1)
Output: Node(1) → points to itself (left and right)

Node.left == Node
Node.right == Node
```

#### 🔹 Test Case 3: Balanced BST

```
      4
     / \
    2   5
   / \
  1   3

Output Doubly Linked List (Circular):  
1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5 → and circular back to 1
```

---

### ✅ Dry Run for Input: \[4, 2, 5, 1, 3]

In-order traversal: `1 → 2 → 3 → 4 → 5`
While visiting each node:

* Connect `prev.right = current`
* Connect `current.left = prev`

At the end:

* `first = 1`, `last = 5`
* Connect:

  * `5.right = 1`
  * `1.left = 5`

Return `first`, which is `1`.

---

### ✅ Summary

| Concept                      | Value                     |
| ---------------------------- | ------------------------- |
| Converts BST to DLL          | Yes                       |
| Maintains sorted order       | Yes (in-order)            |
| Circular                     | Yes                       |
| Space Efficient?             | Yes (no extra structures) |
| Time Complexity              | O(n)                      |
| Space Complexity (recursive) | O(h)                      |

Let me know if you want to convert this to **Python** or add **unit tests** using custom Node class!
