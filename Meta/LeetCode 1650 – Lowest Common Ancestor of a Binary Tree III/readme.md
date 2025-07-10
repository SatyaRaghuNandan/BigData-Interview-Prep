


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




Great! Let's walk through **more examples and edge cases** for both **LCA with parent pointers** solutions — so you can confidently handle **interviews** and **corner cases**.

---

## ✅ Let’s Reuse This Tree Structure:

```
        A
       / \
      B   C
     / \   \
    D   F   E
```

With these parent links:

```java
A.parent = null
B.parent = A
C.parent = A
D.parent = B
F.parent = B
E.parent = C
```

We'll define nodes:

* A, B, C, D, E, F

---

## ✅ Test Case 1: `p = D`, `q = F`

**Common Ancestor:** `B`

🔁 Path from D: D → B → A
🔁 Path from F: F → B → A
➡️ First common node: **B**

---

## ✅ Test Case 2: `p = D`, `q = E`

**Common Ancestor:** `A`

🔁 Path from D: D → B → A
🔁 Path from E: E → C → A
➡️ First common node: **A**

---

## ✅ Test Case 3: `p = A`, `q = D`

**Common Ancestor:** `A`

🧠 Since `A` is the ancestor of **all**, it should always return `A` if either input is `A`.

---

## ✅ Test Case 4: `p = D`, `q = D` (Same Node)

**Common Ancestor:** `D`

🧠 Edge case — Same input.
LCA is the node itself.

---

## ✅ Test Case 5: `p = null`, `q = E`

**Common Ancestor:** `null`

🧠 If either node is `null`, the LCA cannot be determined.
Expected behavior: **Return null or handle as invalid input.**

---

## ✅ Test Case 6: Disconnected Nodes

```java
Node A = new Node(1);
Node B = new Node(2);
A.parent = null;
B.parent = null;  // No shared ancestry
```

**Common Ancestor:** `null`

🧠 Edge case — Nodes belong to different trees.
Since there's **no connection**, return **null**.

---

## ✅ Test Case 7: Deeply Nested Tree

```
        A
         \
          B
           \
            C
             \
              D
```

```java
A.parent = null
B.parent = A
C.parent = B
D.parent = C
```

**`p = C`, `q = D` → LCA = C**
**`p = B`, `q = D` → LCA = B**

🧠 Chain-like tree (linked-list shape).
Still works because we always walk up `parent`.

---

## ✅ Java Test Case Setup

```java
public static void main(String[] args) {
    Node A = new Node(1);
    Node B = new Node(2);
    Node C = new Node(3);
    Node D = new Node(4);
    Node E = new Node(5);
    Node F = new Node(6);

    B.parent = A;
    C.parent = A;
    D.parent = B;
    F.parent = B;
    E.parent = C;

    Solution sol = new Solution();

    System.out.println(sol.lowestCommonAncestorUsingSet(D, F).val); // ➤ 2 (B)
    System.out.println(sol.lowestCommonAncestorUsingSet(D, E).val); // ➤ 1 (A)
    System.out.println(sol.lowestCommonAncestorTwoPointer(D, D).val); // ➤ 4 (D)
    System.out.println(sol.lowestCommonAncestorTwoPointer(A, D).val); // ➤ 1 (A)
}
```

---

## 🔍 Interview Tip

> Always clarify with the interviewer:
>
> * Can the nodes belong to separate trees?
> * Are values unique or do we need to use node references?
> * Can inputs be `null`?

---

Do you want me to write **JUnit test cases** or simulate this tree visually with a dry run for pointers like `p1` and `p2`?

