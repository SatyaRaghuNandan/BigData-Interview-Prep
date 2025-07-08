


Perfect! Let’s walk through **Leetcode 973 – K Closest Points to Origin** using the **same consistent structure** as your earlier requests (like 215 and 347), and include:

* ✅ **4 major approaches** (Sort, Max Heap, QuickSelect, Binary Search)
* ✅ Inline **Telugu-style comments** (in English script)
* ✅ **Time/Space Complexity Table**
* ✅ Recommendation on **when to use each**

---

## ✅ Problem Recap – Leetcode 973

> Given an array of points `[x, y]` on the 2D plane, return the `k` closest points to the origin `(0, 0)` using **Euclidean distance**.

---

## ✅ Time & Space Complexity Comparison

| Approach      | Time Complexity           | Space Complexity | Best Use Case                        |
| ------------- | ------------------------- | ---------------- | ------------------------------------ |
| Sort          | `O(N log N)`              | `O(1)`           | Simple, clear                        |
| Max Heap      | `O(N log K)`              | `O(K)`           | When `k` is small                    |
| Quick Select  | `O(N)` avg, `O(N²)` worst | `O(1)`           | Optimal average case                 |
| Binary Search | `O(N log D)`              | `O(N)`           | When precision/range questions arise |

---

## ✅ Approach 1: Sorting (Custom Comparator)

```java
public int[][] kClosest_sort(int[][] points, int k) {
    // ✅ Distance sort using squared Euclidean distance
    Arrays.sort(points, (a, b) -> squaredDist(a) - squaredDist(b));
    
    // ✅ Return first k closest points
    return Arrays.copyOf(points, k);
}

private int squaredDist(int[] point) {
    // Telugu: Distance formula ni simplify cheyyadam (no sqrt)
    return point[0] * point[0] + point[1] * point[1];
}
```

* ✅ Simple and easy to remember
* ❌ Not optimal for large `N`

---

## ✅ Approach 2: Max Heap (Priority Queue)

```java
public int[][] kClosest_heap(int[][] points, int k) {
    // ✅ Max heap comparator – farthest point first
    PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]);

    for (int i = 0; i < points.length; i++) {
        int dist = squaredDist(points[i]);
        maxHeap.add(new int[]{dist, i}); // [distance, index]
        
        if (maxHeap.size() > k) {
            maxHeap.poll(); // Telugu: Max size k undali, farthest ni remove cheyyali
        }
    }

    // ✅ Extract result from heap using stored indices
    int[][] result = new int[k][2];
    for (int i = 0; i < k; i++) {
        int index = maxHeap.poll()[1];
        result[i] = points[index];
    }

    return result;
}
```

* ✅ Works well when `k << N`
* ❌ Slower for very large `k`

---

## ✅ Approach 3: Quick Select (Optimized Average Case)

```java
public int[][] kClosest_quickSelect(int[][] points, int k) {
    quickSelect(points, 0, points.length - 1, k);
    return Arrays.copyOf(points, k);
}

private void quickSelect(int[][] points, int left, int right, int k) {
    while (left <= right) {
        int pivotIndex = partition(points, left, right);
        
        // Telugu: pivotIndex ante entha mandhi manaki left lo undho
        if (pivotIndex == k) return;
        else if (pivotIndex < k) left = pivotIndex;
        else right = pivotIndex - 1;
    }
}

private int partition(int[][] points, int left, int right) {
    int[] pivot = points[left + (right - left) / 2];
    int pivotDist = squaredDist(pivot);

    while (left < right) {
        if (squaredDist(points[left]) >= pivotDist) {
            // Swap with right
            int[] temp = points[left];
            points[left] = points[right];
            points[right] = temp;
            right--;
        } else {
            left++;
        }
    }

    if (squaredDist(points[left]) < pivotDist) left++;
    return left;
}

private int squaredDist(int[] point) {
    return point[0] * point[0] + point[1] * point[1];
}
```

* ✅ Very fast for large datasets
* ⚠️ Can be tricky to implement and debug
* ⚠️ Worst case `O(N²)` (rare)

---

## ✅ Approach 4: Binary Search on Distance (Advanced)

```java
public int[][] kClosest_binarySearch(int[][] points, int k) {
    double[] distances = new double[points.length];
    double low = 0, high = 0;
    List<Integer> remaining = new ArrayList<>();

    for (int i = 0; i < points.length; i++) {
        distances[i] = squaredDist(points[i]);
        high = Math.max(high, distances[i]);
        remaining.add(i);
    }

    List<Integer> closest = new ArrayList<>();
    while (k > 0) {
        double mid = (low + high) / 2;
        List<List<Integer>> split = splitDistances(remaining, distances, mid);

        List<Integer> closer = split.get(0), farther = split.get(1);
        if (closer.size() > k) {
            remaining = closer;
            high = mid;
        } else {
            k -= closer.size();
            closest.addAll(closer);
            remaining = farther;
            low = mid;
        }
    }

    int[][] result = new int[closest.size()][2];
    for (int i = 0; i < closest.size(); i++) {
        result[i] = points[closest.get(i)];
    }
    return result;
}

private List<List<Integer>> splitDistances(List<Integer> remaining, double[] distances, double mid) {
    List<Integer> closer = new ArrayList<>();
    List<Integer> farther = new ArrayList<>();
    for (int index : remaining) {
        if (distances[index] <= mid) closer.add(index);
        else farther.add(index);
    }
    return Arrays.asList(closer, farther);
}

private double squaredDist(int[] point) {
    return point[0] * point[0] + point[1] * point[1];
}
```

* ✅ Advanced and interview-worthy
* ✅ Binary search on numeric value range (not index!)
* ❌ Usually not needed unless precision is involved

---

## ✅ Summary Table

| Approach      | Time         | Space  | When to Use                           |
| ------------- | ------------ | ------ | ------------------------------------- |
| Sort          | `O(N log N)` | `O(1)` | Simple, easy                          |
| Max Heap      | `O(N log K)` | `O(K)` | When `k` is small                     |
| Quick Select  | `O(N)` avg   | `O(1)` | Optimal for large N, complex to debug |
| Binary Search | `O(N log D)` | `O(N)` | Range-based filtering, rarely needed  |

---

Would you like:

* 🧪 Dry-run of QuickSelect partitioning
* 📌 Top-K **farthest** points variant
* 💡 Explanation of `Arrays.copyOf()` vs manual array building

Let me know!
