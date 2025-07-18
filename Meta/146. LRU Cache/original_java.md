Here’s a detailed breakdown of your **LRU Cache** implementation:

---

## ✅ **Plain English Approach (5–6 Bullet Points)**

1. **Use a HashMap + Doubly Linked List**:

   * HashMap (`cache`) helps us access nodes in **O(1)** time.
   * Doubly Linked List keeps track of the **usage order** (most recent at head, least at tail).

2. **Access (`get`)**:

   * If key exists in cache, return value and move that node to the **front (head)**.
   * If not, return -1.

3. **Insert/Update (`put`)**:

   * If key exists, update value and move node to the front.
   * If not, create a new node, add to front, and update map.
   * If adding exceeds capacity, remove the **tail node** (least recently used), and remove it from map.

4. **Move-to-head logic**:

   * On every `get` or `put` of existing key, that node becomes most recently used → moved to **head**.

5. **Tail is always least recently used (LRU)**:

   * So if capacity is exceeded, we just **remove the tail's previous node** (not dummy tail itself).

---

## 🧠 **Time Complexity**

| Operation         | Time Complexity | Why                                         |
| ----------------- | --------------- | ------------------------------------------- |
| `get(key)`        | **O(1)**        | HashMap lookup and linked list move-to-head |
| `put(key, value)` | **O(1)**        | HashMap + list insert/remove at head/tail   |

✅ All operations are **O(1)** amortized due to the use of HashMap and efficient doubly linked list manipulation.

---

## 💾 **Space Complexity**

* **O(capacity)**:

  * The HashMap and Doubly Linked List store up to `capacity` number of items.

---

## 🔍 Telugu Comments Version of Code

```java
class LRUCache {
    // Doubly Linked List node class
    class DLinkedNode {
        int key;
        int value;
        DLinkedNode pre;
        DLinkedNode post;
    }

    // ✅ Node ni head ki immediate ga add cheyyadam
    private void addNode(DLinkedNode node) {
        node.pre = head;
        node.post = head.post;

        head.post.pre = node;
        head.post = node;
    }

    // ✅ Node ni list nunchi remove cheyyadam
    private void removeNode(DLinkedNode node) {
        DLinkedNode pre = node.pre;
        DLinkedNode post = node.post;

        pre.post = post;
        post.pre = pre;
    }

    // ✅ Node ni head ki move cheyyadam (recent ga use aindi kabatti)
    private void moveToHead(DLinkedNode node) {
        this.removeNode(node); // first remove from current position
        this.addNode(node);    // then add to head
    }

    // ✅ Least Recently Used node ni pop cheyyadam (tail previous node)
    private DLinkedNode popTail() {
        DLinkedNode res = tail.pre;
        this.removeNode(res);
        return res;
    }

    private Map<Integer, DLinkedNode> cache = new HashMap<>();
    private int count;
    private int capacity;
    private DLinkedNode head, tail;

    public LRUCache(int capacity) {
        this.count = 0;
        this.capacity = capacity;

        // ✅ Dummy head and tail create chestunnam
        head = new DLinkedNode();
        head.pre = null;

        tail = new DLinkedNode();
        tail.post = null;

        head.post = tail;
        tail.pre = head;
    }

    // ✅ get operation: cache lo key vunte value return cheyyi, lekapote -1
    public int get(int key) {
        DLinkedNode node = cache.get(key);
        if (node == null) return -1;

        // ✅ Recent ga access chesam kabatti head ki move cheyyali
        this.moveToHead(node);
        return node.value;
    }

    // ✅ put operation
    public void put(int key, int value) {
        DLinkedNode node = cache.get(key);

        if (node == null) {
            // ✅ New node create cheyyadam
            DLinkedNode newNode = new DLinkedNode();
            newNode.key = key;
            newNode.value = value;

            cache.put(key, newNode);  // map lo petti
            this.addNode(newNode);   // list lo head ki add cheyyi
            ++count;

            if (count > capacity) {
                // ✅ Capacity exceed aithe tail nunchi LRU node remove cheyyi
                DLinkedNode tail = this.popTail();
                cache.remove(tail.key);
                --count;
            }
        } else {
            // ✅ Existing node unte value update cheyyi
            node.value = value;
            this.moveToHead(node);
        }
    }
}
```

---

## 📝 Summary

| Feature         | Description                            |
| --------------- | -------------------------------------- |
| Data Structures | HashMap + Doubly Linked List           |
| Operations      | `get()` and `put()` in **O(1)** time   |
| Why DLinkedList | To quickly reorder items when accessed |
| Why HashMap     | To instantly find the node for a key   |

Let me know if you'd like this converted into **JavaScript**, or if you'd like to add **unit tests or enhancements** (like TTL or size tracking).
