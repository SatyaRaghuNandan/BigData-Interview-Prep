Here’s the equivalent Python version of your C++ graph cloning code (LeetCode 133) with **detailed Telugu comments** and **time/space complexity** analysis:

---

### ✅ Python Code with Telugu Comments

```java


Iterative Solution.


class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        if (node.neighbors.isEmpty()) return new Node(node.val);

        HashMap<Node, Node> cp = new HashMap<>();
        Queue<Node> qu = new LinkedList<>();

        cp.put(node, new Node(node.val));
        qu.offer(node);

        while(!qu.isEmpty()) {
            Node curr = qu.poll();
            for(Node nei: curr.neighbors) {
                if(!cp.containsKey(nei)) {
                    cp.put(nei, new Node(nei.val));
                    qu.add(nei);
                }
                cp.get(curr).neighbors.add(cp.get(nei));
            }
        }
        return cp.get(node);
    }
}

Recursive Solution.


// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {
        neighbors = new ArrayList<>();
    }

    public Node(int val) {
        this.val = val;
        neighbors = new ArrayList<>();
    }

    public Node(int val, List<Node> neighbors) {
        this.val = val;
        this.neighbors = neighbors;
    }
}

class Solution {
    public Node cloneGraph(Node node) {
        // 🔴 Null check - input lo node lekapote, return null
        if (node == null) return null;

        // 🗺️ HashMap: original node ⟶ cloned node mapping maintain cheyyadam
        Map<Node, Node> oldToNew = new HashMap<>();

        // 🔁 DFS call to start cloning
        return dfsClone(node, oldToNew);
    }

    private Node dfsClone(Node node, Map<Node, Node> oldToNew) {
        // 🟡 Ee node ni clone chesamo ledo ani check cheyyadam
        if (oldToNew.containsKey(node)) {
            return oldToNew.get(node); // 🟢 Already clone chesina node return cheyyadam (cycles kosam)
        }

        // 🔵 Kotha node create cheyyadam (clone chesinattu)
        Node clone = new Node(node.val);
        oldToNew.put(node, clone); // 🟢 Mapping ni store cheyyadam

        // 🔁 Neighbors ni recursive ga clone cheyyadam
        for (Node neighbor : node.neighbors) {
            // 🟣 Prati neighbor ni clone chesi, clone object ki add cheyyadam
            clone.neighbors.add(dfsClone(neighbor, oldToNew));
        }

        return clone;
    }
}


```


```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def dfs_clone_graph(node, old_to_new):
    # 🟡 Ee node ni clone chesamo ledo ane info old_to_new lo untundi
    if node in old_to_new:
        return old_to_new[node]  # 🟢 Already clone chesina node ni return cheyyadam (cycle avoid cheyyadam kosam)

    # 🔵 Kotha node create cheddam (clone)
    clone = Node(node.val)
    old_to_new[node] = clone  # 🟢 Original node ki clone mapping save cheyyadam

    # 🔁 Neighbors ni recursive ga clone cheyyadam
    for neighbor in node.neighbors:
        # 🟣 Prati neighbor ni clone chesi, clone object ki add cheyyadam
        clone.neighbors.append(dfs_clone_graph(neighbor, old_to_new))

    return clone

def cloneGraph(node):
    # 🔴 Null check - input lo node lekapothe direct ga None return cheyyadam
    if not node:
        return None

    # 🗺️ HashMap: Original Node ⟶ Cloned Node mapping maintain cheyyadam
    old_to_new = {}

    # 🔁 DFS call to start cloning
    return dfs_clone_graph(node, old_to_new)
```

---

### 🧠 Example Graph:

```
Node 1: [2, 4]
Node 2: [1, 3]
Node 3: [2, 4]
Node 4: [1, 3]
```

After cloning, the structure will be **identical**, but all node instances will be **new memory allocations** (deep copy).

---

### ⏱️ Time and Space Complexity:

#### ✅ Time Complexity: `O(N + E)`

* `N` = number of nodes.
* `E` = number of edges.
* Each node and each edge is visited **once**.
* DFS explores all nodes and edges in the graph.

#### ✅ Space Complexity: `O(N)`

* Recursion stack uses `O(N)` space in the **worst case** (e.g., a linear graph).
* Hash map `old_to_new` stores `N` key-value pairs (each node once).

---

### ⚠️ Edge Cases:

* `node = None` → return `None`.
* Graph with **cycles** → handled via `old_to_new` lookup.
* Graph with only **one node** or **self-loops** → handled correctly.

---

Let me know if you want:

* A **BFS version with queue**,
* Visual trace of execution,
* Or **test cases** to validate this.




Great! Let’s go step-by-step with a **visual trace of execution** for the `cloneGraph()` function using DFS, including memory state and control flow.

---

## 🧩 Sample Graph Input:

Let’s take a **simple cyclic graph**:

```
1 -- 2
|    |
4 -- 3
```

Each node is connected to two neighbors, forming a **cycle**.

Let’s assume:

```python
# Original Graph creation
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

# Start clone
cloneGraph(n1)
```

---

## 🔍 Step-by-Step DFS Visual Trace

### ➤ Step 0:

**Function Call**: `cloneGraph(n1)`
✅ `old_to_new = {}` (empty)

---

### ➤ Step 1: Clone node 1

```
dfs_clone_graph(node = 1)
```

* `1 not in old_to_new` → Create clone: `clone1`
* `old_to_new = {1: clone1}`

➡️ Now process neighbors: **\[2, 4]**

---

### ➤ Step 2: Clone node 2

```
dfs_clone_graph(node = 2)
```

* `2 not in old_to_new` → Create clone: `clone2`
* `old_to_new = {1: clone1, 2: clone2}`

➡️ Neighbors of 2 → \[1, 3]

#### ✅ Node 1 already cloned → add `clone1` to `clone2.neighbors`

➡️ Go to next neighbor → call `dfs_clone_graph(3)`

---

### ➤ Step 3: Clone node 3

```
dfs_clone_graph(node = 3)
```

* `3 not in old_to_new` → Create clone: `clone3`
* `old_to_new = {1: clone1, 2: clone2, 3: clone3}`

➡️ Neighbors of 3 → \[2, 4]

#### ✅ Node 2 already cloned → add `clone2` to `clone3.neighbors`

➡️ Call `dfs_clone_graph(4)`

---

### ➤ Step 4: Clone node 4

```
dfs_clone_graph(node = 4)
```

* `4 not in old_to_new` → Create clone: `clone4`
* `old_to_new = {1: clone1, 2: clone2, 3: clone3, 4: clone4}`

➡️ Neighbors of 4 → \[1, 3]

#### ✅ Node 1 already cloned → add `clone1` to `clone4.neighbors`

#### ✅ Node 3 already cloned → add `clone3` to `clone4.neighbors`

🔙 Return `clone4` → used in `clone3.neighbors`

---

### 🔁 Backtracking:

* `clone3` gets `clone4` in its neighbors
* `clone2` gets `clone3`
* `clone1` gets both `clone2` and `clone4`

---

## 📦 Final Cloned Graph in Memory

You now have **new nodes**:

```
clone1.val = 1, clone1.neighbors = [clone2, clone4]
clone2.val = 2, clone2.neighbors = [clone1, clone3]
clone3.val = 3, clone3.neighbors = [clone2, clone4]
clone4.val = 4, clone4.neighbors = [clone1, clone3]
```

Each node is **deep-copied**, and all references point to the new nodes. No shared memory with the original graph.

---

## 📘 State of `old_to_new` (HashMap):

| Original | Clone  |
| -------- | ------ |
| Node 1   | clone1 |
| Node 2   | clone2 |
| Node 3   | clone3 |
| Node 4   | clone4 |

---

## 🧠 Key Concepts Recap:

| Concept         | Meaning                                                   |
| --------------- | --------------------------------------------------------- |
| DFS traversal   | Avoids revisiting already-cloned nodes via hashmap        |
| Cycles          | Prevented from infinite loop using `old_to_new` lookup    |
| Deep copy       | Entire graph is recreated with **new memory allocations** |
| Recursion stack | Used instead of an explicit stack or queue                |

---

Would you like:

* ✍️ A **hand-drawn diagram** of the traversal order?
* 🧪 Sample test case code for verification?
* 🔁 A **BFS version** instead of DFS?

Let me know and I’ll provide it next.
