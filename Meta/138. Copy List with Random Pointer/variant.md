# // VARIANT: What if you had to deep copy a binary tree, not a linked list?

Great! You're now working on the **variant of Leetcode 138**, where instead of copying a **linked list with random pointers**, you're copying a **binary tree** where each node has:

* `left` and `right` pointers (normal binary tree)
* a `random` pointer pointing to **any other node (or null)** in the tree

---

## ✅ What You Need

We'll convert your **C++ variant code** to **Java** with:

* ✅ Telugu-style comments
* ✅ Clean recursive logic
* ✅ HashMap for mapping old → new nodes
* ✅ Time & space complexity
* ✅ Bonus test structure (if needed)

---

## ✅ Java Node Definition

```java
class TreeNodeRandom {
    int val;
    TreeNodeRandom left, right, random;

    TreeNodeRandom(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
        this.random = null;
    }
}
```

---

## ✅ Java Solution (2-Pass: Deep Copy + Random Assignment)

```java
import java.util.HashMap;

public class CopyRandomBinaryTree {

    // 🔁 Step 1: Deep copy the structure (left & right) and build map
    private TreeNodeRandom deepCopy(TreeNodeRandom node, HashMap<TreeNodeRandom, TreeNodeRandom> oldToNew) {
        if (node == null) return null;

        TreeNodeRandom clone = new TreeNodeRandom(node.val);
        oldToNew.put(node, clone);

        // 🔁 Left and Right children ki recursive copy
        clone.left = deepCopy(node.left, oldToNew);
        clone.right = deepCopy(node.right, oldToNew);

        return clone;
    }

    // 🔁 Step 2: Random pointer set cheyyadam using map
    private void copyRandom(TreeNodeRandom node, HashMap<TreeNodeRandom, TreeNodeRandom> oldToNew) {
        if (node == null) return;

        TreeNodeRandom clone = oldToNew.get(node);
        clone.random = oldToNew.get(node.random); // random might be null → map.get(null) = null

        // 🔁 Traverse entire tree
        copyRandom(node.left, oldToNew);
        copyRandom(node.right, oldToNew);
    }

    // ✅ Final function
    public TreeNodeRandom copyRandomBinaryTree(TreeNodeRandom root) {
        HashMap<TreeNodeRandom, TreeNodeRandom> oldToNew = new HashMap<>();

        // 🧱 Step 1: Deep copy tree without random
        TreeNodeRandom cloneRoot = deepCopy(root, oldToNew);

        // 🔗 Step 2: Setup random pointers
        copyRandom(root, oldToNew);

        return cloneRoot;
    }
}
```

---

## ✅ Time & Space Complexity

| Metric                      | Value |
| --------------------------- | ----- |
| Time                        | O(N)  |
| Space (Map)                 | O(N)  |
| N = Number of nodes in tree |       |

* Each node is visited **twice** → once for `deepCopy`, once for `copyRandom`.

---

## ✅ Interview Explanation

> "I perform the deep copy in **two passes**:
>
> 🔹 In the first pass, I use DFS to clone the structure (left and right) and maintain a mapping between original → clone.
> 🔹 In the second pass, I re-traverse the original tree and use the map to copy the `random` pointers."

🧠 This is the most intuitive and robust approach. Alternatives like weaving (as in linked list) don't apply well to trees.

---

## ✅ Would You Like?

* 📐 Tree diagram walkthrough
* 🧪 Test scaffolding for building custom binary tree
* 💡 Extension: Include parent pointer support or non-binary structure?

Let me know!
