Great! Here's how you can **simulate and test the Robot Room Cleaner (Leetcode 489)** with a **mock `Robot` class** and a test room layout in Java.

---

## ✅ Mock Environment Setup (for Local Testing)

Since Leetcode gives you only the `Robot` API, we need to:

1. Create a mock room (2D grid).
2. Implement a fake `Robot` that obeys the API (`move()`, `turnLeft()`, `turnRight()`, `clean()`).
3. Run your `Solution.cleanRoom()` on the robot.

---

## ✅ Example Grid Representation

We use:

* `1` → free space
* `0` → obstacle/wall

```java
int[][] room = {
    {1, 1, 1, 1},
    {1, 0, 1, 0},
    {1, 1, 1, 1}
};
```

---

## ✅ Full Java Code with Mock Robot

```java
import java.util.*;

// Interface (like Leetcode's)
interface Robot {
    boolean move();
    void turnLeft();
    void turnRight();
    void clean();
}

// Mock implementation for local testing
class RobotImpl implements Robot {
    private int[][] room;
    private boolean[][] cleaned;
    private int x, y, dir;
    private int rows, cols;
    private static final int[][] DIRS = {
        {-1, 0}, {0, 1}, {1, 0}, {0, -1} // ↑ → ↓ ←
    };

    public RobotImpl(int[][] room, int startX, int startY) {
        this.room = room;
        this.cleaned = new boolean[room.length][room[0].length];
        this.x = startX;
        this.y = startY;
        this.dir = 0; // initially facing up
        this.rows = room.length;
        this.cols = room[0].length;
    }

    public boolean move() {
        int nx = x + DIRS[dir][0];
        int ny = y + DIRS[dir][1];
        if (nx >= 0 && ny >= 0 && nx < rows && ny < cols && room[nx][ny] == 1) {
            x = nx;
            y = ny;
            return true;
        }
        return false;
    }

    public void turnLeft() {
        dir = (dir + 3) % 4;
    }

    public void turnRight() {
        dir = (dir + 1) % 4;
    }

    public void clean() {
        cleaned[x][y] = true;
        System.out.println("Cleaned: (" + x + ", " + y + ")");
    }

    public boolean[][] getCleanedMap() {
        return cleaned;
    }
}
```

---

## ✅ Reuse the Main Solution Code

You can use the same `Solution` class from earlier:

```java
class Solution {
    int[][] directions = {
        {-1, 0}, {0, 1}, {1, 0}, {0, -1}  // ↑ → ↓ ←
    };

    Set<String> visited = new HashSet<>();

    public void cleanRoom(Robot robot) {
        backtrack(robot, 0, 0, 0);
    }

    private void backtrack(Robot robot, int row, int col, int dir) {
        robot.clean();
        visited.add(row + "," + col);

        for (int i = 0; i < 4; i++) {
            int newDir = (dir + i) % 4;
            int nextRow = row + directions[newDir][0];
            int nextCol = col + directions[newDir][1];

            if (!visited.contains(nextRow + "," + nextCol)) {
                if (robot.move()) {
                    backtrack(robot, nextRow, nextCol, newDir);
                    goBack(robot);
                }
            }

            robot.turnRight();
        }
    }

    private void goBack(Robot robot) {
        robot.turnLeft();
        robot.turnLeft();
        robot.move();
        robot.turnRight();
        robot.turnRight();
    }
}
```

---

## ✅ Driver Code

```java
public class Main {
    public static void main(String[] args) {
        int[][] room = {
            {1, 1, 1, 1},
            {1, 0, 1, 0},
            {1, 1, 1, 1}
        };

        // Start at (1, 2) which is an open cell
        RobotImpl robot = new RobotImpl(room, 1, 2);
        Solution cleaner = new Solution();
        cleaner.cleanRoom(robot);

        // Optionally print cleaned map
        boolean[][] cleaned = robot.getCleanedMap();
        System.out.println("\nCleaned Grid:");
        for (boolean[] row : cleaned) {
            for (boolean cell : row) {
                System.out.print(cell ? "C " : ". ");
            }
            System.out.println();
        }
    }
}
```

---

## ✅ Sample Output

```
Cleaned: (1, 2)
Cleaned: (0, 2)
Cleaned: (0, 3)
Cleaned: (0, 1)
...
Cleaned: (2, 0)

Cleaned Grid:
C C C C 
C . C . 
C C C C
```

---

## ✅ What You Can Do Now

* 🔁 Change starting positions to test different corners
* 🧱 Modify the grid to add more obstacles
* ✅ Track the robot’s path if needed (for animations or visual debug)

---

Would you like this as a **single downloadable Java file**? Or want to simulate it in a GUI?
