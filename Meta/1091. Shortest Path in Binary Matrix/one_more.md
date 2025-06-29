Introduction

Maze/grid traversal problems are incredibly common in technical interviews, and LC 1091: Shortest Path in Binary Matrix is a perfect entry point. It is one of the most frequently asked problems in Meta coding interview. It involves finding the distance of the shortest path from the top-left to the bottom-right corner in a binary grid using 8-directional movement.

Once you solve the base version with Breadth-First Search (BFS), there are five natural and interview-friendly follow-ups:
I, Return one shortest path
II, Return the number of shortest paths
III, Return all shortest paths
IV, Return all valid paths
V, Return the number of valid paths (LC 63: Unique Paths II)

This post walks through each variant with working Python code and a short explanation.
Original Problem: Shortest Path in Binary Matrix

Task: Find the length of the shortest 8-directional path from the top-left cell to the bottom-right cell in a binary matrix where:

    0 = walkable cell
    1 = obstacle
    If no such path exits, return -1

Solution: BFS with Distance Mapping

This is a shortest path problem on an unweighted grid. In unweighted graphs, BFS guarantees the shortest path because it explores all nodes at distance k before moving to distance k+1. DFS doesn't guarantee shortest path unless you explore all possible paths, which is less efficient. Dijkstra’s algorithm is overkill here since all edges have equal weight (i.e., 1 step per move).

A distance_map is used to track the shortest distance from (0, 0) to any cell and mark the visited. We start from (0, 0) with an initial distance of 1. BFS queue initialized with the starting cell and explores all reachable nodes level-by-level. For each neighbor, if it's within bounds, not blocked, and not visited yet, we mark its distance and add it to the queue for future exploration. The first time we reach the bottom-right cell, we return the current distance.

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        m, n = len(grid), len(grid[0])
        distance_map = [[-1] * n for _ in range(m)]
        distance_map[0][0] = 1
        queue = deque([(0, 0)])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        while queue:
            x, y = queue.popleft()

            if (x, y) == (m - 1, n - 1):
                return distance_map[x][y]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m) or not (0 <= ny < n):
                    continue
                if grid[nx][ny] == 1 or distance_map[nx][ny] != -1:
                    continue
                distance_map[nx][ny] = distance_map[x][y] + 1
                queue.append((nx, ny))

        return -1

# Time Complexity: O(mn)
# Space Complexity: O(mn)

Follow-up I: Return One Shortest Path

Task: Given a binary matrix grid, return one shortest path (as a list of coordinates) from the top-left to the bottom-right cell. Movement is allowed in 8 directions, and only on cells with value 0.
Solution: BFS with Parent Mapping

A parent_map is used to track how we reached each cell and mark the visited. We start from (0, 0) with a parent to be None. We use BFS for traversal and use parent_map to build the final path. For each neighbor, if it's within bounds, not blocked, and not visited yet, we mark its parent and add it to the queue for future exploration. The first time we reach the bottom-right cell, we reconstruct the path by backtracking using parent_map from the bottom-right to the top-left cell and return the reversed path.

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> List[Tuple[int, int]]:
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
            return []

        m, n = len(grid), len(grid[0])
        queue = collections.deque([(0, 0)])
        parent_map = {(0, 0): None}  # maps each node to its parent
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        while queue:
            x, y = queue.popleft()

            if (x, y) == (m - 1, n - 1):
                # reconstruct path from destination to source
                path = []
                curr = (m - 1, n - 1)
                while curr is not None:
                    path.append(curr)
                    curr = parent_map[curr]
                return path[::-1]  # reverse the path

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m) or not (0 <= ny < n):
                    continue
                if grid[nx][ny] == 1 or (nx, ny) in parent_map:
                    continue

                parent_map[(nx, ny)] = (x, y)
                queue.append((nx, ny))

        return []  # no valid path

# Time Complexity: O(mn)
# Space Complexity: O(mn)

Follow-up II: Return the Number of Shortest Paths

Task: Given a binary matrix grid, return the count of all the shortest paths from the top-left to the bottom-right cell. Movement is allowed in 8 directions, and only on cells with value 0.
Solution: BFS with Distance and Count Mapping

We’ll use BFS to:

    Track the shortest distance to each cell (distance_map)
    Track the number of shortest paths to reach each cell (count_map)

When we visit a cell for the first time, we record the distance and initialize its path count. If we reach it again with the same shortest distance, we add the new path count to the existing one.

from collections import deque
class Solution:
    def countShortestPaths(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        m, n = len(grid), len(grid[0])

        distance_map = [[-1] * n for _ in range(m)]
        distance_map[0][0] = 1
        count_map = [[0] * n for _ in range(m)]
        count_map[0][0] = 1
        queue = deque([(0, 0)])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                    if distance_map[nx][ny] == -1:
                        distance_map[nx][ny] = distance_map[x][y] + 1
                        count_map[nx][ny] = count_map[x][y]
                        queue.append((nx, ny))
                    elif distance_map[nx][ny] == distance_map[x][y] + 1:
                        count_map[nx][ny] += count_map[x][y]

        
        if distance_map[m-1][n-1] == -1:
            return 0
        return count_map[m-1][n-1]

# Time Complexity: O(mn)
# Space Complexity: O(mn)

Follow-up III: Return All Shortest Paths

Task: Given a binary matrix grid, return all the shortest paths (each path as a list of coordinates) from the top-left to the bottom-right cell. Movement is allowed in 8 directions, and only on cells with value 0.
Solution: BFS and Backtracking

Step 1 BFS:

    Use to find the shortest distance to every cell.
    Build a parent_map to track all previous cells that can lead to a given cell via the shortest path.

Step 2 Backtracking (DFS-style):

    Reconstruct all shortest paths from the destination back to the start using the parent_map.

from collections import deque, defaultdict
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> List[List[Tuple[int, int]]]:
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
            return []
        
        m, n = len(grid), len(grid[0])
        distance_map = [[-1] * n for _ in range(m)]
        distance_map[0][0] = 1
        parent_map = defaultdict(list) # map cell to list of parent cells
        queue = deque([(0, 0)])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        # BFS to find shortest paths
        while queue:
            x, y = queue.popleft()
            
            if (x, y) == (m - 1, n - 1):
                break  # We'll reconstruct paths after BFS completes
                
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                    if distance_map[nx][ny] == -1:  # Not visited yet
                        distance_map[nx][ny] = distance_map[x][y] + 1
                        parent_map[(nx, ny)].append((x, y))
                        queue.append((nx, ny))
                    elif distance_map[nx][ny] == distance_map[x][y] + 1:
                        # Found another shortest path to (nx, ny)
                        parent_map[(nx, ny)].append((x, y))
        
        # Reconstruct all shortest paths
        def backtrack(node):
            if node == (0, 0):
                return [[(0, 0)]]
            paths = []
            for pred in parent_map[node]:
                for path in backtrack(pred):
                    paths.append(path + [node])
            return paths
        
        if distance_map[m-1][n-1] > 0:
            return backtrack((m - 1, n - 1))
        return []

# Time Complexity: O(mn + 2^{m+n} × (m+n))
# Space Complexity: O(mn + 2^{m+n} × (m+n))

Follow-up VI: Return All Valid Paths

Task: Given a binary matrix grid, return all the valid paths (each path as a list of coordinates, not necessarily the shortest) from the top-left to the bottom-right cell. Each cell can be visited at most once. Movement is allowed in 8 directions, and only on cells with value 0.
Solution: DFS with Backtracking

Use DFS with backtracking to find all possible paths from the top-left corner (0, 0) to the bottom-right corner (m-1, n-1).
⚠️ This is acceptable only for small grids, since number of paths grows exponentially.

class Solution:
    def validPathBinaryMatrix(self, grid: List[List[int]]) -> List[List[Tuple[int, int]]]:
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
            return []

        res = []
        visited = set([(0, 0)])
        path = [(0, 0)]
        self.dfs(grid, 0, 0, path, visited, res)
        return res

    def dfs(self, grid, x, y, path, visited, res):
        if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
            res.append(path[:])
            return

        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < len(grid)) or not (0 <= ny < len(grid[0])):
                continue
            if (nx, ny) in visited or grid[nx][ny] == 1:
                continue

            visited.add((nx, ny))
            path.append((nx, ny))
            self.dfs(grid, nx, ny, path, visited, res)
            path.pop()
            visited.remove((nx, ny))

# Time Complexity: O(8^{m+n})
# Space Complexity: O(mn + 8^{m+n} × (m+n))           

Follow-up V: Return the Number of Valid Paths (Unique Paths II)

Task: Given an m x n grid with obstacles (1 = blocked, 0 = traversable), find the number of unique paths from the top-left cell to the bottom-right cell. Movement is restricted to right or down only.
Solution: DFS with Memoization / Dynamic Programming

DFS with Memoization (Top-down):

    Uses DFS with memoization (explicitly defined memo table) to avoid redundant calculations.
    Recursive DFS explores paths while storing computed results in memo.

Dynamic Programming (Bottom-up):

    Uses dynamic programming (DP) with space optimization (reduces space to O(n)).
    Iterative bottom-up approach fills a 1D DP array.

class Solution:
    # ===== Solution 1: Original Memoization (Top-Down DFS) =====
    # Time: O(mn), Space: O(mn)
    def uniquePathsWithObstacles_memo(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[-1] * n for _ in range(m)]

        def dfs(x, y):
            if x >= m or y >= n or obstacleGrid[x][y] == 1:
                return 0
            if x == m - 1 and y == n - 1:
                return 1
            if memo[x][y] != -1:
                return memo[x][y]
            memo[x][y] = dfs(x + 1, y) + dfs(x, y + 1)
            return memo[x][y]

        return dfs(0, 0)


    # ===== Solution 2: Bottom-Up DP (Space Optimized) =====
    # Time: O(mn), Space: O(n)
    def uniquePathsWithObstacles_dp(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1  # Starting point

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # Blocked
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[-1]       

Conclusion

Navigating grid-based problems is a journey—one that begins with finding the shortest path but extends far beyond. LC 1091 (Shortest Path in Binary Matrix) serves as the perfect launchpad, introducing BFS for guaranteed shortest paths in unweighted grids. But the odyssey doesn’t end there. Each follow-up reveals deeper layers of algorithmic thinking:

BFS + Parent Tracking retrieves one shortest path.

BFS + Count Tracking calculates the number of shortest paths.

BFS + Backtracking reconstructs all shortest paths.

DFS + Backtracking explores all possible paths (feasible only for small grids).

DFS with memo or DP efficiently counts paths in restricted movement scenarios.

Mastering these techniques ensures you can tackle grid-based problems with confidence, whether optimizing for speed, memory, or path reconstruction. Happy coding, and may your pathfinding always be optimal!

If you found this helpful, a quick upvote would be much appreciated! 🙌
