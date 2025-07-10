# // VARIANT: What if you had to implement two more functions: the del(key) and last() functions?



Excellent! You're exploring a **variant of the LRU (Least Recently Used) Cache** — with operations like:

* `get(key)` – standard
* `put(key, value)` – standard
* `del(key)` – 🔄 custom delete operation
* `last()` – 🔍 fetch the **most recently used (MRU)** value (instead of least)

Let’s walk through:

---

## ✅ Difference From Original LRU Cache

| Feature           | Original LRU Cache                 | `LRUCacheVariant`                            |
| ----------------- | ---------------------------------- | -------------------------------------------- |
| `put(key, value)` | Inserts/updates and evicts **LRU** | Only inserts/updates. ❌ No capacity/eviction |
| `get(key)`        | Fetch and update as **MRU**        | ✅ Same behavior                              |
| `del(key)`        | ❌ Not part of standard API         | ✅ Custom method to remove a key              |
| `last()`          | ❌ Not available                    | ✅ Returns most recently used value           |

✅ This variant is a **customized MRU tracker** without eviction logic.

---

## ✅ Full Java Code with Telugu Comments

```java
import java.util.HashMap;
import java.util.Map;

public class LRUCacheVariant {

    // 🔁 Node structure for Doubly Linked List
    private static class Node {
        int key;
        int value;
        Node prev, next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    // 🔁 HashMap for O(1) access to nodes
    private final Map<Integer, Node> keyToNode;

    // Dummy head and tail for easier pointer manipulation
    private final Node head;  // head.next = LRU
    private final Node tail;  // tail.prev = MRU

    public LRUCacheVariant() {
        keyToNode = new HashMap<>();
        head = new Node(-1, -1); // Dummy head
        tail = new Node(-1, -1); // Dummy tail

        head.next = tail;
        tail.prev = head;
    }

    // ✅ get() → MRU lo move cheyyadam
    public int get(int key) {
        if (!keyToNode.containsKey(key)) {
            return -1;
        }

        Node curr = keyToNode.get(key);
        remove(curr);         // Current location nundi remove cheyyadam
        insertAtTail(curr);   // Tail daggara (MRU) ki move cheyyadam
        return curr.value;
    }

    // ✅ put() → update or insert cheyyadam (no eviction logic)
    public void put(int key, int value) {
        if (keyToNode.containsKey(key)) {
            Node existing = keyToNode.get(key);
            remove(existing);
            keyToNode.remove(key);
        }

        Node newNode = new Node(key, value);
        keyToNode.put(key, newNode);
        insertAtTail(newNode); // MRU ga insert cheyyadam
    }

    // ✅ del() → key delete cheyyadam
    public boolean del(int key) {
        if (!keyToNode.containsKey(key)) return false;

        Node toDelete = keyToNode.get(key);
        remove(toDelete);
        keyToNode.remove(key);
        return true;
    }

    // ✅ last() → MRU value return cheyyadam
    public int last() {
        if (tail.prev == head) return -1; // Cache empty
        return tail.prev.value; // Most Recently Used value
    }

    // 🔁 Tail ki node insert cheyyadam
    private void insertAtTail(Node node) {
        Node prevLast = tail.prev;

        prevLast.next = node;
        node.prev = prevLast;

        node.next = tail;
        tail.prev = node;
    }

    // 🔁 Node ni list nunchi remove cheyyadam
    private void remove(Node node) {
        Node before = node.prev;
        Node after = node.next;

        before.next = after;
        after.prev = before;
    }
}
```

---

## ✅ Dry Run

### Sample Calls:

```java
LRUCacheVariant cache = new LRUCacheVariant();
cache.put(1, 10); // MRU: 1
cache.put(2, 20); // MRU: 2 → 1
cache.get(1);     // MRU: 1 → 2
cache.put(3, 30); // MRU: 3 → 1 → 2
cache.del(2);     // removes 2
cache.last();     // returns 3 (MRU)
```

### List State:

```
head ⇄ 2 ⇄ 1 ⇄ tail  (after 2 puts)
get(1) → move 1 to tail (MRU)
head ⇄ 2 ⇄ 1 ⇄ tail

put(3)
head ⇄ 2 ⇄ 1 ⇄ 3 ⇄ tail

del(2)
head ⇄ 1 ⇄ 3 ⇄ tail

last() → 3
```

---

## ✅ Test Cases

```java
public class LRUCacheVariantTest {
    public static void main(String[] args) {
        LRUCacheVariant cache = new LRUCacheVariant();

        cache.put(1, 10);
        cache.put(2, 20);
        assert cache.get(1) == 10;
        assert cache.get(2) == 20;
        assert cache.get(3) == -1;

        cache.put(3, 30);
        assert cache.last() == 30;

        assert cache.del(2);           // should return true
        assert !cache.del(99);         // should return false

        assert cache.get(2) == -1;     // already deleted

        assert cache.last() == 30;     // 3 is still MRU
    }
}
```

---

## ✅ Summary Table

| Feature  | Description                     | Time |
| -------- | ------------------------------- | ---- |
| `get()`  | Fetch and move key to MRU       | O(1) |
| `put()`  | Insert/update and move to MRU   | O(1) |
| `del()`  | Delete from map and list        | O(1) |
| `last()` | Return most recently used value | O(1) |

---

## ✅ Recap: Variant vs Original LRU

| Feature           | Original LRU (Leetcode) | Variant (Your Code)       |
| ----------------- | ----------------------- | ------------------------- |
| Capacity/Eviction | ✅ Yes                   | ❌ No                      |
| `del()`           | ❌ Not present           | ✅ Supported               |
| `last()`          | ❌ Not available         | ✅ Returns MRU value       |
| Use Case          | Bounded cache           | MRU tracking, partial LRU |

---

Let me know if you'd like to:

* ✅ Add **capacity & eviction** support to this variant
* 🔄 Extend this to **thread-safe version**
* 📦 Add **unit tests using JUnit 5**

Would you like a **full LRU with both MRU & LRU tracking** next?


Here's the **equivalent Java code** for your **`LRUCache_146_Variant`** C++ class, including the additional `del(key)` and `last()` methods:

---

### ✅ Java Equivalent of C++ Variant

```java
import java.util.HashMap;
import java.util.Map;

public class LRUCacheVariant {
    private static class Node {
        int key;
        int value;
        Node prev;
        Node next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private final Map<Integer, Node> keyToNode;
    private final Node head; // dummy head
    private final Node tail; // dummy tail

    public LRUCacheVariant() {
        keyToNode = new HashMap<>();
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        if (!keyToNode.containsKey(key)) {
            return -1;
        }

        Node curr = keyToNode.get(key);
        remove(curr);      // Remove from current position
        insertAtTail(curr); // Re-insert as MRU
        return curr.value;
    }

    public void put(int key, int value) {
        if (keyToNode.containsKey(key)) {
            Node curr = keyToNode.get(key);
            remove(curr);
            keyToNode.remove(key);
        }

        Node newNode = new Node(key, value);
        keyToNode.put(key, newNode);
        insertAtTail(newNode);
    }

    public boolean del(int key) {
        if (!keyToNode.containsKey(key)) {
            return false;
        }

        Node toDelete = keyToNode.get(key);
        remove(toDelete);
        keyToNode.remove(key);
        return true;
    }

    public int last() {
        if (tail.prev == head) {
            return -1;
        }
        return tail.prev.value; // Most Recently Used
    }

    // Internal helpers
    private void insertAtTail(Node node) {
        Node prevLast = tail.prev;

        prevLast.next = node;
        node.prev = prevLast;

        node.next = tail;
        tail.prev = node;
    }

    private void remove(Node node) {
        Node before = node.prev;
        Node after = node.next;

        before.next = after;
        after.prev = before;
    }
}
```

---

### ✅ Summary of Differences from Original LRU:

| Function   | Behavior                                                   |
| ---------- | ---------------------------------------------------------- |
| `put()`    | No capacity limit (can be added easily if needed)          |
| `get()`    | Updates recency (moves to tail)                            |
| `del(key)` | Deletes the node if it exists                              |
| `last()`   | Returns value of **most recently used** item (tail’s prev) |

---

Would you like me to integrate **capacity logic** like your earlier version or provide **JUnit test cases** for `del()` and `last()`?
