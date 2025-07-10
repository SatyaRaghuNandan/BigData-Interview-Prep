
Absolutely! Let's now convert the entire solution of **Leetcode 348 – Design TicTacToe** into Java — along with:

* ✅ Telugu-style comments
* ✅ Best approach explanation
* ✅ Dry Run
* ✅ Test cases
* ✅ Time & Space complexity

---

## ✅ Problem: Leetcode 348 – Design TicTacToe

Design a TicTacToe game that can:

* Initialize a board of size `n x n`
* Allow player 1 or 2 to make a move at position `(row, col)`
* Return the winner (1 or 2) **immediately after a move**, or 0 if no winner yet

---

## ✅ Approaches

### 🔴 Approach 1: Brute Force Grid Check (❌ Not Optimal)

* Use a `n x n` grid to track moves.
* After every move, check row, column, and both diagonals manually.

⛔ **Time Complexity**: `O(n)` per move
⛔ **Space Complexity**: `O(n^2)`

---

### ✅ Approach 2: Count-Based Optimized Approach

Instead of checking the whole row/column/diagonal:

* Track **sums** of moves for each `row`, `col`, `diag`, and `anti_diag`
* Player 1 → contributes `+1`
* Player 2 → contributes `-1`
* If **absolute value** of any tracker becomes `n`, declare the winner.

✅ **Time**: `O(1)` per move
✅ **Space**: `O(n)`
✅ **Best Approach**

---

## ✅ Final Java Code with Telugu-Style Comments

```java
public class TicTacToe {
    private int[] rows;
    private int[] cols;
    private int diagonal;
    private int antiDiagonal;
    private int n;

    // Constructor lo board size initialize chestunnam
    public TicTacToe(int n) {
        this.n = n;
        this.rows = new int[n];  // Each row lo total sum track cheyyadam
        this.cols = new int[n];  // Each column lo total sum track cheyyadam
        this.diagonal = 0;
        this.antiDiagonal = 0;
    }

    // Move function → player e row, col lo move chesadu
    public int move(int row, int col, int player) {
        // Player 1 → +1 ; Player 2 → -1
        int point = player == 1 ? 1 : -1;

        // Row, column update cheyyadam
        rows[row] += point;
        cols[col] += point;

        // Diagonal ayithe → row == col
        if (row == col) {
            diagonal += point;
        }

        // Anti-diagonal ayithe → row + col == n - 1
        if (row + col == n - 1) {
            antiDiagonal += point;
        }

        // Win condition check cheyyadam
        if (Math.abs(rows[row]) == n || 
            Math.abs(cols[col]) == n || 
            Math.abs(diagonal) == n || 
            Math.abs(antiDiagonal) == n) {
            return player;  // Ee player win ayyadu
        }

        return 0; // Inka winner ledu
    }
}
```

---

## ✅ Time & Space Complexity

| Operation      | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| Constructor    | O(n)            | O(n)             |
| move(row, col) | O(1)            | O(n)             |

---

## ✅ Dry Run (n = 3)

```java
TicTacToe game = new TicTacToe(3);
game.move(0, 0, 1); // → Player 1
game.move(0, 2, 2); // → Player 2
game.move(1, 1, 1); // → Player 1
game.move(1, 0, 2); // → Player 2
game.move(2, 2, 1); // → Player 1 wins via diagonal!
```

### Internal Tracker After Each Move:

| Move   | Player | rows       | cols        | diag | anti\_diag | Result |
| ------ | ------ | ---------- | ----------- | ---- | ---------- | ------ |
| (0, 0) | 1      | \[1, 0, 0] | \[1, 0, 0]  | 1    | 0          | 0      |
| (0, 2) | 2      | \[0, 0, 0] | \[1, 0, -1] | 1    | -1         | 0      |
| (1, 1) | 1      | \[0, 1, 0] | \[1, 1, -1] | 2    | -1         | 0      |
| (1, 0) | 2      | \[0, 0, 0] | \[0, 1, -1] | 2    | -1         | 0      |
| (2, 2) | 1      | \[0, 0, 1] | \[0, 1, 0]  | 3    | -1         | 1 ✅    |

---

## ✅ Test Cases

```java
public class TicTacToeTest {
    public static void main(String[] args) {
        TicTacToe game1 = new TicTacToe(3);
        assert game1.move(0, 0, 1) == 0;
        assert game1.move(0, 2, 2) == 0;
        assert game1.move(1, 1, 1) == 0;
        assert game1.move(1, 0, 2) == 0;
        assert game1.move(2, 2, 1) == 1; // Diagonal win

        TicTacToe game2 = new TicTacToe(2);
        assert game2.move(0, 0, 1) == 0;
        assert game2.move(1, 1, 2) == 0;
        assert game2.move(0, 1, 1) == 1; // Row win
    }
}
```

---

## ✅ Summary

| Approach         | Time per Move | Space | Efficiency    |
| ---------------- | ------------- | ----- | ------------- |
| Grid Brute Force | O(n)          | O(n²) | ❌ Inefficient |
| Count-Based ✅    | O(1)          | O(n)  | ✅ Best Choice |

---

Would you like me to:

* Add **undo support**?
* Add **2D Board visual simulation**?
* Extend this to **multiplayer (n players)**?

Let me know!
