Here's a **detailed breakdown** of the **Sliding Window Maximum (Leetcode 239)** problem with:

* ✅ **5-Step Easy Approach**
* ✅ **Java Code with Telugu Comments**
* ✅ **Time & Space Complexity**
* ✅ **Memory Tip to Remember**

---

### ✅ Problem Statement:

Given an integer array `nums` and a sliding window of size `k`, return the **maximum element in each sliding window**.

---

### ✅ Easy 5-Step Approach (with Visualization in Mind):

1. **Use a Deque (Double-Ended Queue)** to store **indices**, not actual values.
2. Maintain the **Deque in decreasing order** of values: largest element's index at the front.
3. For each index:

   * 🔁 Remove indices **out of window** (i.e., index < i - k + 1).
   * 🔁 Remove indices from back if their values are **less than current number**.
   * ➕ Add current index at the back of deque.
4. The **front of deque** will always be the index of the maximum value for the current window.
5. Add `nums[dq.peekFirst()]` to result once the first window is processed.

---

### ✅ Java Code with Telugu Comments:

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        // Result list ni create cheddam
        List<Integer> res = new ArrayList<>();

        // Indices ni store cheyyadam kosam deque (double ended queue) use chestunnam
        Deque<Integer> dq = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++) {

            // 1. Window nunchi biteindi ane indices remove cheyyali (window start out of range ayipothundi ante)
            if (!dq.isEmpty() && dq.peekFirst() == i - k) {
                dq.pollFirst(); // front nunchi remove cheyyadam
            }

            // 2. Back nunchi remove cheyyali: current element kanna chinna elements useless
            while (!dq.isEmpty() && nums[i] >= nums[dq.peekLast()]) {
                dq.pollLast(); // back nunchi remove
            }

            // 3. Current index ni add cheyyali
            dq.offerLast(i);

            // 4. Window full ayyaka (i >= k - 1), max element ni result lo add cheyyali
            if (i >= k - 1) {
                res.add(nums[dq.peekFirst()]);
            }
        }

        // List ni array ga marchadam
        return res.stream().mapToInt(i -> i).toArray();
    }
}
```

---

### ✅ Time and Space Complexity:

| Operation | Complexity                                                       |
| --------- | ---------------------------------------------------------------- |
| Time      | O(n) — Each element is added and removed from deque at most once |
| Space     | O(k) — At most `k` elements in the deque at any time             |

---

### ✅ Easy Way to Remember:

🧠 **Think of the Deque like a "Super Queue"** that:

* Removes **smaller numbers from the back**
* Maintains **only potential max elements**
* Keeps track of **valid indices within window**

🧠 **Mnemonic:**
👉 “**Clean from back, drop from front, always max at the front**”

---

### ✅ Dry Run Example:

```java
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3  
Output:       [3,3,5,5,6,7]
```

* First window: \[1,3,-1] → max = 3
* Slide: \[3,-1,-3] → max = 3
* Slide: \[-1,-3,5] → max = 5
* Slide: \[-3,5,3] → max = 5
* Slide: \[5,3,6] → max = 6
* Slide: \[3,6,7] → max = 7

---

Let me know if you want a Python version or a visual walkthrough for better memory aid!
