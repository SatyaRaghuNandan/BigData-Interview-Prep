Here is the **Python version of your LRUCache (LeetCode 146)** implementation with detailed **Telugu comments**, closely following your C++ logic using a **doubly linked list + hashmap** approach:

---

## ✅ Python Code with Telugu Comments

```python
class Node:
    def __init__(self, key: int, value: int):
        self.key = key          # 🔑 Key ni store cheyyadam
        self.value = value      # 🔢 Value ni store cheyyadam
        self.prev = None        # 👈 Munde unna node (left)
        self.next = None        # 👉 Tarvata unna node (right)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # 🔁 Dummy head and tail nodes create cheyyadam (easy linking kosam)
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        # 🗺️ key to node map maintain cheyyadam
        self.key_to_node = {}

    def _remove(self, node: Node):
        # 🔧 Node ni DLL nunchi remove cheyyadam
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _append_to_end(self, node: Node):
        # 🔚 Node ni tail daggara ki move cheyyadam (most recently used)
        last_node = self.tail.prev

        last_node.next = node
        node.prev = last_node

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1  # ❌ Key lekapothe -1 return cheyyadam

        node = self.key_to_node[key]
        value = node.value

        # 🔁 Node use aindhi kabatti recent ga use chesina position ki move cheyyadam
        self._remove(node)
        self._append_to_end(node)

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            # 🔄 Duplicate key vachesindhi ante old node ni remove cheyyadam
            old_node = self.key_to_node[key]
            self._remove(old_node)
            del self.key_to_node[key]

        # ➕ New node create cheyyadam
        new_node = Node(key, value)
        self._append_to_end(new_node)
        self.key_to_node[key] = new_node

        # 🧹 Capacity minchina size aithe, least recently used node ni delete cheyyali
        if len(self.key_to_node) > self.capacity:
            lru_node = self.head.next  # 👈 Least recently used node (head next)
            self._remove(lru_node)
            del self.key_to_node[lru_node.key]
```

---

## 🧠 Explanation (in English)

* Uses **Doubly Linked List** to maintain LRU order.
* `get()` makes the node **most recently used**.
* `put()` either updates an existing key or adds a new node.
* If the capacity is exceeded, we remove the **least recently used node** from the front (`head.next`).

---

## ⏱️ Time and Space Complexity

| Operation | Time Complexity | Explanation                                   |
| --------- | --------------- | --------------------------------------------- |
| `get`     | `O(1)`          | Hashmap lookup + DLL manipulation             |
| `put`     | `O(1)`          | Insertion/removal in both DLL and hashmap     |
| Space     | `O(N)`          | Where N = `capacity` (number of nodes stored) |

---

Would you like:

* 📊 Diagram of head/tail structure before and after operations?
* 🧪 Test cases to validate this LRU implementation?

Let me know and I’ll provide that!
