✅ **BFS is preferred** in this problem because it explores all cells level by level, guaranteeing the **shortest path** is found first in an unweighted grid.
Unlike DFS, which can go deep into longer paths, BFS ensures that the **first time we reach the destination**, it's via the **minimum number of steps**.



---

### TL;DR Meta Answer:

> “I chose BFS because it guarantees the shortest path in an unweighted grid. It expands level by level, so the first time we reach the destination is with the minimum number of steps. DFS could reach the destination via a longer route and would need backtracking, making it less efficient for this problem.”

---

Let me know if you'd like to translate this into STAR format or add variations (e.g., DFS + pruning)!




You're working on **Leetcode 1091 – Shortest Path in Binary Matrix**, and your provided solution already uses **Breadth-First Search (BFS)** — which **is the best approach** for this problem in terms of **interview performance, correctness, and optimality**.

---

### ✅ Why **BFS** is Preferred Over DFS for This Problem

| BFS (Preferred)                                       | DFS (Not Ideal)                        |
| ----------------------------------------------------- | -------------------------------------- |
| Finds the **shortest path** first.                    | May explore long paths before short.   |
| Level-by-level traversal (minimum step count).        | Requires pruning to avoid deep paths.  |
| Guarantees optimal solution in **unweighted** graphs. | Not guaranteed to find shortest path.  |
| Memory-efficient for small/medium grids.              | Risk of StackOverflow for large grids. |

**This is an *unweighted shortest path problem in a grid*. Always use BFS for such cases.**

---

## ✅ Java BFS with Clean Comments & Structure

```java
class Solution {

    // 🔁 All 8 directions → Up, Down, Left, Right + Diagonals
    private static final int[][] DIRECTIONS = {
        {-1, -1}, {-1, 0}, {-1, 1},
        { 0, -1},          { 0, 1},
        { 1, -1}, { 1, 0}, { 1, 1}
    };

    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;

        // 🛑 Edge case: start or end blocked
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0)
            return -1;

        // ✅ BFS initialization
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});  // {row, col}
        grid[0][0] = 1; // Use grid to track distance (visited too)

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int row = cell[0], col = cell[1];
            int distance = grid[row][col];

            // 🎯 Reached destination
            if (row == n - 1 && col == n - 1)
                return distance;

            // 🔁 Explore all 8 directions
            for (int[] dir : DIRECTIONS) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];

                // 🔒 Boundary and visited check
                if (newRow < 0 || newCol < 0 || newRow >= n || newCol >= n)
                    continue;
                if (grid[newRow][newCol] != 0)
                    continue;

                // ✅ Valid cell
                queue.offer(new int[]{newRow, newCol});
                grid[newRow][newCol] = distance + 1;
            }
        }

        // ❌ Destination unreachable
        return -1;
    }
}
```

---

## ✅ Time and Space Complexity

| Metric        | Complexity | Explanation                                  |
| ------------- | ---------- | -------------------------------------------- |
| Time          | O(N²)      | Each cell is visited once in an N×N grid     |
| Space (Queue) | O(N²)      | In worst case, queue holds all cells         |
| Space (Grid)  | O(1)       | Grid is reused to track distance and visited |

---

## ✅ Test Cases with Clear Breakdown

### ✅ Test Case 1: Happy Path (Straight Diagonal)

```java
Input:
grid = [
  [0, 0, 0],
  [1, 1, 0],
  [1, 1, 0]
]
Output: 4

Explanation:
(0,0) → (0,1) → (0,2) → (1,2) → (2,2)
```

### ✅ Test Case 2: Blocked Start or End

```java
Input: grid = [
  [1, 0],
  [0, 0]
]
Output: -1

Reason: Start is blocked

Input: grid = [
  [0, 0],
  [0, 1]
]
Output: -1

Reason: End is blocked
```

### ✅ Test Case 3: No Path Exists

```java
Input: grid = [
  [0, 1],
  [1, 0]
]
Output: -1

Blocked completely from all directions
```

### ✅ Test Case 4: Single Cell Open

```java
Input: grid = [[0]]
Output: 1

Start == End
```

### ✅ Test Case 5: 5x5 Complex Grid

```java
Input: grid = [
  [0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 0, 1, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 1, 0]
]
Output: 9
```

---

## ✅ Summary (What to Say in Interview)

* Use **BFS** because you're solving a **shortest path** problem on an unweighted grid.
* Use the grid itself to store visited status and distance → avoids extra space.
* All **8 directions** are allowed, so diagonals must be considered.
* Handle edge cases early: start or end cell blocked.

Let me know if you want a **bidirectional BFS** version or want to compare with A\* search in advanced interviews.




Absolutely! Let's walk through this **Leetcode 1091: Shortest Path in Binary Matrix** solution **step-by-step**, with 3 example inputs and **line-by-line execution** including queue states and grid updates.

---

## ✅ Reminder: What the algorithm does

* Performs **Breadth-First Search (BFS)** starting from `(0,0)`
* Explores **8 directions** (diagonal + straight)
* **Marks visited cells** by writing distance directly into `grid[row][col]`
* Returns the **shortest distance** when reaching bottom-right corner `(n-1, n-1)`

---

# ✅ **Example 1**

```java
grid = [
  [0, 1],
  [1, 0]
]
```

### Step-by-step Execution:

**Initial checks:**

* `grid[0][0] == 0` and `grid[1][1] == 0` ✅ Proceed

**Initialize:**

* `queue = [(0, 0)]`
* `grid[0][0] = 1` // distance = 1

---

### 🔁 First Loop

* `cell = (0, 0)`, distance = 1
* Check all 8 directions:

| Direction | newRow, newCol | Status                     |
| --------- | -------------- | -------------------------- |
| `(-1,-1)` | (-1,-1)        | ❌ Out of bounds            |
| `(-1,1)`  | (-1,1)         | ❌ Out of bounds            |
| `(1,-1)`  | (1,-1)         | ❌ Out of bounds            |
| `(-1,0)`  | (-1,0)         | ❌ Out of bounds            |
| `(0,-1)`  | (0,-1)         | ❌ Out of bounds            |
| `(1,0)`   | (1,0)          | ❌ grid\[1]\[0] == 1 (wall) |
| `(0,1)`   | (0,1)          | ❌ grid\[0]\[1] == 1 (wall) |
| `(1,1)`   | (1,1)          | ✅ Add to queue, mark 2     |

➡️ `queue = [(1, 1)]`, `grid[1][1] = 2`

---

### 🔁 Second Loop

* `cell = (1, 1)`, distance = 2
* It's the target → ✅ return `2`

---

### ✅ Final Output: `2`

---

# ✅ **Example 2**

```java
grid = [
  [0, 0, 0],
  [1, 1, 0],
  [1, 1, 0]
]
```

---

### Initialization:

* `queue = [(0, 0)]`
* `grid[0][0] = 1`

---

### 🔁 Loop 1 (poll (0,0))

* distance = 1
* Valid neighbor: `(0,1)` and `(1,2)`
* Add `(0,1)` → `grid[0][1] = 2`
* Add `(1,2)` → `grid[1][2] = 2`

➡️ `queue = [(0,1), (1,2)]`

---

### 🔁 Loop 2 (poll (0,1))

* distance = 2
* Valid: `(0,2)`
* Add `(0,2)` → `grid[0][2] = 3`

➡️ `queue = [(1,2), (0,2)]`

---

### 🔁 Loop 3 (poll (1,2))

* distance = 2
* Valid: `(2,2)`
* Add `(2,2)` → `grid[2][2] = 3`

➡️ `queue = [(0,2), (2,2)]`

---

### 🔁 Loop 4 (poll (0,2)) → nothing new

---

### 🔁 Loop 5 (poll (2,2)) → 🎯 Target reached

✅ Return `3`

---

### ✅ Final Output: `3`

---

# ✅ **Example 3: No Path**

```java
grid = [
  [0, 1],
  [1, 1]
]
```

### Initialization:

* `queue = [(0, 0)]`
* `grid[0][0] = 1`

---

### 🔁 Loop 1 (poll (0,0))

* All 8 directions blocked or walls

➡️ `queue = []`

---

### Queue empty, target not reached → ❌ return `-1`

---

### ✅ Final Output: `-1`

---

## 🧠 Summary

| Grid                        | Output | Notes                     |
| --------------------------- | ------ | ------------------------- |
| `[[0,1],[1,0]]`             | `2`    | Direct diagonal path      |
| `[[0,0,0],[1,1,0],[1,1,0]]` | `3`    | One of the shortest paths |
| `[[0,1],[1,1]]`             | `-1`   | No path exists            |

---

Let me know if you'd like:

* Visual trace (grid snapshots)
* DFS version walk-through
* Variant: return path, not just distance

Happy to help!



