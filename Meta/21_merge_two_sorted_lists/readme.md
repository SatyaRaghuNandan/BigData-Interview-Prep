Here’s the **Java version** of your C++ code for merging two sorted linked lists (Leetcode 21):

---

## ✅ Java Code: `mergeTwoLists`

```java
public class MergeTwoSortedLists {

    // Definition for singly-linked list.
    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Dummy node create cheyyadam → merged list ni build cheyyadam kosam
        ListNode dummy = new ListNode(-1);
        ListNode curr = dummy;

        ListNode l1 = list1, l2 = list2;

        // Both lists ni scan cheyyadam until oka list aypoyedaka
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                curr.next = l1; // smaller value ni attach cheyyadam
                l1 = l1.next;    // move l1 forward
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }

        // Remaining nodes attach cheyyadam
        if (l1 != null) {
            curr.next = l1;
        } else {
            curr.next = l2;
        }

        // First node dummy kabatti, return dummy.next
        return dummy.next;
    }
}
```

---

## ✅ Time and Space Complexity

| Metric | Value    |
| ------ | -------- |
| Time   | O(n + m) |
| Space  | O(1)     |

* `n` = length of `list1`, `m` = length of `list2`
* Only one new dummy node is used — no extra space apart from pointers

---

## ✅ Sample Usage

```java
public static void main(String[] args) {
    MergeTwoSortedLists merge = new MergeTwoSortedLists();

    ListNode l1 = new ListNode(1, new ListNode(3, new ListNode(5)));
    ListNode l2 = new ListNode(2, new ListNode(4, new ListNode(6)));

    ListNode result = merge.mergeTwoLists(l1, l2);

    // Print the merged list
    while (result != null) {
        System.out.print(result.val + " ");
        result = result.next;
    }
}
```

---

Would you like the **recursive version** of this as well (often asked in follow-ups)?



Great! Here's the **recursive version** of the solution to **merge two sorted linked lists** (Leetcode 21), using **Java**, with:

✅ Clean structure
✅ Telugu-style comments
✅ Time & space complexity

---

## ✅ Recursive Java Solution

```java
public class MergeTwoSortedListsRecursive {

    // Definition for singly-linked list.
    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    // ✅ Recursive solution
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // 🛑 Base Case 1: list1 empty aithe → return list2
        if (list1 == null) return list2;

        // 🛑 Base Case 2: list2 empty aithe → return list1
        if (list2 == null) return list1;

        // ✅ Choose smaller node and recurse
        if (list1.val <= list2.val) {
            list1.next = mergeTwoLists(list1.next, list2); // list1 pick chesi, next ni recurse cheyyadam
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next); // list2 pick chesi, next ni recurse cheyyadam
            return list2;
        }
    }
}
```

---

## ✅ Time & Space Complexity

| Metric             | Value    |
| ------------------ | -------- |
| Time               | O(n + m) |
| Space (Call stack) | O(n + m) |

* Time is same as iterative: traverses all nodes.
* But recursion uses **stack frames** for each node, which adds **O(n + m)** space (for balanced merges).

---

## ✅ Interview Tip (How to Explain):

> “In the recursive solution, I compare the heads of both lists and recursively build the merged list by picking the smaller value each time. The recursion naturally handles the traversal and pointer linking. Base case handles empty lists. While it's clean and elegant, the space complexity is higher due to the recursive stack.”

---

Would you like to also explore:

* ✅ Merging **K sorted lists** (Leetcode 23)?
* ✅ Recursive + Memoized version (for more than 2 lists)?

