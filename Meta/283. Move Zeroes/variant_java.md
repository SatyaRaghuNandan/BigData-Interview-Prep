# // VARIANT: What if you had to move zeroes to the front, not the back?

Here is the **Java version** of your C++ variant:

> ✅ Move **zeroes to the front** of the array, preserving the order of non-zero elements (at the back)

Also includes:

* ✅ Telugu-style comments
* ✅ Time & space complexity
* ✅ Dry-run behavior and correctness

---

## ✅ Java Code: `moveZeroesToFront`

```java
import java.util.*;

public class MoveZeroesToFront {

    public void moveZeroesToFront(int[] nums) {
        int swapIndex = nums.length - 1;

        // 🔁 Right to left iterate cheyyadam
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] != 0) {
                // ✅ non-zero element ni current swapIndex position ki swap cheyyadam
                int temp = nums[i];
                nums[i] = nums[swapIndex];
                nums[swapIndex] = temp;

                swapIndex--; // 🔁 next zero ki space reserve cheyyadam
            }
        }
    }
}
```

---

## ✅ Example Test in `main()`

```java
public class Main {
    public static void main(String[] args) {
        MoveZeroesToFront mover = new MoveZeroesToFront();

        int[] nums = {0, 1, 0, 3, 12, 0};
        mover.moveZeroesToFront(nums);
        System.out.println(Arrays.toString(nums)); // Output: [0, 0, 0, 1, 3, 12]

        nums = new int[]{1, 2, 3, 4, 5};
        mover.moveZeroesToFront(nums);
        System.out.println(Arrays.toString(nums)); // Output: [1, 2, 3, 4, 5]

        nums = new int[]{0, 0, 3, 4, 5};
        mover.moveZeroesToFront(nums);
        System.out.println(Arrays.toString(nums)); // Output: [0, 0, 3, 4, 5]
    }
}
```

---

## ✅ Dry Run: `[1, 0, 3, 0, 12]`

```text
Initial:      [1, 0, 3, 0, 12]
i = 4 → 12 swap with nums[4] → [1, 0, 3, 0, 12]
i = 3 → 0 → skip
i = 2 → 3 swap with nums[3] → [1, 0, 0, 3, 12]
i = 1 → 0 → skip
i = 0 → 1 swap with nums[1] → [0, 1, 0, 3, 12]
Final:        [0, 0, 1, 3, 12]
```

---

## ✅ Time & Space Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(n)  |
| Space Complexity | O(1)  |

---

## ✅ Summary

| Feature             | This Variant (`moveZeroesToFront`) | Classic `moveZeroesToEnd` |
| ------------------- | ---------------------------------- | ------------------------- |
| Traversal Direction | Right to Left                      | Left to Right             |
| Zero Placement      | Front                              | Back                      |
| Non-zero Order      | Preserved (at back)                | Preserved (at front)      |
| In-place?           | ✅ Yes                              | ✅ Yes                     |
| Time Complexity     | O(n)                               | O(n)                      |

---

Would you like a **stable version** that preserves the full original order of non-zero and zero elements, or a **functional programming** approach using Java streams (for learning)?
