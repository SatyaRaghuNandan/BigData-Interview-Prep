Here is the **Java version** of **Leetcode 398: Random Pick Index** using **Reservoir Sampling** — an efficient, **space-optimized solution** that doesn't store all the indices of the target number.

---

## ✅ Java Implementation (with Telugu-style comments)

```java
import java.util.Random;

public class Solution {
    private int[] nums;
    private Random rand;

    public Solution(int[] nums) {
        this.nums = nums;        // ✅ Input array ni store cheyyadam
        this.rand = new Random(); // ✅ Random number generator
    }

    public int pick(int target) {
        int count = 0;       // ✅ Target values count
        int result = -1;     // ✅ Picked index

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                count++; // Idi 'count-th' occurrence of target

                // ✅ 1/count chance to replace result
                if (rand.nextInt(count) == 0) {
                    result = i;
                }
            }
        }

        return result;
    }
}
```

---

## ✅ Example Usage

```java
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution(new int[]{1, 2, 3, 3, 3});

        // Repeated calls will randomly return one of the indices of 3 → [2, 3, 4]
        System.out.println(sol.pick(3));  // Example: 3
        System.out.println(sol.pick(3));  // Example: 2
        System.out.println(sol.pick(1));  // Always 0
    }
}
```

---

## ✅ Time and Space Complexity

| Operation      | Time   | Space  | Explanation                       |
| -------------- | ------ | ------ | --------------------------------- |
| Constructor    | `O(1)` | `O(1)` | Only stores input array           |
| `pick(target)` | `O(n)` | `O(1)` | One pass to randomly select index |

---

## ✅ How Reservoir Sampling Works

Every time we encounter a new instance of the `target`, we pick it with probability `1/count`, where `count` is the number of times we've seen the `target` so far. This ensures **each index** of the `target` has **equal probability** of being selected.

---

## ✅ Interview Summary

> "This approach uses **Reservoir Sampling** to pick a random index for the target without using extra space. For each match with `target`, I decide whether to replace the current choice based on probability `1/count`. This keeps space `O(1)` and works well for **large arrays** or **streaming data**."

---

Would you like me to include:

* ✅ Unit test class for this?
* ✅ Simulation to verify uniform distribution?
* ✅ Conversion to return **all indices** if needed?

Let me know!
