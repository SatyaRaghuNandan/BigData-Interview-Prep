
Excellent! Let's go over each of your **three approaches for Leetcode 314: Binary Tree Vertical Order Traversal** with:

* ✅ Telugu comments (inline and summary)
* ✅ Time and Space Complexity

---

## ✅ Approach 1: **BFS with Sorting**

### 💻 Code with Telugu Comments

```python
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        columnTable = defaultdict(list)  # Column-wise node values store cheyyadaniki
        queue = deque([(root, 0)])  # BFS ki queue lo (node, column) pairs veyyadam

        while queue:
            node, column = queue.popleft()  # Queue nunchi node and column extract cheyyadam

            if node is not None:
                columnTable[column].append(node.val)  # Column lo current node value add cheyyadam
                
                queue.append((node.left, column - 1))   # Left child ki column - 1
                queue.append((node.right, column + 1))  # Right child ki column + 1
                        
        # Column keys ni sort chesi, order lo result prepare cheyyadam
        return [columnTable[x] for x in sorted(columnTable.keys())]
```

### ⏱ Time Complexity:

* `O(N log K)` where:

  * `N` = total number of nodes
  * `K` = number of unique columns (for `sorted(columnTable.keys())`)
* Each node is processed once → `O(N)`
* Sorting column keys → `O(K log K)`

### 📦 Space Complexity:

* `O(N)` for `columnTable` and `queue` (at most N nodes stored)

---

## ✅ Approach 2: **BFS Without Sorting (Tracking min and max columns)**

### 💻 Code with Telugu Comments

```python
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0  # Column range track cheyyadam
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        # min_column nunchi max_column varaku result prepare cheyyadam
        return [columnTable[x] for x in range(min_column, max_column + 1)]
```

### ⏱ Time Complexity:

* `O(N)` → No sorting, just simple traversal and min/max tracking
* Each node processed once

### 📦 Space Complexity:

* `O(N)` → for `columnTable` and `queue`

📌 **Advantage**: No `sort()` on column keys = more efficient than Approach 1

---

## ✅ Approach 3: **DFS with Row Tracking + Sorting**

### 💻 Code with Telugu Comments

```python
from collections import defaultdict

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))  # Row tho patu append cheyyadam
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        ret = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x: x[0])  # Row order lo sort cheyyadam
            colVals = [val for row, val in columnTable[col]]
            ret.append(colVals)

        return ret
```

### ⏱ Time Complexity:

* `O(N log M)`

  * `N` = number of nodes
  * `M` = average number of nodes per column (due to sorting per column)

### 📦 Space Complexity:

* `O(N)` for storing columnTable + recursive call stack (max depth H)

📌 **Note**: Sorting by row needed to ensure top-to-bottom vertical order.

---

## 🧠 Telugu Comments Summary (All Approaches)

```text
- columnTable: Oka dictionary laaga column number to list of node values ni map cheyyadam
- queue = deque(): BFS ki node visit order maintain cheyyadam
- min_column, max_column: BFS lo column range ni track cheyyadam to avoid sorting
- DFS lo (row, column) ni track cheyyadam to sort vertically and top-down
- DFS lo recursion lo tree ni depth-first ga explore cheyyadam
```

---

## 🏁 Summary Table:

| Approach | Traversal | Sorting Needed | Time       | Space    | Notes                              |
| -------- | --------- | -------------- | ---------- | -------- | ---------------------------------- |
| BFS (1)  | Level     | ✅ (on keys)    | O(N log K) | O(N)     | Easy to implement, minor sort cost |
| BFS (2)  | Level     | ❌              | O(N)       | O(N)     | Most efficient, no sorting         |
| DFS (3)  | Depth     | ✅ (per column) | O(N log M) | O(N + H) | Required for precise row ordering  |

---

Let me know if you'd like this in **Java**, or want to visualize a sample tree run!
