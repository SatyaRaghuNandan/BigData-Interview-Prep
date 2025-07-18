Let's break down the **difference** between the three problems first:

---

### ✅ **Difference Between Problems**

| Problem                        | Description                                                                         | Input                                       | Goal                                                  | Key Constraint                            |        |                              |
| ------------------------------ | ----------------------------------------------------------------------------------- | ------------------------------------------- | ----------------------------------------------------- | ----------------------------------------- | ------ | ---------------------------- |
| **20. Valid Parentheses**      | Check if every opening bracket has a matching closing bracket in the correct order. | A string with '(', ')', '{', '}', '\[', ']' | Return `true` if valid                                | Use a **stack** to track opening brackets |        |                              |
| **219. Contains Duplicate II** | Check if there are **duplicate elements** within distance `k`.                      | Integer array + integer `k`                 | Return `true` if `nums[i] == nums[j]` and \`          | i - j                                     | <= k\` | Use a **sliding window set** |
| **217. Contains Duplicate**    | Check if the array contains **any duplicate**.                                      | Integer array                               | Return `true` if any value appears **more than once** | Use a **set**                             |        |                              |

---

## 🧠 Memory Tip:

* **20 → Stack of Brackets**
* **219 → Duplicates with Distance `k` (Window Set)**
* **217 → Just Any Duplicates (Simple Set)**

---

Now let's go one by one with:

* ✅ Java code
* 📝 Telugu comments
* ⏱️ Time & Space Complexity

---

## ✅ 20. Valid Parentheses

```java
import java.util.*;

public class Solution {
    public boolean isValid(String s) {
        // Stack lo brackets store cheddam
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        for (char ch : s.toCharArray()) {
            // Opening bracket ayite push cheyyadam
            if (map.containsValue(ch)) {
                stack.push(ch);
            } 
            // Closing ayite pop chesi match avuthundha chuddam
            else if (map.containsKey(ch)) {
                if (stack.isEmpty() || stack.pop() != map.get(ch)) {
                    return false;
                }
            }
        }

        // Stack empty unte valid
        return stack.isEmpty();
    }
}
```

### ⏱️ Complexity:

* **Time:** O(n) – loop through all characters once
* **Space:** O(n) – worst case all open brackets in stack

---

## ✅ 217. Contains Duplicate

```java
import java.util.*;

public class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Set lo already chusthunnava check cheddam
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true; // duplicate kanpinchindi
            }
            seen.add(num);
        }
        return false; // duplicates ledu
    }
}
```

### ⏱️ Complexity:

* **Time:** O(n)
* **Space:** O(n) – in worst case, all unique elements

---

## ✅ 219. Contains Duplicate II

```java
import java.util.*;

public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        // Sliding window lo values track cheyyadam
        Set<Integer> window = new HashSet<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (window.contains(nums[i])) {
                return true; // duplicate within k distance
            }

            window.add(nums[i]);

            // Window size > k ayithe first element remove cheyyali
            if (window.size() > k) {
                window.remove(nums[i - k]);
            }
        }

        return false;
    }
}
```

### ⏱️ Complexity:

* **Time:** O(n)
* **Space:** O(k) – max window of size `k`

---

## ✅ Summary Table

| Problem | Data Structure | Time | Space | Key Logic                      |
| ------- | -------------- | ---- | ----- | ------------------------------ |
| 20      | Stack + Map    | O(n) | O(n)  | Match brackets                 |
| 217     | Set            | O(n) | O(n)  | Any duplicates                 |
| 219     | Sliding Set    | O(n) | O(k)  | Duplicates within distance `k` |

---

Let me know if you want:

* Python versions
* Dry run for any problem
* Interview tricks to remember each one

Ready to help 🚀
