# // VARIANT: What if you had to print to console the left and right side views?
Here's the **Java version** of the variant you described (inspired by Leetcode 199 – Right Side View), with:

---

## ✅ Problem:

Print **Left Side View (bottom-to-top)** followed by **Right Side View (top-to-bottom)**.

---

## ✅ Java Code with Detailed Telugu Comments

```java
import java.util.*;

// Node Definition
class Node {
    int val;
    Node left, right;

    Node(int val) {
        this.val = val;
    }
}

public class SideViewPrinter {

    // Main Function to Print Left and Right Side Views
    public static void printLeftRightSideViews(Node root) {
        if (root == null) return;

        List<Integer> leftView = new ArrayList<>();
        List<Integer> rightView = new ArrayList<>();

        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);

        // BFS level-order traversal
        while (!queue.isEmpty()) {
            int levelSize = queue.size();  // Current level lo enni nodes unnayo

            for (int i = 0; i < levelSize; i++) {
                Node current = queue.poll();

                // Level lo first node (i == 0) → Left Side view lo add cheyyali
                if (i == 0) {
                    leftView.add(current.val);
                }

                // Level lo last node (i == levelSize - 1) → Right Side view lo add cheyyali
                if (i == levelSize - 1) {
                    rightView.add(current.val);
                }

                // Next level ki children ni queue lo pettadam
                if (current.left != null) queue.offer(current.left);
                if (current.right != null) queue.offer(current.right);
            }
        }

        // Left side view should be printed bottom-to-top
        Collections.reverse(leftView);

        for (int val : leftView) {
            System.out.print(val + " ");
        }

        // Right side view should be printed top-to-bottom, except root duplicate (if present)
        for (int i = 1; i < rightView.size(); i++) {
            System.out.print(rightView.get(i) + " ");
        }

        System.out.println();
    }

    // Test Cases
    public static void main(String[] args) {

        // TEST CASE 1
        // Tree:
        //          1
        //        /   \
        //       2     3
        //      / \   / \
        //     4   5 6   7
        //              /
        //             8
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);
        root.right.right.left = new Node(8);

        // Output: 8 4 2 1 3 7 8
        printLeftRightSideViews(root);

        // TEST CASE 2 - Only root node
        root = new Node(1);
        // Output: 1
        printLeftRightSideViews(root);

        // TEST CASE 3 - Null root
        root = null;
        // Output: (empty)
        printLeftRightSideViews(root);

        // TEST CASE 4 - Left-skewed tree
        // Tree:
        //     1
        //    /
        //   2
        //  /
        // 3
        root = new Node(1);
        root.left = new Node(2);
        root.left.left = new Node(3);

        // Output: 3 2 1 2 3
        printLeftRightSideViews(root);
    }
}
```

---

## ✅ Sample Dry Run

### 🔹 Test Case 1

**Tree:**

```
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
            /
           8
```

### 🔹 Level Order Traversal:

| Level | Nodes   | i==0 (left) | i==size-1 (right) |
| ----- | ------- | ----------- | ----------------- |
| 0     | 1       | 1           | 1                 |
| 1     | 2,3     | 2           | 3                 |
| 2     | 4,5,6,7 | 4           | 7                 |
| 3     | 8       | 8           | 8                 |

* Left View (top to bottom): \[1, 2, 4, 8] → reversed → **\[8, 4, 2, 1]**
* Right View (top to bottom): \[1, 3, 7, 8] → skip first (1) → **\[3, 7, 8]**

✅ **Output:** `8 4 2 1 3 7 8`

---

## ✅ Time and Space Complexity

| Metric    | Complexity                                               |
| --------- | -------------------------------------------------------- |
| **Time**  | `O(N)`                                                   |
| **Space** | `O(W)`     where W is the max width of tree (queue size) |

---

## ✅ Summary

* Left Side View = first node per level → reversed.
* Right Side View = last node per level → print from second element onward.
* Use **BFS** (level order) to handle both in **one pass** efficiently.

Let me know if you want to convert this to use **DFS** or want to handle **duplicate nodes**, height-balanced trees, etc.
