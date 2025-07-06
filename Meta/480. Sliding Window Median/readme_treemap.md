## 🧭 LeetCode 480 – Sliding Window Median (TreeMap Java Version)

---

### ✅ Problem Summary
> You are given an integer array `nums` and an integer `k`. There is a sliding window of size `k` moving from the very left of the array to the very right. You need to return the median of each window.

---

### ✅ Java Code Using TreeMap
```java
import java.util.*;

public class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        TreeMap<Integer, Integer> left = new TreeMap<>(Collections.reverseOrder()); // max side
        TreeMap<Integer, Integer> right = new TreeMap<>(); // min side
        double[] result = new double[nums.length - k + 1];

        for (int i = 0; i < nums.length; i++) {
            addNum(left, right, nums[i]);
            balance(left, right);

            if (i >= k - 1) {
                result[i - k + 1] = getMedian(left, right, k);
                removeNum(left, right, nums[i - k + 1]);
                balance(left, right);
            }
        }
        return result;
    }

    private void addNum(TreeMap<Integer, Integer> left, TreeMap<Integer, Integer> right, int num) {
        if (left.isEmpty() || num <= left.firstKey()) {
            left.put(num, left.getOrDefault(num, 0) + 1);
        } else {
            right.put(num, right.getOrDefault(num, 0) + 1);
        }
    }

    private void removeNum(TreeMap<Integer, Integer> left, TreeMap<Integer, Integer> right, int num) {
        if (left.containsKey(num)) {
            decrement(left, num);
        } else {
            decrement(right, num);
        }
    }

    private void decrement(TreeMap<Integer, Integer> map, int key) {
        if (map.get(key) == 1) {
            map.remove(key);
        } else {
            map.put(key, map.get(key) - 1);
        }
    }

    private void balance(TreeMap<Integer, Integer> left, TreeMap<Integer, Integer> right) {
        while (size(left) > size(right) + 1) {
            int val = left.firstKey();
            decrement(left, val);
            right.put(val, right.getOrDefault(val, 0) + 1);
        }

        while (size(right) > size(left)) {
            int val = right.firstKey();
            decrement(right, val);
            left.put(val, left.getOrDefault(val, 0) + 1);
        }
    }

    private int size(TreeMap<Integer, Integer> map) {
        int size = 0;
        for (int freq : map.values()) size += freq;
        return size;
    }

    private double getMedian(TreeMap<Integer, Integer> left, TreeMap<Integer, Integer> right, int k) {
        if (k % 2 == 0) {
            return ((long) left.firstKey() + (long) right.firstKey()) / 2.0;
        } else {
            return (double) left.firstKey();
        }
    }
}
```

---

### ✅ Time and Space Complexity

| Operation        | Complexity                |
|------------------|---------------------------|
| `add/removeNum()`| `O(log k)` due to TreeMap |
| `balance()`      | `O(log k)`                |
| `getMedian()`    | `O(1)`                    |
| **Total**        | ✅ `O(n log k)`            |
| **Space**        | ✅ `O(k)` for TreeMaps     |

---

### ✅ Sample Test Case
```java
public static void main(String[] args) {
    Solution sol = new Solution();
    int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    System.out.println(Arrays.toString(sol.medianSlidingWindow(nums, k)));
    // Output: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
}
```

---

### 🧠 How to Remember This Approach

- Use **two TreeMaps**: max-side (`left`) and min-side (`right`).
- Always **balance sizes** (left can have 1 more).
- For **even window**, median is average of tops of both trees.
- For **odd window**, median is top of max-side.
- Use TreeMap to efficiently support `O(log k)` insert/delete/median queries.

---

Let me know if you'd like the **heap-based** comparison or edge-case coverage!
