Perfect! Here's the **Union-Find (Disjoint Set Union)** solution for **Leetcode 721 – Accounts Merge** in Java, with:

✅ **Clean modular structure**
✅ **Telugu-style comments**
✅ Proper **Union-Find (DSU)** implementation
✅ Time & Space complexity
✅ Output matches DFS solution

---

## ✅ Java Code: Union-Find Version with Telugu Comments

```java
import java.util.*;

public class AccountsMergeUnionFind {

    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, String> parent = new HashMap<>();  // ✅ email → parentEmail (DSU mapping)
        Map<String, String> emailToName = new HashMap<>(); // ✅ email → person name

        // ✅ Step 1: Initialize Union-Find structure
        for (List<String> account : accounts) {
            String name = account.get(0);
            String firstEmail = account.get(1);

            for (int i = 1; i < account.size(); i++) {
                String email = account.get(i);
                parent.putIfAbsent(email, email); // ✅ Email ki self parent assign cheyyadam
                union(parent, email, firstEmail); // ✅ First email tho union cheyyadam
                emailToName.put(email, name);     // ✅ Email ki name mapping cheyyadam
            }
        }

        // ✅ Step 2: Group emails by root parent
        Map<String, TreeSet<String>> unions = new HashMap<>(); // ✅ rootEmail → set of emails
        for (String email : parent.keySet()) {
            String root = find(parent, email);
            unions.computeIfAbsent(root, k -> new TreeSet<>()).add(email);
        }

        // ✅ Step 3: Final result prepare cheyyadam
        List<List<String>> merged = new ArrayList<>();
        for (String root : unions.keySet()) {
            List<String> group = new ArrayList<>();
            group.add(emailToName.get(root));  // ✅ Name ni front lo pettadam
            group.addAll(unions.get(root));    // ✅ Sorted email list add cheyyadam
            merged.add(group);
        }

        return merged;
    }

    // 🔸 DSU - Find operation with path compression
    private String find(Map<String, String> parent, String email) {
        if (!parent.get(email).equals(email)) {
            parent.put(email, find(parent, parent.get(email)));
        }
        return parent.get(email);
    }

    // 🔸 DSU - Union operation
    private void union(Map<String, String> parent, String a, String b) {
        String rootA = find(parent, a);
        String rootB = find(parent, b);
        if (!rootA.equals(rootB)) {
            parent.put(rootA, rootB); // ✅ rootA ni rootB ki attach cheyyadam
        }
    }

    // ✅ Test
    public static void main(String[] args) {
        AccountsMergeUnionFind sol = new AccountsMergeUnionFind();

        List<List<String>> input = List.of(
            List.of("John", "johnsmith@mail.com", "john_newyork@mail.com"),
            List.of("John", "johnsmith@mail.com", "john00@mail.com"),
            List.of("Mary", "mary@mail.com"),
            List.of("John", "johnnybravo@mail.com")
        );

        List<List<String>> result = sol.accountsMerge(input);
        for (List<String> account : result) {
            System.out.println(account);
        }
    }
}
```

---

## ✅ Output

```text
[John, john00@mail.com, john_newyork@mail.com, johnsmith@mail.com]
[Mary, mary@mail.com]
[John, johnnybravo@mail.com]
```

---

## ✅ Time & Space Complexity

Let:

* `N` = total number of accounts
* `E` = total number of unique emails
* `K` = avg. number of emails per account

| Step                      | Time                         |
| ------------------------- | ---------------------------- |
| Union-Find ops            | O(E \* α(E)) → nearly linear |
| Grouping & sorting        | O(E log E)                   |
| Final result construction | O(E)                         |
| ✅ Total                   | **O(E log E)**               |

| Step                         | Space |
| ---------------------------- | ----- |
| `parent`, `emailToName`      | O(E)  |
| `unions` (TreeSet per group) | O(E)  |

---

## 🧠 Summary (Meta-style)

> I use **Union-Find** to group emails into sets by their root parent.
> If two emails appear in the same account, they get **unioned** together.
> After all unions, I group emails by their **root representative**, and sort them for final output.

This solution is **more scalable** than DFS when merging massive datasets with thousands of emails.

---

Would you like:

* 🔁 Visual comparison: DFS vs Union-Find
* 🧪 JUnit test coverage
* ✂️ Support for email deduplication or sorting without TreeSet?

Let me know!
