Great! You’re asking for the **iterative version** of the recursive solution to **Leetcode 236: Lowest Common Ancestor of a Binary Tree**, using an approach similar to:

```python
def lca(root, target):
    if not root or root in target:
        return root
    ...
```

---

## ✅ Goal:

Convert the **recursive postorder DFS** into an **explicit iterative postorder traversal**, and track both `p` and `q` during traversal to find the LCA.

---

## ✅ Final Iterative Code (Postorder Traversal with Stack):

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 🌲 Step 1: Stack to simulate recursion, and a map to record parent of each node
        stack = [root]
        parent = {root: None}

        # ⛳ Step 2: DFS until both p and q are found, record parents
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # 👣 Step 3: Build ancestor set for p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        # 🧬 Step 4: Traverse ancestors of q until we find first one in p's ancestor set
        while q not in ancestors:
            q = parent[q]

        return q
```

---

## 🧠 Intuition (Same as Recursive, but Iterative):

* Instead of recursively bubbling up the return values,
* We **build parent links** with DFS,
* Then **climb up from `p` and `q`** to find where they intersect (just like recursive LCA does via `if left and right`).

---

## 🔁 Dry Run Example:

Tree:

```
       3
      / \
     5   1
    / \  / \
   6  2 0  8
```

`p = 5`, `q = 1`

* Parent map:

  * 5 → 3
  * 1 → 3
* Ancestors of 5: `{5, 3}`
* Climb from 1: `1 → 3`, found in set → ✅ LCA is 3

---

## ✅ Time and Space Complexity

* **Time:** `O(n)` (full DFS in worst case)
* **Space:** `O(n)` for parent map + ancestor set

> Equivalent to recursive version in behavior and complexity — just explicitly manages the recursion stack.

---

Let me know if you'd like a **postorder true simulation** (using two stacks) that behaves closer to the recursion tree traversal.
