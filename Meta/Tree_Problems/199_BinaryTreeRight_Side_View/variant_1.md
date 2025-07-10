# // VARIANT: What if you had to return both the left- and right side views of a binary tree?

You're testing a **custom tree traversal variant** that prints the **left-side view reversed + right-side view (excluding root duplication)** — a combination of left-to-right boundary visual layers of the tree. Let's break it down with:

---

## ✅ What the Code Does (High-Level)

### 🔍 Function: `leftRightSideViewVariant()`

* **Collects**:

  * Leftmost node from each level (`left_side`)
  * Rightmost node from each level (`right_side`)

* **Final result**:

  ```
  reversed(left_side) + right_side[1:]
  ```

### 🧠 Output Meaning:

* First half: bottom-to-top **left view**
* Second half: top-to-bottom **right view**
* `right_side[1:]` avoids duplicating the root (already in left\_side reversed)

---

## ✅ Java Code with Telugu Comments


```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

class Solution {
    public List<Integer> leftRightSideViewVariant(TreeNode root) {
        if (root == null) return new ArrayList<>();

        List<Integer> leftSide = new ArrayList<>();   // Prathi level lo first (leftmost) node
        List<Integer> rightSide = new ArrayList<>();  // Prathi level lo last (rightmost) node
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);  // BFS traversal ki root node ni queue lo pettaali

        while (!queue.isEmpty()) {
            int levelSize = queue.size();  // Ee level lo entha mandi unnaru

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();

                // First node of this level — left side view
                if (i == 0) {
                    leftSide.add(node.val);
                }

                // Last node of this level — right side view
                if (i == levelSize - 1) {
                    rightSide.add(node.val);
                }

                // Children ni next level queue lo veyyadam
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }

        // leftSide reverse cheyyadam (bottom-up order)
        Collections.reverse(leftSide);

        // rightSide[1:] ni include cheyyadam (duplicate root avoid cheyyadam ki)
        for (int i = 1; i < rightSide.size(); i++) {
            leftSide.add(rightSide.get(i));
        }

        return leftSide;
    }
}
```

## ✅ Python Code with Telugu Comments

```python
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leftRightSideViewVariant(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        left_side = []      # Prathi level lo first (leftmost) node ni store cheyyadam
        right_side = []     # Prathi level lo last (rightmost) node ni store cheyyadam
        q = deque([root])   # BFS traversal ki queue

        while q:
            size = len(q)   # Current level size

            for i in range(size):
                node = q.popleft()

                # First node of this level — left side view
                if i == 0:
                    left_side.append(node.val)

                # Last node of this level — right side view
                if i == size - 1:
                    right_side.append(node.val)

                # Children ni next level queue lo veyyadam
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        # left_side reverse cheyyadam — bottom-up order kavali
        # right_side[1:] — root ni duplicate cheyyakunda avoid cheyyadam
        result = list(reversed(left_side)) + right_side[1:]
        return result
```

---

## 🧪 Sample Output Example

For:

```
        1
       / \
      2   3
     /     \
    5       4
```

* `left_side = [1, 2, 5]`
  → reversed = `[5, 2, 1]`

* `right_side = [1, 3, 4]`
  → right\_side\[1:] = `[3, 4]`

✅ Final Output = `[5, 2, 1, 3, 4]`

---

## ⏱ Time & Space Complexity

| Metric           | Value                                    |
| ---------------- | ---------------------------------------- |
| Time Complexity  | `O(N)` – every node visited once         |
| Space Complexity | `O(W)` – queue size at max width of tree |

---

Let me know if you want to:

* Visualize level-by-level traversal
* Extend this to a **spiral view**
* Or combine **top + bottom** view in one pass!
