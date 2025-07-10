Here’s the **Java version** of your `moveZeroes` Python code, with:

✅ Clean code structure
💬 Telugu-style comments
📊 Time and Space complexity

---

## ✅ Java Code: `moveZeroes`

```java
public class MoveZeroes {

    // Function to move all 0s to the end while maintaining the order of non-zero elements
    public void moveZeroes(int[] nums) {
        int swapIndex = 0; // 🟢 non-zero element ni ekkada petali ani track cheyyadam

        // 🔁 Entire array lo loop cheyyadam
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                // ✅ Non-zero element unte, current position (i) ni swap cheyyadam with swapIndex
                int temp = nums[i];
                nums[i] = nums[swapIndex];
                nums[swapIndex] = temp;

                swapIndex++; // 🔁 Next non-zero ki position move cheyyadam
            }
        }
    }
}
```

---

## ✅ Example Test in `main()`

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        MoveZeroes mover = new MoveZeroes();
        int[] nums = {0, 1, 0, 3, 12};

        mover.moveZeroes(nums);
        System.out.println(Arrays.toString(nums)); // Output: [1, 3, 12, 0, 0]
    }
}
```

---

## 📊 Time & Space Complexity

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(n)  |
| Space Complexity | O(1)  |

* Each element is visited exactly once
* In-place rearrangement, no extra space used

---

## ✅ Interview Tip (How to Explain):

> “I maintain a `swapIndex` pointer to track where the next non-zero should go. Every time I see a non-zero, I swap it to `swapIndex` and move the pointer. This preserves the order of non-zero elements and pushes all zeroes to the end. Time complexity is O(n), space is O(1), done in-place.”

---

Would you like a version that preserves relative order but **minimizes swaps** (only swap when `i != swapIndex`)?
