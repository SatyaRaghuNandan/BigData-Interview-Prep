Here’s your text fully formatted and structured for clarity, professionalism, and readability — especially useful for documentation, blogs, or interview prep:

---

# ✅ Tree Mountain View (Java Implementation with Telugu Comments)

This problem is a custom variant of **LeetCode 199: Binary Tree Right Side View**, where the output consists of:

* The **left view reversed**, followed by
* The **right view excluding the root**.

---

## 📌 Problem Description

### ✳️ Input:

Root node of a binary tree.

### ✳️ Output:

A list representing:
`reverse(left view) + right view (excluding the root node)`

### 🔍 Example:

Given the tree:

```
      1
     / \
    2   3
   /     \
  5       4
```

* **Left View** = `[1, 2, 5]` → reversed = `[5, 2, 1]`
* **Right View** = `[1, 3, 4]` → exclude root = `[3, 4]`
* **Output** = `[5, 2, 1, 3, 4]`

---

## 🛠️ Java Implementations

### 🧠 Approach

* Compute both views (left and right) using either **DFS** or **BFS**.
* Reverse the left view and skip the root from the right view.
* Concatenate the two lists.

---

## 🔷 DFS-Based Java Solution (Dual Traversals)

```java
class Solution {
    public List<Integer> mountainView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;

        List<Integer> leftView = new ArrayList<>();
        List<Integer> rightView = new ArrayList<>();

        // Telugu: Left view ni compute cheyyadam
        leftViewDFS(root, 0, leftView);
        // Telugu: Right view ni compute cheyyadam
        rightViewDFS(root, 0, rightView);

        Collections.reverse(leftView);
        result.addAll(leftView);
        result.addAll(rightView.subList(1, rightView.size())); // Skip root

        return result;
    }

    private void leftViewDFS(TreeNode node, int level, List<Integer> leftView) {
        if (node == null) return;
        if (level == leftView.size()) leftView.add(node.val);
        leftViewDFS(node.left, level + 1, leftView);
        leftViewDFS(node.right, level + 1, leftView);
    }

    private void rightViewDFS(TreeNode node, int level, List<Integer> rightView) {
        if (node == null) return;
        if (level == rightView.size()) rightView.add(node.val);
        rightViewDFS(node.right, level + 1, rightView);
        rightViewDFS(node.left, level + 1, rightView);
    }
}
```

---

## 🔶 BFS-Based Java Solution (Single Pass)

```java
class Solution {
    public List<Integer> mountainView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;

        List<Integer> leftView = new ArrayList<>();
        List<Integer> rightView = new ArrayList<>();
        Queue<Object[]> queue = new LinkedList<>();
        queue.offer(new Object[]{root, 0});

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                Object[] entry = queue.poll();
                TreeNode node = (TreeNode) entry[0];
                int level = (int) entry[1];

                if (i == 0 && level == leftView.size()) leftView.add(node.val);
                if (i == levelSize - 1 && level == rightView.size()) rightView.add(node.val);

                if (node.left != null) queue.offer(new Object[]{node.left, level + 1});
                if (node.right != null) queue.offer(new Object[]{node.right, level + 1});
            }
        }

        Collections.reverse(leftView);
        result.addAll(leftView);
        result.addAll(rightView.subList(1, rightView.size())); // Skip root

        return result;
    }
}
```

---

## 🧪 Test Cases

### ✅ Test Case 1: Base Example

```
      1
     / \
    2   3
   /     \
  5       4
```

* Output: `[5, 2, 1, 3, 4]`

### ✅ Test Case 2: Single Node

```
1
```

* Output: `[1]`

### ✅ Test Case 3: Left-Skewed Tree

```
1
 \
  2
   \
    3
```

* Output: `[3, 2, 1, 2, 3]`

### ✅ Test Case 4: Full Balanced Tree

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

* Output: `[4, 2, 1, 3, 7]`

### ✅ Test Case 5: Empty Tree

* Output: `[]`

---

## ⏱️ Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes          |
| -------- | --------------- | ---------------- | -------------- |
| DFS      | `O(n)`          | `O(h)`           | Two DFS passes |
| BFS      | `O(n)`          | `O(w)`           | Single pass    |

Where:

* `n` = number of nodes
* `h` = height of tree
* `w` = max width of tree

---

## 🗣️ Telugu Explanation Summary

> **“Ee problem lo left view ni reverse chesi, right view lo root ni skip chesi, rendu combine chestam. DFS lo rendu separate traversals, BFS lo single pass use chestam. DFS space `O(h)`, BFS space `O(w)`. Time rendu ki `O(n)`. Example tree `[1 (2, 3) (5, 4)]` ki output `[5, 2, 1, 3, 4]`.”**

(Translation: We reverse the left view, skip the root in the right view, and combine both. DFS does two separate traversals, BFS handles both in one pass.)

---

## 🏁 Final Notes

* ✅ This pattern is useful in UI-focused questions (tree visualization).
* ✅ Preferred approach: **BFS** for clarity and single-pass traversal.
* 🧠 Both are acceptable in interviews depending on the constraints.

Let me know if you'd like the **Python version**, unit tests, or this as a LeetCode-style class!
