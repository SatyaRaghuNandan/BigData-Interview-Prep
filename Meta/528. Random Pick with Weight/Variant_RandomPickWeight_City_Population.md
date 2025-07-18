# // VARIANT: What if you had to return the city that a person lives in? The input is given very differently.


Sure! Here's the approach explained in **5–6 plain English bullet points**:

* 🧮 First, we calculate a **running total (prefix sum)** of populations for each city — this helps us assign each city a proportional range based on its population.

* 📦 We store each city name along with its cumulative population using a `Pair(city, prefixSum)` in a list.

* 🎯 To pick a random city, we generate a random number between `0` and total population (like throwing a dart at the full population line).

* 🔍 We then perform **binary search** on the prefix sum list to find the **first city whose cumulative population exceeds the random number**.

* ✅ That city is returned — it has a higher chance of being picked if it has a larger population.

* 🚀 This ensures cities are chosen **with probability proportional to their population**, efficiently using `O(log n)` time.


Here's a complete breakdown of your `CityPicker` solution along with improvements as per your request.

---

## ✅ **Approach (Plain English in 5–6 Bullet Points)**

1. **Prefix Sum Construction:**
   For each city’s population, we calculate the cumulative sum so that higher population cities have a wider range assigned to them in a 1D number line.

2. **Random Number Generation:**
   We randomly pick a number between `1` and the total population. This random number represents a point on the cumulative number line.

3. **Binary Search on Prefix Array:**
   Using binary search, we locate which city this point falls into by finding the first prefix sum that is **greater than or equal to** the target.

4. **City Selection:**
   Once we find the correct index in the prefix array, we return the city at that index.

5. **Higher Population = Higher Chance:**
   Since bigger population cities have a larger range in the prefix sum array, they are more likely to be picked.

6. **Repeatable API:**
   You can repeatedly call `pickCity()` to simulate weighted random selection of cities based on population.

---

## ✅ Time and Space Complexity

| Operation    | Time Complexity | Space Complexity |
| ------------ | --------------- | ---------------- |
| Constructor  | O(n)            | O(n)             |
| `pickCity()` | O(log n)        | O(1)             |

* **n = number of cities**

---

## ✅ Rewritten Version (with Custom Binary Search instead of `Arrays.binarySearch`)

```java
package LC_528_RandomPickWithWeight;

import java.util.Random;

class CityPicker {
    private final String[] cities;
    private final int[] prefixSums;
    private final Random rand;

    public CityPicker(String[] cities, int[] population) {
        this.cities = cities;
        this.prefixSums = new int[population.length];
        this.rand = new Random();

        // Construct prefix sums
        prefixSums[0] = population[0];
        for (int i = 1; i < population.length; i++) {
            prefixSums[i] = prefixSums[i - 1] + population[i];
        }
    }

    public String pickCity() {
        int totalPopulation = prefixSums[prefixSums.length - 1];
        int target = rand.nextInt(totalPopulation) + 1;  // target is [1, totalPopulation]

        int index = binarySearch(target);
        return cities[index];
    }

    // Custom binary search to find the smallest index where prefixSums[index] >= target
    private int binarySearch(int target) {
        int left = 0;
        int right = prefixSums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (prefixSums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}
```

---

## ✅ Test Cases with Explanation

```java
public class CityPickerTest {
    public static void main(String[] args) {
        testBasicScenario();
        testSingleCity();
        testEqualPopulation();
        testLargePopulationGap();
        testEdgePopulations();
    }

    private static void testBasicScenario() {
        String[] cities = {"A", "B", "C"};
        int[] population = {1, 3, 2};  // Prefix: [1, 4, 6]

        CityPicker picker = new CityPicker(cities, population);

        // Run 10 samples
        System.out.println("Basic Scenario:");
        for (int i = 0; i < 10; i++) {
            System.out.println(picker.pickCity());
        }
    }

    private static void testSingleCity() {
        String[] cities = {"Solo"};
        int[] population = {100};

        CityPicker picker = new CityPicker(cities, population);
        System.out.println("\nSingle City Scenario:");
        for (int i = 0; i < 5; i++) {
            System.out.println(picker.pickCity());  // Should always be "Solo"
        }
    }

    private static void testEqualPopulation() {
        String[] cities = {"X", "Y", "Z"};
        int[] population = {5, 5, 5};  // Equal weight

        CityPicker picker = new CityPicker(cities, population);
        System.out.println("\nEqual Population Scenario:");
        for (int i = 0; i < 10; i++) {
            System.out.println(picker.pickCity());
        }
    }

    private static void testLargePopulationGap() {
        String[] cities = {"Small", "Medium", "Mega"};
        int[] population = {1, 2, 100};  // Mega dominates

        CityPicker picker = new CityPicker(cities, population);
        System.out.println("\nLarge Population Gap Scenario:");
        for (int i = 0; i < 10; i++) {
            System.out.println(picker.pickCity());  // Expect mostly "Mega"
        }
    }

    private static void testEdgePopulations() {
        String[] cities = {"Tiny", "Giant"};
        int[] population = {1, Integer.MAX_VALUE - 1};  // Test near-integer overflow

        CityPicker picker = new CityPicker(cities, population);
        System.out.println("\nEdge Case Scenario:");
        for (int i = 0; i < 5; i++) {
            System.out.println(picker.pickCity());  // Likely always "Giant"
        }
    }
}
```

---

## 🔑 How to Remember This

* Use **prefix sum** for weighted representation.
* **Random number** on cumulative scale (1 to total sum).
* Binary search to locate correct **bucket** (city).
* Wider the bucket → more likely the pick.

Let me know if you'd like to **visualize the prefix buckets** or generate a histogram for large sample sizes!

