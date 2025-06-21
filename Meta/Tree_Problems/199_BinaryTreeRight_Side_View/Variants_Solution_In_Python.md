Here’s the complete **Python implementation** of the **Tree Mountain View** problem using both **DFS** and **BFS** approaches, along with:

* ✅ **Telugu comments**
* ✅ Full test cases
* ✅ Edge case handling
* ✅ Time & space complexity

---

## ✅ Python Code: DFS-Based Approach

```python
from typing import List, Optional
from collections import deque

# 🧱 Binary Tree Node Definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mountainView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # Telugu: Root lekapothe empty result
        if not root:
            return result

        left_view = []
        right_view = []

        # Telugu: Left view collect cheyyadam (left subtree priority)
        def leftViewDFS(node, level):
            if not node:
                return
            if level == len(left_view):
                left_view.append(node.val)
            leftViewDFS(node.left, level + 1)
            leftViewDFS(node.right, level + 1)

        # Telugu: Right view collect cheyyadam (right subtree priority)
        def rightViewDFS(node, level):
            if not node:
                return
            if level == len(right_view):
                right_view.append(node.val)
            rightViewDFS(node.right, level + 1)
            rightViewDFS(node.left, level + 1)

        leftViewDFS(root, 0)
        rightViewDFS(root, 0)

        left_view.reverse()  # Telugu: Left view ni reverse cheyyadam
        result.extend(left_view)
        result.extend(right_view[1:])  # Telugu: Root ni skip cheyyadam in right view

        return result
```

---

## ✅ Python Code: BFS-Based Approach (Level Order)

```python
class SolutionBFS:
    def mountainView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        left_view = []
        right_view = []

        queue = deque([(root, 0)])  # Telugu: Queue lo (node, level) tuples

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node, level = queue.popleft()

                if i == 0 and level == len(left_view):
                    left_view.append(node.val)
                if i == level_size - 1 and level == len(right_view):
                    right_view.append(node.val)

                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

        left_view.reverse()
        result.extend(left_view)
        result.extend(right_view[1:])  # Skip root in right view

        return result
```

---

## ✅ Example Usage and Test Cases

```python
def build_tree_from_tuple(data):
    """Helper: Create tree from nested tuples like (1, (2, ...), (3, ...))"""
    if not data:
        return None
    val, left, right = data if isinstance(data, tuple) else (data, None, None)
    return TreeNode(val, build_tree_from_tuple(left), build_tree_from_tuple(right))


def run_tests():
    sol = Solution()
    sol_bfs = SolutionBFS()

    def test_and_print(name, root_data, expected):
        root = build_tree_from_tuple(root_data)
        out_dfs = sol.mountainView(root)
        out_bfs = sol_bfs.mountainView(root)
        print(f"✅ {name} | DFS: {out_dfs} | BFS: {out_bfs} | Expected: {expected}")
        assert out_dfs == expected
        assert out_bfs == expected

    # Test Case 1
    test_and_print("Example Tree", (1, (2, (5, None, None), None), (3, None, (4, None, None))), [5, 2, 1, 3, 4])
    # Test Case 2: Single Node
    test_and_print("Single Node", (1, None, None), [1])
    # Test Case 3: Left-skewed
    test_and_print("Left Skewed", (1, (2, (3, None, None), None), None), [3, 2, 1, 2, 3])
    # Test Case 4: Balanced Tree
    test_and_print("Balanced Tree", (1, (2, (4, None, None), (5, None, None)), (3, (6, None, None), (7, None, None))), [4, 2, 1, 3, 7])
    # Test Case 5: Empty
    test_and_print("Empty Tree", None, [])

run_tests()
```

---

## 📊 Complexity Analysis

### ✅ DFS

* **Time**: `O(n)`
* **Space**: `O(h)` recursion stack, `O(h)` result lists

### ✅ BFS

* **Time**: `O(n)`
* **Space**: `O(w)` queue, `O(h)` result lists

Where:

* `n` = number of nodes
* `h` = height
* `w` = width

---

## 🗣️ Summary in Telugu

> "Tree Mountain View lo left view ni reverse cheyyadam, right view lo root ni skip cheyyadam. DFS lo rendu traversals, BFS lo single traversal. Output lo reverse(left view) + right view (excluding root)."

---

Let me know if you'd like this as a LeetCode-style `TreeNode` class with serialization, or need visualization diagrams!
