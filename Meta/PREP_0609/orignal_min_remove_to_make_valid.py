class Solution:
    def minRemoveToMakeValid(self, input_string: str) -> str:
        # Step 1: Valid ga unna parentheses ni forward pass lo collect cheddam
        result_after_first_pass = []
        open_seen = 0   # '(' entha sarlu vachindo count cheyyadam kosam
        balance = 0     # ')' ki match aina '(' count cheyyadam kosam

        for ch in input_string:
            if ch == '(':
                open_seen += 1
                balance += 1  # '(' ochindhi ante oka ')' tarvata ravali
            elif ch == ')':
                if balance == 0:
                    # ')' ki match ayye '(' lekapothe skip cheyyali
                    continue
                balance -= 1  # oka ')' ni valid ga consider chesam
            # valid character ni add cheyyadam
            result_after_first_pass.append(ch)

        # Step 2: Backward lo '(' ekkuva vunte avi remove cheyyali
        final_result = []
        open_to_keep = open_seen - balance  
        # open_seen = total '(' count
        # balance = unmatched '(' count (i.e., avi remove cheyyali)

        for ch in result_after_first_pass:
            if ch == '(':
                if open_to_keep == 0:
                    # extra '(' unte skip cheyyali
                    continue
                open_to_keep -= 1  # valid '(' ni keep cheyyadam
            final_result.append(ch)  # valid character ni add cheyyadam

        return ''.join(final_result)




```

Sure! Let's analyze the **Time Complexity** and **Space Complexity** for the Python implementation of `minRemoveToMakeValid`.

---

### ✅ **Time Complexity: `O(n)`**

Where `n = len(input_string)`.

#### 🔍 Why?

* First loop (`for ch in input_string`) → runs `n` times.
* Second loop (`for ch in result_after_first_pass`) → runs at most `n` times again (since we only skip invalid ones).
* Each operation inside the loop is `O(1)`.

➡️ So, overall time complexity = `O(n) + O(n)` = **`O(n)`**

---

### ✅ **Space Complexity: `O(n)`**

#### 🔍 Why?

* `result_after_first_pass` list stores up to `n` characters.
* `final_result` list also stores up to `n` characters.
* Even though we use two lists, they're both at most size `n`, so total auxiliary space is **linear**.

➡️ Therefore, space complexity = **`O(n)`**

---

### 🧠 Note:

* If you were allowed to **mutate the string in place**, you could try optimizing space to `O(1)` (using a character array and two pointers).
* But since Python strings are immutable and we use extra lists, space is **O(n)** in this implementation.

Let me know if you'd like to see an in-place simulation or version with one pass optimization!


```
