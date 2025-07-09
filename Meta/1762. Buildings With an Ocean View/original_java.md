Sure! Let's convert your **Python solution for Leetcode 1762: Buildings With an Ocean View** into **Java**, along with:

1. ✅ **Java Version**
2. ✅ **Telugu-style Comments**
3. ✅ **Test Cases**
4. ✅ **Dry Run Example** (`[4,2,3,1]`)
5. ✅ **Time & Space Complexity**

---

## ✅ Java Version with Telugu Comments

```java
import java.util.*;

public class Solution {
    public int[] findBuildings(int[] heights) {
        int n = heights.length;
        List<Integer> result = new ArrayList<>();
        
        // Last building ki ocean view untundhi, add cheddam
        result.add(n - 1);
        
        // Right lo ekkada ocean view ni block cheyyadam ledu, so last building is max
        int rightMax = heights[n - 1];

        // Right to Left loop
        for (int i = n - 2; i >= 0; i--) {
            // Current building height > rightMax ante, ocean view possible
            if (heights[i] > rightMax) {
                result.add(i); // Index ni add cheyyadam
                rightMax = heights[i]; // rightMax ni update cheyyadam
            }
        }

        // Indices ascending order lo undali, kabatti reverse cheyyadam
        Collections.reverse(result);

        // List ni array lo convert cheyyadam
        return result.stream().mapToInt(i -> i).toArray();
    }
}
```

---

## ✅ Test Cases with Explanation

```java
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] testCases = {
            {4, 2, 3, 1},     // ➜ [0, 2, 3]
            {1, 3, 2, 4},     // ➜ [3]
            {2, 2, 2, 2},     // ➜ [3]
            {1, 2, 3, 4},     // ➜ [3]
            {4, 3, 2, 1},     // ➜ [0, 1, 2, 3]
            {5}               // ➜ [0]
        };

        for (int[] heights : testCases) {
            System.out.println("Input: " + Arrays.toString(heights));
            System.out.println("Ocean View Buildings: " + Arrays.toString(sol.findBuildings(heights)));
            System.out.println("----");
        }
    }
}
```

---

## ✅ Dry Run Example: `[4, 2, 3, 1]`

| i           | heights\[i] | rightMax | heights\[i] > rightMax? | result     |
| ----------- | ----------- | -------- | ----------------------- | ---------- |
| 3           | 1           | 1        | ❌ (1 not > 1)           | \[3]       |
| 2           | 3           | 1        | ✅                       | \[3, 2]    |
| 1           | 2           | 3        | ❌                       | \[3, 2]    |
| 0           | 4           | 3        | ✅                       | \[3, 2, 0] |
| **reverse** |             |          | ➜ \[0, 2, 3]            |            |

---

## ✅ Time & Space Complexity

| Metric           | Complexity   | Explanation                               |
| ---------------- | ------------ | ----------------------------------------- |
| Time Complexity  | `O(N)`       | One backward pass and a reverse operation |
| Space Complexity | `O(1)` extra | Output list is not counted as extra       |

---

Let me know if you want:

* A **graphical grid simulation**
* This code as a **JUnit test**
* Or to handle **2D building heights or variants**

Happy practicing! 🌊🏢
