Great question! Let’s update the **`findPeakElement()`** problem to handle **duplicates** in **Java**, including:

---

## ✅ Problem Recap (Leetcode 162 Variant)

> Given an array of integers `nums`, **return any peak element's index**.
> A peak element is one that is **greater than or equal to** its neighbors.
>
> 🆕 **Duplicates are allowed**, i.e., `nums[i] == nums[i+1]` is possible.

---

## ❗ Why Original Binary Search Fails with Duplicates

The classic Leetcode 162 binary search uses:

```java
if (nums[mid] > nums[mid + 1]) right = mid;
else left = mid + 1;
```

⚠️ This assumes `nums[i] != nums[i+1]`.

Example where this breaks:

```java
nums = [1, 2, 2, 2, 1];
```

* Flat plateau with a peak at `2`.
* Original binary search may skip the entire plateau and return wrong index.

---

# ✅ Approach 1: Modified Binary Search with Duplicates

### 🔧 Java Code with Telugu Comments

```java
public class PeakFinderWithDuplicates {

    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        // 🔁 Loop until left and right pointers meet
        while (left < right) {
            int mid = left + (right - left) / 2;

            // 🔼 Increasing slope → peak will be right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            }
            // 🔽 Decreasing slope → peak could be at mid or left side
            else if (nums[mid] > nums[mid + 1]) {
                right = mid;
            }
            // 🟰 Plateau situation → unsure, shrink window safely
            else {
                right--; // OR left++; both are acceptable
            }
        }

        return left; // OR return right
    }
}
```

---

## ✅ Approach 2: Linear Scan for All Peaks (Brute Force)

If interviewer wants **all peaks** or code simplicity is preferred:

```java
public List<Integer> findAllPeakElements(int[] nums) {
    List<Integer> peaks = new ArrayList<>();
    int n = nums.length;

    for (int i = 0; i < n; i++) {
        boolean leftOk = (i == 0 || nums[i] >= nums[i - 1]);
        boolean rightOk = (i == n - 1 || nums[i] >= nums[i + 1]);
        if (leftOk && rightOk) {
            peaks.add(i);
        }
    }

    return peaks;
}
```

🧪 Input: `[1, 2, 2, 2, 1]` → Output: `[1, 2, 3]`

---

## 📊 Time & Space Complexity Comparison

| Approach                    | Time                               | Space                    | Notes                           |
| --------------------------- | ---------------------------------- | ------------------------ | ------------------------------- |
| **Modified Binary Search**  | `O(log n)` average<br>`O(n)` worst | `O(1)`                   | Worst case when many duplicates |
| **Brute Force Linear Scan** | `O(n)`                             | `O(k)` for output        | Simple and clear                |
| **Find All Peaks**          | `O(n)`                             | `O(k)` for list of peaks | Use when all peaks are required |

---

## 🧠 Interview Talking Points

🎤 “If the array contains duplicates, traditional binary search logic breaks due to **plateaus**. So I use a modified binary search that safely shrinks the window by `right--` when encountering equality. This guarantees progress even when `nums[mid] == nums[mid+1]`, though in worst case it may degrade to linear time.”

---

## ✅ Behavior of Modified Binary Search

| Input             | Output (any valid index) |
| ----------------- | ------------------------ |
| `[1, 2, 3, 1]`    | 2                        |
| `[1, 2, 2, 2, 1]` | 1, 2, or 3               |
| `[5, 5, 5, 5]`    | any index (0–3)          |

---

## 🎯 Want More?

Let me know if you'd like:

* To **return all plateaus** (flat peak zones)
* Version for **2D matrix** peak finding (Leetcode 1901)
* Peak with **strict inequality** (no equal neighbors)

I'll happily extend this!
