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



You're absolutely right — this implementation is a **circular queue** using an **array**, instead of a dynamic `Queue`/`Deque`. Let's break it down step-by-step and then go through **3 dry run examples** with Telugu-style comments.

---

### ✅ Key Concepts in the Circular Queue Approach:

```java
int size, head = 0, windowSum = 0, count = 0;
int[] queue;
```

* `queue`: Fixed-size array to act as a circular queue
* `head`: Points to the most **recent index** where value was inserted
* `size`: Window size `k`
* `count`: Total number of elements seen so far (for early division)
* `windowSum`: Maintains **sliding window sum**

---

### ✅ Logic Behind `next(val)`

```java
++count;
int tail = (head + 1) % size; // Circular overwrite position
windowSum = windowSum - queue[tail] + val; // Remove oldest, add newest
head = (head + 1) % size;  // Move head forward
queue[head] = val;         // Store new value
```

#### 🧠 Telugu Comments:

```java
++count;  // ✅ Total values processed count increment cheyyadam

// ✅ Circular queue lo tail index calculate cheyyadam
int tail = (head + 1) % size;

// ✅ Previous windowSum nundi tail element remove cheyyadam, new val add cheyyadam
windowSum = windowSum - queue[tail] + val;

// ✅ Head ni circular ga increment cheyyadam
head = (head + 1) % size;

// ✅ Head location lo new value ni store cheyyadam
queue[head] = val;

// ✅ Average calculation: window lo unna elements count to divide cheyyadam
return (1.0 * windowSum) / Math.min(count, size);
```

---

### ✅ 3 Dry Run Examples

#### 🧪 Test Case 1:

```java
MovingAverage m = new MovingAverage(3);
m.next(1);  // → 1.0
```

**Initial State:**

```
queue = [0, 0, 0]
head = 0
```

* tail = (0+1)%3 = 1 → queue\[1] = 0
* windowSum = 0 - 0 + 1 = 1
* head = (0+1)%3 = 1
* queue\[1] = 1
* return 1.0 / 1 = 1.0

✅ Result: `1.0`

---

#### 🧪 Test Case 2:

```java
m.next(10); // → (1+10)/2 = 5.5
```

* tail = (1+1)%3 = 2 → queue\[2] = 0
* windowSum = 1 - 0 + 10 = 11
* head = (1+1)%3 = 2
* queue\[2] = 10
* return 11.0 / 2 = **5.5**

✅ Result: `5.5`

---

#### 🧪 Test Case 3:

```java
m.next(3);  // → (1+10+3)/3 = 4.67
```

* tail = (2+1)%3 = 0 → queue\[0] = 0
* windowSum = 11 - 0 + 3 = 14
* head = (2+1)%3 = 0
* queue\[0] = 3
* return 14.0 / 3 = **4.6667**

✅ Result: `4.67`

---

#### 🧪 Test Case 4:

```java
m.next(5);  // (10+3+5)/3 = 6.0
```

* tail = (0+1)%3 = 1 → queue\[1] = 1
* windowSum = 14 - 1 + 5 = 18
* head = (0+1)%3 = 1
* queue\[1] = 5
* return 18.0 / 3 = **6.0**

✅ Result: `6.0`

---

### 🔁 Circular Behavior Visualized

Let’s assume:

* After 3 values, buffer = `[3, 1, 10]`
* Now, new value (5) will overwrite `queue[1]` (oldest: 1)

This is how it acts as a **rotating ring buffer**.

---

### ✅ When to Use This Approach?

* **Fixed window size**, high performance
* **Low memory footprint** — doesn’t grow dynamically
* Used in **real-time analytics**, **sliding window metrics**, etc.

---

Do you want the **test driver with main method** to print all steps or track queue visually in each step?



Absolutely! Let's go **deeper** into the explanation with:

* 📌 **What is a Circular Queue and Why Use It**
* ⚙️ **Detailed step-by-step behavior of the code**
* 🔁 **How `head`, `tail`, and `% size` work**
* 🧠 **Why this approach is clever and efficient**

---

## ✅ What is a **Circular Queue**?

A **circular queue** is a data structure that uses a **fixed-size array** and **reuses space** by wrapping around once it reaches the end.

📦 Think of it like a **circle of boxes**:

* You write into the current box.
* If the circle is full, you overwrite the **oldest box**.
* You don't shift elements like in an `ArrayList` – instead, you just move the index.

In this problem, we’re using this structure to keep a **sliding window of size `k`** for our moving average.

---

## ⚙️ Explanation of Code Step-by-Step

```java
int[] queue = new int[size]; 
```

* Create an array of size `k`. This holds **at most `k` values**.
* It replaces the need for a `Deque`.

---

### What is `head`?

```java
int head = 0;
```

* `head` always **points to the most recent value inserted**.
* Every time you insert a new value, you **move `head` forward** and write there.

---

### What is `tail = (head + 1) % size;`?

```java
int tail = (head + 1) % size;
```

* `tail` is the index of the **value that will be overwritten**.
* When the array is full, we **evict the oldest value** at the `tail` index.
* We calculate `tail` as `(head + 1) % size` because:

  * If head = 2 and size = 3 → (2+1)%3 = 0
  * So we wrap around to the start of the array — that's the **circular behavior**.

---

### What does this line do?

```java
windowSum = windowSum - queue[tail] + val;
```

* We are:

  * Subtracting the **value being overwritten**
  * Adding the **new value**
* This is how we **maintain a rolling sum** in O(1) time.

---

### Final steps

```java
head = (head + 1) % size;
queue[head] = val;
```

* Move head forward to the next box (wrap around if needed)
* Place the new value into that box

---

## 🧠 Why this is Clever and Efficient

| Feature               | Why it's Good                                   |
| --------------------- | ----------------------------------------------- |
| 💡 Fixed-size array   | No memory bloat, very fast access               |
| 🔁 Circular logic     | No shifting or resizing                         |
| 🧮 Rolling sum        | Avoids recalculating sum every time             |
| ⏱️ O(1) per `.next()` | Perfect for real-time or high-frequency streams |

---

## 📊 Visual Simulation Example (size = 3)

Let's simulate step-by-step using:

```java
MovingAverage m = new MovingAverage(3);
```

### Step 1: `m.next(1)`

```text
count = 1
tail = (0+1)%3 = 1
windowSum = 0 - 0 + 1 = 1
head = (0+1)%3 = 1
queue = [0, 1, 0]
return 1 / 1 = 1.0
```

---

### Step 2: `m.next(10)`

```text
count = 2
tail = (1+1)%3 = 2
windowSum = 1 - 0 + 10 = 11
head = (1+1)%3 = 2
queue = [0, 1, 10]
return 11 / 2 = 5.5
```

---

### Step 3: `m.next(3)`

```text
count = 3
tail = (2+1)%3 = 0
windowSum = 11 - 0 + 3 = 14
head = (2+1)%3 = 0
queue = [3, 1, 10]
return 14 / 3 = 4.67
```

---

### Step 4: `m.next(5)`

```text
count = 4
tail = (0+1)%3 = 1 → evict queue[1] = 1
windowSum = 14 - 1 + 5 = 18
head = (0+1)%3 = 1
queue = [3, 5, 10]
return 18 / 3 = 6.0
```

---

## 🔁 Circular Wrap Example

When head reaches the end (index 2), it wraps around to 0:

```
Insert order:
[3, 5, 10] → Overwrite index 1 (wrap around)

Next:
Insert → overwrite index 2, then 0, then 1, then 2 again...

Keeps rotating like a clock.
```

---

## 🚀 Summary

* **Use circular array** when:

  * Window size is fixed and performance matters
  * You want O(1) memory usage
  * You want O(1) sum update

---

Would you like me to add a full Java test class with these prints and visuals included? Or visualize this using a grid/table structure?

