Great! Let's explore two additional advanced approaches for **Top K Frequent Elements**, suitable for different contexts.

---

## ✅ Approach 4: Counting Sort (Only works when value range is small)

### 📌 When to Use:

* Input values are **non-negative and bounded**
* Works best when `min(nums)` to `max(nums)` is a small range (e.g., 0–1000)

---

### ✅ Java Code (Counting Sort for Frequency Bucketing)

```java
public List<Integer> topKFrequent_countingSort(int[] nums, int k) {
    int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;

    for (int num : nums) {
        min = Math.min(min, num);
        max = Math.max(max, num);
    }

    int[] freq = new int[max - min + 1];
    for (int num : nums) {
        freq[num - min]++;
    }

    // Pair: [number, frequency]
    List<int[]> list = new ArrayList<>();
    for (int i = 0; i < freq.length; i++) {
        if (freq[i] > 0) {
            list.add(new int[]{i + min, freq[i]});
        }
    }

    // Sort by frequency descending
    list.sort((a, b) -> b[1] - a[1]);

    List<Integer> result = new ArrayList<>();
    for (int i = 0; i < k; i++) {
        result.add(list.get(i)[0]);
    }

    return result;
}
```

---

### 🧠 Time & Space

| Metric | Value              |
| ------ | ------------------ |
| Time   | O(N + R + R log R) |
| Space  | O(R)               |

> R = Range (`max - min + 1`)

---

### ✅ Example

```java
nums = [1, 1, 2, 2, 3], k = 2
min = 1, max = 3 → freq = [2, 2, 1]
→ Sorted by frequency → [1, 2]
```

---

## ✅ Approach 5: Trie-Based (for strings or custom keys)

### 📌 When to Use:

* Input is **strings or complex tokens** (not just integers)
* You want to **group and count prefixes or structured data**

---

### ✅ Example Problem

```java
words = ["apple", "app", "app", "apex", "apple", "ball"]
k = 2
→ Return top 2 frequent words → ["apple", "app"]
```

---

### ✅ Trie Node Definition

```java
class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    String word = null;
    int freq = 0;
}
```

---

### ✅ Java Code (Trie + Heap for Top K Frequent Strings)

```java
class TrieTopK {
    static class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        String word = null;
        int freq = 0;
    }

    TrieNode root = new TrieNode();

    public void insert(String word) {
        TrieNode curr = root;
        for (char ch : word.toCharArray()) {
            curr = curr.children.computeIfAbsent(ch, c -> new TrieNode());
        }
        curr.word = word;
        curr.freq++;
    }

    public List<String> topKFrequent(String[] words, int k) {
        for (String word : words) {
            insert(word);
        }

        PriorityQueue<TrieNode> heap = new PriorityQueue<>(
            (a, b) -> a.freq == b.freq ? b.word.compareTo(a.word) : a.freq - b.freq);

        collectTopK(root, heap, k);

        List<String> result = new ArrayList<>();
        while (!heap.isEmpty()) result.add(heap.poll().word);
        Collections.reverse(result);
        return result;
    }

    private void collectTopK(TrieNode node, PriorityQueue<TrieNode> heap, int k) {
        if (node == null) return;

        if (node.word != null) {
            heap.offer(node);
            if (heap.size() > k) heap.poll();
        }

        for (TrieNode child : node.children.values()) {
            collectTopK(child, heap, k);
        }
    }
}
```

---

### 🧠 Time & Space

| Metric | Value               |
| ------ | ------------------- |
| Time   | O(N \* L + M log K) |
| Space  | O(N \* L)           |

> N = number of words, L = word length, M = total nodes

---

## ✅ Summary Table

| Approach      | Use Case                             | Time            | Space    |
| ------------- | ------------------------------------ | --------------- | -------- |
| Bucket Sort   | Numbers with high frequency locality | O(N)            | O(N)     |
| Min Heap      | Small K                              | O(N log K)      | O(N + K) |
| Quick Select  | Optimal average case                 | O(N) avg        | O(N)     |
| Counting Sort | Small bounded range of values        | O(N + R log R)  | O(R)     |
| Trie + Heap   | String tokens or prefix structure    | O(NL + M log K) | O(NL)    |

---

Would you like:

* Trie variant to support **autocomplete** or **prefix filtering**?
* Full JUnit tests for these?
* Space-optimized stream-based variant (for massive data)?

Happy to help!
