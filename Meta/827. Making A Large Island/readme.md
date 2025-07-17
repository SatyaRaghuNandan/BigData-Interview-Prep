
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

### ✅ Why DFS is preferred over BFS in this problem:

1. **DFS is easier to implement recursively** for labeling each island and computing its area, which is the main requirement here.
2. It allows **in-place traversal** with clean recursive logic to mark all connected 1's and calculate their size.
3. Since we don't need shortest path or level-wise processing, **BFS doesn't offer any specific advantage** in this case.
4. DFS naturally dives deep into each land path until it fully explores the island, which is exactly what we want.
5. BFS would require an explicit queue and additional code to handle neighbors layer by layer, which adds more boilerplate.
6. For dense islands or small-to-medium grid sizes (like in Leetcode), **DFS is fast, readable, and memory-efficient enough** without risk of stack overflow.

---

### ✅ Approach in 6 Sentences (Plain English):

1. First, go through the entire grid and use DFS to label each island with a unique ID starting from 2 (to avoid confusion with 0 and 1).
2. While labeling, calculate the size of each island and store it in a HashMap with the ID as the key.
3. Track the maximum size of any island found so far.
4. Next, iterate through every cell that contains 0 and **pretend to flip it to 1**.
5. For each 0-cell, check its 4 neighbors and **add the sizes of all uniquely connected islands** (using a Set to avoid duplicates).
6. Update the maximum if this flipped version creates a bigger island, and return the largest possible island size after checking all zeros.



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
