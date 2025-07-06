import java.util.*;

class DisjointSet {
    int[] parent;
    int[] islandSize;

    public DisjointSet(int n) {
        parent = new int[n];
        islandSize = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            islandSize[i] = 1;
        }
    }

    public int findRoot(int node) {
        if (parent[node] != node) {
            parent[node] = findRoot(parent[node]);
        }
        return parent[node];
    }

    public void union(int a, int b) {
        int rootA = findRoot(a);
        int rootB = findRoot(b);
        if (rootA == rootB) return;

        if (islandSize[rootA] < islandSize[rootB]) {
            parent[rootA] = rootB;
            islandSize[rootB] += islandSize[rootA];
        } else {
            parent[rootB] = rootA;
            islandSize[rootA] += islandSize[rootB];
        }
    }
}

public class DSUSolution {
    private static final int[][] DIRECTIONS = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    public int largestIsland(int[][] grid) {
        int n = grid.length;
        DisjointSet dsu = new DisjointSet(n * n);

        // Step 1: Union all adjacent 1s
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == 1) {
                    int curr = row * n + col;
                    for (int[] dir : DIRECTIONS) {
                        int newRow = row + dir[0];
                        int newCol = col + dir[1];
                        if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < n && grid[newRow][newCol] == 1) {
                            int neighbor = newRow * n + newCol;
                            dsu.union(curr, neighbor);
                        }
                    }
                }
            }
        }

        int maxSize = 0;
        boolean hasZero = false;

        // Step 2: Try flipping each 0
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == 0) {
                    hasZero = true;
                    Set<Integer> seen = new HashSet<>();
                    int size = 1;
                    for (int[] dir : DIRECTIONS) {
                        int newRow = row + dir[0];
                        int newCol = col + dir[1];
                        if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < n && grid[newRow][newCol] == 1) {
                            int neighbor = newRow * n + newCol;
                            int root = dsu.findRoot(neighbor);
                            if (seen.add(root)) {
                                size += dsu.islandSize[root];
                            }
                        }
                    }
                    maxSize = Math.max(maxSize, size);
                }
            }
        }

        // Step 3: If no zero found, return full grid size
        if (!hasZero) {
            return n * n;
        }
        return maxSize;
    }

    public static void main(String[] args) {
        DSUSolution sol = new DSUSolution();

        int[][] grid1 = {
            {1, 0},
            {0, 1}
        };
        System.out.println(sol.largestIsland(grid1)); // Output: 3

        int[][] grid2 = {
            {1, 1},
            {1, 0}
        };
        System.out.println(sol.largestIsland(grid2)); // Output: 4

        int[][] grid3 = {
            {1, 1},
            {1, 1}
        };
        System.out.println(sol.largestIsland(grid3)); // Output: 4
    }
}
