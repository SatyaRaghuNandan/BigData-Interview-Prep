


Sure! Below is the **Java version** of both **LCA with parent pointers** solutions:

---

## ✅ **Solution 1: Using HashSet of Node References**

```java
class Node {
    int val;
    Node parent;
    Node(int val) {
        this.val = val;
    }
}

public class Solution {

    public Node lowestCommonAncestorUsingSet(Node p, Node q) {
        Set<Node> visited = new HashSet<>();

        // Step 1: Traverse ancestors of q and add to set
        while (q != null) {
            visited.add(q);
            q = q.parent;
        }

        // Step 2: Traverse ancestors of p and find first match
        while (p != null) {
            if (visited.contains(p)) {
                return p;
            }
            p = p.parent;
        }

        return null;
    }
}
```

### 🧠 Time & Space Complexity

| Metric           | Value                                 |
| ---------------- | ------------------------------------- |
| Time Complexity  | `O(h)`                                |
| Space Complexity | `O(h)` (for storing ancestors of `q`) |

> ✅ Works even if node values are **not unique**, because we store **node references**, not values.

---

## ✅ **Solution 2: Two Pointer Trick (Linked List Intersection Style)**

```java
class Node {
    int val;
    Node parent;
    Node(int val) {
        this.val = val;
    }
}

public class Solution {

    public Node lowestCommonAncestorTwoPointer(Node p, Node q) {
        Node pointer1 = p;
        Node pointer2 = q;

        // Keep walking up until they meet
        while (pointer1 != pointer2) {
            pointer1 = (pointer1 == null) ? q : pointer1.parent;
            pointer2 = (pointer2 == null) ? p : pointer2.parent;
        }

        return pointer1;
    }
}
```

### 🧠 Time & Space Complexity

| Metric           | Value  |
| ---------------- | ------ |
| Time Complexity  | `O(h)` |
| Space Complexity | `O(1)` |

> ✅ Elegant solution that **works with duplicate node values** since we compare **object references**.

---

## ✅ Visual Dry Run Example (Both Methods)

### Tree Structure:

```
        A
       / \
      B   C
     /     \
    D       E
```

### Nodes:

* `D.parent = B`, `B.parent = A`
* `E.parent = C`, `C.parent = A`

### Case:

```java
p = D, q = E
LCA = A
```

---

## ✅ Summary

| Solution        | Uses Extra Space | Handles Duplicates | Intuitive          |
| --------------- | ---------------- | ------------------ | ------------------ |
| HashSet (1)     | ✅ Yes (`O(h)`)   | ✅ Yes (using ref)  | ✅ Easy             |
| Two Pointer (2) | ❌ No (`O(1)`)    | ✅ Yes              | ⚠️ Slightly tricky |

---

Would you like me to add test cases and a full `main()` method to try both versions?


