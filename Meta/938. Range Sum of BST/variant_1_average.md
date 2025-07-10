# // VARIANT: What if you had to return the average of all the nodes within the
# // lower and upper range? 
# // Note sometimes you are expected to use integer divison for the average, other times
# // it's floating point division.

Here’s the **Java version** of the **Average of Range in BST** problem — a variant of the classic *Range Sum of BST*. This implementation uses **recursive DFS with pruning**, tracks both `sum` and `count`, and returns `average = sum / count`.

---

## ✅ Java Implementation (Recursive DFS with Pruning + Telugu Comments)

```java
// ✅ TreeNode definition
class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Solution {

    // Total sum of nodes in range [low, high]
    private int totalSum = 0;

    // Total count of nodes in range [low, high]
    private int count = 0;

    public double averageOfRangeBST(TreeNode root, int low, int high) {
        dfs(root, low, high);

        // ✅ Count = 0 ante, divide by zero avoid cheyyali → 0.0 return cheyyadam
        return count == 0 ? 0.0 : (double) totalSum / count;
    }

    private void dfs(TreeNode node, int low, int high) {
        if (node == null) return;

        // ✅ Current value range lo unte, sum + count update cheyyali
        if (node.val >= low && node.val <= high) {
            totalSum += node.val;
            count++;
        }

        // 🔽 Left subtree lo values unte, if current > low matrame recurse cheyyali
        if (node.val > low) {
            dfs(node.left, low, high);
        }

        // 🔼 Right subtree lo values unte, if current < high matrame recurse cheyyali
        if (node.val < high) {
            dfs(node.right, low, high);
        }
    }
}
```

---

## ✅ Example Usage

```java
public class Main {
    public static void main(String[] args) {
        // BST:
        //        10
        //       /  \
        //      5   15
        //     / \    \
        //    3   7    18

        TreeNode root = new TreeNode(10);
        root.left = new TreeNode(5);
        root.right = new TreeNode(15);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(7);
        root.right.right = new TreeNode(18);

        Solution sol = new Solution();
        double avg = sol.averageOfRangeBST(root, 7, 15);
        System.out.println("Average: " + avg); // Output: 32 / 3 = 10.666...
    }
}
```

---

## ✅ Time & Space Complexity

| Metric           | Value  | Why                                       |
| ---------------- | ------ | ----------------------------------------- |
| Time Complexity  | `O(N)` | Worst case: visit all nodes in skewed BST |
| Space Complexity | `O(H)` | Recursion stack height = height of tree   |
| Best Case        | `<< N` | BST pruning avoids entire branches        |

---

## ✅ Edge Case Handling

| Case                       | Output            | Behavior                        |
| -------------------------- | ----------------- | ------------------------------- |
| Empty tree (`root = null`) | `0.0`             | No nodes to process             |
| No nodes in range          | `0.0`             | count = 0, avoid divide-by-zero |
| One node in range          | Value             | Average = that one value        |
| All nodes in range         | Mean of all nodes |                                 |

---

## ✅ Interview-Ready Summary

> “To solve this average-of-range-in-BST problem, I used recursive DFS with BST-based pruning. At each step, I update a running `sum` and `count` if the node lies within `[low, high]`. If the node is too small, I skip the left; if it’s too large, I skip the right. This makes the approach efficient, using `O(H)` space and pruning unnecessary subtrees.”

---

Let me know if you’d like:

* ✅ Iterative stack version in Java?
* ✅ JUnit test class?
* ✅ Visual representation or Tree builder helper?

I'm happy to help with any of those!
