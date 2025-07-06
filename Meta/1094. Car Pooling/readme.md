

Great! You’ve implemented the **optimal solution** to Leetcode 1094 – **Car Pooling** using the **difference array technique (a.k.a. prefix sum delta method)**.

Let’s break it all down for easy memorization, detailed understanding, and interview readiness.

---

## 🧠 Problem Summary

> You're given `trips[][]` where each trip has:

* `trip[0] = numPassengers`
* `trip[1] = start location`
* `trip[2] = end location`

✅ Determine if you can **pick up and drop off passengers** without exceeding the vehicle capacity at **any time**.

---

## ✅ Java Code Explanation (Clean & Commented)

```java
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] stops = new int[1001]; // range constraint: 0 <= from, to <= 1000

        for (int[] trip : trips) {
            int numPassengers = trip[0];
            int from = trip[1];
            int to = trip[2];

            // Pickup: Add passengers at `from`
            stops[from] += numPassengers;

            // Drop-off: Remove passengers at `to`
            stops[to] -= numPassengers;
        }

        int currentPassengers = 0;
        for (int i = 0; i <= 1000; i++) {
            currentPassengers += stops[i]; // simulate flow

            // If at any point passengers exceed capacity, return false
            if (currentPassengers > capacity)
                return false;
        }

        return true; // All trips accommodated safely
    }
}
```

---

## 🧠 How to Remember This Trick

### 🔁 "Mark and Sweep with Difference Array"

1. **At `from` → add passengers**
2. **At `to` → subtract passengers**
3. **Sweep through all locations with prefix sum**

---

## ✅ Dry Run Example

```java
Trips = [[2,1,5], [3,3,7]]
Capacity = 4
```

### Step 1: Build `stops[1001]` (difference array)

```java
stops[1] += 2   // pickup 2 at 1
stops[5] -= 2   // drop 2 at 5

stops[3] += 3   // pickup 3 at 3
stops[7] -= 3   // drop 3 at 7
```

### Step 2: Sweep locations

```java
At i = 1: current = 2
At i = 2: current = 2
At i = 3: current = 5  ❌ > capacity → return false
```

✅ Perfectly captures real-time passenger count!

---

## ✅ Time and Space Complexity

| Metric    | Complexity             |
| --------- | ---------------------- |
| Time      | O(n + 1001) ≈ O(n)     |
| Space     | O(1001) = O(1)         |
| In-place? | ✅ Yes (no extra lists) |

> Efficient for constraints `0 ≤ trips.length ≤ 1000` and locations ≤ 1000

---

## ✅ Interview Takeaway

> “We model passenger changes as a difference array across locations, marking pickup and dropoff points. Then we simulate capacity usage using prefix sum. This avoids sorting or using extra data structures and gives an O(n) solution.”

---

## 🔁 Related Problems (Same Trick)

1. **Leetcode 253 – Meeting Rooms II**
2. **Leetcode 370 – Range Addition**
3. **Leetcode 1109 – Corporate Flight Bookings**
4. **Leetcode 1854 – Maximum Population Year**

All use similar **sweep-line or delta array patterns**.

---

Let me know if you want a **heap or line sweep** alternative approach too!
