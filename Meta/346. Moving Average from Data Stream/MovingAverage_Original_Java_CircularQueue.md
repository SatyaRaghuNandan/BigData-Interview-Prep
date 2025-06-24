Here is your `MovingAverage` class with **detailed Telugu comments (in English script)** and **time/space complexity analysis**:

---

### ✅ Java Code with Telugu Comments

```java
class MovingAverage {

    int size;              // Window size ni store cheyyadam
    int head = 0;          // Circular queue lo head pointer (latest element ekkada store cheyyalo)
    int windowSum = 0;     // Present window lo unna sum
    int count = 0;         // Total number of values received
    int[] queue;           // Circular queue laga behave cheyyadam kosam array use chestunnam

    public MovingAverage(int size) {
        this.size = size;
        queue = new int[size]; // size fixed queue ni initialize cheyyadam
    }

    public double next(int val) {
        ++count; // total inputs count increment cheyyadam

        // Circular queue lo tail (oldest value) ni identify cheyyadam
        int tail = (head + 1) % size;

        // windowSum nunchi tail value subtract cheyyi, val add cheyyi
        windowSum = windowSum - queue[tail] + val;

        // Head ni next position ki move cheyyi (circular ga)
        head = (head + 1) % size;

        // Latest value ni head lo insert cheyyadam
        queue[head] = val;

        // Average return cheyyadam (minimum of size or total values so far)
        return (windowSum * 1.0) / Math.min(size, count);
    }
}
```

---

### ⏱️ Time Complexity:

* `next(int val)` → **O(1)**

  * All operations (insert, remove, compute average) are done in constant time.

---

### 💾 Space Complexity:

* Constructor creates an `int[] queue` of size `size` → **O(size)**
* Remaining variables are integers → O(1)
* **Total Space Complexity** → **O(size)**

---

### ✅ Summary in Telugu (English Script):

* I code circular queue concept ni use chestundi.
* Old value ni remove cheyyadam, new value ni add cheyyadam `O(1)` time lo jarugutundi.
* Queue lo values circular ga store avutayi, so memory fixed untundi (`O(size)`).
* Ideal for sliding window average problems like moving sensors, stock prices, etc.

Let me know if you'd like a version using `Queue`/`Deque` instead.
