You're exploring a **variant of Leetcode 1091 – Shortest Path in Binary Matrix**, where instead of returning just the **length of the shortest path**, you now need to **return the actual path**.

---

## ✅ Problem Comparison: Original vs Variant

| Feature             | Original Problem (Leetcode 1091)  | Variant (Return Path)                         |
| ------------------- | --------------------------------- | --------------------------------------------- |
| ✅ Return value      | Integer (length of shortest path) | List of cell coordinates (full path)          |
| ✅ BFS queue state   | `{row, col}`                      | `{row, col, path}` (track path so far)        |
| ✅ Distance tracking | Stored in grid itself             | Still possible, but grid used for **visited** |
| ✅ Path tracking     | ❌ Not required                    | ✅ Required (must carry a copy of path so far) |
| ✅ Grid mutation     | Grid stores distance values       | Grid used only for visited (mark `1`)         |

---

## ✅ Java Implementation for the Variant: Return Actual Path

```java
import java.util.*;

public class ShortestPathWithTrace {

    private static final int[][] DIRECTIONS = {
        {-1, 0}, {-1, 1}, {0, 1}, {1, 1},
        {1, 0}, {1, -1}, {0, -1}, {-1, -1}
    };

    public List<int[]> shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;

        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) return new ArrayList<>();

        Queue<Cell> queue = new LinkedList<>();
        List<int[]> startPath = new ArrayList<>();
        startPath.add(new int[]{0, 0});
        queue.offer(new Cell(0, 0, startPath));
        grid[0][0] = 1; // Mark visited

        while (!queue.isEmpty()) {
            Cell curr = queue.poll();
            int row = curr.row, col = curr.col;
            List<int[]> pathSoFar = curr.path;

            // ✅ Goal reached
            if (row == n - 1 && col == n - 1) {
                return pathSoFar;
            }

            for (int[] dir : DIRECTIONS) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];

                if (newRow < 0 || newCol < 0 || newRow >= n || newCol >= n)
                    continue;
                if (grid[newRow][newCol] != 0)
                    continue;

                grid[newRow][newCol] = 1; // Mark visited
                List<int[]> newPath = new ArrayList<>(pathSoFar);
                newPath.add(new int[]{newRow, newCol});
                queue.offer(new Cell(newRow, newCol, newPath));
            }
        }

        return new ArrayList<>(); // ❌ No path found
    }

    static class Cell {
        int row, col;
        List<int[]> path;

        Cell(int row, int col, List<int[]> path) {
            this.row = row;
            this.col = col;
            this.path = path;
        }
    }
}
```

---

## ✅ Example Output

**Input:**

```java
grid = [
  [0, 0, 0],
  [1, 1, 0],
  [1, 1, 0]
], k = 1
```

**Output Path:**

```
[
 [0, 0],
 [0, 1],
 [0, 2],
 [1, 2],
 [2, 2]
]
```

---

## ✅ Time and Space Complexity

| Operation | Complexity                    |
| --------- | ----------------------------- |
| Time      | O(N²) in worst-case           |
| Space     | O(N²) – queue and path copies |

---

## 🧠 Key Differences from Original Problem

| Feature        | Original           | Variant                            |
| -------------- | ------------------ | ---------------------------------- |
| Grid as memory | Stores distance    | Used as visited flag (1 = visited) |
| Path tracking  | Not required       | ✅ You must carry path in queue     |
| Queue type     | `int[] {row, col}` | Custom `Cell` with full path       |

---

## ✅ Memory Optimizations (if needed)

* Instead of copying the full path, store **previous cell reference** (backtracking)
* Or use a `Map<Point, Parent>` if post-trace reconstruction is acceptable

---

Would you like:

* 🧪 Dry run visualized?
* 📦 Version that returns all shortest paths?
* 🌐 DFS variant to return one *any* valid path (not necessarily shortest)?

Let me know!


