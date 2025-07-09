Great question — you're analyzing different **designs for calculating a Moving Average from a Data Stream**, a very popular **system design + sliding window** problem that often shows up in **Meta, Google, Amazon** interviews.

Let’s break down **all 3 approaches**:

---

### ✅ **Approach 1: ArrayList (Brute Force Sliding Window)**

```java
class MovingAverage {
    int size;
    List<Integer> queue = new ArrayList<>();

    public MovingAverage(int size) {
        this.size = size;
    }

    public double next(int val) {
        queue.add(val); // Add the new value at the end

        int windowSum = 0;

        // Loop only over last 'size' elements
        for (int i = Math.max(0, queue.size() - size); i < queue.size(); ++i) {
            windowSum += queue.get(i);
        }

        return (1.0 * windowSum) / Math.min(queue.size(), size);
    }
}
```

#### 🔍 Explanation:

* We store **all elements** in a list.
* For each `.next(val)`, we **recalculate the sum** from scratch over the last `k` elements.

#### ⏱️ Time Complexity:

* `O(k)` for each `.next()` call (worst-case traversal of window size).

#### 🧠 Space Complexity:

* `O(n)` where `n` = number of `.next()` calls. All past values stored.

#### ⚠️ Interview Drawbacks:

* **Inefficient** due to repeated sum calculations.
* Not scalable — avoid in real-time systems or interviews unless explicitly asked to use a list.

---

### ✅✅ **Approach 2: Deque with Rolling Sum (Optimal for Interviews)**

```java
class MovingAverage {
    int size, windowSum = 0, count = 0;
    Deque<Integer> queue = new ArrayDeque<>();

    public MovingAverage(int size) {
        this.size = size;
    }

    public double next(int val) {
        ++count;

        // Maintain sliding window
        queue.add(val);
        int tail = count > size ? queue.poll() : 0;

        // Maintain rolling sum
        windowSum = windowSum - tail + val;

        return (1.0 * windowSum) / Math.min(size, count);
    }
}
```

#### 🔍 Explanation:

* We **maintain a fixed-size window** using `Deque`.
* Instead of re-computing the sum, we **keep a rolling sum**.
* If the queue exceeds `size`, we remove the oldest value and subtract it from the sum.

#### ⏱️ Time Complexity:

* `O(1)` for `.next()`

#### 🧠 Space Complexity:

* `O(k)` for storing at most `k` elements.

#### ✅ Why it's Interview-Preferred:

* Clean logic
* Optimized for time and space
* Easy to justify use of **queue + rolling sum** technique
* Can be extended to real-time stream scenarios

---

### ✅✅✅ **Approach 3: Circular Array (Most Space Efficient)**

```java
class MovingAverage {
    int size, head = 0, windowSum = 0, count = 0;
    int[] queue;

    public MovingAverage(int size) {
        this.size = size;
        queue = new int[size]; // Fixed-size circular buffer
    }

    public double next(int val) {
        ++count;

        // Calculate the index to overwrite
        int tail = (head + 1) % size;

        // Adjust the rolling sum
        windowSum = windowSum - queue[tail] + val;

        head = (head + 1) % size;
        queue[head] = val;

        return (1.0 * windowSum) / Math.min(count, size);
    }
}
```

#### 🔍 Explanation:

* Avoids dynamic memory (`Deque`) by using a **fixed-size circular array**.
* Just like a ring buffer — overwrite oldest element and roll forward.

#### ⏱️ Time Complexity:

* `O(1)` for `.next()`

#### 🧠 Space Complexity:

* `O(k)` (fixed and minimal)

#### ⚠️ Drawbacks:

* Slightly harder to debug or extend for dynamic window sizes.
* Needs careful tracking of head/tail.

---

## 🏁 Summary: Which Should I Use in Interviews?

| Approach              | Time Complexity | Space Complexity | Pros             | Cons                     | Interview Usage              |
| --------------------- | --------------- | ---------------- | ---------------- | ------------------------ | ---------------------------- |
| **1. List**           | O(k)            | O(n)             | Simple to write  | Very slow for large data | ❌ Avoid                      |
| **2. Deque**          | O(1)            | O(k)             | Efficient, clean | Uses dynamic structure   | ✅✅ Recommended               |
| **3. Circular Array** | O(1)            | O(k)             | Best space usage | Harder to debug          | ✅ For follow-up optimization |

---

### 🧠 What Should I Say in an Interview?

> "I’d start with Approach 2 using a `Deque` and a rolling sum, because it gives constant time complexity and is simple to implement. If memory is a concern, I’d switch to a circular array (Approach 3), which uses a fixed-size buffer. I would avoid the brute-force list-based solution since it recalculates sums every time and doesn’t scale well."

---

Would you like me to write **unit tests** or a **driver class with test cases** to help remember this pattern better?
