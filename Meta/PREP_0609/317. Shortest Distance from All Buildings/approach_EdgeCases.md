Here’s a complete and optimized solution to the problem **“Build House with Minimum Distance to All Buildings”**, using BFS from each building. I’ll provide:

1. ✅ Full Python code with detailed Telugu comments
2. ✅ Dry run example
3. ✅ Edge case analysis
4. ✅ Time and space complexity

---

## ✅ Step-by-Step Strategy (in English + Telugu)

### 🔍 Goal:

Build a house (`0`) that minimizes the sum of shortest distances to all buildings (`1`).
You can move in 4 directions (up, down, left, right), and must avoid obstacles (`2`).

### 💡 Key Idea:

* Do **multi-source BFS from each building**.
* For each `0` land cell, accumulate:

  * 🧮 `distance_sum[i][j]` → sum of distances from all buildings
  * 🏠 `reach_count[i][j]` → how many buildings can reach this land

Finally, return the minimum `distance_sum[i][j]` where `reach_count[i][j] == total_buildings`.

---

## ✅ Python Code with Telugu Comments

```python
from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        total_buildings = 0  # Telugu: total ga enni buildings unnayo count cheyyadam
        distance_sum = [[0] * n for _ in range(m)]  # Telugu: prathi 0 location ki total distance
        reach_count = [[0] * n for _ in range(m)]   # Telugu: prathi 0 location ni enni buildings reach chesayo

        # Telugu: Total buildings ni count cheyyadam
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_buildings += 1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # Telugu: Prathi building nundi BFS start cheddam
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited = [[False] * n for _ in range(m)]
                    queue = deque([(i, j, 0)])  # (row, col, distance)

                    while queue:
                        r, c, dist = queue.popleft()

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            # Telugu: bounds lo undali, visited kakudadhu, and empty land aundali
                            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                                visited[nr][nc] = True
                                distance_sum[nr][nc] += dist + 1
                                reach_count[nr][nc] += 1
                                queue.append((nr, nc, dist + 1))

        # Telugu: Final ga valid land cells ni check cheyyali
        min_distance = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach_count[i][j] == total_buildings:
                    min_distance = min(min_distance, distance_sum[i][j])

        return min_distance if min_distance != float('inf') else -1
```

---

## 🧪 Dry Run Example

```python
grid = [
  [1, 0, 2, 0, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0]
]
```

* Buildings at: `(0,0)`, `(0,4)`, `(2,2)`
* Start BFS from each and calculate cumulative distances
* Valid locations that all 3 buildings can reach will be in `distance_sum`
* Output: `7` (building house at (1,2))

---

## 🧱 Edge Cases

| Case              | Input                       | Output | Explanation                           |
| ----------------- | --------------------------- | ------ | ------------------------------------- |
| Empty grid        | `[]`                        | `-1`   | No cells to build                     |
| Only buildings    | `[[1,1],[1,1]]`             | `-1`   | No empty land                         |
| Obstacle blocks   | `[[1,2,0],[2,2,0],[0,0,0]]` | `-1`   | No path from building to any land     |
| Only one building | `[[1,0,0]]`                 | `1`    | Optimal spot is adjacent to building  |
| All zeros         | `[[0,0],[0,0]]`             | `-1`   | No buildings to compute distance from |

---

## 🧠 Time & Space Complexity

### ⏱ Time Complexity:

* Sorting not involved.
* For each building → BFS through empty cells → `O(m × n × total_buildings)`

### 💾 Space Complexity:

* `distance_sum`, `reach_count`, and `visited` → `O(m × n)`

---

Let me know if you want a visual BFS animation or a **Java version** with the same logic and Telugu comments.
