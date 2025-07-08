You're exploring a new **variant of Leetcode 1091**:

> **"What if you had to return *a single valid path* (not necessarily the shortest) from top-left to bottom-right in a binary matrix?"**

This is now a **DFS-based solution** where:

* You're **guaranteed only one path**, not necessarily the shortest.
* You use **backtracking** to explore all valid directions until you find the end.

---

## ✅ How is this Variant Different from Previous Ones?

| Feature         | BFS (Shortest Path) Variant       | DFS (Any Path) Variant               |
| --------------- | --------------------------------- | ------------------------------------ |
| Goal            | Find shortest path                | Find any valid path                  |
| Search Strategy | Breadth-First Search (Queue)      | Depth-First Search (Recursion)       |
| Return Type     | Path (List of `[r, c]`)           | Path (List of `[r, c]`)              |
| Early Exit      | As soon as shortest path is found | As soon as *any valid* path is found |
| Grid usage      | Track distance or visited         | Track visited + backtrack (undo)     |
| Path tracking   | Copied at every level in BFS      | Backtracking via recursive stack     |
| Optimality      | ✅ Guaranteed shortest path        | ❌ Not guaranteed to be shortest      |

---

## ✅ Java Version of This Variant (DFS with Backtracking)

```java
import java.util.*;

public class AnyPathInBinaryMatrix {

    private static final int[][] DIRECTIONS = {
        {-1, 0}, {-1, 1}, {0, 1}, {1, 1},
        {1, 0}, {1, -1}, {0, -1}, {-1, -1}
    };

    public List<int[]> pathBinaryMatrix(int[][] grid) {
        int n = grid.length;

        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1)
            return new ArrayList<>();

        List<int[]> path = new ArrayList<>();
        dfs(grid, 0, 0, path);
        return path;
    }

    private boolean dfs(int[][] grid, int row, int col, List<int[]> path) {
        int n = grid.length;

        // ✅ Visit
        grid[row][col] = 1; // Telugu: Visited mark cheyyadam
        path.add(new int[]{row, col});

        // ✅ Base case
        if (row == n - 1 && col == n - 1) {
            return true;
        }

        // 🔁 Explore all 8 directions
        for (int[] dir : DIRECTIONS) {
            int newRow = row + dir[0];
            int newCol = col + dir[1];

            if (newRow < 0 || newCol < 0 || newRow >= n || newCol >= n)
                continue;

            if (grid[newRow][newCol] == 0) {
                if (dfs(grid, newRow, newCol, path))
                    return true;
            }
        }

        // 🔁 Backtrack
        path.remove(path.size() - 1);
        return false;
    }
}
```

---

## ✅ Example Input and Output

### Input:

```java
grid = [
 [0, 0, 1],
 [1, 0, 1],
 [1, 0, 0]
]
```

### One Valid Output Path:

```java
[
 [0, 0],
 [0, 1],
 [1, 1],
 [2, 1],
 [2, 2]
]
```

---

## ✅ Time and Space Complexity

| Metric | Value                     |
| ------ | ------------------------- |
| Time   | `O(8^N)` worst case (DFS) |
| Space  | `O(N)` for recursion path |

> Note: In practice, DFS returns quickly as soon as a path is found.

---

## ✅ When to Use This Variant

| Goal                           | Use This Variant?              |
| ------------------------------ | ------------------------------ |
| You need **a path**, any path  | ✅ Yes                          |
| You want the **shortest path** | ❌ Use BFS instead              |
| You're generating all paths    | ❌ Need full backtracking logic |

---

Would you like:

* 🧪 Variant that **returns all possible paths**?
* ✅ Conversion of this to **matrix of 1s/0s** representing path?
* 📤 String representation for serialization?

Happy to provide more!
