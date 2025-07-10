


You're solving **Leetcode 986: Interval List Intersections** – a classic **two-pointer problem**.

---

## ✅ Problem Statement (Brief)

Given two lists of **disjoint sorted intervals** `A` and `B`, return their **intersection**, i.e., intervals that overlap in both.

---

## ✅ Approaches

### 🔸 Brute Force (Nested Loop) – `O(M * N)`

Compare every interval in `A` with every interval in `B`:

* Check if two intervals `[a1, a2]` and `[b1, b2]` overlap using:

  * `max(a1, b1) <= min(a2, b2)`
* If yes, record the intersection.

🚫 Inefficient for large inputs.

---

### ✅ Optimal Approach – **Two Pointers** `O(M + N)`

* Since both `A` and `B` are **sorted by start times**, use two pointers:

  * `i` for list A
  * `j` for list B
* At each step:

  1. Compute overlap using `lo = max(startA, startB)` and `hi = min(endA, endB)`
  2. If `lo <= hi`, add `[lo, hi]` to the result
  3. Move the pointer which has the **smaller end time**, since it **can't contribute to future intersections**

✅ Efficient and easy to dry run.

---

## ✅ Java Code with Telugu Comments

```java
class Solution {
  public int[][] intervalIntersection(int[][] A, int[][] B) {
    List<int[]> ans = new ArrayList<>(); // 🔹 Final Result list
    int i = 0, j = 0; // 🔹 Two Pointers for A and B

    while (i < A.length && j < B.length) {
      // 🔸 A[i] = [start1, end1], B[j] = [start2, end2]
      int startA = A[i][0], endA = A[i][1];
      int startB = B[j][0], endB = B[j][1];

      // ✅ Overlapping region start: max(startA, startB)
      // ✅ Overlapping region end: min(endA, endB)
      int lo = Math.max(startA, startB);
      int hi = Math.min(endA, endB);

      // 🔹 If lo <= hi → Valid overlap interval
      if (lo <= hi) {
        ans.add(new int[] {lo, hi});
      }

      // 🔹 Smaller interval finish ayindi ante, aa pointer ni move cheyyali
      if (endA < endB) {
        i++;
      } else {
        j++;
      }
    }

    // 🔚 Convert List<int[]> to 2D array
    return ans.toArray(new int[ans.size()][]);
  }
}
```

---

## 🧪 Test Cases and Dry Run

### ✅ Test Case 1: Overlapping Intervals

```java
A = [[1,3],[5,6],[7,9]]
B = [[2,5],[7,10]]
```

| A\[i]  | B\[j]   | Overlap      | Result    |
| ------ | ------- | ------------ | --------- |
| \[1,3] | \[2,5]  | \[2,3]       | ✔️ \[2,3] |
| \[5,6] | \[2,5]  | \[5,5]       | ✔️ \[5,5] |
| \[5,6] | \[7,10] | ❌ No overlap |           |
| \[7,9] | \[7,10] | \[7,9]       | ✔️ \[7,9] |

✅ Output: `[[2,3],[5,5],[7,9]]`

---

### ✅ Test Case 2: No Overlap

```java
A = [[1,2],[5,6]]
B = [[3,4],[7,8]]
```

❌ No overlap for any pair → Output: `[]`

---

### ✅ Test Case 3: One List Empty

```java
A = []
B = [[1,5]]
```

✅ Output: `[]`

---

### ✅ Test Case 4: Exact Match

```java
A = [[1,5]]
B = [[1,5]]
```

✅ Output: `[[1,5]]`

---

### ✅ Test Case 5: Full Containment

```java
A = [[1,10]]
B = [[2,3],[4,5],[6,7]]
```

✅ Output: `[[2,3],[4,5],[6,7]]`

---

### ✅ Test Case 6: Single Point Touch

```java
A = [[1,2],[5,6]]
B = [[2,3],[4,5]]
```

✅ Output: `[[2,2],[5,5]]`

---

## 🧠 Time & Space Complexity

| Complexity | Value    | Explanation                              |
| ---------- | -------- | ---------------------------------------- |
| Time       | O(M + N) | Each interval in A and B is visited once |
| Space      | O(K)     | K = number of intersections stored       |

---

## 🏁 Summary

| Approach      | Time     | Space | When to Use             |
| ------------- | -------- | ----- | ----------------------- |
| Brute Force   | O(M×N)   | O(1)  | Small inputs only       |
| ✅ Two-Pointer | ✅ O(M+N) | O(K)  | ✅ Best for sorted lists |

Let me know if you'd like a **Python version**, **variant with merged intervals**, or **visual diagram**!
