Absolutely! Let’s walk through a **happy path test case** for the optimized solution of **Subarray Sum Equals K**, step by step, like a **compiler or debugger**.

---

## ✅ Problem:

Find the **number of continuous subarrays** that **sum to `k`**.

---

## ✅ Code (for reference):

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int sum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1); // Handles subarrays starting at index 0

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];

            if (map.containsKey(sum - k)) {
                count += map.get(sum - k);
            }

            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }

        return count;
    }
}
```

---

## ✅ Happy Path Test Case:

```java
nums = [1, 2, 1, 3], k = 3
```

We are looking for the **number of subarrays** whose sum is exactly **3**.

---

## ✅ Step-by-Step Dry Run:

We'll track:

| Step | i | nums\[i] | sum | sum - k | map (before update)  | count | map (after update)        |
| ---- | - | -------- | --- | ------- | -------------------- | ----- | ------------------------- |
| 1    | 0 | 1        | 1   | -2      | {0=1}                | 0     | {0=1, 1=1}                |
| 2    | 1 | 2        | 3   | 0       | {0=1, 1=1}           | 1     | {0=1, 1=1, 3=1}           |
| 3    | 2 | 1        | 4   | 1       | {0=1, 1=1, 3=1}      | 2     | {0=1, 1=1, 3=1, 4=1}      |
| 4    | 3 | 3        | 7   | 4       | {0=1, 1=1, 3=1, 4=1} | 3     | {0=1, 1=1, 3=1, 4=1, 7=1} |

---

### 🔍 Walkthrough per iteration:

---

### 🔹 Step 1: `i = 0`

* `nums[0] = 1`
* `sum = 0 + 1 = 1`
* `sum - k = 1 - 3 = -2`
* `map.containsKey(-2)` → ❌ Not found
* No subarray found yet
* Update map: `map[1] = 1`

🧠 **State**:
`sum = 1`, `count = 0`, `map = {0=1, 1=1}`

---

### 🔹 Step 2: `i = 1`

* `nums[1] = 2`
* `sum = 1 + 2 = 3`
* `sum - k = 3 - 3 = 0`
* `map.containsKey(0)` → ✅ Yes! map\[0] = 1
  → Found 1 subarray ending here: `[1, 2]`
* Increment count: `count = 0 + 1 = 1`
* Update map: `map[3] = 1`

🧠 **State**:
`sum = 3`, `count = 1`, `map = {0=1, 1=1, 3=1}`

---

### 🔹 Step 3: `i = 2`

* `nums[2] = 1`
* `sum = 3 + 1 = 4`
* `sum - k = 4 - 3 = 1`
* `map.containsKey(1)` → ✅ Yes! map\[1] = 1
  → Found subarray ending here: `[2]` from prefix ending at index 0
* Increment count: `count = 1 + 1 = 2`
* Update map: `map[4] = 1`

🧠 **State**:
`sum = 4`, `count = 2`, `map = {0=1, 1=1, 3=1, 4=1}`

---

### 🔹 Step 4: `i = 3`

* `nums[3] = 3`
* `sum = 4 + 3 = 7`
* `sum - k = 7 - 3 = 4`
* `map.containsKey(4)` → ✅ Yes! map\[4] = 1
  → Found subarray ending here: `[3]` from prefix ending at index 2
* Increment count: `count = 2 + 1 = 3`
* Update map: `map[7] = 1`

🧠 **State**:
`sum = 7`, `count = 3`, `map = {0=1, 1=1, 3=1, 4=1, 7=1}`

---

## ✅ Final Result:

```java
count = 3
```

---

## ✅ Valid Subarrays:

1. `[1, 2]` → sum = 3
2. `[2, 1]` → sum = 3
3. `[3]`     → sum = 3

---

Let me know if you'd like:

* A **Java main method** to test this
* A **visual explanation**
* Or a **variation** like returning actual subarray indices!
