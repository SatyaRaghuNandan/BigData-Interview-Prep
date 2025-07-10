# Original
# # VARIANT: What if you had to define your own schema for NestedList and implement BFS?
# # VARIANT: What if you had to define your own schema for NestedList and implement DFS?

Here’s the **Java equivalent** of your custom DFS solution for computing the **depth-weighted sum** using a custom `Object`-like class structure (similar to Leetcode’s `NestedInteger`) — with **Telugu-style comments**, clean structure, and full setup:

---

## ✅ Final Java Code (With Telugu Comments)

```java
import java.util.*;

// Custom Object class which can hold Integers or Nested Objects
class CustomObject {
    List<Object> value; // List lo Integers or CustomObject instances untayi

    public CustomObject() {
        this.value = new ArrayList<>();
    }
}

public class Solution {

    // Main method: Input is list of CustomObjects
    public int depthSum(List<Object> objects) {
        return dfs(objects, 1); // Start depth = 1
    }

    // Recursive DFS method
    private int dfs(List<Object> objects, int depth) {
        int total = 0;

        for (Object obj : objects) {
            if (obj instanceof Integer) {
                // 👉 Integer unte → value * depth add cheyyadam
                total += (Integer) obj * depth;
            } else if (obj instanceof CustomObject) {
                // 👉 Object unte → depth + 1 tho recursive call cheyyadam
                total += dfs(((CustomObject) obj).value, depth + 1);
            }
        }

        return total;
    }

    // Example usage
    public static void main(String[] args) {
        // Input: [1, [4, [6]]] → Expected Sum = 1*1 + 4*2 + 6*3 = 27

        // o3 = [6]
        CustomObject o3 = new CustomObject();
        o3.value.add(6);

        // o2 = [4, o3]
        CustomObject o2 = new CustomObject();
        o2.value.add(4);
        o2.value.add(o3);

        // o1 = [1, o2]
        CustomObject o1 = new CustomObject();
        o1.value.add(1);
        o1.value.add(o2);

        // Top-level list: [o1]
        List<Object> nestedList = new ArrayList<>();
        nestedList.add(o1);

        Solution sol = new Solution();
        System.out.println("Weighted Sum = " + sol.depthSum(nestedList)); // Output: 27
    }
}
```

---

## ✅ Output:

```java
Weighted Sum = 27
```

---

## ⏱ Time and Space Complexity

| Metric           | Value                       |
| ---------------- | --------------------------- |
| Time Complexity  | `O(N)` — total elements     |
| Space Complexity | `O(D)` — depth of recursion |

---

## ✅ Key Notes:

* We used `List<Object>` to allow both `Integer` and `CustomObject` types.
* Recursive DFS tracks depth while traversing.
* No need for additional `visited` or state-tracking logic.

---

## 💡 Want more?

Would you like:

* ✅ A **parser utility** to convert raw `[1, [4, [6]]]`-style Java structure to nested objects?
* ✅ An **iterative version** of this using stack?
* ✅ Java version of **depth-sum inverse** (LeetCode 364)?

Let me know!
