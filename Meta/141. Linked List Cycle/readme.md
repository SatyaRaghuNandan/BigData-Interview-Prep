Great! You're working on the **Linked List Cycle Detection** problem using **Floyd’s Tortoise and Hare Algorithm** — an efficient and widely used method to detect cycles in a linked list.

Let’s break it down completely:

---

## ✅ Problem

> Given the `head` of a singly linked list, determine if the list has a **cycle**.

---

## ✅ Java Code with Detailed Comments

```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
class Solution {
    public boolean hasCycle(ListNode head) {
        // ✅ Base case: If list is empty or has only one node, cycle is impossible
        if (head == null || head.next == null) {
            return false;
        }

        // ✅ Two pointers — slow moves 1 step, fast moves 2 steps
        ListNode slow = head;
        ListNode fast = head;

        // 🔁 Keep traversing while fast and fast.next are not null
        while (fast != null && fast.next != null) {
            slow = slow.next;           // Move slow one step
            fast = fast.next.next;      // Move fast two steps

            if (slow == fast) {
                // ✅ Cycle detected — both pointers met inside the loop
                return true;
            }
        }

        // ❌ If fast reaches end, no cycle
        return false;
    }
}
```

---

## ✅ Time & Space Complexity

| Metric              | Value  | Reasoning                                     |
| ------------------- | ------ | --------------------------------------------- |
| ⏱ Time Complexity   | `O(N)` | Worst-case each node visited at most twice    |
| 🧠 Space Complexity | `O(1)` | Constant space; no extra data structures used |

✅ Very efficient for large linked lists!

---

## ✅ Code Walkthrough

Let’s simulate this example:

### Linked List:

```
1 → 2 → 3 → 4 → 5
          ↑     ↓
          ← ← ←
```

* `head = 1`
* Cycle: `5.next = 3`

### Step-by-Step Execution:

| Step | slow | fast | Notes                        |
| ---- | ---- | ---- | ---------------------------- |
| 1    | 2    | 3    | fast = 1 → 3                 |
| 2    | 3    | 5    | fast = 3 → 5                 |
| 3    | 4    | 4    | fast = 5 → 3 → 4 ✅ MATCH     |
|      |      |      | Cycle detected — return true |

---

## ✅ Edge Cases and Test Cases

| Test Case Description          | Input                           | Expected Output |
| ------------------------------ | ------------------------------- | --------------- |
| 🔹 Empty List                  | `head = null`                   | `false`         |
| 🔹 Single Node (no cycle)      | `head = [1]`                    | `false`         |
| 🔹 Two Nodes (no cycle)        | `1 → 2 → null`                  | `false`         |
| 🔹 Two Nodes (with cycle)      | `1 → 2 → 1 (cycle)`             | `true`          |
| 🔹 Multiple Nodes (no cycle)   | `1 → 2 → 3 → 4 → null`          | `false`         |
| 🔹 Multiple Nodes (with cycle) | `1 → 2 → 3 → 4 → 5 → 3 (cycle)` | `true`          |
| 🔹 Tail connects to head       | `1 → 2 → 3 → 4 → 1 (cycle)`     | `true`          |

---

## ✅ Interview-Ready Summary

> “To detect a cycle in a linked list, I used **Floyd’s Cycle Detection Algorithm** (Tortoise and Hare). It uses two pointers: slow (1 step) and fast (2 steps). If a cycle exists, they will eventually meet. If fast reaches the end (`null`), no cycle exists. This runs in `O(N)` time and uses `O(1)` space — optimal for this problem.”

---

Would you like:

* ✅ Code to **return the node** where the cycle begins?
* ✅ Visual simulation with ASCII animation?
* ✅ Conversion to detect cycles in **graphs** instead?

Let me know how you’d like to go deeper!
