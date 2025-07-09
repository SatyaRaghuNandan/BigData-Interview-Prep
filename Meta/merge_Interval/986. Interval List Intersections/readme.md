





This code solves the **Interval Intersection** problem — a classic two-pointer pattern.

---

## ✅ Problem Statement (Leetcode 986 - Interval List Intersections)

Given two lists of **disjoint** and **sorted** intervals `A` and `B`, return the intersection of these two interval lists.

---

## ✅ Approach Explained (Two Pointers)

### 🔧 Core Idea:

You're walking through both lists at the same time, comparing intervals to see if they **overlap**, and advancing the pointer that ends earlier.

---

### ✅ Step-by-Step with Telugu-style Comments:

```java
class Solution {
  public int[][] intervalIntersection(int[][] A, int[][] B) {
    List<int[]> ans = new ArrayList<>();
    int i = 0, j = 0;

    while (i < A.length && j < B.length) {

      // A[i] = [a1, a2], B[j] = [b1, b2]
      // Overlap occurs between max(a1, b1) and min(a2, b2)
      int lo = Math.max(A[i][0], B[j][0]); // Telugu: Renditiki start ekkada overlap avvachho
      int hi = Math.min(A[i][1], B[j][1]); // Telugu: Renditiki end ekkada overlap avvachho

      // Valid intersection unte lo <= hi untundi
      if (lo <= hi)
        ans.add(new int[]{lo, hi}); // Add this overlapping interval

      // End ekkuvaga undedi move cheyyali to avoid missing future overlaps
      if (A[i][1] < B[j][1]) {
        i++; // A lo interval complete ayindi, move to next
      } else {
        j++; // B lo interval complete ayindi, move to next
      }
    }

    return ans.toArray(new int[ans.size()][]);
  }
}
```

---

## ✅ Dry Run Example

### Input:

```java
A = [[1, 3], [5, 6], [7, 9]]
B = [[2, 5], [7, 8]]
```

### Steps:

1. Compare \[1,3] and \[2,5] → Intersection = \[2,3]
2. \[5,6] and \[2,5] → Intersection = \[5,5]
3. \[5,6] and \[7,8] → No overlap
4. \[7,9] and \[7,8] → Intersection = \[7,8]

✅ Output:

```java
[[2,3], [5,5], [7,8]]
```

---

## ✅ Time and Space Complexity

| Metric | Value                                        |
| ------ | -------------------------------------------- |
| Time   | `O(m + n)`                                   |
| Space  | `O(k)` (for result list, worst case `m + n`) |

Where `m` = length of A, `n` = length of B, and `k` = number of overlapping intervals.

---

Let me know if you'd like this in Python, dry run visuals, or a variant like merge union of intervals.
