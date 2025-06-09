Absolutely! Below is your code for **Copy Random Binary Tree** with **detailed Telugu comments (transliterated in English)** to help you understand each step clearly.

---

### ✅ Problem Goal:

`Node` ane binary tree lo prathi node ki `val`, `left`, `right`, and `random` pointers untayi.

Manam cheyyalsina pani:

* Oka **new tree create cheyyali**, where:

  * Structure (`left`, `right`) same undali.
  * Random pointers kuda original tree lo unna structure ni **mirror** cheyyali.
  * **Original tree lo references undakudadhu** (deep copy).

---

### ✅ Python Code with Telugu Comments:

```python
from typing import Optional

# Original Tree Node class
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

# Copied Tree Node class
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: "Optional[Node]") -> "Optional[NodeCopy]":
        visited = {}  # Original node → Copied node mapping store cheyyadam kosam dictionary

        # Recursive function for DFS-based deep copy
        def dfs(root) -> "Optional[NodeCopy]":
            if root is None:
                return None  # Base case: empty node unte direct ga None return cheyyali

            if root in visited:
                return visited[root]  
                # Idi important:
                # Already copy chesina node unte, repeated ga malli copy cheyyakudadhu
                # cycles or multiple randoms pointing to same node ni handle cheyyadaniki

            # Step 1: current node ki copy create cheyyadam
            copy = NodeCopy(root.val)

            # Step 2: visited lo original → copy map cheyyadam
            visited[root] = copy

            # Step 3: Recursive calls for left, right, random children
            copy.left = dfs(root.left)        # Left subtree ni copy cheyyadam
            copy.right = dfs(root.right)      # Right subtree ni copy cheyyadam
            copy.random = dfs(root.random)    # Random pointer ki corresponding copy ni link cheyyadam

            return copy  # Final ga copy return cheyyadam

        return dfs(root)  # Main root node nunchi DFS start cheyyadam
```

---

### 🧠 Deep Copy Explanation (Telugu):

```text
- Manaki original tree lo prathi node ki copy kavali.
- copy tree lo `left`, `right`, and `random` pointers kuda original tree ni simulate cheyyali.
- Oka node already copy ayite, aa node ki malli copy cheyyakudadhu → visited map lo check cheyyali.
- Recursive ga DFS valla prathi node process ayipotundi.
```

---

### ✅ Time and Space Complexity:

| Metric    | Value  |
| --------- | ------ |
| **Time**  | `O(n)` |
| **Space** | `O(n)` |

* `n` = number of nodes in the tree.
* `visited` map uses O(n).
* Recursion stack also uses up to `O(n)` in worst-case (skewed tree).

---

### 🌳 Example:

Imagine this structure:

```
        1
       / \
      2   3
         /
        4

Random Pointers:
1.random → 3
2.random → 1
4.random → 2
```

After copying, the new tree should **look identical** and `random` pointers should point to **copied nodes**, not original ones.

---

Let me know if you want:

* A **visual diagram** for this logic.
* A test case with print/debug steps.
* An **iterative version** or **two-pass alternative** solution.
