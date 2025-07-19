
Here is your Java code for **"Subarrays Divisible by K"** with detailed **Telugu-style comments** to help you understand and remember:

---

### ✅ Java Code with Telugu Comments

```java
class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int n = nums.length;
        int prefixMod = 0; // ✅ Prefix sum ki mod value ni track cheyyadam kosam
        int result = 0;    // ✅ Total valid subarrays count

        // ✅ Modulo values 0 nunchi k-1 varaku untaayi. 
        // modGroups[i] ante... i mod value tho entha sarlu prefix sum ochindo
        int[] modGroups = new int[k];

        // ✅ Initial ga mod 0 ki oka subarray undi ani consider cheyyali (empty prefix)
        modGroups[0] = 1;

        for (int num : nums) {
            // ✅ prefixMod ni update cheyyali... mod k tho
            // (modulo operation negative values ki issue isthadi kabatti... +k vesi again mod k chestham)
            prefixMod = (prefixMod + num % k + k) % k;

            // ✅ Same mod value munde ochindante... aa subarray madhya lo difference divisible by k untundi
            result += modGroups[prefixMod];

            // ✅ Current mod value ni count lo add cheyyali
            modGroups[prefixMod]++;
        }

        return result;
    }
}
```

---

### ✅ Example Dry Run

For `nums = [4,5,0,-2,-3,1]` and `k = 5`:

* Prefix sums (mod 5): \[4, 4, 4, 2, 4, 0]
* Matching mod values → count valid subarrays

---

### ✅ Time & Space Complexity

| Type     | Complexity |
| -------- | ---------- |
| ⏱ Time   | O(n)       |
| 🧠 Space | O(k)       |

---

Let me know if you'd like a **visual trace**, **interview-ready explanation**, or a **Python version with Telugu comments**.
