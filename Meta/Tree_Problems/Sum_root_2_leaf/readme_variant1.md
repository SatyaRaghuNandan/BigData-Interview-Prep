# // VARIANT: What if you nodes could be larger than 9?

Absolutely! You're working on a **variant of Leetcode 129** where:

> 🔄 **Each node can now hold multi-digit values (like `42`, `911`, `2000`, not just `0-9`)**

This makes the problem trickier, because we can't use `cur = cur * 10 + node.val` anymore.

---

## ✅ Key Insight:

If current number is `cur`, and the next node's value is `val` with `d` digits,
then the new number is:

```
cur * 10^d + val
```

We calculate `d = number of digits in node.val` to compute this properly.

---

## ✅ Java Implementation (with Telugu-style Comments)

```java
class Solution {
    public int sumNumbers(Node root) {
        return dfs(root, 0);
    }

    private int dfs(Node node, int currSum) {
        if (node == null) return 0;

        int digitCount = getDigitCount(node.val); // val lo entha digits unnayo chuddam
        int place = (int) Math.pow(10, digitCount); // 10^digitCount
        int newSum = currSum * place + node.val;

        if (node.left == null && node.right == null) {
            return newSum; // Leaf node aithe return cheyyali
        }

        return dfs(node.left, newSum) + dfs(node.right, newSum);
    }

    private int getDigitCount(int num) {
        if (num == 0) return 2; // As per your C++ variant's handling of `0` nodes
        int count = 0;
        while (num > 0) {
            count++;
            num /= 10;
        }
        return count;
    }

    // 🧪 Test Harness
    public static void main(String[] args) {
        Solution sol = new Solution();

        Node root = new Node(1);
        root.left = new Node(2);
        root.left.left = new Node(90);
        root.right = new Node(42);
        root.right.left = new Node(511);
        assert sol.sumNumbers(root) == 1290 + 142511;

        root = new Node(1);
        root.left = new Node(2);
        root.left.left = new Node(912);
        root.left.left.left = new Node(3);
        root.left.left.right = new Node(4);
        root.right = new Node(46);
        root.right.left = new Node(5);
        root.right.right = new Node(61);
        assert sol.sumNumbers(root) == 129123 + 129124 + 1465 + 14661;

        root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        assert sol.sumNumbers(root) == 12 + 13;

        root = new Node(10);
        root.left = new Node(200);
        root.right = new Node(3000);
        assert sol.sumNumbers(root) == 10200 + 103000;

        root = new Node(10);
        root.left = new Node(0);
        root.right = new Node(0);
        assert sol.sumNumbers(root) == 200;

        root = null;
        assert sol.sumNumbers(root) == 0;

        System.out.println("✅ All test cases passed!");
    }
}
```

---

## ✅ Custom `Node` Class

If you don’t already have one:

```java
class Node {
    int val;
    Node left, right;
    Node(int val) {
        this.val = val;
    }
}
```

---

## 🔍 Dry Run Example:

For:

```
      10
     /  \
   200  3000
```

* Left path: `10 → 200` → `10 * 1000 + 200 = 10200`
* Right path: `10 → 3000` → `10 * 10000 + 3000 = 103000`

Total = `10200 + 103000 = 113200`

---

## ✅ Time and Space Complexity:

* **Time:** `O(N)` → Every node is visited once
* **Space:** `O(H)` → Max recursion stack (height of tree)

---

Let me know if you'd like a **unit test class** using JUnit or a **visual walkthrough** for any case.
