Here’s the **Java version** of your Python solution to **Leetcode 987 – Vertical Order Traversal of a Binary Tree**, with:

* ✅ Clear structure and class setup
* 💬 **Telugu-style comments**
* 📊 **Time & Space Complexity**
* 🧪 Easy to follow for interviews

---

## ✅ Java Code with Telugu Comments

```java
import java.util.*;

// TreeNode class definition
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

class Solution {

    // Main function to return vertical order traversal
    public List<List<Integer>> verticalTraversal(TreeNode root) {

        // Column-wise data ni store cheyyadaniki → col => list of (row, val)
        Map<Integer, List<int[]>> columnMap = new HashMap<>();

        // Queue for BFS traversal → (node, row, col)
        Queue<NodeInfo> queue = new LinkedList<>();

        // Min & Max columns track cheyyadam result build cheyyadaniki
        int minCol = 0, maxCol = 0;

        // BFS start cheyyadam
        queue.offer(new NodeInfo(root, 0, 0));

        while (!queue.isEmpty()) {
            NodeInfo current = queue.poll();
            TreeNode node = current.node;
            int row = current.row;
            int col = current.col;

            // Column ki list of (row, val) add cheyyadam
            columnMap
                .computeIfAbsent(col, k -> new ArrayList<>())
                .add(new int[]{row, node.val});

            // Min/max columns update cheyyadam
            minCol = Math.min(minCol, col);
            maxCol = Math.max(maxCol, col);

            // Left and right children BFS ki add cheyyadam
            if (node.left != null)
                queue.offer(new NodeInfo(node.left, row + 1, col - 1));

            if (node.right != null)
                queue.offer(new NodeInfo(node.right, row + 1, col + 1));
        }

        // Final result ni construct cheyyadam
        List<List<Integer>> result = new ArrayList<>();

        for (int col = minCol; col <= maxCol; col++) {
            List<int[]> colList = columnMap.get(col);

            // (row, val) sort cheyyadam → vertical + lexicographical order maintain cheyyadam
            Collections.sort(colList, (a, b) -> {
                if (a[0] != b[0]) return a[0] - b[0];  // row order
                return a[1] - b[1];                    // value order
            });

            List<Integer> sortedValues = new ArrayList<>();
            for (int[] pair : colList)
                sortedValues.add(pair[1]);

            result.add(sortedValues);
        }

        return result;
    }

    // ✅ Helper class to hold (node, row, col)
    static class NodeInfo {
        TreeNode node;
        int row, col;

        NodeInfo(TreeNode node, int row, int col) {
            this.node = node;
            this.row = row;
            this.col = col;
        }
    }
}
```

---

## ✅ Time and Space Complexity

| Metric              | Value        | Explanation                                                                              |
| ------------------- | ------------ | ---------------------------------------------------------------------------------------- |
| 🕒 Time Complexity  | `O(N log N)` | Each node processed once → `O(N)`, and each column's list sorted → `O(N log N)` in total |
| 🧠 Space Complexity | `O(N)`       | Queue for BFS, column map, and result list store all nodes                               |

---

## ✅ Example Dry Run

**Input:**

```text
       3
      / \
     9   20
         / \
        15  7
```

**Coordinates:**

* 3 → (0, 0)
* 9 → (1, -1)
* 20 → (1, 1)
* 15 → (2, 0)
* 7 → (2, 2)

**Grouped & Sorted:**

```java
col -1 → [9]
col  0 → [3, 15]    → (0,3), (2,15)
col  1 → [20]
col  2 → [7]
```

✅ **Output:** `[[9], [3, 15], [20], [7]]`

---

## ✅ Interview-Ready Summary

> "I treat the binary tree as a 2D grid and assign `(row, col)` coordinates to every node. Then I use a **BFS** traversal to group all `(val, row)` pairs by column. Once traversal is done, I **sort each column** by `(row, value)` to maintain vertical and lexicographical order. Finally, I collect the values column-wise from left to right."

---

Let me know if you'd like:

* DFS version for comparison
* Extension to Diagonal Traversals
* Visual tree with coordinates
* Conversion to `PriorityQueue` version
