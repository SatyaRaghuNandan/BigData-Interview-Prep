Here's the Python version of all 3 approaches with detailed Telugu comments, along with time & space complexity analysis and recommendations for Meta interviews.

---

## ✅ Problem: Shortest Distance from All Buildings (Leetcode 317)

### Goal:

Given a grid with:

* `0`: empty land
* `1`: house
* `2`: obstacle
  Return the shortest total distance from any empty land to **all** houses. If not possible, return `-1`.

---

## ✅ Approach 1: BFS from Empty Land to All Houses (Brute-force)

```python
from collections import deque

class Solution:
    def bfs(self, grid, row, col, total_houses):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        vis = [[False] * cols for _ in range(rows)]
        q = deque([(row, col)])
        vis[row][col] = True

        distance_sum = 0
        houses_reached = 0
        steps = 0

        while q and houses_reached != total_houses:
            for _ in range(len(q)):
                r, c = q.popleft()

                if grid[r][c] == 1:
                    # Ee house ki distance add cheyyali
                    distance_sum += steps
                    houses_reached += 1
                    continue

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not vis[nr][nc] and grid[nr][nc] != 2:
                        vis[nr][nc] = True
                        q.append((nr, nc))
            steps += 1

        # Anni houses reach cheyyakapothe, visited empty cells ni block cheyyali
        if houses_reached != total_houses:
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 0 and vis[r][c]:
                        grid[r][c] = 2  # mark as visited & invalid
            return float('inf')

        return distance_sum

    def shortestDistance(self, grid):
        rows, cols = len(grid), len(grid[0])
        total_houses = sum(cell == 1 for row in grid for cell in row)
        min_dist = float('inf')

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    min_dist = min(min_dist, self.bfs(grid, r, c, total_houses))

        return -1 if min_dist == float('inf') else min_dist
```

🧠 **Time Complexity:**

* For each empty cell (`O(R*C)`), BFS to all houses takes `O(R*C)`
* Total: **O((RC)^2)**
  🧠 **Space Complexity:** `O(R*C)` for visited array

❌ Not preferred in interviews due to brute-force nature and mutation of `grid`.

---

## ✅ Approach 2: BFS from Houses to Empty Land (Using distances array)

```python
from collections import deque

class Solution:
    def bfs(self, grid, distances, row, col):
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        vis = [[False] * cols for _ in range(rows)]
        q = deque([(row, col)])
        vis[row][col] = True
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not vis[nr][nc] and grid[nr][nc] == 0:
                        vis[nr][nc] = True
                        distances[nr][nc][0] += steps
                        distances[nr][nc][1] += 1
                        q.append((nr, nc))

    def shortestDistance(self, grid):
        rows, cols = len(grid), len(grid[0])
        distances = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
        total_houses = sum(cell == 1 for row in grid for cell in row)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.bfs(grid, distances, r, c)

        min_dist = float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and distances[r][c][1] == total_houses:
                    min_dist = min(min_dist, distances[r][c][0])

        return -1 if min_dist == float('inf') else min_dist
```

🧠 **Time Complexity:**

* BFS from each house → `O(H * R * C)`
* Final scan → `O(R*C)`
* Total: **O(H \* R \* C)**
  🧠 **Space Complexity:** `O(R*C)` for `distances` and visited

✅ **Preferred in interviews (Meta-ready)** due to better scalability and clean logic.

---

## ✅ Approach 3: Optimized BFS from Houses, Reusing Grid State

```python
from collections import deque

class Solution:
    def shortestDistance(self, grid):
        rows, cols = len(grid), len(grid[0])
        total = [[0] * cols for _ in range(rows)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        empty_land_val = 0
        min_dist = float('inf')

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    visited_q = deque([(r, c)])
                    steps = 0

                    while visited_q:
                        steps += 1
                        for _ in range(len(visited_q)):
                            cr, cc = visited_q.popleft()

                            for dr, dc in dirs:
                                nr, nc = cr + dr, cc + dc
                                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == empty_land_val:
                                    grid[nr][nc] -= 1
                                    total[nr][nc] += steps
                                    visited_q.append((nr, nc))
                                    min_dist = min(min_dist, total[nr][nc])
                    empty_land_val -= 1

        return -1 if min_dist == float('inf') else min_dist
```

🧠 **Time Complexity:**

* Each empty land is visited once per house → `O(H * R * C)`
  🧠 **Space Complexity:** `O(R*C)` for total + queue

✅ Most optimal in practice (but less readable for interviews due to in-place mutation of grid)

---

## 📌 Summary Table

| Approach               | Time Complexity | Space Complexity | Mutates Grid | Meta Interview Suitability |
| ---------------------- | --------------- | ---------------- | ------------ | -------------------------- |
| 1. BFS from Empty Land | O((RC)^2)       | O(RC)            | ✅ Yes        | ❌ Too brute-force          |
| 2. BFS from Houses     | ✅ O(HRC)        | ✅ O(RC)          | ❌ No         | ✅ Highly preferred         |
| 3. Optimized BFS       | ✅ O(HRC)        | ✅ O(RC)          | ✅ Yes        | ⚠️ Advanced, less readable |

---

## 🔥 Recommendation for Meta

Use **Approach 2** in interviews:

* ✅ Clean code with clear reasoning
* ✅ Does not mutate input
* ✅ Easy to explain visited tracking and `distances` matrix
* 


Here are comprehensive **✅ test cases** for the **“Shortest Distance from All Buildings”** problem. Each test case is followed by:

* 🔍 Explanation
* 📤 Expected Output
* 💡 Why it's an edge case

---

## ✅ Test Case 1: Basic 3x3 Grid

```python
grid = [
    [1, 0, 2],
    [0, 0, 0],
    [0, 0, 1]
]
```

### 🔍 Explanation:

* 2 houses at `(0,0)` and `(2,2)`
* The cell `(1,1)` can reach both and has the **shortest total distance:**

  * Distance from `(0,0)` → 2
  * Distance from `(2,2)` → 2
  * Total = 4

### 📤 Output:

```python
4
```

---

## ✅ Test Case 2: Only One House

```python
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
```

### 🔍 Explanation:

* Only one house at `(1,1)`
* Any surrounding cell has distance = 1
* Best answer = 1

### 📤 Output:

```python
1
```

---

## ✅ Test Case 3: Blocked by Walls (No Path)

```python
grid = [
    [1, 2, 0],
    [2, 2, 2],
    [0, 2, 1]
]
```

### 🔍 Explanation:

* Houses at `(0,0)` and `(2,2)`
* All paths between houses are blocked by `2`s
* No empty land can reach both houses

### 📤 Output:

```python
-1
```

### 💡 Edge case:

Disconnected graph → must return `-1`

---

## ✅ Test Case 4: All Houses, No Empty Land

```python
grid = [
    [1, 1],
    [1, 1]
]
```

### 🔍 Explanation:

* No empty cell to consider
* Return `-1`

### 📤 Output:

```python
-1
```

---

## ✅ Test Case 5: All Obstacles

```python
grid = [
    [2, 2],
    [2, 2]
]
```

### 🔍 Explanation:

* No houses or empty land
* Return `-1`

### 📤 Output:

```python
-1
```

---

## ✅ Test Case 6: Large Empty Area, One House

```python
grid = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]
```

### 🔍 Explanation:

* One house at `(1,1)`
* Closest empty cell is adjacent → best answer = 1

### 📤 Output:

```python
1
```

---

## ✅ Test Case 7: Only One Empty Cell Between Two Houses

```python
grid = [
    [1, 0, 1]
]
```

### 🔍 Explanation:

* Two houses at `(0,0)` and `(0,2)`
* Middle cell `(0,1)`:

  * Distance from `(0,0)` → 1
  * Distance from `(0,2)` → 1
  * Total = 2

### 📤 Output:

```python
2
```

---

## ✅ Test Case 8: All Empty, No House

```python
grid = [
    [0, 0],
    [0, 0]
]
```

### 🔍 Explanation:

* No house to calculate distance to
* Return `-1`

### 📤 Output:

```python
-1
```

---

## ✅ Test Case 9: Only One Cell, House

```python
grid = [[1]]
```

### 🔍 Explanation:

* No empty land
* Return `-1`

### 📤 Output:

```python
-1
```

---

## ✅ Test Case 10: Zig-Zag Path Required

```python
grid = [
    [1, 2, 0],
    [0, 2, 0],
    [0, 0, 1]
]
```

### 🔍 Explanation:

* Need to go around the 2s to connect houses
* Best empty cell is `(1,2)`

  * Distance to `(0,0)` = 4
  * Distance to `(2,2)` = 1
  * Total = 5

### 📤 Output:

```python
5
```

---

## 🧪 Python Test Function (Optional for Unit Testing)

```python
def test_shortest_distance():
    sol = Solution()

    assert sol.shortestDistance([[1, 0, 2], [0, 0, 0], [0, 0, 1]]) == 4
    assert sol.shortestDistance([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 1
    assert sol.shortestDistance([[1, 2, 0], [2, 2, 2], [0, 2, 1]]) == -1
    assert sol.shortestDistance([[1, 1], [1, 1]]) == -1
    assert sol.shortestDistance([[2, 2], [2, 2]]) == -1
    assert sol.shortestDistance([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]) == 1
    assert sol.shortestDistance([[1, 0, 1]]) == 2
    assert sol.shortestDistance([[0, 0], [0, 0]]) == -1
    assert sol.shortestDistance([[1]]) == -1
    assert sol.shortestDistance([[1, 2, 0], [0, 2, 0], [0, 0, 1]]) == 5

    print("✅ All test cases passed!")
```

---

Let me know if you want:

* Graph visualization of BFS layers per house 🧭
* Extension with weights or diagonal movement 🧩
* Java versions of these test cases 🧪




Let me know if you'd like:

* Java version with Telugu comments
* Test cases for all 3 versions
* Visualization of BFS levels for better intuition
