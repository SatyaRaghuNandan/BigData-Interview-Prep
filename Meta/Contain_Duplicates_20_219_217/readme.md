Sure! Here's the **approach for each problem** in **5 bullet points** (plain English, quick to remember 👇):

---

## ✅ **20. Valid Parentheses – Stack Approach**

1. Use a **stack** to keep track of opening brackets: `(`, `{`, `[`.
2. Use a **map** to define valid pairs like `)` → `(`, `}` → `{`, etc.
3. Loop through each character in the string:

   * If it's an opening bracket, **push** it onto the stack.
   * If it's a closing bracket, check if it matches the **top of the stack**.
4. If it doesn’t match or stack is empty, return **false**.
5. At the end, if the stack is **empty**, return true; else false.

> 🎯 Use Stack + Map → Opening push, Closing match and pop.

---

## ✅ **217. Contains Duplicate – Simple Set**

1. Create an empty **Set** to track seen numbers.
2. Loop through the array.
3. For each number, check if it’s already in the Set.
4. If yes, return **true** (duplicate found).
5. If not, add the number to the Set. Return false at the end.

> 🎯 Simple linear scan with Set to catch any duplicate.

---

## ✅ **219. Contains Duplicate II – Sliding Window Set**

1. Create an empty **Set** to act as a window of size `k`.
2. Loop through the array with index `i`.
3. If `nums[i]` is already in the Set, return **true**.
4. Add `nums[i]` to the Set.
5. If window size exceeds `k`, remove `nums[i - k]` from the Set.

> 🎯 Keep window of last `k` elements in Set; check if new element exists.

---

Let me know if you want these in Telugu-style notes or as diagrams for quick revision 🧠✨


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
