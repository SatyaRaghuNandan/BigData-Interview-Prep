# // VARIANT: What if you had to return the minimum cost to buy a roundtrip flight?
# // Note you cannot fly somewhere and back on the same day.

Here’s the equivalent **Java code** for the Python function `find_cheapest_tickets`, followed by a breakdown of **time and space complexity** and inline comments for clarity.

---

### ✅ **Java Implementation**

```java
import java.util.*;

public class TicketFinder {

    public static int findCheapestTickets(int[] departures, int[] returns) {
        int minDepartureCost = departures[0];
        int minCost = Integer.MAX_VALUE;

        // Start from index 1 since we're comparing with minDepartureCost
        for (int i = 1; i < departures.length; i++) {
            // Check current min departure + current return cost
            minCost = Math.min(minCost, minDepartureCost + returns[i]);

            // Update the minimum departure cost seen so far
            if (departures[i] < minDepartureCost) {
                minDepartureCost = departures[i];
            }
        }

        return minCost;
    }

    public static void main(String[] args) {
        assert findCheapestTickets(new int[]{8, 3, 6, 10}, new int[]{10, 9, 5, 8}) == 8;
        assert findCheapestTickets(new int[]{10, 3, 10, 9, 3}, new int[]{4, 20, 6, 7, 10}) == 9;
        assert findCheapestTickets(new int[]{1, 3, 10, 9, 3}, new int[]{1, 20, 6, 7, 10}) == 7;
        assert findCheapestTickets(new int[]{1, 3, 10, 9, 3}, new int[]{1, 1, 6, 7, 10}) == 2;
        assert findCheapestTickets(new int[]{1, 3, 10, 9, 3}, new int[]{10, 9, 8, 7, 6}) == 7;
        assert findCheapestTickets(new int[]{12, 33, 44, 9, 23}, new int[]{100, 90, 80, 70, 15}) == 24;
        assert findCheapestTickets(new int[]{4, 3, 5, 11, 2}, new int[]{1, 6, 10, 2, 9}) == 5;

        System.out.println("All test cases passed!");
    }
}
```

---

### 🔍 Time Complexity: `O(n)`

* You iterate once over the `departures` and `returns` arrays (size `n`).
* Each operation inside the loop is `O(1)`.
* ✅ Total time complexity is **O(n)**.

---

### 🧠 Space Complexity: `O(1)`

* Only uses a few integer variables: `minDepartureCost` and `minCost`.
* No additional data structures.
* ✅ Space complexity is **O(1)** (constant space).

---

### 🧪 What the code does:

* For every return trip from day `i`, it checks if you could have departed earlier (from day 0 to i-1) at a cheaper cost.
* It maintains the **minimum departure cost seen so far** and tries to combine it with the **current return cost**.
* The goal is to find the minimum sum `departure[i] + return[j]` such that `i < j`.

---

Let me know if you want a dry run or edge case breakdown for interview purposes!
