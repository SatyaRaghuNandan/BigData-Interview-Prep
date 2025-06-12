Awesome! You’ve covered **all four standard approaches** to solve **LeetCode 199: Binary Tree Right Side View**. Below, I’ll walk you through each approach with:

1. ✅ **Python code with detailed inline comments**
2. ✅ **High-level explanation**
3. ✅ **Time and space complexity**

---

## ✅ Approach 1: BFS using **Two Queues**

### 💡 Idea:

Use two queues — one for the **current level** and one for the **next level**. After each level finishes, add the **last node** from that level to the result (this will be the rightmost one).

### 💻 Code with Comments:

```python
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        next_level = deque([root])  # Queue for next level
        rightside = []

        while next_level:
            curr_level = next_level  # Move nodes from next to current level
            next_level = deque()     # Clear next_level for the next iteration

            while curr_level:
                node = curr_level.popleft()

                # Add children to next_level queue
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # After current level ends, the last node is the rightmost
            rightside.append(node.val)

        return rightside
```

### ⏱ Complexity:

* **Time:** `O(N)` – visit each node once
* **Space:** `O(W)` – max width of the tree (due to the queue)

---

## ✅ Approach 2: BFS using **One Queue + Sentinel (None)**

### 💡 Idea:

Use a single queue and use `None` as a **level delimiter**. Track the previous node and when the level ends, `prev` will be the rightmost.

### 💻 Code with Comments:

```python
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        queue = deque([root, None])  # Sentinel marks the end of the level
        rightside = []
        curr = root

        while queue:
            prev, curr = curr, queue.popleft()

            while curr:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                prev, curr = curr, queue.popleft()

            # End of level reached → prev is the last node of the level
            rightside.append(prev.val)

            # Queue still has nodes → push sentinel for next level
            if queue:
                queue.append(None)

        return rightside
```

### ⏱ Complexity:

* **Time:** `O(N)`
* **Space:** `O(W)`
* **Note:** Sentinel `None` helps mark level boundaries cleanly.

---

## ✅ Approach 3: BFS using **One Queue + Level Size Measurement**

### 💡 Idea:

Track the number of nodes at each level (`level_length`). Iterate through those many nodes and store the **last node** of that level.

### 💻 Code with Comments:

```python
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        queue = deque([root])
        rightside = []

        while queue:
            level_length = len(queue)  # Number of nodes at this level

            for i in range(level_length):
                node = queue.popleft()

                # Rightmost node of the level
                if i == level_length - 1:
                    rightside.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rightside
```

### ⏱ Complexity:

* **Time:** `O(N)`
* **Space:** `O(W)`
* **Note:** Clean and widely used in BFS-based level-order problems

---

## ✅ Approach 4: **Recursive DFS (Right-to-Left Preorder)**

### 💡 Idea:

Do a DFS, but visit the **right child first**. When we hit a new level (level == len(rightside)), the first node we see is the **rightmost** for that level.

### 💻 Code with Comments:

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        rightside = []

        def helper(node: TreeNode, level: int) -> None:
            # If this is the first time we're visiting this level
            if level == len(rightside):
                rightside.append(node.val)

            # First go right (to capture rightmost first), then left
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)

        helper(root, 0)
        return rightside
```

### ⏱ Complexity:

* **Time:** `O(N)`
* **Space:** `O(H)` – due to recursion stack (H = height of tree)
* **Note:** Elegant for interview, especially for recursion-heavy problems

---

## 🏁 Summary Table:

| Approach                     | Time | Space | Notes                                |
| ---------------------------- | ---- | ----- | ------------------------------------ |
| BFS (Two Queues)             | O(N) | O(W)  | Simple, clean separation of levels   |
| BFS (One Queue + Sentinel)   | O(N) | O(W)  | Elegant level boundary marking       |
| BFS (One Queue + Level Size) | O(N) | O(W)  | Most practical + clean               |
| DFS (Recursive, right-first) | O(N) | O(H)  | Recursive, great if tree is not deep |

---

### ✅ Interview Recommendation:

* **Go with Approach 3 (One Queue + Level Size)** or **Approach 4 (Recursive DFS)** depending on the question theme.
* BFS is safer for **deep trees** (avoids recursion limit).
* DFS gives a nice recursive flavor and shows control over tree traversal order.

Let me know if you want the **left side view**, or **bottom/top view** next!
