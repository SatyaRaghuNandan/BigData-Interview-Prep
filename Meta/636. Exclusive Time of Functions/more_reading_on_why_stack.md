Great question! Let's break it down **step-by-step**, understand the **original problem**, the **variant**, and then explore **why a `Stack` is essential**.

---

## ✅ Problem Type: **Exclusive Time of Functions (Leetcode 636 + Variant)**

---

## 🔷 Original Problem (Leetcode 636) — `exclusiveTime`

### 📌 Problem:

You are given a list of **function call logs** in the format:

```
"function_id:start_or_end:timestamp"
```

* Only one function runs at a time.
* A function can call **another function (nested)**.
* You need to return the **exclusive time** of each function (time spent excluding child calls).

---

### 🔁 Example Input:

```java
n = 2
logs = [
  "0:start:0",
  "1:start:2",
  "1:end:5",
  "0:end:6"
]
```

### 🔍 Visual Execution:

```
Time:   0 1 2 3 4 5 6
Stack: [0]
                [1]  
                []   
                [0]
```

* `0:start:0` → Function 0 starts at t=0
* `1:start:2` → Function 1 starts at t=2 (pauses Function 0)
* `1:end:5`   → Function 1 ends at t=5
* `0:end:6`   → Function 0 resumes at t=6 and ends

---

### ✅ What We Need:

* **Function 0 runs**: \[0–1] and \[6] → total 3 units
* **Function 1 runs**: \[2–5] → 4 units

So, `result = [3, 4]`

---

### 📦 Why Use Stack?

We need the **last running function**, and **nesting is allowed**, so we need a **LIFO structure**.

* `stack.push()` on `"start"`
* `stack.pop()` on `"end"`

It helps us know **which function is currently running**, and manage **nested calls** cleanly.

---

## 🔶 Variant Problem — `profileApp(List<Log>)`

### 📌 Problem:

Instead of numeric IDs, you have:

```java
class Log {
    String functionName;
    String type; // "start" or "end"
    int timestamp;
}
```

And you want to return:

```java
Map<String, Integer> → functionName → exclusiveTime
```

🟡 Same idea, just **function names instead of IDs**, and **return a Map** instead of array.

---

### Example:

```java
Log("A", "start", 0)
Log("B", "start", 2)
Log("B", "end", 5)
Log("A", "end", 6)
```

Result:

```
A → 3
B → 3
```

---

## ✅ Summary of Concepts

| Concept             | Explanation                                                            |
| ------------------- | ---------------------------------------------------------------------- |
| **Exclusive Time**  | Time spent in a function, excluding child function calls               |
| **Stack**           | Keeps track of which function is currently running (last-in-first-out) |
| **`prev` Variable** | Tracks last known timestamp to calculate delta for each function       |
| **Nested Calls**    | Requires pausing outer function and resuming after inner function ends |

---

## 🧠 Tip to Remember:

Think of this like:

* You are tracing logs of nested method calls.
* You need to measure *how much actual time* each method spent running.
* Only one method runs at a time.
* Stack helps pause/resume parent-child relationships correctly.

---

Would you like a **dry run** with visual stack state and how each `result` value is calculated?
