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
