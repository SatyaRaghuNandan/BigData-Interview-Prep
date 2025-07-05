Absolutely! Here's a **cleaner, structured, and Markdown-friendly format** for your notes or documentation file — ideal for interview prep or uploading to GitHub or Notion.

---

# 🧠 Binary Search on Answer – Java Solutions (Meta Interview Prep)

---

## ✅ 1011. Capacity To Ship Packages Within D Days

### 📌 Problem Summary

> Given weights of packages and a number of days `D`, find the **minimum ship capacity** such that all packages can be shipped in `D` days. You must ship packages in order.

---

### 💡 Approach

* Binary search on capacity: search range is `[max(weights), sum(weights)]`
* For each mid value (guessed capacity), check if we can ship within `D` days
* Use greedy check to simulate the days needed

---

### ✅ Java Code

```java
class ShipPackages {
    public int shipWithinDays(int[] weights, int D) {
        int left = Arrays.stream(weights).max().getAsInt();
        int right = Arrays.stream(weights).sum();

        while (left < right) {
            int mid = (left + right) / 2;
            if (canShip(weights, D, mid)) right = mid;
            else left = mid + 1;
        }
        return left;
    }

    private boolean canShip(int[] weights, int D, int capacity) {
        int days = 1, total = 0;
        for (int w : weights) {
            total += w;
            if (total > capacity) {
                days++;
                total = w;
                if (days > D) return false;
            }
        }
        return true;
    }
}
```

---

### 🧪 Test Cases

```java
shipWithinDays([1,2,3,1,1], 4) ➞ 3  
shipWithinDays([3,2,2,4,1,4], 3) ➞ 6  
```

---

### ⏱️ Time & Space Complexity

| Metric | Value            |
| ------ | ---------------- |
| Time   | O(N \* log(S))   |
| Space  | O(1)             |
| Notes  | S = sum(weights) |

---

## ✅ 875. Koko Eating Bananas

### 📌 Problem Summary

> Koko can eat at a fixed speed (bananas/hour). Given piles of bananas and `H` hours, find the **minimum eating speed** required to finish all bananas in time.

---

### 💡 Approach

* Binary search over speed from `[1, max(piles)]`
* For each speed, check if total eating time ≤ H
* Use `Math.ceil(pile / speed)` to compute hours per pile

---

### ✅ Java Code

```java
class KokoBananas {
    public int minEatingSpeed(int[] piles, int H) {
        int left = 1, right = Arrays.stream(piles).max().getAsInt();
        while (left < right) {
            int mid = (left + right) / 2;
            if (canFinish(piles, H, mid)) right = mid;
            else left = mid + 1;
        }
        return left;
    }

    private boolean canFinish(int[] piles, int H, int speed) {
        int hours = 0;
        for (int pile : piles)
            hours += (pile + speed - 1) / speed;
        return hours <= H;
    }
}
```

---

### 🧪 Test Cases

```java
minEatingSpeed([3,6,7,11], 8) ➞ 4  
minEatingSpeed([30,11,23,4,20], 5) ➞ 30  
```

---

### ⏱️ Time & Space Complexity

| Metric | Value          |
| ------ | -------------- |
| Time   | O(N \* log M)  |
| Space  | O(1)           |
| Notes  | M = max(piles) |

---

## ✅ 1482. Minimum Days to Make m Bouquets

### 📌 Problem Summary

> Given `bloomDay[]`, find the **minimum day** such that you can make `m` bouquets using `k` consecutive flowers each.

---

### 💡 Approach

* Binary search on day in `[min(bloomDay), max(bloomDay)]`
* On each guess, check how many bouquets can be made with that day as limit
* Reset count if you hit an unbloomed flower

---

### ✅ Java Code

```java
class MinimumDaysBouquets {
    public int minDays(int[] bloomDay, int m, int k) {
        if ((long) m * k > bloomDay.length) return -1;
        int left = Arrays.stream(bloomDay).min().getAsInt();
        int right = Arrays.stream(bloomDay).max().getAsInt();

        while (left < right) {
            int mid = (left + right) / 2;
            if (canMake(bloomDay, m, k, mid)) right = mid;
            else left = mid + 1;
        }
        return left;
    }

    private boolean canMake(int[] bloomDay, int m, int k, int days) {
        int count = 0, bouquets = 0;
        for (int bloom : bloomDay) {
            if (bloom <= days) {
                count++;
                if (count == k) {
                    bouquets++;
                    count = 0;
                }
            } else {
                count = 0;
            }
        }
        return bouquets >= m;
    }
}
```

---

### 🧪 Test Cases

```java
minDays([1,10,3,10,2], m=3, k=1) ➞ 3  
minDays([1,10,3,10,2], m=3, k=2) ➞ -1  
```

---

### ⏱️ Time & Space Complexity

| Metric | Value             |
| ------ | ----------------- |
| Time   | O(N \* log R)     |
| Space  | O(1)              |
| Notes  | R = range of days |

---

## ✅ 1891. Cutting Ribbons

### 📌 Problem Summary

> You are given ribbons and want to cut them into equal lengths. Find the **maximum length** such that you get at least `k` pieces.

---

### 💡 Approach

* Binary search on length from `[1, max(ribbons)]`
* Check how many pieces can be formed with current length guess
* Maximize result when feasible

---

### ✅ Java Code

```java
class CuttingRibbons {
    public int maxLength(int[] ribbons, int k) {
        int left = 1, right = Arrays.stream(ribbons).max().getAsInt(), res = 0;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (canCut(ribbons, k, mid)) {
                res = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
    }

    private boolean canCut(int[] ribbons, int k, int length) {
        int count = 0;
        for (int r : ribbons) count += r / length;
        return count >= k;
    }
}
```

---

### 🧪 Test Cases

```java
maxLength([9,7,5], k=3) ➞ 5  
maxLength([7,5,9], k=4) ➞ 4  
```

---

### ⏱️ Time & Space Complexity

| Metric | Value          |
| ------ | -------------- |
| Time   | O(N \* log M)  |
| Space  | O(1)           |
| Notes  | M = max ribbon |

---

## ✅ Summary Table

| Problem               | Search Range           | Feasibility Function               |
| --------------------- | ---------------------- | ---------------------------------- |
| 1011. Ship Packages   | `[max, sum]`           | Can ship in D days                 |
| 875. Koko Bananas     | `[1, max pile]`        | Can eat in H hours                 |
| 1482. Bouquets        | \`\[min, max] bloomDay | Can make m bouquets of size k      |
| 1891. Cutting Ribbons | `[1, max ribbon]`      | Can cut ≥ k pieces of given length |

---

Let me know if you want this exported to `.md`, GitHub README-style layout, or paired with visual diagrams/dry runs!
