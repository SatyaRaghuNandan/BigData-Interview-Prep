# // VARIANT: What if you were given all the nodes as a part of a vector, and no longer the root node?

Here’s a **clean, Java implementation** of the variant problem:

> **🧠 Problem Statement (Variant of Leetcode 1650):**
> You’re given a **list of all nodes** (not the root) and two nodes `p` and `q`.
> Each node has `.left`, `.right`, but no `.parent`.
> You must find their **Lowest Common Ancestor** (LCA).

---

## ✅ **Approach 1: Build `child → parent` map, then apply Two-Pointer Trick**

This is similar to **Linked List Intersection + Tree Traversal**.

### 🔧 Java Code

```java
import java.util.*;

// 🔁 Node structure with left/right pointers
class Node {
    int val;
    Node left, right;
    Node(int val) {
        this.val = val;
    }
}

public class LCAFromNodeList {

    // ✅ Main function for this variant
    public Node lowestCommonAncestor(List<Node> nodes, Node pStart, Node qStart) {
        // Step 1: Build child → parent map
        Map<Node, Node> childToParent = new HashMap<>();
        for (Node node : nodes) {
            if (node.left != null) childToParent.put(node.left, node);
            if (node.right != null) childToParent.put(node.right, node);
        }

        // Step 2: Simulate parent pointers using two pointers
        Node p = pStart;
        Node q = qStart;

        while (p != q) {
            p = childToParent.containsKey(p) ? childToParent.get(p) : qStart;
            q = childToParent.containsKey(q) ? childToParent.get(q) : pStart;
        }

        return p; // or return q, both are same
    }
}
```

---

## ✅ Test Tree Setup

We’ll convert your C++ tree to Java:

```java
public static void main(String[] args) {
    Node root = new Node(1);
    Node node2 = new Node(2);
    Node node3 = new Node(3);
    Node node4 = new Node(4);
    Node node5 = new Node(5);
    Node node6 = new Node(6);
    Node node7 = new Node(7);

    root.left = node2;
    root.right = node3;

    node2.left = node4;
    node2.right = node5;

    node5.right = node6;
    node6.left = node7;

    List<Node> allNodes = Arrays.asList(root, node2, node3, node4, node5, node6, node7);
    LCAFromNodeList sol = new LCAFromNodeList();

    System.out.println(sol.lowestCommonAncestor(allNodes, node4, node7).val); // ➤ 2
    System.out.println(sol.lowestCommonAncestor(allNodes, node5, node6).val); // ➤ 5
    System.out.println(sol.lowestCommonAncestor(allNodes, node5, node7).val); // ➤ 5
    System.out.println(sol.lowestCommonAncestor(allNodes, root, node3).val);  // ➤ 1
    System.out.println(sol.lowestCommonAncestor(allNodes, node3, node3).val); // ➤ 3
}
```

---

## ✅ Alternate Approach (Set + Climb Up)

This is like Leetcode 1650 – we climb from both nodes upward.

```java
public Node lcaUsingSet(List<Node> nodes, Node p, Node q) {
    // Step 1: Build child → parent map
    Map<Node, Node> childToParent = new HashMap<>();
    for (Node node : nodes) {
        if (node.left != null) childToParent.put(node.left, node);
        if (node.right != null) childToParent.put(node.right, node);
    }

    // Step 2: Visit q's ancestors
    Set<Node> ancestors = new HashSet<>();
    while (q != null) {
        ancestors.add(q);
        q = childToParent.get(q);
    }

    // Step 3: Traverse p's ancestors
    while (p != null) {
        if (ancestors.contains(p)) return p;
        p = childToParent.get(p);
    }

    return null;
}
```

---

## 🔍 Comparison Table

| Feature                | **Two Pointer**           | **Set + Traverse**        |
| ---------------------- | ------------------------- | ------------------------- |
| Space                  | `O(1)` (no extra space)   | `O(h)` (Set of ancestors) |
| Time                   | `O(h)`                    | `O(h)`                    |
| Values must be unique? | ❌ No                      | ❌ No                      |
| Requires parent info?  | 🚫 No (reconstruct it)    | 🚫 No                     |
| Elegance               | ✅ Very elegant            | ✅ Simple and clear        |
| Interview Friendly?    | ✅ Yes (2-pointer analogy) | ✅ Yes (HashSet idea)      |

---

## ✅ Summary to Remember

### 🔁 Rebuild Parent Pointers:

```java
Map<Node, Node> parent = new HashMap<>();
for (Node n : nodes)
    if (n.left != null) parent.put(n.left, n);
    if (n.right != null) parent.put(n.right, n);
```

### 💡 Two Techniques:

1. **Set + Climb (standard LCA if parent exists)**
2. **2-Pointer Trick (like Linked List Intersection)**

---

Would you like me to generate **diagrams or dry runs** for each case to help with memorization?
