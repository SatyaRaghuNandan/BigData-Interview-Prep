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



Absolutely! Here's a full **Java test harness** with:

---

### ✅ `Main` method

### ✅ 5 Comprehensive Test Cases

### ✅ Telugu-style comments

### ✅ Edge cases and meaningful tree structure

### ✅ Output verification via pre-order print (with random pointers)

---

## ✅ Complete Java Code: Main + Test Cases

```java
import java.util.*;

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

public class CopyRandomBinaryTree {

    // ✅ Step 1: Structure clone cheyyadam (left, right)
    private TreeNodeRandom deepCopy(TreeNodeRandom node, HashMap<TreeNodeRandom, TreeNodeRandom> map) {
        if (node == null) return null;

        TreeNodeRandom clone = new TreeNodeRandom(node.val);
        map.put(node, clone);

        clone.left = deepCopy(node.left, map);
        clone.right = deepCopy(node.right, map);

        return clone;
    }

    // ✅ Step 2: Random pointers copy cheyyadam
    private void copyRandom(TreeNodeRandom node, HashMap<TreeNodeRandom, TreeNodeRandom> map) {
        if (node == null) return;

        TreeNodeRandom clone = map.get(node);
        clone.random = map.get(node.random); // null ayina saripothundi

        copyRandom(node.left, map);
        copyRandom(node.right, map);
    }

    public TreeNodeRandom copyRandomBinaryTree(TreeNodeRandom root) {
        HashMap<TreeNodeRandom, TreeNodeRandom> map = new HashMap<>();
        TreeNodeRandom cloneRoot = deepCopy(root, map);
        copyRandom(root, map);
        return cloneRoot;
    }

    // ✅ Helper: Print tree in Preorder + Random Pointer
    private static void printTree(TreeNodeRandom node) {
        if (node == null) return;
        String randomVal = (node.random == null) ? "null" : String.valueOf(node.random.val);
        System.out.println("Node: " + node.val + ", Random: " + randomVal);
        printTree(node.left);
        printTree(node.right);
    }

    public static void main(String[] args) {
        CopyRandomBinaryTree solver = new CopyRandomBinaryTree();

        // 🧪 Test Case 1: Basic Tree with Random = null
        TreeNodeRandom root1 = new TreeNodeRandom(1);
        root1.left = new TreeNodeRandom(2);
        root1.right = new TreeNodeRandom(3);
        // Randoms not set → all null
        System.out.println("\n🔹 Test Case 1: Randoms null");
        TreeNodeRandom clone1 = solver.copyRandomBinaryTree(root1);
        printTree(clone1); // Expect all randoms as null

        // 🧪 Test Case 2: Randoms point to siblings
        TreeNodeRandom root2 = new TreeNodeRandom(10);
        root2.left = new TreeNodeRandom(20);
        root2.right = new TreeNodeRandom(30);
        root2.left.random = root2.right;  // 20 → 30
        root2.right.random = root2.left;  // 30 → 20
        System.out.println("\n🔹 Test Case 2: Randoms to siblings");
        TreeNodeRandom clone2 = solver.copyRandomBinaryTree(root2);
        printTree(clone2); // Verify randoms

        // 🧪 Test Case 3: Randoms point to root
        TreeNodeRandom root3 = new TreeNodeRandom(100);
        root3.left = new TreeNodeRandom(200);
        root3.right = new TreeNodeRandom(300);
        root3.left.random = root3;     // 200 → 100
        root3.right.random = root3;    // 300 → 100
        root3.random = root3.left;     // 100 → 200
        System.out.println("\n🔹 Test Case 3: Randoms to root and left");
        TreeNodeRandom clone3 = solver.copyRandomBinaryTree(root3);
        printTree(clone3);

        // 🧪 Test Case 4: Complex randoms in deeper nodes
        TreeNodeRandom root4 = new TreeNodeRandom(1);
        root4.left = new TreeNodeRandom(2);
        root4.right = new TreeNodeRandom(3);
        root4.left.left = new TreeNodeRandom(4);
        root4.left.right = new TreeNodeRandom(5);
        root4.right.right = new TreeNodeRandom(6);

        root4.random = root4.left.right;      // 1 → 5
        root4.left.left.random = root4.right; // 4 → 3
        root4.right.random = root4.left.left; // 3 → 4
        root4.right.right.random = root4;     // 6 → 1
        System.out.println("\n🔹 Test Case 4: Deep tree with mixed randoms");
        TreeNodeRandom clone4 = solver.copyRandomBinaryTree(root4);
        printTree(clone4);

        // 🧪 Test Case 5: Edge Case → Empty Tree
        TreeNodeRandom root5 = null;
        System.out.println("\n🔹 Test Case 5: Empty Tree");
        TreeNodeRandom clone5 = solver.copyRandomBinaryTree(root5);
        if (clone5 == null) {
            System.out.println("✅ Passed: clone is also null");
        } else {
            System.out.println("❌ Failed: clone should be null");
        }
    }
}
```

---

## ✅ What Each Test Case Covers

| Test Case | Description                   | Highlights Random Pointer Edge           |
| --------- | ----------------------------- | ---------------------------------------- |
| TC1       | Basic binary tree, no randoms | All null → verify safe defaults          |
| TC2       | Random to siblings            | Cross random → validate map logic        |
| TC3       | Randoms point to parent/root  | Validate upward references               |
| TC4       | Deep tree with mixed randoms  | Stress test on recursion and pointer mix |
| TC5       | Null tree                     | Base case – no crash                     |

---

## 🧠 Final Tips for Meta/FAANG Interviews

* Emphasize **2-pass strategy**: clone + random
* Justify `HashMap` choice: allows O(1) lookup to resolve `random`
* Mention that this doesn’t work with weave-style (unlike linked list)
* Use **DFS** for clean recursion, or BFS for iterative version (if asked)

---

Would you like BFS-style version or unit-test (JUnit) setup as well?



