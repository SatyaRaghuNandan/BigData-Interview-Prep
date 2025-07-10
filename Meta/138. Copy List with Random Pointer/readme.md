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
class SolutionIterativeConstantSpace {
    public Node copyRandomList(Node head) {
        if (head == null) return null;

        // 🔵 Step 1: Weave the clone nodes → A → A' → B → B'
        Node curr = head;
        while (curr != null) {
            Node clone = new Node(curr.val);
            clone.next = curr.next;
            curr.next = clone;
            curr = clone.next;
        }

        // 🔴 Step 2: Setup random pointers for clones
        curr = head;
        while (curr != null) {
            if (curr.random != null) {
                curr.next.random = curr.random.next;
            }
            curr = curr.next.next;
        }

        // 🟢 Step 3: Unweave the list → separate original and clone
        curr = head;
        Node cloneHead = head.next;
        Node cloneCurr = cloneHead;

        while (curr != null) {
            curr.next = curr.next.next;
            cloneCurr.next = (cloneCurr.next != null) ? cloneCurr.next.next : null;

            curr = curr.next;
            cloneCurr = cloneCurr.next;
        }

        return cloneHead;
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
