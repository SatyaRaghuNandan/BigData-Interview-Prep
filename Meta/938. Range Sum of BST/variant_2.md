# // VARIANT: What if you had to optimize your solution for 10^4 function invocations?
# // How would your algorithm change?

Here's the **Java version** of the **Second Variant** — optimized for **10⁴+ range queries** over a static BST. We use **in-order traversal**, a **prefix sum array**, and **binary search** to handle each query in `O(log N)` time after a one-time `O(N)` preprocessing step.

---

## ✅ Java Implementation with Telugu Comments

```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

public class RangeSumCalculator {

    private final List<Integer> sortedValues = new ArrayList<>();
    private final List<Integer> prefixSums = new ArrayList<>();

    // ✅ Constructor — Preprocessing the BST
    public RangeSumCalculator(TreeNode root) {
        inorder(root);
    }

    // ✅ Inorder traversal to build sortedValues and prefixSums
    private void inorder(TreeNode node) {
        if (node == null) return;

        inorder(node.left);

        sortedValues.add(node.val); // BST lo inorder ante sorted values
        if (prefixSums.isEmpty()) {
            prefixSums.add(node.val); // First element
        } else {
            int lastSum = prefixSums.get(prefixSums.size() - 1);
            prefixSums.add(lastSum + node.val); // Running sum
        }

        inorder(node.right);
    }

    // ✅ Query — Sum of values in range [low, high]
    public int rangeSum(int low, int high) {
        int left = lowerBound(sortedValues, low);   // First index >= low
        int right = upperBound(sortedValues, high); // First index > high

        if (left >= right) return 0; // No elements in range

        if (left == 0) {
            return prefixSums.get(right - 1);
        } else {
            return prefixSums.get(right - 1) - prefixSums.get(left - 1);
        }
    }

    // ✅ Lower Bound — First index >= target
    private int lowerBound(List<Integer> list, int target) {
        int left = 0, right = list.size();
        while (left < right) {
            int mid = (left + right) / 2;
            if (list.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    // ✅ Upper Bound — First index > target
    private int upperBound(List<Integer> list, int target) {
        int left = 0, right = list.size();
        while (left < right) {
            int mid = (left + right) / 2;
            if (list.get(mid) <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
```

---

## ✅ Example Usage

```java
public class Main {
    public static void main(String[] args) {
        /*
            Tree:
                  10
                 /  \
                5    15
               / \     \
              3   7     18
        */

        TreeNode root = new TreeNode(10);
        root.left = new TreeNode(5);
        root.right = new TreeNode(15);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(7);
        root.right.right = new TreeNode(18);

        RangeSumCalculator calc = new RangeSumCalculator(root);

        System.out.println(calc.rangeSum(7, 15)); // Output: 32
        System.out.println(calc.rangeSum(6, 10)); // Output: 17
        System.out.println(calc.rangeSum(1, 2));  // Output: 0
    }
}
```

---

## ✅ Time & Space Complexity

| Phase             | Time Complexity  | Space Complexity | Explanation                        |
| ----------------- | ---------------- | ---------------- | ---------------------------------- |
| Inorder Build     | `O(N)`           | `O(N)`           | Build `sortedValues` + prefix sums |
| Per Query         | `O(log N)`       | `O(1)`           | Binary search in sorted list       |
| Total (Q queries) | `O(N + Q log N)` | `O(N)`           | Efficient for many queries         |

---

## ✅ Edge Case Handling

| Case                      | Behavior                 |
| ------------------------- | ------------------------ |
| No nodes in range         | Returns `0`              |
| Tree is null              | Still works, returns `0` |
| Range outside tree values | Returns `0`              |
| Exact match at boundaries | Included properly        |

---

## ✅ Summary (Interview Style)

> "For many queries over a static BST, I preprocess the tree into a **sorted list** using in-order traversal, then compute **prefix sums** for quick summation. Each query uses **binary search** to find the lower and upper bounds of the range, and subtracts prefix sums to compute the result in `O(log N)` time. This reduces total time from `O(N * Q)` to `O(N + Q log N)` — ideal for large-scale querying."

---

Would you like to extend this with:

* ✅ Floating-point average over range?
* ✅ Median of values in range?
* ✅ Integration with `Stream` or `Map<Integer, Integer>`?

Let me know and I’ll build on top of this!
