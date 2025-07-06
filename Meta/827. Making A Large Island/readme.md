## 🏝️ LeetCode 827 – Making a Large Island (Java Version)

---

### ✅ Problem Summary
You're given an `n x n` grid of 0s and 1s. You can change at most **one 0 to a 1**. Return the **size of the largest island** possible after this transformation.

An island is made up of **connected 1s (4-directionally)**.

---

### ✅ Java Code (with Comments)

```java
import java.util.*;

public class Solution {
    private static final int[][] DIRECTIONS = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    public int largestIsland(int[][] grid) {
        int n = grid.length;
        int id = 2; // Start island ID from 2 to distinguish from 0 and 1
        Map<Integer, Integer> islandSizeMap = new HashMap<>();
        int max = 0;

        // Step 1: Label all islands with unique ID and store their sizes
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == 1) {
                    int size = dfsLabel(grid, row, col, id);
                    islandSizeMap.put(id, size);
                    max = Math.max(max, size);
                    id++;
                }
            }
        }

        // Step 2: Try flipping each 0 to 1
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == 0) {
                    Set<Integer> seen = new HashSet<>();
                    int potentialSize = 1; // The flipped cell itself

                    for (int[] dir : DIRECTIONS) {
                        int newRow = row + dir[0];
                        int newCol = col + dir[1];
                        if (newRow < 0 || newRow >= n || newCol < 0 || newCol >= n)
                            continue;

                        int neighborId = grid[newRow][newCol];
                        if (neighborId > 1 && seen.add(neighborId)) {
                            potentialSize += islandSizeMap.get(neighborId);
                        }
                    }
                    max = Math.max(max, potentialSize);
                }
            }
        }

        return max;
    }

    // DFS to label and count island
    private int dfsLabel(int[][] grid, int row, int col, int id) {
        int n = grid.length;
        if (row < 0 || row >= n || col < 0 || col >= n || grid[row][col] != 1)
            return 0;

        grid[row][col] = id;
        int size = 1;
        for (int[] dir : DIRECTIONS) {
            size += dfsLabel(grid, row + dir[0], col + dir[1], id);
        }
        return size;
    }
}
```

---

### ✅ Time and Space Complexity

| Step                            | Time Complexity | Space Complexity |
|--------------------------------|------------------|------------------|
| Labeling islands (DFS)         | `O(N^2)`         | `O(N^2)` (call stack + map) |
| Checking all zero-cells        | `O(N^2)`         | `O(1)` (constant neighbors) |
| **Total**                      | ✅ `O(N^2)`       | ✅ `O(N^2)`       |

---

### 🧠 Easy Way to Remember This Solution

1. **Step 1: Label each island** uniquely with DFS, store the size in a map.
   - Replace 1s with ID starting from 2
   - Build: `Map<id, size>`

2. **Step 2: Flip each 0 to 1**, and look around in 4 directions.
   - Track neighbor IDs in a `Set` to avoid double-counting
   - Add sizes of unique neighbor islands + 1 (flipped cell)

3. Track the **maximum size** across all flips.

✅ Tips:
- `id = 2` because grid uses 0 and 1
- Store island sizes to avoid recomputing
- Max 4 neighbors → constant-time flip evaluation

---

### ✅ Sample Test Case

```java
int[][] grid = {
    {1, 0},
    {0, 1}
};
Solution sol = new Solution();
System.out.println(sol.largestIsland(grid)); // Output: 3
```

---

Let me know if you want the BFS version or iterative DFS!
