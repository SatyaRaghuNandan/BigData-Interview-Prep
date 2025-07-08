Perfect! You're working on **Leetcode 347: Top K Frequent Elements** – a classic variant of the heap/QuickSelect problem, similar in structure to **Leetcode 215**.

Let’s structure this **just like we did for 215**:

---

## ✅ Problem Recap (Leetcode 347)

> Given an integer array `nums` and an integer `k`, return the **k most frequent elements**.

---

## ✅ Top 3 Approaches

| Approach         | Time Complexity           | Space Complexity | When to Use                           |
| ---------------- | ------------------------- | ---------------- | ------------------------------------- |
| 1. Bucket Sort   | `O(N)`                    | `O(N)`           | Best overall when N is large          |
| 2. Min Heap (PQ) | `O(N log K)`              | `O(N + K)`       | Great when `k` is small               |
| 3. Quick Select  | `O(N)` avg, `O(N²)` worst | `O(N)`           | Optimal average case, complex to code |

---

## ✅ Approach 1: Bucket Sort (Linear Time)

### 🔧 Key Idea:

* Use a hashmap to count frequencies
* Store elements in a "bucket" at index = frequency
* Iterate from highest to lowest frequency

```java
public List<Integer> topKFrequent_bucket(int[] nums, int k) {
    Map<Integer, Integer> freqMap = new HashMap<>();
    for (int num : nums) {
        freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
    }

    // Bucket index = frequency
    List<Integer>[] bucket = new List[nums.length + 1];
    for (int key : freqMap.keySet()) {
        int freq = freqMap.get(key);
        if (bucket[freq] == null) {
            bucket[freq] = new ArrayList<>();
        }
        bucket[freq].add(key);
    }

    List<Integer> result = new ArrayList<>();
    for (int i = bucket.length - 1; i >= 0 && result.size() < k; i--) {
        if (bucket[i] != null) {
            result.addAll(bucket[i]);
        }
    }

    return result;
}
```

### 🧠 Time & Space

| Metric | Value |
| ------ | ----- |
| Time   | O(N)  |
| Space  | O(N)  |

---

## ✅ Approach 2: Min Heap (Priority Queue)

### 🔧 Key Idea:

* Count frequencies using a map
* Use a **min-heap** of size `k` to keep top `k` frequent elements

```java
public int[] topKFrequent_heap(int[] nums, int k) {
    Map<Integer, Integer> count = new HashMap<>();
    for (int num : nums) {
        count.put(num, count.getOrDefault(num, 0) + 1);
    }

    PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> count.get(a) - count.get(b));

    for (int num : count.keySet()) {
        heap.add(num);
        if (heap.size() > k) {
            heap.poll();
        }
    }

    int[] result = new int[k];
    for (int i = k - 1; i >= 0; i--) {
        result[i] = heap.poll();
    }
    return result;
}
```

### 🧠 Time & Space

| Metric | Value      |
| ------ | ---------- |
| Time   | O(N log K) |
| Space  | O(N + K)   |

---

## ✅ Approach 3: Quick Select

### 🔧 Key Idea:

* Use frequency map and apply QuickSelect to partition by frequency
* Return top `k` most frequent from the right side of array

```java
public class TopKFrequentQuickSelect {
    int[] unique;
    Map<Integer, Integer> count;

    public int[] topKFrequent(int[] nums, int k) {
        count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        int n = count.size();
        unique = new int[n];
        int i = 0;
        for (int num : count.keySet()) {
            unique[i++] = num;
        }

        quickselect(0, n - 1, n - k);
        return Arrays.copyOfRange(unique, n - k, n);
    }

    private void quickselect(int left, int right, int kSmallest) {
        if (left == right) return;

        Random rand = new Random();
        int pivotIndex = left + rand.nextInt(right - left + 1);
        pivotIndex = partition(left, right, pivotIndex);

        if (kSmallest == pivotIndex) return;
        else if (kSmallest < pivotIndex)
            quickselect(left, pivotIndex - 1, kSmallest);
        else
            quickselect(pivotIndex + 1, right, kSmallest);
    }

    private int partition(int left, int right, int pivotIndex) {
        int pivotFreq = count.get(unique[pivotIndex]);
        swap(pivotIndex, right);

        int storeIndex = left;
        for (int i = left; i < right; i++) {
            if (count.get(unique[i]) < pivotFreq) {
                swap(storeIndex, i);
                storeIndex++;
            }
        }

        swap(storeIndex, right);
        return storeIndex;
    }

    private void swap(int i, int j) {
        int temp = unique[i];
        unique[i] = unique[j];
        unique[j] = temp;
    }
}
```

### 🧠 Time & Space

| Metric | Value                 |
| ------ | --------------------- |
| Time   | O(N) avg, O(N²) worst |
| Space  | O(N)                  |

---

## ✅ Example Dry Run

### Input:

```java
nums = [1,1,1,2,2,3], k = 2
```

* Frequency map: `{1:3, 2:2, 3:1}`
* Top 2 frequent: `[1, 2]`

---

## ✅ Which Approach to Use?

| Use Case                                | Best Approach |
| --------------------------------------- | ------------- |
| You want fastest solution               | ✅ Bucket Sort |
| You want memory efficiency              | ✅ Min Heap    |
| Interviewer wants QuickSelect challenge | ✅ QuickSelect |

---

Let me know if you'd like the **Counting Sort** variant (when values are bounded), or a **Trie-based extension for strings**.



