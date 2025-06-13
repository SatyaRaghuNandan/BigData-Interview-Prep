Absolutely! Below are the **three updated Python implementations** for **"Copy List with Random Pointer" (Leetcode 138)** with:

* ✅ Clean variable naming
* ✅ Detailed Telugu comments in English script
* ✅ Explicit time and space complexity at the top of each approach

---

## ✅ Approach 1: Recursive with HashMap

```python
# ✅ Time Complexity: O(N)
# ✅ Space Complexity: O(N) - HashMap + Recursive Call Stack

class SolutionRecursive:
    def __init__(self):
        # 🗺️ Original node → Cloned node mapping maintain cheyyadam
        self.original_to_clone = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # ⚠️ Base case: List lekapothe None return cheyyali
        if head is None:
            return None

        # 🟢 Already clone chesina node aithe, direct ga clone return cheyyadam
        if head in self.original_to_clone:
            return self.original_to_clone[head]

        # 🔵 New clone node create cheyyadam (random and next to be filled later)
        clone = Node(head.val, None, None)

        # 🔁 Mapping original → clone
        self.original_to_clone[head] = clone

        # 🔁 Recursive calls for next and random
        clone.next = self.copyRandomList(head.next)
        clone.random = self.copyRandomList(head.random)

        return clone
```

---

## ✅ Approach 2: Iterative with O(N) Space

```python
# ✅ Time Complexity: O(N)
# ✅ Space Complexity: O(N) - Only HashMap (no recursion)

class SolutionIterativeWithMap:
    def __init__(self):
        # 🗺️ Original → Clone map
        self.original_to_clone = {}

    def get_or_create_clone(self, node):
        # 🎯 Node ki corresponding clone return cheyyadam or create cheyyadam
        if node:
            if node in self.original_to_clone:
                return self.original_to_clone[node]
            clone = Node(node.val, None, None)
            self.original_to_clone[node] = clone
            return clone
        return None

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        current_original = head
        clone_head = Node(head.val, None, None)
        self.original_to_clone[current_original] = clone_head

        current_clone = clone_head

        # 🔁 List traverse cheyyadam while cloning
        while current_original:
            # 🔗 next and random pointers set cheyyadam
            current_clone.next = self.get_or_create_clone(current_original.next)
            current_clone.random = self.get_or_create_clone(current_original.random)

            # ⏩ Move to next node
            current_original = current_original.next
            current_clone = current_clone.next

        return clone_head
```

---

## ✅ Approach 3: Iterative with O(1) Space (Weaving Technique)

```python
# ✅ Time Complexity: O(N)
# ✅ Space Complexity: O(1) - No extra space other than output

class SolutionIterativeConstantSpace:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # Step 1: Cloning nodes and weaving (A → A' → B → B'...)
        current = head
        while current:
            new_node = Node(current.val, current.next, None)
            current.next = new_node
            current = new_node.next

        # Step 2: Setting random pointers for cloned nodes
        current = head
        while current:
            clone_node = current.next
            clone_node.random = current.random.next if current.random else None
            current = clone_node.next

        # Step 3: Unweaving original and cloned lists
        current_original = head
        clone_head = head.next
        current_clone = clone_head

        while current_original:
            current_original.next = current_clone.next
            current_clone.next = current_clone.next.next if current_clone.next else None

            current_original = current_original.next
            current_clone = current_clone.next

        return clone_head
```

---

## 🏁 Summary Table (Again, with Updated Naming & Comments)

| Approach                          | Time | Space | Safe for Large Inputs?  | Mutates Input? | Highlights                    |
| --------------------------------- | ---- | ----- | ----------------------- | -------------- | ----------------------------- |
| Recursive with HashMap            | O(N) | O(N)  | ❌ (stack overflow risk) | ❌              | Clean recursion logic         |
| Iterative with HashMap            | O(N) | O(N)  | ✅                       | ❌              | Clean & safe                  |
| Iterative with O(1) Space (weave) | O(N) | O(1)  | ✅                       | ✅ (temporary)  | Optimal, tricky pointer logic |

---

Let me know if you'd like:

* 🧪 Sample input/output trace
* 🧠 Mock interview-style explanation for any one of these
* 📈 Visual pointer diagrams for woven structure

I’ll help you with that next!
