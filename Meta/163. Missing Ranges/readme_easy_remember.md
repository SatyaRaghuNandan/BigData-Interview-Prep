Great! Let’s convert both versions of the **Missing Ranges** problem into **Java** and highlight **how to remember and differentiate them**.

---

## ✅ PROBLEM 1: Original Version

**Return ranges as `List<List<Integer>>`**
Format: `[[3, 4], [7, 8], [10, 12]]`

### ✅ Java Code

```java
public class MissingRangesOriginal {

    public List<List<Integer>> findMissingRanges(int[] nums, int lower, int upper) {
        List<List<Integer>> result = new ArrayList<>();

        if (nums.length == 0) {
            result.add(Arrays.asList(lower, upper));
            return result;
        }

        // Before first element
        if (lower < nums[0]) {
            result.add(Arrays.asList(lower, nums[0] - 1));
        }

        // Between elements
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] - nums[i - 1] > 1) {
                result.add(Arrays.asList(nums[i - 1] + 1, nums[i] - 1));
            }
        }

        // After last element
        if (upper > nums[nums.length - 1]) {
            result.add(Arrays.asList(nums[nums.length - 1] + 1, upper));
        }

        return result;
    }
}
```

---

## ✅ PROBLEM 2: Variant Version

**Return ranges as `List<String>` using 3 formatting rules**

* `"5"` if only one number
* `"5", "6"` if two consecutive
* `"5-8"` if three or more missing

### ✅ Java Code

```java
public class MissingRangesVariant {

    public List<String> findMissingRangesVariant(int[] nums, int lower, int upper) {
        List<String> result = new ArrayList<>();
        long prev = (long) lower - 1;  // use long to avoid overflow
        int i = 0;

        while (i <= nums.length) {
            long curr = (i < nums.length) ? nums[i] : (long) upper + 1;

            if (curr - prev >= 2) {
                long start = prev + 1;
                long end = curr - 1;

                if (start == end) {
                    result.add(String.valueOf(start));
                } else if (end == start + 1) {
                    result.add(String.valueOf(start));
                    result.add(String.valueOf(end));
                } else {
                    result.add(start + "-" + end);
                }
            }

            prev = curr;
            i++;
        }

        return result;
    }
}
```

---

## 🧠 HOW TO REMEMBER BOTH?

| Feature            | Original Version                  | Variant Version (Formatted)                   |
| ------------------ | --------------------------------- | --------------------------------------------- |
| **Return Type**    | `List<List<Integer>>`             | `List<String>`                                |
| **Edge Handling**  | Lower edge, upper edge explicitly | Append sentinel `upper+1` to simplify logic   |
| **Format**         | Always return `[start, end]`      | Format depends on range length                |
| **Loop Logic**     | Use `nums[i] - nums[i-1] > 1`     | Use `curr - prev >= 2` and format accordingly |
| **Overflow-safe?** | Not always                        | Yes (`long` is used to avoid overflow)        |
| **Usage**          | Range-based filtering             | Display or reporting with string formatting   |

---

## 🧠 MEMORY HOOKS

### 🔹 Original:

* Think **"raw numbers"**: just return the gaps as start-end pairs.
* Handle three parts:
  `before`, `between`, `after`.

### 🔹 Variant:

* Think **"formatting based on length of the gap"**:

  * `1 missing` → `"x"`
  * `2 missing` → `"x", "x+1"`
  * `≥3 missing` → `"x-y"`

Use sentinel trick `upper + 1` to finish loop in one pass.

---

## 🧪 Example Dry Run

```java
int[] nums = {2, 5, 8};
int lower = 1, upper = 10;
```

**Original Output:**

```
[[1,1], [3,4], [6,7], [9,10]]
```

**Variant Output:**

```
"1", "3-4", "6-7", "9-10"
```

---

Would you like me to generate test methods for both in Java as well?
