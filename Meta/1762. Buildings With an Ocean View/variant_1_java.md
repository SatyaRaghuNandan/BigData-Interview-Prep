# // VARIANT: What if you had to return the number of buildings with an ocean view?

Let's **convert your C++ variant** of the **"Buildings With an Ocean View"** problem — where we return the **count** of such buildings — into **Java**, and then compare it to the **original problem**.

---

### ✅ Java Version: Count of Buildings with Ocean View

```java
public class SolutionVariant {

    public int findBuildingViewCount(int[] heights) {
        int n = heights.length;

        if (n == 0) return 0;

        // Last building ki ocean view untundhi
        int count = 1;

        // Right max height ni track cheyyadam
        int rightMax = heights[n - 1];

        // Right to left loop
        for (int i = n - 2; i >= 0; i--) {
            // height > rightMax ante ocean view possible
            if (heights[i] > rightMax) {
                count++;
                rightMax = heights[i];
            }
        }

        return count;
    }

    public static void main(String[] args) {
        SolutionVariant sol = new SolutionVariant();

        System.out.println(sol.findBuildingViewCount(new int[]{4, 2, 3, 1})); // 3
        System.out.println(sol.findBuildingViewCount(new int[]{6, 1, 2, 4, 2, 2, 2, 2, 3, 1})); // 4
        System.out.println(sol.findBuildingViewCount(new int[]{4, 3, 2, 1})); // 4
        System.out.println(sol.findBuildingViewCount(new int[]{1, 3, 2, 4})); // 1
        System.out.println(sol.findBuildingViewCount(new int[]{2, 2, 2, 2, 2, 2, 2})); // 1
        System.out.println(sol.findBuildingViewCount(new int[]{0, 1, 2, 3, 2, 1, 0})); // 4
        System.out.println(sol.findBuildingViewCount(new int[]{1, 2, 3, 4})); // 1
        System.out.println(sol.findBuildingViewCount(new int[]{10})); // 1
    }
}
```

---

### ✅ Key Differences: **Original vs Variant**

| Aspect              | Original Version (`List`)                         | Variant Version (`Count`)                            |
| ------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| **Return Type**     | `int[]` of building indices                       | `int` count of buildings with ocean view             |
| **Purpose**         | Find **which** buildings have the view            | Find **how many** buildings have the view            |
| **Logic**           | Add qualifying indices to a `List`, then reverse  | Increment `count` directly if condition is satisfied |
| **Post-processing** | Needs `reverse()` and `list.toArray()` conversion | No extra processing required                         |
| **Memory Usage**    | `O(K)` where K = qualifying buildings             | `O(1)` auxiliary memory                              |
| **Use Case**        | Needed when we care about **positions**           | Needed when we care only about **count/statistics**  |

---

### ✅ Time & Space Complexity

| Metric | Complexity   | Explanation                               |
| ------ | ------------ | ----------------------------------------- |
| Time   | `O(N)`       | Single reverse iteration over array       |
| Space  | `O(1)` extra | Only one counter and one max tracker used |

---

Let me know if you want a version where you **return both the count and the indices**, or visualize the buildings and ocean view with a 2D grid. 🌊🏢
