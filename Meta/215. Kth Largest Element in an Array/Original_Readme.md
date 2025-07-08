Great! You're solving **Leetcode 215 – Find Kth Largest Element in an Array**, a classic and **frequent interview question**.

---

## ✅ Problem Recap

> Given an integer array `nums` and an integer `k`, return the **k-th largest element** in the array.

📝 Note: The answer is **not the K-th distinct** element, just the one at position `k` in the **sorted (descending)** array.

---

## ✅ 3 Most Common Approaches:

| Approach         | Time Complexity | Space Complexity | Use Case / Suitability           |
| ---------------- | --------------- | ---------------- | -------------------------------- |
| 1. Sorting       | `O(N log N)`    | `O(1)` or `O(N)` | Simplest, but not optimal        |
| 2. Min Heap (PQ) | `O(N log K)`    | `O(K)`           | Best when `k << N`               |
| 3. Quick Select  | `O(N)` avg      | `O(1)`           | Optimal, but tricky to implement |

---

## 🔹 Approach 1: Sorting

### ✅ Java Code:

```java
import java.util.Arrays;

public int findKthLargest_sort(int[] nums, int k) {
    Arrays.sort(nums);  // Ascending sort
    return nums[nums.length - k]; // k-th largest is (n - k)-th index
}
```

### ✅ Time & Space

* Time: `O(N log N)`
* Space: `O(1)` (in-place sort if allowed)

---

## 🔹 Approach 2: Min Heap (Priority Queue)

> ✅ Maintain a min-heap of size `k`. Push elements and **remove smallest** when size exceeds `k`.

### ✅ Java Code:

```java
import java.util.PriorityQueue;

public int findKthLargest_heap(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    for (int num : nums) {
        minHeap.add(num);
        if (minHeap.size() > k) {
            minHeap.poll(); // Remove smallest
        }
    }

    return minHeap.peek(); // Root is k-th largest
}
```

### ✅ Time & Space:

* Time: `O(N log K)`
* Space: `O(K)`

---

## 🔹 Approach 3: Quick Select (Hoare’s Partition)

> ✅ Use Quickselect (like QuickSort but only search one side).
> Finds the K-th largest in **O(N)** average time.

### ✅ Java Code:

```java
public int findKthLargest_quickSelect(int[] nums, int k) {
    return quickSelect(nums, 0, nums.length - 1, nums.length - k);
}

private int quickSelect(int[] nums, int left, int right, int targetIndex) {
    if (left == right) return nums[left];

    int pivotIndex = partition(nums, left, right);

    if (pivotIndex == targetIndex) {
        return nums[pivotIndex];
    } else if (pivotIndex < targetIndex) {
        return quickSelect(nums, pivotIndex + 1, right, targetIndex);
    } else {
        return quickSelect(nums, left, pivotIndex - 1, targetIndex);
    }
}

private int partition(int[] nums, int left, int right) {
    int pivot = nums[right];
    int i = left;

    for (int j = left; j < right; j++) {
        if (nums[j] <= pivot) {
            swap(nums, i, j);
            i++;
        }
    }

    swap(nums, i, right);
    return i;
}

private void swap(int[] nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
```

### ✅ Time & Space:

| Metric | Value                          |
| ------ | ------------------------------ |
| Time   | `O(N)` average, `O(N^2)` worst |
| Space  | `O(1)` in-place                |

---

## ✅ Which One to Use?

\| If `k` is small (`k << N`)      | Use Min-Heap `O(N log K)` ✅ |
\| If speed is critical            | Use Quickselect `O(N)` avg ✅ |
\| If simplicity is preferred      | Use Sorting `O(N log N)` 🟡 |

---

## 🧪 Example:

Input: `nums = [3,2,1,5,6,4], k = 2`

Sorted: `[1, 2, 3, 4, 5, 6]`
Answer: `5` (2nd largest)

---

Let me know if you’d like:

* Python versions
* Dry run visualizations
* Hoare vs. Lomuto partition comparison

Happy to walk you through!




Great! You're solving **Leetcode 215 – Find Kth Largest Element in an Array**, a classic and **frequent interview question**.

---

## ✅ Problem Recap

> Given an integer array `nums` and an integer `k`, return the **k-th largest element** in the array.

📝 Note: The answer is **not the K-th distinct** element, just the one at position `k` in the **sorted (descending)** array.

---

## ✅ 3 Most Common Approaches:

| Approach         | Time Complexity | Space Complexity | Use Case / Suitability           |
| ---------------- | --------------- | ---------------- | -------------------------------- |
| 1. Sorting       | `O(N log N)`    | `O(1)` or `O(N)` | Simplest, but not optimal        |
| 2. Min Heap (PQ) | `O(N log K)`    | `O(K)`           | Best when `k << N`               |
| 3. Quick Select  | `O(N)` avg      | `O(1)`           | Optimal, but tricky to implement |

---

## 🔹 Approach 1: Sorting

### ✅ Java Code:

```java
import java.util.Arrays;

public int findKthLargest_sort(int[] nums, int k) {
    Arrays.sort(nums);  // Ascending sort
    return nums[nums.length - k]; // k-th largest is (n - k)-th index
}
```

### ✅ Time & Space

* Time: `O(N log N)`
* Space: `O(1)` (in-place sort if allowed)

---

## 🔹 Approach 2: Min Heap (Priority Queue)

> ✅ Maintain a min-heap of size `k`. Push elements and **remove smallest** when size exceeds `k`.

### ✅ Java Code:

```java
import java.util.PriorityQueue;

public int findKthLargest_heap(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    for (int num : nums) {
        minHeap.add(num);
        if (minHeap.size() > k) {
            minHeap.poll(); // Remove smallest
        }
    }

    return minHeap.peek(); // Root is k-th largest
}
```

### ✅ Time & Space:

* Time: `O(N log K)`
* Space: `O(K)`

---

## 🔹 Approach 3: Quick Select (Hoare’s Partition)

> ✅ Use Quickselect (like QuickSort but only search one side).
> Finds the K-th largest in **O(N)** average time.

### ✅ Java Code:

```java
public int findKthLargest_quickSelect(int[] nums, int k) {
    return quickSelect(nums, 0, nums.length - 1, nums.length - k);
}

private int quickSelect(int[] nums, int left, int right, int targetIndex) {
    if (left == right) return nums[left];

    int pivotIndex = partition(nums, left, right);

    if (pivotIndex == targetIndex) {
        return nums[pivotIndex];
    } else if (pivotIndex < targetIndex) {
        return quickSelect(nums, pivotIndex + 1, right, targetIndex);
    } else {
        return quickSelect(nums, left, pivotIndex - 1, targetIndex);
    }
}

private int partition(int[] nums, int left, int right) {
    int pivot = nums[right];
    int i = left;

    for (int j = left; j < right; j++) {
        if (nums[j] <= pivot) {
            swap(nums, i, j);
            i++;
        }
    }

    swap(nums, i, right);
    return i;
}

private void swap(int[] nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
```

### ✅ Time & Space:

| Metric | Value                          |
| ------ | ------------------------------ |
| Time   | `O(N)` average, `O(N^2)` worst |
| Space  | `O(1)` in-place                |

---

## ✅ Which One to Use?

\| If `k` is small (`k << N`)      | Use Min-Heap `O(N log K)` ✅ |
\| If speed is critical            | Use Quickselect `O(N)` avg ✅ |
\| If simplicity is preferred      | Use Sorting `O(N log N)` 🟡 |

---

## 🧪 Example:

Input: `nums = [3,2,1,5,6,4], k = 2`

Sorted: `[1, 2, 3, 4, 5, 6]`
Answer: `5` (2nd largest)

---

Let me know if you’d like:

* Python versions
* Dry run visualizations
* Hoare vs. Lomuto partition comparison

Happy to walk you through!
