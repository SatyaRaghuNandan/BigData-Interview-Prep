# // VARIANT: What if you had to ignore negative signs in your calculations until
# // you reached a leaf node, and instead, only consider signage if a root-to-leaf path is
# // a "negative path"?

Excellent variant! You're solving a nuanced version of **Leetcode 129 (Sum Root to Leaf Numbers)**:

---

### ✅ Variant Rule:

> Ignore **negative signs** during path calculation.
> But at the **leaf**, if the number of negative nodes in that path is **odd**, make the path number **negative**.

---

### ✅ Java Translation with Telugu Comments (Transliterated)

We’ll implement:

* Recursive DFS (`O(N)` time)
* Use `Math.abs()` for digits
* Maintain `numNegatives` along the path

---

### ✅ Java Code:

```java
class Solution {
    public int sumNumbers(Node root) {
        return dfs(root, 0, 0); // currSum = 0, numNegatives = 0
    }

    private int dfs(Node node, int currSum, int numNegatives) {
        if (node == null) return 0;

        // Node value lo negative sign ignore cheyyadam
        currSum = currSum * 10 + Math.abs(node.val);
        if (node.val < 0) {
            numNegatives++;
        }

        // Leaf ki vachinappudu signage decide cheyyadam
        if (node.left == null && node.right == null) {
            int sign = (numNegatives % 2 == 1) ? -1 : 1;
            return currSum * sign;
        }

        // Left + Right subtrees ni explore cheyyadam
        return dfs(node.left, currSum, numNegatives) +
               dfs(node.right, currSum, numNegatives);
    }

    // Helper Node class (if needed)
    static class Node {
        int val;
        Node left, right;
        Node(int val) { this.val = val; }
    }

    // 🧪 Test Harness
    public static void main(String[] args) {
        Solution sol = new Solution();

        Node root = new Node(-1);
        root.left = new Node(-2);
        root.left.left = new Node(-9);
        root.right = new Node(4);
        root.right.left = new Node(-5);
        assert sol.sumNumbers(root) == (-129 + 145);

        root = new Node(-1);
        root.left = new Node(-2);
        root.left.left = new Node(-9);
        root.left.left.left = new Node(3);
        root.left.left.right = new Node(-3);
        root.right = new Node(4);
        root.right.left = new Node(-5);
        root.right.right = new Node(6);
        assert sol.sumNumbers(root) == (-1293 + 1293 + 145 + -146);

        root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        assert sol.sumNumbers(root) == (12 + 13);

        root = new Node(-1);
        root.left = new Node(-2);
        root.right = new Node(-3);
        assert sol.sumNumbers(root) == (12 + 13); // negatives even → cancel out

        root = new Node(-1);
        root.left = new Node(-2);
        root.left.left = new Node(-3);
        assert sol.sumNumbers(root) == (-123);

        root = null;
        assert sol.sumNumbers(root) == 0;

        System.out.println("✅ All test cases passed!");
    }
}
```

---

### ✅ Time & Space Complexity:

* **Time:** `O(N)` → Every node visited once
* **Space:** `O(H)` → Recursion stack (tree height)

---

### 🧠 Core Intuition Recap:

* Path calculation uses **absolute values**.
* Sign is determined at the **leaf**, based on **odd/even count of negatives**.

---

Let me know if you'd like:

* BFS or Morris variant for this too
* A printable explanation sheet for your interview

I'm happy to help further!
