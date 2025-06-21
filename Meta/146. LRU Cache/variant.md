Here’s the **Python version** of your enhanced `LRUCache_146_Variant` class with:

* ✅ `get(key)`
* ✅ `put(key, value)`
* ✅ `del(key)` — delete a key from the cache
* ✅ `last()` — return **most recently used** value

All with **detailed Telugu comments** for clarity.

---

## ✅ Python Implementation with Telugu Comments

```python
class Node:
    def __init__(self, key: int, value: int):
        self.key = key            # 🔑 Key ni store cheyyadam
        self.value = value        # 🔢 Value ni store cheyyadam
        self.prev = None          # 👈 Left node (previous)
        self.next = None          # 👉 Right node (next)

class LRUCacheVariant:
    def __init__(self):
        # Dummy head and tail setup cheddam
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_to_node = {}  # 🗺️ Key to Node mapping

    def _remove(self, node: Node):
        # 🔧 Node ni list nunchi remove cheyyadam
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_end(self, node: Node):
        # 🔚 Node ni tail ki (most recently used) move cheyyadam
        last = self.tail.prev

        last.next = node
        node.prev = last

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1  # ❌ Key lekapothe -1

        node = self.key_to_node[key]
        self._remove(node)
        self._move_to_end(node)

        return node.value

    def put(self, key: int, value: int):
        if key in self.key_to_node:
            # 🔁 Old node ni remove cheyyali
            self._remove(self.key_to_node[key])
            del self.key_to_node[key]

        new_node = Node(key, value)
        self._move_to_end(new_node)
        self.key_to_node[key] = new_node

    def delete(self, key: int) -> bool:
        if key not in self.key_to_node:
            return False  # ❌ Key ledu kabatti delete kuda cheyyatam ledu

        node = self.key_to_node[key]
        self._remove(node)
        del self.key_to_node[key]

        return True  # ✅ Delete success

    def last(self) -> int:
        # 🟢 Most recently used node ni return cheyyadam
        if self.tail.prev == self.head:
            return -1  # ❌ Cache lo emi ledu

        return self.tail.prev.value
```

---

## 🧠 Summary of Telugu Comments

| Function             | Purpose                                                             |
| -------------------- | ------------------------------------------------------------------- |
| `_remove(node)`      | Node ni list nunchi clean ga remove cheyyadam                       |
| `_move_to_end(node)` | Node ni recent ga use chesina laga tail ki move cheyyadam           |
| `get(key)`           | Value ni return cheyyadam & node ni most recent laga mark cheyyadam |
| `put(key, value)`    | New node insert cheyyadam (update if duplicate)                     |
| `delete(key)`        | Key ni cache nunchi remove cheyyadam                                |
| `last()`             | Tail prev lo unna most recent value ni return cheyyadam             |

---

## ⏱️ Time and Space Complexity

| Operation                      | Time   | Space                                       |
| ------------------------------ | ------ | ------------------------------------------- |
| `get`, `put`, `delete`, `last` | `O(1)` | `O(N)` — where `N` is number of keys stored |

---

Let me know if you want:

* 🧪 Unit tests for this implementation
* 🎯 Capacity tracking and LRU eviction
* 📊 Diagram of list after operations

I’ll help you add it!
