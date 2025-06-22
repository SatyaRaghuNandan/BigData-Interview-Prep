Here's the full translation of all 3 approaches for **Leetcode 23 – Merge k Sorted Lists** into **Java**, with:

* ✅ Detailed **Telugu comments**
* 📊 Clear **Time and Space Complexity** per approach
* 🧠 Clean structure for interviews

---

## ✅ 1. Min-Heap (PriorityQueue) – Optimal Approach

### 🔧 Java Code with Telugu Comments

```java
import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class MergeKLists_Heap {
    public ListNode mergeKLists(ListNode[] lists) {
        // 🧺 Min Heap declare cheyyadam
        PriorityQueue<ListNode> heap = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.val, b.val)
        );

        // 🔁 First node ni heap lo pettadam (oka list ki oka node)
        for (ListNode node : lists) {
            if (node != null) {
                heap.offer(node);
            }
        }

        ListNode dummy = new ListNode(0); // Result build cheyyadaniki dummy node
        ListNode current = dummy;

        while (!heap.isEmpty()) {
            // 🏆 Minimum node ni pop cheyyadam
            ListNode node = heap.poll();
            current.next = node;
            current = current.next;

            // ☑️ Migilina nodes unte heap lo add cheyyadam
            if (node.next != null) {
                heap.offer(node.next);
            }
        }

        return dummy.next;
    }
}
```

---

### ⏱ Time Complexity:

* `O(N log k)`

  * `N` = total number of nodes
  * `k` = number of linked lists
  * Each node inserted and removed from heap once (`log k`)

### 📦 Space Complexity:

* `O(k)` heap size (at most one node per list)

---

## ✅ 2. Divide and Conquer

### 🔧 Java Code with Telugu Comments

```java
public class MergeKLists_DivideAndConquer {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;

        int interval = 1;
        int total = lists.length;

        // 🪄 Pair ga merge cheyyadam - Merge Sort logic
        while (interval < total) {
            for (int i = 0; i + interval < total; i += interval * 2) {
                lists[i] = mergeTwoLists(lists[i], lists[i + interval]);
            }
            interval *= 2;
        }

        return lists[0];
    }

    // ✅ Rendu sorted lists ni merge cheyyadam
    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        // 🔁 Compare chesthu merge cheyyadam
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                current.next = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                l2 = l2.next;
            }
            current = current.next;
        }

        // 🔚 Migilina nodes attach cheyyadam
        current.next = (l1 != null) ? l1 : l2;

        return dummy.next;
    }
}
```

---

### ⏱ Time Complexity:

* `O(N log k)`

  * `log k` levels of merging (like merge sort)
  * At each level, total `O(N)` merge operations

### 📦 Space Complexity:

* `O(1)` extra (in-place merge)
* `O(log k)` if done recursively (here it's iterative)

---

## ✅ 3. Brute Force (Collect + Sort + Rebuild)

### 🔧 Java Code with Telugu Comments

```java
public class MergeKLists_BruteForce {
    public ListNode mergeKLists(ListNode[] lists) {
        List<Integer> values = new ArrayList<>();

        // 🔁 All values ni gather cheyyadam
        for (ListNode node : lists) {
            while (node != null) {
                values.add(node.val);
                node = node.next;
            }
        }

        // 🔃 Sort cheyyadam
        Collections.sort(values);

        // 🔧 New Linked List create cheyyadam
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        for (int val : values) {
            current.next = new ListNode(val);
            current = current.next;
        }

        return dummy.next;
    }
}
```

---

### ⏱ Time Complexity:

* `O(N log N)` due to sorting
* `N` = total number of nodes

### 📦 Space Complexity:

* `O(N)` to store all node values in array list

---

## 🏁 Final Summary Table

| Approach           | Time       | Space | Preferred When                        |
| ------------------ | ---------- | ----- | ------------------------------------- |
| ✅ Min-Heap         | O(N log k) | O(k)  | Most optimal & practical (interviews) |
| ✅ Divide & Conquer | O(N log k) | O(1)  | Elegant, scalable, merge-sort style   |
| ❌ Brute Force      | O(N log N) | O(N)  | Quick prototype or validation only    |

---

Would you like:

* Dry run of any one of these approaches?
* Java version using recursion for divide & conquer?
* Visual heap explanation?

Let me know, happy to help!
