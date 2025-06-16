Third and Final Approach which has O(N) Time and O(1) Space Complexity. Weave Unweave. 

![image](https://github.com/user-attachments/assets/fd26622e-e4e5-41a4-ac37-13baa27ce3b9)


Absolutely! Let's break this solution down clearly with:

1. ✅ **Plain English explanation of the approach**
2. ✅ **Easy way to remember**
3. ✅ **Full Python code with detailed Telugu-style comments**
4. ✅ **Time & Space Complexity analysis**

---

## ✅ 1. Plain English Explanation of Approach

You're given a **linked list** where:

* Each node has a `val`, a `next` pointer, and a `random` pointer that may point to any node in the list (or `None`).

Your goal: **Deep copy** the entire list, including the `random` links.

### Core idea:

We use **Recursion + Hash Map (visitedHash)** to:

* Clone each node only **once**.
* Prevent **infinite loops** caused by cycles from `random` pointers.
* **Map original node ➝ cloned node** in a dictionary.

When copying:

* If we’ve **already cloned** a node, we just **return the copy** from the map.
* Else, we **create a new node**, then recursively set `.next` and `.random`.

---

## ✅ 2. Easy Way to Remember

> “If visited, return copy. Else, clone it, store it, and recurse on `.next` and `.random`.”

Just 3 steps:

1. **Base Case**: If node is `None`, return `None`.
2. **Check Cache**: Already cloned? Return it.
3. **Clone & Recurse**: Create new node, store it, then recursively assign `.next` and `.random`.

---

## ✅ 3. Python Code with Detailed Telugu Comments

```python
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        # HashMap lo original node ni key ga petti, dani clone (new) node ni value ga store chestam
        self.visitedHash = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Base case: head null aithe return cheyyali
        if head is None:
            return None

        # Ee node ni clone chesamu antey, direct ga return cheyyali (avoid cycle/redundant copy)
        if head in self.visitedHash:
            return self.visitedHash[head]

        # New node create cheddam (val matrame copy chestam now)
        node = Node(head.val, None, None)

        # Hash map lo store cheyyali original ➝ new node mapping
        self.visitedHash[head] = node

        # Next and random ni recursive ga copy cheyyali
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        # Final node return cheyyali
        return node
```

---

## ✅ 4. Time & Space Complexity

### ⏱ Time Complexity: **O(N)**

* Every node is **visited once**, and we do constant work (clone, store, recurse) for each.
* `N` = total number of unique nodes in the list.

### 🧠 Space Complexity: **O(N)**

* For the `visitedHash` map that stores original ➝ cloned mapping.
* Also includes recursion stack (max depth = `N` in worst case).

---

## 🔄 Summary Table

| Component        | Detail                                       |
| ---------------- | -------------------------------------------- |
| Approach         | DFS Recursion + HashMap                      |
| Data structure   | `visitedHash`: Maps original ➝ cloned nodes  |
| Time Complexity  | O(N)                                         |
| Space Complexity | O(N) (hash map + recursion stack)            |
| Handles Cycles?  | ✅ Yes, avoids infinite loops via memoization |
| Pattern          | “Clone + Recurse + Memoize”                  |

---

Let me know if you want:

* ✅ A dry run walkthrough
* ✅ Iterative version
* ✅ Java version
* ✅ Test case builder or visualizer




Perfect! Let’s walk through a **dry run** with edge cases to understand how the **recursive + hash map** solution for `copyRandomList()` behaves, step by step.

---

## 🧪 Test Case 1: Single node pointing to itself via `random`

```python
Original: Node A
A.val = 1
A.next = None
A.random = A (self loop)

Expected:
Cloned A'
A'.val = 1
A'.next = None
A'.random = A' (self-loop copy)
```

---

### 🔍 Dry Run Step-by-Step:

#### Step 1: First call

```python
copyRandomList(A)
```

* `A` not in `visitedHash`
* Create new node `A'` with `val=1`
* Store in map: `visitedHash[A] = A'`

---

#### Step 2: Recurse on `.next`

```python
A.next is None → copyRandomList(None)
→ returns None
→ A'.next = None
```

---

#### Step 3: Recurse on `.random`

```python
A.random = A
→ copyRandomList(A) again
```

* This time, `A` **is** in `visitedHash`
  → Return `A'` from map
  → `A'.random = A'`

---

#### Final State:

* `A'` has:

  * `val = 1`
  * `next = None`
  * `random = A'` ✅ (self-loop preserved)

---

## ✅ Output: A deep-cloned version of the original list

---

## 🧪 Test Case 2: Two nodes pointing to each other via `.random`

```
Original:
A → B → None
A.random = B
B.random = A

Expected Clone:
A' → B' → None
A'.random = B'
B'.random = A'
```

---

### 🔍 Dry Run Steps:

#### Step 1: Call `copyRandomList(A)`

* A not in `visitedHash`
* Create `A'`, store `visitedHash[A] = A'`

#### Step 2: Copy `A.next = B`

* Call `copyRandomList(B)`

  * Not in map → create `B'`, store `visitedHash[B] = B'`
  * `B.next = None` → return `None`
  * `B.random = A` → call `copyRandomList(A)`

    * `A` is in map → return `A'`
  * Set `B'.random = A'`
* Set `A'.next = B'`

#### Step 3: Copy `A.random = B`

* `B` is in map → return `B'`
* Set `A'.random = B'`

✅ Done!

---

## ✅ Output: Correctly cloned list:

```
A'.val = 1, A'.next = B', A'.random = B'
B'.val = 2, B'.next = None, B'.random = A'
```

---

## ✅ Summary of Edge Cases

| Case                                    | Behavior                                  |
| --------------------------------------- | ----------------------------------------- |
| Node points to itself (`random = self`) | Handles correctly via map                 |
| Nodes with circular `.random`           | Avoids infinite loops using `visitedHash` |
| Empty list (`head = None`)              | Returns `None` directly                   |
| Long list with mixed `random`           | Recursively handled, only visits once     |

---

Let me know if you want these test cases in runnable form with visual print functions or a helper function to build and verify linked structures.




Great! This is the **iterative version** of deep copying a linked list with `random` pointers using a **hash map (visited)** and a **helper function** `getClonedNode()`.

Let’s break it down step-by-step with:

---

## ✅ 1. Plain English Explanation

### 🎯 Goal:

Create a **deep copy** of a linked list where each node has:

* `val`
* `next`
* `random` → can point to any node (or `None`)

### 🧠 Strategy:

* Use a **dictionary `visited`** to map each original node → its cloned copy.
* Traverse the original list **iteratively**.
* For each node:

  * Create/get its **clone**
  * Set the **`.next`** and **`.random`** pointers using the helper function `getClonedNode()`.

---

## ✅ 2. Easy Way to Remember

> **“Iterate and map: for every original node, build or fetch its clone and update `.next` and `.random`.”**

* Use a **helper** to manage mapping/creation: `getClonedNode(node)`
* In the main loop:

  * Update the `random` and `next` of the cloned node.
  * Move both pointers forward.

---

## ✅ 3. Python Code with Detailed Telugu-Style Comments

```python
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        # Original ➝ Cloned node mapping
        self.visited = {}

    def getClonedNode(self, node):
        if node:
            # Already clone chesam antey, return clone from map
            if node in self.visited:
                return self.visited[node]
            else:
                # New node create cheyyadam and store in visited map
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        old_node = head
        # First node ki clone create cheyyadam
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Linked list ni iterate cheyyadam, each node ki clone create cheyyadam
        while old_node:
            # current node ki random & next pointer clone cheyyadam
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # move old_node and new_node forward
            old_node = old_node.next
            new_node = new_node.next

        # visited[head] will be the head of the cloned list
        return self.visited[head]
```

---

## ✅ 4. Time & Space Complexity

| Metric              | Value                                |
| ------------------- | ------------------------------------ |
| ⏱ Time Complexity   | O(N) – Visit each node once          |
| 🧠 Space Complexity | O(N) – Hash map for original ➝ clone |

* N = total number of nodes in the list

---

## ✅ 5. Dry Run – Key Edge Case

### 🔬 Test Case: Two nodes, cross-pointing `random`

```
Original:
A.val = 1, A.random = B
B.val = 2, B.random = A
A.next = B
B.next = None
```

---

### Step-by-Step Execution:

#### Initial:

* `old_node = A`
* `new_node = A' (clone of A)`
* `visited = { A: A' }`

---

#### First iteration (`old_node = A`):

* `new_node.random = getClonedNode(B)`

  * B not in map → clone B → store `visited[B] = B'`
* `new_node.next = getClonedNode(B)`

  * Already cloned → return B'
* Move: `old_node = B`, `new_node = B'`

---

#### Second iteration (`old_node = B`):

* `new_node.random = getClonedNode(A)`

  * Already in map → return A'
* `new_node.next = getClonedNode(None)` → return None
* Done

---

✅ Output:

* A' and B' are deep clones
* `A'.random = B'`
* `B'.random = A'`
* `A'.next = B'`
* `B'.next = None`

---

## ✅ Summary Table

| Concept         | Description                                      |
| --------------- | ------------------------------------------------ |
| Pattern         | Iterative with mapping                           |
| Handles Cycles? | ✅ Yes                                            |
| Hash Map        | Prevents re-cloning and resolves `.random` paths |
| Reusability     | `getClonedNode()` makes code modular and clean   |

---

Let me know if you'd like:

* ✅ Visual Diagram
* ✅ Java version
* ✅ Test harness to validate deep copy
* ✅ Performance comparison with recursive version



Perfect — you've now shared the **most optimal solution** for `copyRandomList` known as the **“interleaving (weaving) method”**, which:

* Requires **O(1)** extra space (no hash map).
* Still achieves **O(N)** time complexity.

Let’s walk through this in detail, including:

* ✅ Plain English approach
* ✅ Easy way to remember
* ✅ Telugu-style code comments
* ✅ Time and Space complexity
* ✅ Dry run with edge case

---

## ✅ 1. Plain English Explanation of Approach

We follow **three phases**:

### 🔹 Step 1: **Weave the clone nodes**

* For each original node, insert its clone **just after it**.

  * Example: A → B → C becomes: A → A' → B → B' → C → C'

### 🔹 Step 2: **Copy random pointers**

* For each cloned node, set its `.random` to:

  ```python
  original.random.next  # which is the clone of original.random
  ```

### 🔹 Step 3: **Unweave the list**

* Split the interleaved list into:

  * Original list: A → B → C
  * Cloned list:  A' → B' → C'

---

## ✅ 2. Easy Way to Remember

> “Weave → Wire → Unweave”

| Step   | Mnemonic | What it means                   |
| ------ | -------- | ------------------------------- |
| Step 1 | Weave    | Interleave clone nodes          |
| Step 2 | Wire     | Set `.random` pointers          |
| Step 3 | Unweave  | Restore original, extract clone |

---

## ✅ 3. Code with Detailed Telugu Comments

```python
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        # Step 1: Weave clone nodes into original list
        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)  # Clone node
            new_node.next = ptr.next
            ptr.next = new_node  # Insert after original
            ptr = new_node.next

        # Step 2: Wire random pointers for clone nodes
        ptr = head
        while ptr:
            # ptr.next is clone, ptr.random is original's random
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next  # Jump to next original

        # Step 3: Unweave both lists
        ptr_old = head         # Pointer to original list
        ptr_new = head.next    # Pointer to cloned list
        head_new = head.next   # Save head of cloned list

        while ptr_old:
            ptr_old.next = ptr_old.next.next  # Skip cloned node
            ptr_new.next = ptr_new.next.next if ptr_new.next else None
            ptr_old = ptr_old.next
            ptr_new = ptr_new.next

        return head_new
```

---

## ✅ 4. Time and Space Complexity

| Metric           | Value             |
| ---------------- | ----------------- |
| Time Complexity  | O(N) — 3 passes   |
| Space Complexity | O(1) — no hashmap |

This is the most space-efficient solution possible while maintaining O(N) time.

---

## ✅ 5. Dry Run – Key Edge Case

### 🧪 Test Case:

```
A → B → None
A.random = B
B.random = A
```

---

### 🔍 Step-by-Step:

#### 🔸 Phase 1: Weaving

* A → A' → B → B'
* A'.val = A.val, B'.val = B.val

#### 🔸 Phase 2: Wiring

* A'.random = A.random.next = B'
* B'.random = B.random.next = A'

✅ Random pointers set correctly.

#### 🔸 Phase 3: Unweaving

* Restore A → B
* Extract A' → B'

✅ Original and clone lists are restored and separated.

---

## ✅ Summary Table

| Phase   | Action                      | Key Trick                             |
| ------- | --------------------------- | ------------------------------------- |
| Weave   | Insert clone nodes inline   | `ptr.next = clone`                    |
| Wire    | Connect `.random` pointers  | `clone.random = original.random.next` |
| Unweave | Detach clones from original | Restore pointers cleanly              |

---

Let me know if you'd like:

* A **visual diagram** of the weaving process
* A **unit test builder** to validate correctness
* A **C++ or Java version** for reference


Absolutely! Here's a **step-by-step visual diagram** of the optimal **interleaving solution** to `copyRandomList()`.

---

## 🎯 Input: A simple linked list with `random` pointers

```
Original List:
A --> B --> C --> None
|     |     |
v     v     v
C     A     B
```

Each node points via `.next` to the next node
Each `.random` pointer points elsewhere in the list.

---

## 🧩 Step 1: **Weave clone nodes in between**

We insert a clone of each node **just after** the original node:

```
Weaved List (after Step 1):
A --> A' --> B --> B' --> C --> C' --> None
|     |     |     |     |     |
v     v     v     v     v     v
C     ?     A     ?     B     ?
```

* `A'`, `B'`, `C'` are the cloned nodes.
* Clone nodes don't have their `.random` set yet.

---

## 🔧 Step 2: **Wire random pointers**

Now we set the `.random` of each clone node using:

```python
original.next.random = original.random.next
```

Why this works:

* `original.random` gives the original node that should be pointed to.
* `original.random.next` gives the **clone** of that target.

Updated diagram:

```
Weaved List (after Step 2):
A --> A' --> B --> B' --> C --> C' --> None
|     |     |     |     |     |
v     v     v     v     v     v
C     C'    A     A'    B     B'
```

---

## 🔓 Step 3: **Unweave to separate original and cloned lists**

Now we detach the clones:

```
Original List:         A  -->  B  -->  C  --> None
                       |       |       |
                       v       v       v
                       C       A       B

Cloned List:           A' --> B' --> C' --> None
                       |      |      |
                       v      v      v
                       C'     A'     B'
```

* Both lists are correctly restored.
* All `.next` and `.random` pointers are copied correctly.

---

## 🧠 Key Takeaways from the Diagram

| Concept       | Visual Outcome                              |
| ------------- | ------------------------------------------- |
| Interleaving  | Original and clone are right next to each   |
| Random wiring | Clones can reach other clones using `.next` |
| Separation    | Cleanly restores two separate lists         |

---

Would you like a hand-drawn version as an image? I can generate a visual diagram too.


