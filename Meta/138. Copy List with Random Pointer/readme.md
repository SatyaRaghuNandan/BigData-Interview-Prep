Here’s the full **Java implementation** of all three approaches for **Leetcode 138: Copy List with Random Pointer**, including:

✅ Clean structure
✅ Telugu-style comments
✅ Time & space complexity
✅ Suitable naming and interview tips

---

## ✅ Node Definition in Java

```java
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
```

---

## ✅ Approach 1: Recursive with HashMap

```java
import java.util.HashMap;

class SolutionRecursive {
    private HashMap<Node, Node> originalToClone = new HashMap<>();

    public Node copyRandomList(Node head) {
        // 🛑 Base case: original list lo node lekapothe null return cheyyali
        if (head == null) return null;

        // 🔁 Already clone chesina node unte, return the existing clone
        if (originalToClone.containsKey(head)) {
            return originalToClone.get(head);
        }

        // 🔨 Clone node create cheyyadam
        Node clone = new Node(head.val);
        originalToClone.put(head, clone);

        // 🔁 Recurse for next and random pointers
        clone.next = copyRandomList(head.next);
        clone.random = copyRandomList(head.random);

        return clone;
    }
}
```

⏱️ **Time**: O(N)
📦 **Space**: O(N) (Map + Recursion stack)

---

## ✅ Approach 2: Iterative with HashMap

```java
import java.util.HashMap;

class SolutionIterativeWithMap {
    public Node copyRandomList(Node head) {
        if (head == null) return null;

        HashMap<Node, Node> map = new HashMap<>();

        Node curr = head;
        // 🟢 Step 1: Create all clone nodes and map them
        while (curr != null) {
            map.put(curr, new Node(curr.val));
            curr = curr.next;
        }

        // 🔁 Step 2: Setup next and random pointers
        curr = head;
        while (curr != null) {
            map.get(curr).next = map.get(curr.next);
            map.get(curr).random = map.get(curr.random);
            curr = curr.next;
        }

        return map.get(head);
    }
}
```

⏱️ **Time**: O(N)
📦 **Space**: O(N) (HashMap only)

---

## ✅ Approach 3: Iterative with O(1) Space (Weaving)

```java
class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        } 

        Node current = head;

        // ✅ Step 1: Clone nodes and interleave them with original list
        while (current != null) {
            Node cloneNode = new Node(current.val); // Current node ki clone create cheyyadam
            cloneNode.next = current.next; // Clone node next ni original next ki point cheyyadam
            current.next = cloneNode;      // Original node next ni clone ki point cheyyadam
            current = cloneNode.next;      // Next original node ki move avvadam
        }

        // ✅ Step 2: Set random pointers of clone nodes
        current = head;
        while (current != null) {
            if (current.random != null) {
                current.next.random = current.random.next; // Clone node ki correct random pointer set cheyyadam
            }
            current = current.next.next; // Skip clone node, go to next original
        }

        // ✅ Step 3: Separate clone list from original list
        current = head;                  // Start from head again
        Node cloneHead = head.next;      // First clone node as head
        Node cloneCurrent = cloneHead;

        while (current != null) {
            current.next = current.next.next; // Original list ni restore cheyyadam
            cloneCurrent.next = (cloneCurrent.next != null) ? cloneCurrent.next.next : null; // Clone list fix cheyyadam

            current = current.next;       // Move to next original
            cloneCurrent = cloneCurrent.next; // Move to next clone
        }

        return cloneHead; // Return head of cloned list
    }
}

```

⏱️ **Time**: O(N)
📦 **Space**: O(1) (no HashMap used)

---

## 🧠 Interview Explanation: “Weave–Wire–Weave Out”

1. **Weave**: Insert clones next to originals
2. **Wire**: Setup `random` using `original.random.next`
3. **Weave Out**: Separate original and cloned list cleanly

This is optimal in both **space** and **time**, and shows mastery over pointer operations.

---

Let me know if you'd like:

* 📊 Diagrams of weaving process
* 🧪 Test harness for all approaches
* 🧠 Tips to choose one approach in interviews based on constraints
