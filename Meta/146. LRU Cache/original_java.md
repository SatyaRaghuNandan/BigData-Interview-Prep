Great! Let’s walk through the **Java version** of the original **Leetcode 146: LRU Cache**, and compare it with your **custom variant**.

---

## ✅ What Are We Solving?

### Problem: Implement an LRU Cache with the following operations:

* `get(key)` – return the value if present, move it to **MRU (Most Recently Used)** position
* `put(key, value)` – insert/update a value, **evict LRU** if cache exceeds capacity

---

## ✅ Final Java Code with Detailed Telugu Comments

```java
import java.util.HashMap;
import java.util.Map;

public class LRUCache_146 {
    // 🔁 Doubly Linked List node
    private class Node {
        int key, value;
        Node prev, next;

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    // 🔁 Head = dummy LRU, Tail = dummy MRU
    private final Node head;
    private final Node tail;
    private final Map<Integer, Node> cache;
    private final int capacity;

    public LRUCache_146(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        
        head = new Node(-1, -1);  // Dummy node for easy LRU handling
        tail = new Node(-1, -1);  // Dummy node for MRU

        head.next = tail;
        tail.prev = head;
    }

    // ✅ Get operation → O(1)
    public int get(int key) {
        if (!cache.containsKey(key)) return -1;

        Node curr = cache.get(key);
        remove(curr);        // Current position nundi remove cheyyadam
        insertAtTail(curr);  // MRU position ki move cheyyadam

        return curr.value;
    }

    // ✅ Put operation → O(1)
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node old = cache.get(key);
            remove(old);        // Remove existing node
            cache.remove(key);  // Remove from map
        }

        Node newNode = new Node(key, value);
        cache.put(key, newNode);
        insertAtTail(newNode);  // Insert as MRU

        // Capacity exceed ayithe LRU ni remove cheyyadam
        if (cache.size() > capacity) {
            Node lru = head.next;         // head.next is LRU
            remove(lru);                  
            cache.remove(lru.key);
        }
    }

    // 🔁 Doubly Linked List nunchi node remove cheyyadam
    private void remove(Node node) {
        Node before = node.prev;
        Node after = node.next;

        before.next = after;
        after.prev = before;
    }

    // 🔁 Node ni MRU position (tail.prev) daggara insert cheyyadam
    private void insertAtTail(Node node) {
        Node prevTail = tail.prev;

        prevTail.next = node;
        node.prev = prevTail;

        node.next = tail;
        tail.prev = node;
    }
}
```

---

## ✅ Dry Run Example

```java
LRUCache_146 cache = new LRUCache_146(2); // capacity = 2
cache.put(1, 10); // [1]
cache.put(2, 20); // [1, 2]
cache.get(1);     // [2, 1] → 1 becomes MRU
cache.put(3, 30); // Evict 2 (LRU) → [1, 3]
cache.get(2);     // returns -1 (evicted)
cache.get(1);     // returns 10
```

---

## ✅ Test Cases

```java
public class LRUCacheTest {
    public static void main(String[] args) {
        LRUCache_146 cache = new LRUCache_146(2);

        cache.put(1, 100);
        cache.put(2, 200);
        assert cache.get(1) == 100;

        cache.put(3, 300);  // Evict key 2
        assert cache.get(2) == -1;
        assert cache.get(3) == 300;

        cache.put(4, 400);  // Evict key 1
        assert cache.get(1) == -1;
        assert cache.get(3) == 300;
        assert cache.get(4) == 400;
    }
}
```

---

## ✅ Differences: `LRUCache_146` (Original) vs `LRUCacheVariant`

| Feature             | `LRUCache_146` (Leetcode 146)          | `LRUCacheVariant`         |
| ------------------- | -------------------------------------- | ------------------------- |
| **Eviction logic**  | ✅ Evicts LRU when over capacity        | ❌ No eviction logic       |
| **Capacity limit**  | ✅ Yes                                  | ❌ No                      |
| **`get()`**         | ✅ Moves to MRU                         | ✅ Same                    |
| **`put()`**         | ✅ Inserts/updates and handles eviction | ✅ Inserts/updates only    |
| **`del()` method**  | ❌ Not present                          | ✅ Custom delete supported |
| **`last()` method** | ❌ Not supported                        | ✅ Custom MRU peek         |
| **Use Case**        | Real cache eviction logic              | MRU tracker / basic cache |

---

## ✅ Summary

* `LRUCache_146` is the **real production-grade** implementation with eviction.
* `LRUCacheVariant` is useful when:

  * You don’t want automatic eviction
  * You want to `del()` manually
  * You need access to **last inserted or accessed** item

---

Let me know if you'd like:

* ✅ A thread-safe version
* ✅ Add `first()` for LRU peek
* ✅ Version with generics for keys and values

Would you like to implement this with `LinkedHashMap` as well (1-liner LRU)?



```java

class LRUCache {
    int capacity;
    Map<Integer, ListNode> dict; 
    ListNode head;
    ListNode tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        dict = new HashMap<>();
        head = new ListNode(-1, -1);
        tail = new ListNode(-1, -1);
        head.next = tail;
        tail.previous = head; 
    }

    public int get(int key) {
        if (!dict.containsKey(key)) {
            return -1;
        }
        ListNode node = dict.get(key);
        remove(node);
        addToHead(node);
        return node.value;
    }   

    public void put(int key, int value) {   
        if (dict.containsKey(key)) {
            ListNode oldNode = dict.get(key);
            remove(oldNode);
        }
        ListNode newNode = new ListNode(key, value);
        dict.put(key, newNode);
        addToHead(newNode);

        if (dict.size() > capacity) {
            ListNode nodeToDelete = head.next;
            remove(nodeToDelete);
            dict.remove(nodeToDelete.key);
        }
    }

    private void addToHead(ListNode node) {
        // Mundu Node 
        ListNode previousEnd = tail.previous; // get the Tail .next. 
        previousEnd.next = node; 
        // 
        node.previous = previousEnd;
        node.next = tail;
        tail.previous = node;
    }

    private void remove(ListNode node) {
        node.previous.next = node.next;
        node.next.previous = node.previous;
    }
}
```
