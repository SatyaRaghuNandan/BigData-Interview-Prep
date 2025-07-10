# // VARIANT: What if you had to return all of the buildings that either have an ocean view
# // to its left and/or its right? This becomes very similar to Leetcode 42 Trapping Rain Water

Great! You're now exploring a **more advanced variant** of the **"Buildings With Ocean View"** problem.

---

### ✅ Problem Statement (Variant):

> Return all the building indices that have a view **either to the left or right**, i.e., a building is **not blocked by a taller building on at least one side**.

This is similar to **Leetcode 42 (Trapping Rain Water)** where we track max from left and right. You're combining a two-pointer approach to simulate this efficiently.

---

## ✅ Java Version of the Second Variant

```java
import java.util.*;

public class SolutionVariantTwo {

    public List<Integer> findBuildingsWithLeftOrRightView(int[] heights) {
        int n = heights.length;

        if (n == 1) return List.of(0);

        List<Integer> leftView = new ArrayList<>();
        List<Integer> rightView = new ArrayList<>();

        int left = 0, right = n - 1;
        int leftMax = heights[left];
        int rightMax = heights[right];

        leftView.add(left);
        rightView.add(right);

        while (left < right) {
            if (leftMax < rightMax) {
                left++;
                if (heights[left] > leftMax && left < right) {
                    leftView.add(left);
                    leftMax = heights[left];
                }
            } else {
                right--;
                if (heights[right] > rightMax && left < right) {
                    rightView.add(right);
                    rightMax = heights[right];
                }
            }
        }

        // Merge both lists: leftView + reverse(rightView)
        List<Integer> result = new ArrayList<>(leftView);
        Collections.reverse(rightView);
        result.addAll(rightView);
        return result;
    }

    public static void main(String[] args) {
        SolutionVariantTwo sol = new SolutionVariantTwo();

        int[][] tests = {
            {1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 2},
            {1, 2, 3, 3, 2, 1},
            {1, 4, 3, 9, 8, 6},
            {1, 2, 1, 1, 3, 1, 1, 3, 1, 3, 2, 1},
            {1, 1, 1, 1},
            {5},
            {1, 10}
        };

        for (int[] heights : tests) {
            System.out.println("Heights: " + Arrays.toString(heights));
            List<Integer> result = sol.findBuildingsWithLeftOrRightView(heights);
            System.out.println("Buildings with Left/Right Ocean View: " + result);
            System.out.println("Count: " + result.size());
            System.out.println("----");
        }
    }
}
```

---

## ✅ Key Differences vs Original Problem

| Feature                    | Original Problem (`Leetcode 1762`)   | This Variant (Left or Right View)                         |
| -------------------------- | ------------------------------------ | --------------------------------------------------------- |
| **View Direction**         | Only Right side (Ocean to the right) | Either Left **or** Right side (similar to trapping peaks) |
| **Approach**               | Backward traversal (one pass)        | Two-pointer: max from both ends                           |
| **Space Used**             | O(K) for result                      | O(K) for leftView + rightView                             |
| **When is view possible?** | If no taller building on the right   | If no taller building on **at least one side**            |
| **Reversal Needed?**       | Yes, for final answer                | Yes, reverse rightView before merging                     |

---

## ✅ Time & Space Complexity

| Metric | Complexity | Explanation                              |
| ------ | ---------- | ---------------------------------------- |
| Time   | `O(N)`     | Single pass with two pointers            |
| Space  | `O(K)`     | For result list (depends on output size) |

---

Let me know if you want a visualization for how left-max and right-max are updated — or if you want to **combine this logic with trapping rain water** detection for height valleys! 🌊🏢
