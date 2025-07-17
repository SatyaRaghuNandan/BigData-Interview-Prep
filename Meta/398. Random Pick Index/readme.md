
---

## ✅ Approach 1: Brute Force (Pick From List Each Time)

### ✅ Explanation in Plain English

1. Every time `pick(target)` is called, you **search the entire array**.
2. You collect all the indices where `nums[i] == target` into a list.
3. After collecting, you randomly choose one index from the list.
4. This guarantees uniform random selection because all valid indices are explicitly collected.
5. It’s **simple to implement**, but has **O(N)** time per pick call.
6. Suitable when number of queries is **low** or `nums` is **small**.
7. No extra memory is used during object construction.

---

## ✅ Approach 2: HashMap Preprocessing (Index Caching)

### ✅ Explanation in Plain English

1. During initialization, build a **HashMap** where key = number, value = list of all its indices.
2. When `pick(target)` is called, just fetch the list from the map.
3. Randomly select one index from the list.
4. Since pre-processing happens once, each pick is **very fast (O(1))**.
5. Ideal when `pick()` will be called **many times**.
6. **Downside**: Takes **extra memory** for the map, especially if the array is large or has many unique numbers.
7. Good tradeoff for **time efficiency over space**.

---

## ✅ Approach 3: Reservoir Sampling

### ✅ Explanation in Plain English

1. Traverse the array once per `pick()` call.
2. For every match `nums[i] == target`, keep a count of how many times you’ve seen it.
3. With `1/count` probability, update the result to current index (`i`).
4. This is called **Reservoir Sampling**, and ensures uniform probability.
5. It **doesn’t use any extra memory**, just a counter and a result variable.
6. Very **space efficient** and great when array is **large** or **immutable**.
7. Takes **O(N)** time per pick, but **constant space**.

---



Excellent! Below is a detailed explanation of all **three approaches** in **Java**, with:

* ✅ Telugu-style inline comments
* ✅ Time & Space Complexity for each
* ✅ Summary table for comparison

---

## ✅ Approach 1: **Brute Force**

```java
class Solution {

    private int[] nums;
    private Random rand;

    public Solution(int[] nums) {
        // nums ni store cheyyadam (extra space vadakunda)
        this.nums = nums;
        this.rand = new Random();
    }

    public int pick(int target) {
        List<Integer> indices = new ArrayList<>();
        
        // Target equal unna indices ni collect cheyyadam
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                indices.add(i);
            }
        }

        // Random ga oka index ni pick cheyyadam
        int randomIndex = indices.get(rand.nextInt(indices.size()));
        return randomIndex;
    }
}
```

### ✅ Time & Space Complexity:

* **Time**: O(N) per `pick()` (entire array traverse)
* **Space**: O(K) — where K = count of `target` in array

---

## ✅ Approach 2: **Caching with HashMap**

```java
class Solution {

    private HashMap<Integer, List<Integer>> indices;
    private Random rand;

    public Solution(int[] nums) {
        this.rand = new Random();
        this.indices = new HashMap<>();

        // Oka sari pre-processing lo anni target values ki indices cache cheyyadam
        for (int i = 0; i < nums.length; i++) {
            indices.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
    }

    public int pick(int target) {
        // Already cached list nunchi random index pick cheyyadam
        List<Integer> targetIndices = indices.get(target);
        return targetIndices.get(rand.nextInt(targetIndices.size()));
    }
}
```

### ✅ Time & Space Complexity:

* **Constructor Time**: O(N)
* **pick() Time**: O(1)
* **Space**: O(N) for HashMap storing all value-to-indices mapping

---

## ✅ Approach 3: **Reservoir Sampling** (Best for Large Arrays)

```java
class Solution {

    private int[] nums;
    private Random rand;

    public Solution(int[] nums) {
        this.nums = nums;
        this.rand = new Random();
    }

    public int pick(int target) {
        int count = 0;
        int result = 0;

        // Reservoir sampling: uniform ga oka index pick cheyyadam
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                count++;
                // 1/count chance tho current index ni pick cheyyadam
                if (rand.nextInt(count) == 0) {
                    result = i;
                }
            }
        }

        return result;
    }
}
```

### ✅ Time & Space Complexity:

* **Time**: O(N) per `pick()`
* **Space**: O(1) — constant space, no extra storage

---

## 🔁 Summary Table

| Approach      | Time (`pick`) | Space | Notes                                             |
| ------------- | ------------- | ----- | ------------------------------------------------- |
| Brute Force   | O(N)          | O(K)  | Simple, but recreates list every call             |
| HashMap Cache | O(1)          | O(N)  | Best for **multiple pick() calls**                |
| Reservoir     | O(N)          | O(1)  | Best for **memory efficiency / streaming arrays** |

---

### ✅ Interview Tip:

* Explain all 3 if time permits.
* Choose:

  * **HashMap** if array is fixed and many calls expected
  * **Reservoir** if low memory or one-time scan of large input

Let me know if you want a **test harness**, **Java dry run**, or **Python equivalent**!


map solution on LC allows you to precompute by using N space but let's you pick in (1) time


multiple calls encourages map solution at the cost of space

if it's a single call map solution is objectively worse


![image](https://github.com/user-attachments/assets/31602720-ce9d-475e-817f-d78caccfc00d)




---

## ✅ Test Cases (Happy Path + Edge Cases)

### Test Case 1:

```java
Input: nums = [1, 2, 3, 3, 3], target = 3
Expected: Randomly return 2, 3, or 4 with equal probability
```

* All approaches should return one of these 3 indices with \~equal chance over time.

---

### Test Case 2:

```java
Input: nums = [5, 5, 5, 5, 5], target = 5
Expected: Any index from 0 to 4, uniformly at random
```

* Check whether uniformity is maintained across repeated picks.

---

### Test Case 3:

```java
Input: nums = [10], target = 10
Expected: Always return 0
```

* Only one match, all approaches must return 0.

---

### Test Case 4:

```java
Input: nums = [1, 2, 3], target = 4
Expected: Error or safe handling (based on implementation)
```

* Edge case: target doesn't exist → return -1 or throw exception or handle gracefully.

---

### Test Case 5:

```java
Input: nums = [], target = 1
Expected: Handle empty array gracefully
```

* Should not crash; either return -1 or handle properly (as per your app logic).

---

## ✅ Summary Table

| Approach             | Time per `pick()` | Space Usage | Use Case Preference                      |
| -------------------- | ----------------- | ----------- | ---------------------------------------- |
| Brute Force          | O(N)              | O(1)        | Fewer queries, simple, no precomputation |
| HashMap (Preprocess) | O(1)              | O(N)        | Frequent queries, faster response        |
| Reservoir Sampling   | O(N)              | O(1)        | Large arrays, minimal memory usage       |

---

Let me know if you want performance simulations or uniformity tests using Java/Python!
