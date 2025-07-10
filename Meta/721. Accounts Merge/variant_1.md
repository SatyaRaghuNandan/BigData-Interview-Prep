# // VARIANT: What if you were given the input as a map from an ID to a list of corresponding emails?
# // Furthermore, you have to return a 2D list of all of the same IDs.

Thanks! This is a **graph variant of the Leetcode 721 - Accounts Merge** problem where:

### ✅ Problem Variant:

> You're given a map of:

```java
Map<String, List<String>> idToEmails
```

Each **ID** has a list of emails. If **two IDs share even one common email**, they're considered **the same person**.
Return groups of **same IDs** that belong to the same person.

---

### ✅ Java Version (DFS-based) with Full Explanation + Telugu Comments

```java
import java.util.*;

public class AccountIdMerge {

    // 🔹 DFS function: oka email ki sambandhinchina anni emails explore cheyyadam
    private void dfs(String currEmail,
                     Map<String, List<String>> adj,
                     Map<String, String> emailToId,
                     Set<String> visited,
                     String id) {

        visited.add(currEmail);            // ✅ Already visited ani mark cheyyadam
        emailToId.put(currEmail, id);      // ✅ Email ni id ki map cheyyadam

        for (String neighbor : adj.getOrDefault(currEmail, new ArrayList<>())) {
            if (!visited.contains(neighbor)) {
                dfs(neighbor, adj, emailToId, visited, id);
            }
        }
    }

    // 🔸 Main function
    public List<List<String>> mergeAccountsById(Map<String, List<String>> idToEmails) {
        Map<String, List<String>> adj = new HashMap<>();  // ✅ Graph: email ↔ email

        // ✅ Step 1: Build graph using bi-directional edges
        for (Map.Entry<String, List<String>> entry : idToEmails.entrySet()) {
            String id = entry.getKey();
            List<String> emails = entry.getValue();
            String base = emails.get(0);
            for (int i = 1; i < emails.size(); i++) {
                String email = emails.get(i);

                adj.computeIfAbsent(base, k -> new ArrayList<>()).add(email);
                adj.computeIfAbsent(email, k -> new ArrayList<>()).add(base);
            }
        }

        Map<String, String> emailToId = new HashMap<>();     // ✅ email → connected group id
        Set<String> visited = new HashSet<>();               // ✅ visited emails
        Map<String, List<String>> result = new HashMap<>();  // ✅ id → same ids group

        // ✅ Step 2: Traverse emails and group them by connected ID
        for (Map.Entry<String, List<String>> entry : idToEmails.entrySet()) {
            String id = entry.getKey();
            String firstEmail = entry.getValue().get(0);

            if (visited.contains(firstEmail)) {
                String existingId = emailToId.get(firstEmail);
                result.get(existingId).add(id);  // ✅ Already part of some group
            } else {
                result.put(id, new ArrayList<>());  // ✅ New group
                dfs(firstEmail, adj, emailToId, visited, id);
            }
        }

        // ✅ Step 3: Format output
        List<List<String>> output = new ArrayList<>();
        for (Map.Entry<String, List<String>> entry : result.entrySet()) {
            List<String> group = new ArrayList<>();
            group.add(entry.getKey());               // ✅ Main/root ID
            group.addAll(entry.getValue());          // ✅ Other same IDs
            output.add(group);
        }

        return output;
    }

    // ✅ Test
    public static void main(String[] args) {
        AccountIdMerge sol = new AccountIdMerge();

        Map<String, List<String>> input = new HashMap<>();
        input.put("A1", List.of("x@mail.com", "y@mail.com"));
        input.put("A2", List.of("y@mail.com", "z@mail.com"));
        input.put("A3", List.of("a@mail.com"));
        input.put("A4", List.of("a@mail.com", "b@mail.com"));
        input.put("A5", List.of("q@mail.com"));

        List<List<String>> result = sol.mergeAccountsById(input);
        for (List<String> group : result) {
            System.out.println(group);
        }
    }
}
```

---

## ✅ Sample Output:

```text
[A1, A2]
[A3, A4]
[A5]
```

---

## ✅ Time & Space Complexity

Let:

* `N` = number of IDs
* `E` = total number of emails
* `C` = total connections (edges)

### ⏱ Time Complexity:

| Step               | Time          |
| ------------------ | ------------- |
| Graph construction | O(N \* K)     |
| DFS traversal      | O(E + C)      |
| Result formatting  | O(N)          |
| ✅ Total            | **O(N \* K)** |

> `K` = average number of emails per ID

### 💾 Space Complexity:

| Structure        | Space        |
| ---------------- | ------------ |
| Graph (adj list) | O(E + C)     |
| Visited set      | O(E)         |
| emailToId map    | O(E)         |
| Result map       | O(N)         |
| ✅ Total          | **O(N + E)** |

---

## ✅ Which is Better?

| Approach       | Use Case                                     | Notes                          |
| -------------- | -------------------------------------------- | ------------------------------ |
| **DFS**        | Easy to implement, fits graph variant        | ✅ Good for small/medium graphs |
| **Union-Find** | Efficient for repeated merging               | ✅ Faster for large merges      |
| **Iteration**  | Not suitable here (requires graph traversal) | ❌ Complex and less intuitive   |

### 🧠 Verdict:

> Use **DFS or Union-Find**.
> For **simple connected component problems**, **DFS is intuitive**.
> For **heavy merging of disjoint sets**, go with **Union-Find**.

---

Would you like the **Union-Find version of this exact variant** (`id → emails` map as input)? Or a **visual walkthrough** of how the graph is built?
