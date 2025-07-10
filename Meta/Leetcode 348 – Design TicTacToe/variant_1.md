


Great! You're now tackling a **variant of Leetcode 348**:

---

## ✅ Variant:

**"What if you were given an existing board and had to figure out if one move led to a win?"**

---

## 🔍 Key Difference from Original Problem

| Feature | Original Problem                              | Variant                                                         |
| ------- | --------------------------------------------- | --------------------------------------------------------------- |
| Input   | `move(row, col, player)`                      | A full or partial **existing board**, with a **move just made** |
| State   | You maintain row/col/diag counters internally | You inspect the **current board state** from scratch            |
| Goal    | Efficient winner check per move               | **One-time check** if given move results in a win               |

---

## ✅ When is this Variant Useful?

* Checking win condition **after** loading a saved board from file/database
* Validating a move in **offline games / undo operations**
* Replay or Simulation Analysis

---

## ✅ Java Code for the Variant

With clear Telugu-style comments and explanation

```java
public class TicTacToeWinChecker {

    // Idi existing board, latest move info (row, col, player) istundi
    // Return cheyyali → aa move win ayindha leda
    public static boolean isWinningMove(int[][] board, int player, int row, int col) {
        int n = board.length;

        // Step 1: Assume this move was made
        board[row][col] = player;

        int rowCount = 0;
        int colCount = 0;
        int diagCount = 0;
        int antiDiagCount = 0;

        // Step 2: Row, Column, Diagonal ni scan cheyyadam
        for (int i = 0; i < n; i++) {
            if (board[row][i] == player) rowCount++;          // Same row lo player ni count cheyyadam
            if (board[i][col] == player) colCount++;          // Same column lo player count
            if (board[i][i] == player) diagCount++;           // Main diagonal
            if (board[i][n - 1 - i] == player) antiDiagCount++; // Anti-diagonal
        }

        // Step 3: Win condition check
        return rowCount == n || colCount == n || diagCount == n || antiDiagCount == n;
    }
}
```

---

## ✅ Time & Space Complexity

| Operation              | Complexity |
| ---------------------- | ---------- |
| Win check              | O(n)       |
| Space (in-place board) | O(1)       |

---

## ✅ Test Cases

```java
public class TicTacToeWinCheckerTest {
    public static void main(String[] args) {
        int[][] board1 = {
            {1, 2, 0},
            {1, 2, 0},
            {0, 0, 0}
        };

        // Place 1 at (2, 0) → full column 0 is 1s → win
        boolean result1 = TicTacToeWinChecker.isWinningMove(board1, 1, 2, 0);
        System.out.println("Test 1 (Win Expected): " + result1); // true

        int[][] board2 = {
            {2, 1, 1},
            {2, 1, 0},
            {0, 0, 0}
        };

        // Place 1 at (2, 1) → doesn't complete row/col/diagonal
        boolean result2 = TicTacToeWinChecker.isWinningMove(board2, 1, 2, 1);
        System.out.println("Test 2 (No Win): " + result2); // false

        int[][] board3 = {
            {1, 0, 0},
            {0, 1, 2},
            {0, 2, 0}
        };

        // Place 1 at (2, 2) → completes main diagonal
        boolean result3 = TicTacToeWinChecker.isWinningMove(board3, 1, 2, 2);
        System.out.println("Test 3 (Diagonal Win): " + result3); // true
    }
}
```

---

## ✅ Summary

| Problem                   | Approach                  | Time | Space | Use Case                           |
| ------------------------- | ------------------------- | ---- | ----- | ---------------------------------- |
| **Original Leetcode 348** | Count Tracking (`move()`) | O(1) | O(n)  | Repeated moves in-game             |
| **This Variant**          | Board Scan                | O(n) | O(1)  | One-time check from external board |

---

Let me know if you want:

* ✅ Tie/Draw detection logic
* ✅ Undo/Redo move simulation
* ✅ Extension to 4x4 or 5x5 board

Would you like a **generalized method to check any player’s win** from the board (not just last move)?
