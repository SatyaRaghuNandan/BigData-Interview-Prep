Question 2:
Variation of https://leetcode.com/problems/shortest-distance-from-all-buildings/ (premium)
Given a NxN matrix of integers as follows:
1 - space (can dig)
2 - house (cannot dig)
3 - obstacle (cannot dig)
Dig a single well so that distance to each house from the well is minimal

https://leetcode.com/discuss/post/562431/facebook-phone-remove-nth-node-shortest-906lw/


https://leetcode.com/discuss/post/302416/facebook-phone-screen-shortest-distance-twbmq/

You’ve been tasked to help a village find the best place to install a new well. You’re given a 2D grid where cells can be empty, a house, or a tree. People can walk up, down, left and right, but they can’t walk through trees. Place the well that minimizes the total sum distance from all the houses.

=. =. =. =
= H T =
= H T =
= = H =


https://leetcode.com/discuss/post/302416/facebook-phone-screen-shortest-distance-twbmq/comments/2451601/



```python

What is the expected output for the given input? Can anyone let me know.
Related leetcode question: https://leetcode.com/problems/shortest-distance-from-all-buildings/
Tried to modify the code of https://algo.monster/liteproblems/317

from collections import deque
from typing import List

def shortestDistance(grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        total_buildings = 0

        EMPTY = '='
        BUILDING = 'H'
        OBSTACLE = 'T'

        # to keep track of total distances from each empty land to all buldings
        distance_sum = [[0] * COLS for _ in range(ROWS)]

        # to keep count of how many buildings each empty land can reach
        reach_count = [[0] * COLS for _ in range(ROWS)]

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            level_distance = 0
            visited = set()
            
            while queue:
                # Increase the distance level by 1 for each level of BFS
                level_distance += 1
                level_size = len(queue)
                      
                # Loop through each cell in the current BFS level
                for _ in range(level_size):
                    curr_row, curr_col = queue.popleft()
                    
                    for offset_x, offset_y in directions:
                        next_row = curr_row + offset_x
                        next_col = curr_col + offset_y
                        
                        # If the next cell is valid, not visited, and is an empty land
                        if (0 <= next_row < ROWS 
                        and 0 <= next_col < COLS 
                        and grid[next_row][next_col] == EMPTY
                        and (next_row, next_col) not in visited):
                            # Increment the building reach count and add the distance
                            reach_count[next_row][next_col] += 1
                            distance_sum[next_row][next_col] += level_distance
                                  
                            # Add the cell to the queue and mark it as visited
                            queue.append((next_row, next_col))
                            visited.add((next_row, next_col))
        
        for r in range(ROWS):
            for c in range(COLS):
                # If the cell is a building, do a BFS from this building to all other empty lands
                if grid[r][c] == BUILDING:
                    total_buildings += 1
                    bfs(r, c)
                
                
        answer = float('inf')
        for r in range(ROWS):
            for c in range(COLS):
                # find the minimum distance of an empty land that can reach all buildings
                if grid[r][c] == EMPTY and reach_count[r][c] == total_buildings:
                    answer = min(answer, distance_sum[r][c])                      
        
        # If no cell can reach all buildings, return -1; otherwise, return the minimum distance
        if answer == float('inf'):
            return -1
        else:
            return answer
grid = [
['=','=','=','='],
['=','H','T','='],
['=','=','H','=']
]
print(shortestDistance(grid))

>>>

2

>>>

```
