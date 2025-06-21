Excellent! You're tackling a classic problem: **Sum Root to Leaf Numbers** (LeetCode 129) — where you treat each path from root to leaf as a number and sum them all.

You've already written the **Morris Traversal** version (bravo 👏) — let's now cover:

---

## 🚀 Problem Recap:

Given a binary tree where each node contains a digit (0-9), each root-to-leaf path represents a number (e.g., 1 → 2 → 3 = 123). Return the sum of all such numbers.

---

## ✅ Approach 1: **DFS (Recursive Preorder)**

### 🔧 Logic:

* Traverse the tree top-down (root to leaf).
* At each node, pass the current path number.
* When a leaf is reached, add that number to total.

### 💻 Code:

```python
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def dfs(node, cur):
        if not node:
            return 0
        cur = cur * 10 + node.val
        if not node.left and not node.right:
            return cur
        return dfs(node.left, cur) + dfs(node.right, cur)
    
    return dfs(root, 0)
```

### ⏱ Time Complexity: `O(N)`

* Every node is visited once.

### 📦 Space Complexity: `O(H)`

* H = height of the tree
* Recursive call stack uses space = `O(H)` in worst case (unbalanced tree).

---

## ✅ Approach 2: **BFS (Iterative Level Order with Queue)**

### 🔧 Logic:

* Use a queue to store `(node, current_number)` pairs.
* When a leaf node is reached, add its path number to total.

### 💻 Code:

```python
from collections import deque

def sumNumbers(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    total = 0
    queue = deque([(root, root.val)])

    while queue:
        node, cur = queue.popleft()
        if not node.left and not node.right:
            total += cur
        if node.left:
            queue.append((node.left, cur * 10 + node.left.val))
        if node.right:
            queue.append((node.right, cur * 10 + node.right.val))
    
    return total
```

### ⏱ Time Complexity: `O(N)`

* Each node is visited once.

### 📦 Space Complexity: `O(W)`

* W = width of the tree (max nodes at any level) — space used by the queue.

---

## ✅ Approach 3: **Morris Traversal (O(1) Space)**

### 🔧 Logic:

* Use **threaded binary tree** (Morris traversal) for root-to-leaf traversal.
* Maintain current number while traversing.
* Restore the tree afterward.

### 💻 Code: (same as yours, with comments)

```python
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    tot_sum, cur, depth = 0, 0, 0
    while root:
        if root.left:
            pre, depth = root.left, 1
            while pre.right and pre.right != root:
                pre, depth = pre.right, depth + 1
            if not pre.right:
                pre.right = root
                cur = cur * 10 + root.val
                root = root.left
            else:
                pre.right = None
                if not pre.left:
                    tot_sum += cur
                cur //= 10**depth
                root = root.right
        else:
            cur = cur * 10 + root.val
            if not root.right:
                tot_sum += cur
            root = root.right
    return tot_sum
```

### ⏱ Time Complexity: `O(N)`

* Every edge is visited at most twice (threading + unthreading).

### 📦 Space Complexity: `O(1)`

* No recursion or stack or queue — **true constant space** (tree is modified temporarily).

---

## 🧠 Summary Table:

| Approach         | Time Complexity | Space Complexity | Notes                                     |
| ---------------- | --------------- | ---------------- | ----------------------------------------- |
| DFS (Recursive)  | `O(N)`          | `O(H)`           | Clean, elegant, but uses call stack       |
| BFS (Queue)      | `O(N)`          | `O(W)`           | Good for breadth-first problems           |
| Morris Traversal | `O(N)`          | `O(1)`           | Most space-efficient; tricky to implement |

---

Would you like a **Java version** or **visual tree dry-run** for any of these?
