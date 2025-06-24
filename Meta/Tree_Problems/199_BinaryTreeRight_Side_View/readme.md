## 🔍 Why BFS is Preferred

### 🔧 BFS Traverses Level-by-Level

* BFS naturally processes all nodes **level by level**, **left to right**, using a queue.
* This makes it **very easy to know**:

  * Who is the **first node** at the level (`i == 0`)
  * Who is the **last node** at the level (`i == size - 1`)
* You can capture **left/right views during the same loop** without extra logic.

✅ **Efficient and Natural for Level Order Problems**

---

## 🧠 Why DFS is Less Natural for This Case

DFS is **depth-first**, so it:

* Traverses **deep** before **wide**
* Requires you to manually **track level numbers**
* Needs extra checks like:

  * "Is this the **first node** I'm visiting at this level?" → then it's left view
  * "Is this the **last node** I'm visiting at this level?" → needs post-order or overwrite logic

### DFS works best when:

* You’re looking for **any one path** (e.g., root-to-leaf path sum)
* You want to go **deep into subtrees** (e.g., max depth, tree diameter)


// ✅ Approach 1: BFS using Two Queues

// 💡 Idea:
// Use two queues — one for the current level and one for the next level.
// After each level finishes, add the last node from that level to the result (this will be the rightmost one).

```java
import java.util.*;

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null) return new ArrayList<>();

        Queue<TreeNode> nextLevel = new LinkedList<>();
        nextLevel.offer(root);
        List<Integer> rightside = new ArrayList<>();

        while (!nextLevel.isEmpty()) {
            Queue<TreeNode> currLevel = nextLevel;
            nextLevel = new LinkedList<>();
            TreeNode node = null;

            while (!currLevel.isEmpty()) {
                node = currLevel.poll();
                if (node.left != null) nextLevel.offer(node.left);
                if (node.right != null) nextLevel.offer(node.right);
            }

            // After current level ends, the last node is the rightmost
            rightside.add(node.val);
        }

        return rightside;
    }
}

// ⏱ Complexity:
// Time: O(N) – visit each node once
// Space: O(W) – max width of the tree (due to the queue)



// ✅ Approach 2: BFS using One Queue + Sentinel (null)

// 💡 Idea:
// Use a single queue and use `null` as a level delimiter.
// Track the previous node and when the level ends, `prev` will be the rightmost.

class Solution2 {
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null) return new ArrayList<>();

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        queue.offer(null); // Sentinel to mark end of level
        List<Integer> rightside = new ArrayList<>();
        TreeNode curr = root, prev = null;

        while (!queue.isEmpty()) {
            prev = curr;
            curr = queue.poll();

            while (curr != null) {
                if (curr.left != null) queue.offer(curr.left);
                if (curr.right != null) queue.offer(curr.right);

                prev = curr;
                curr = queue.poll();
            }

            // End of level reached → prev is the last node of the level
            rightside.add(prev.val);

            // Queue still has nodes → push sentinel for next level
            if (!queue.isEmpty()) queue.offer(null);
        }

        return rightside;
    }
}

// ⏱ Complexity:
// Time: O(N)
// Space: O(W)
// Note: Sentinel null helps mark level boundaries cleanly.



// ✅ Approach 3: BFS using One Queue + Level Size Measurement

// 💡 Idea:
// Track the number of nodes at each level (level_length).
// Iterate through those many nodes and store the last node of that level.

class Solution3 {
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null) return new ArrayList<>();

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        List<Integer> rightside = new ArrayList<>();

        while (!queue.isEmpty()) {
            int levelLength = queue.size();
            for (int i = 0; i < levelLength; i++) {
                TreeNode node = queue.poll();

                // Rightmost node of the level
                if (i == levelLength - 1) {
                    rightside.add(node.val);
                }

                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }

        return rightside;
    }
}

// ⏱ Complexity:
// Time: O(N)
// Space: O(W)
// Note: Clean and widely used in BFS-based level-order problems



// ✅ Approach 4: Recursive DFS (Right-to-Left Preorder)

// 💡 Idea:
// Do a DFS, but visit the right child first.
// When we hit a new level (level == rightside.size()),
// the first node we see is the rightmost for that level.

class Solution4 {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> rightside = new ArrayList<>();
        if (root == null) return rightside;

        dfs(root, 0, rightside);
        return rightside;
    }

    private void dfs(TreeNode node, int level, List<Integer> rightside) {
        if (node == null) return;

        // If this is the first time we're visiting this level
        if (level == rightside.size()) {
            rightside.add(node.val);
        }

        // First go right (to capture rightmost first), then left
        dfs(node.right, level + 1, rightside);
        dfs(node.left, level + 1, rightside);
    }
}

// ⏱ Complexity:
// Time: O(N)
// Space: O(H) – due to recursion stack (H = height of tree)
// Note: Elegant for interview, especially for recursion-heavy problems

```

// 🏁 Summary Table:
//
// | Approach                     | Time | Space | Notes                                |
// | ---------------------------- | ---- | ----- | ------------------------------------ |
// | BFS (Two Queues)             | O(N) | O(W)  | Simple, clean separation of levels   |
// | BFS (One Queue + Sentinel)   | O(N) | O(W)  | Elegant level boundary marking       |
// | BFS (One Queue + Level Size) | O(N) | O(W)  | Most practical + clean               |
// | DFS (Recursive, right-first) | O(N) | O(H)  | Recursive, great if tree is not deep |

// ✅ Interview Recommendation:
// - Go with Approach 3 (One Queue + Level Size) or Approach 4 (Recursive DFS)
// - BFS is safer for deep trees (avoids recursion limit)
// - DFS gives a nice recursive flavor and shows control over tree traversal order
