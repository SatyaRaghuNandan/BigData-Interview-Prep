from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Initialize graph and indegree
        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        # Step 2: Build graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""  # Invalid prefix case
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        # Step 3: BFS Topological Sort (Kahn's Algorithm)
        queue = deque([c for c in indegree if indegree[c] == 0])
        result = []

        while queue:
            c = queue.popleft()
            result.append(c)
            for neighbor in graph[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If result doesn't include all letters, graph has a cycle
        if len(result) != len(indegree):
            return ""

        return ''.join(result)


Here are the solutions to the 5 "Lowest Common Ancestor" problems from LeetCode, written in Python with variable names and comments explained in **Telugu (typed in English)**:

---

### ✅ LC 236: Lowest Common Ancestor of a Binary Tree

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Base condition: root lekapote or root == p/q unte direct return
        if not root or root == p or root == q:
            return root
        
        # Left and right subtree lo check cheyyadam
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Left and right rendu valid ayite root e LCA
        if left and right:
            return root
        
        # Only one side valid ayite adi return cheyyadam
        return left or right
```

---

### ✅ LC 235: LCA of a Binary Search Tree (BST ni use chesi optimize cheyyadam)

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # BST kabatti left/right logic use cheyyachu
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
```

---

### ✅ LC 1644: LCA of Binary Tree II (p or q lekapovachu — so validation needed)

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if not node:
                return None, False, False
            left, lp, lq = dfs(node.left)
            right, rp, rq = dfs(node.right)

            found_p = lp or rp or node == p
            found_q = lq or rq or node == q

            if node == p or node == q:
                return node, found_p, found_q
            if left and right:
                return node, found_p, found_q
            return (left or right), found_p, found_q
        
        lca, has_p, has_q = dfs(root)
        return lca if has_p and has_q else None
```

---

### ✅ LC 1650: LCA of Binary Tree III (parent pointer untundi)

```python
class Solution:
    def lowestCommonAncestor(self, p, q):
        visited = set()
        # p ni root daka trace cheyyadam
        while p:
            visited.add(p)
            p = p.parent
        # q track cheyyadam p daggara match ayithe adi LCA
        while q:
            if q in visited:
                return q
            q = q.parent
```

---

### ✅ LC 1676: LCA of Binary Tree IV (multiple nodes, not just 2)

```python
class Solution:
    def lowestCommonAncestor(self, root, nodes):
        node_set = set(nodes)

        def dfs(node):
            if not node:
                return None
            if node in node_set:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            return left or right

        return dfs(root)
```

---

## 🔍 Differences Between These LCA Variants

| LeetCode # | Problem Focus            | Input Constraint                | What’s Special                          | How is it Different?                  |
| ---------- | ------------------------ | ------------------------------- | --------------------------------------- | ------------------------------------- |
| **236**    | Binary Tree              | p and q **always exist**        | Normal LCA using recursion              | Base case, post-order recursion       |
| **235**    | BST                      | Binary Search Tree + p, q exist | Can use BST properties to go left/right | Optimized with `while` loop           |
| **1644**   | Binary Tree              | p or q might be **missing**     | Must validate both p and q found        | Needs boolean flags during recursion  |
| **1650**   | Tree with Parent Pointer | Only nodes `p` and `q` given    | Walk up the tree with `.parent`         | Similar to finding cycle intersection |
| **1676**   | Binary Tree              | List of `n` nodes               | Must find LCA of **multiple** nodes     | Use set lookup in DFS                 |

---

Let me know if you’d like:

* 🧪 Custom test cases
* 🧠 Behavioral story for any one of these implementations
* ✅ Java versions of the same

This is a very Meta-style favorite pattern, especially when combined with **follow-ups like Tree reconstruction or serialization**.
