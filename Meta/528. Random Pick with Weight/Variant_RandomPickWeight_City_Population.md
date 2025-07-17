# // VARIANT: What if you had to return the city that a person lives in? The input is given very differently.


Sure! Here's the approach explained in **5–6 plain English bullet points**:

* 🧮 First, we calculate a **running total (prefix sum)** of populations for each city — this helps us assign each city a proportional range based on its population.

* 📦 We store each city name along with its cumulative population using a `Pair(city, prefixSum)` in a list.

* 🎯 To pick a random city, we generate a random number between `0` and total population (like throwing a dart at the full population line).

* 🔍 We then perform **binary search** on the prefix sum list to find the **first city whose cumulative population exceeds the random number**.

* ✅ That city is returned — it has a higher chance of being picked if it has a larger population.

* 🚀 This ensures cities are chosen **with probability proportional to their population**, efficiently using `O(log n)` time.



Here's the **formatted and well-documented version** of your `CityAndPopulation_1` variant in **Java**, with **Telugu-style comments**, **time/space complexity analysis**, and a **comparison table with the original `pickIndex()` problem**.

---

### ✅ Formatted Code (City + Prefix Sums using List<Pair>)

```java
import java.util.*;

public class CityAndPopulation_1 {

    // 👇 Pair class lo oka city peru and aa varaku population sum ni store chestunnam
    static class Pair {
        String city;
        int sum; // prefix sum till this city

        Pair(String city, int sum) {
            this.city = city;
            this.sum = sum;
        }
    }

    // 👇 List of prefix sums along with city names (city -> prefix sum)
    private List<Pair> prefixSums = new ArrayList<>();

    // 👇 Constructor – prefix sum array build chesthunnam
    public CityAndPopulation_1(List<Pair> cityPopulations) {
        for (Pair entry : cityPopulations) {
            if (prefixSums.isEmpty()) {
                // 🧮 First entry ni direct ga add cheyyali
                prefixSums.add(new Pair(entry.city, entry.sum));
            } else {
                // 🔁 Last prefix sum + current population
                int newSum = prefixSums.get(prefixSums.size() - 1).sum + entry.sum;
                prefixSums.add(new Pair(entry.city, newSum));
            }
        }
    }

    // 👇 Test kosam wrapper – 0 ante random select, else override
    public String pickIndexWrapper(int generatedPerson) {
        return pickIndex(generatedPerson);
    }

    // 👇 Binary Search – person number ni base cheskoni city pick cheyyadam
    public String pickIndex(int override) {
        int totalPopulation = prefixSums.get(prefixSums.size() - 1).sum;

        // 🧍 Person ni generate cheyyadam (random or override)
        int person = (override == 0) 
            ? new Random().nextInt(totalPopulation) 
            : override;

        int left = 0, right = prefixSums.size() - 1;

        // 🔍 Binary search to find first prefixSum > person
        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (person < prefixSums.get(mid).sum) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return prefixSums.get(left).city;
    }
}
```

---

### ✅ Time and Space Complexity

| Operation           | CityAndPopulation\_1 (Pair) | Original Solution (Array) |
| ------------------- | --------------------------- | ------------------------- |
| Constructor (build) | O(n) – one pass over input  | O(n)                      |
| `pickIndex()`       | O(log n) – binary search    | O(log n)                  |
| Space               | O(n) for `List<Pair>`       | O(n) for `int[] prefix`   |
| Object Overhead     | Higher (Pair objects)       | Lower (raw int array)     |

---

### ✅ Why `List<Pair>` instead of `int[]`?

* We’re **returning city names**, not just indexes.
* Each city is tied to its **cumulative sum** (prefix sum).
* We need both: `cityName` + `sum`. So one of:

  * `List<Pair<city, sum>>` ✅ (clean, readable)
  * or two arrays: `String[] cities` and `int[] prefix` ✅ (more efficient)

---

### ✅ How to Optimize?

If you want **space savings**, use this:

```java
String[] cities;
int[] prefixSums;
```

This avoids creating `Pair` objects (less heap usage, faster access), while preserving `O(n)` space.

---

Let me know if you want this version using two parallel arrays (cities + prefix), or if you'd like a test class with example cities and populations!



Here is the **Java version** of your C++ code for the **city population picker using prefix sums and binary search**:

---

### ✅ Java Equivalent with Comments

```java
import java.util.*;

public class SolutionVariant528 {
    private List<Pair> prefixSums = new ArrayList<>();

    // Custom Pair class for city and prefix sum
    static class Pair {
        String city;
        int sum;

        Pair(String city, int sum) {
            this.city = city;
            this.sum = sum;
        }
    }

    // Constructor that builds prefix sums
    public SolutionVariant528(List<Pair> cityPopulations) {
        for (Pair entry : cityPopulations) {
            if (prefixSums.isEmpty()) {
                prefixSums.add(new Pair(entry.city, entry.sum));
            } else {
                int newSum = prefixSums.get(prefixSums.size() - 1).sum + entry.sum;
                prefixSums.add(new Pair(entry.city, newSum));
            }
        }
    }

    // Wrapper for testability (0 means use random)
    public String pickIndexWrapper(int generatedPerson) {
        return pickIndex(generatedPerson);
    }

    // Binary search to find city
    public String pickIndex(int override) {
        int totalPopulation = prefixSums.get(prefixSums.size() - 1).sum;
        int person = (override == 0) ? new Random().nextInt(totalPopulation) : override;

        int left = 0, right = prefixSums.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (person < prefixSums.get(mid).sum) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return prefixSums.get(left).city;
    }

    // Test the solution
    public static void main(String[] args) {
        List<Pair> input = Arrays.asList(
            new Pair("US", 300),
            new Pair("VN", 100),
            new Pair("BR", 200)
        );

        SolutionVariant528 solution = new SolutionVariant528(input);

        assert solution.pickIndexWrapper(0).equals("US");
        assert solution.pickIndexWrapper(150).equals("US");
        assert solution.pickIndexWrapper(299).equals("US");

        assert solution.pickIndexWrapper(300).equals("VN");
        assert solution.pickIndexWrapper(375).equals("VN");
        assert solution.pickIndexWrapper(399).equals("VN");

        assert solution.pickIndexWrapper(400).equals("BR");
        assert solution.pickIndexWrapper(420).equals("BR");
        assert solution.pickIndexWrapper(599).equals("BR");

        System.out.println("All assertions passed!");
    }
}
```

---

### 🧠 Summary

* `prefixSums`: Stores cumulative population count for each city.
* `pickIndex(int override)`: Uses binary search to find the city where the given `person` index falls.
* Time Complexity:

  * Constructor: `O(n)`
  * pickIndex(): `O(log n)`
* Space Complexity: `O(n)` for prefixSums.

Let me know if you want this modified to use `Map<String, Integer>` or converted to a cleaner utility form!



Here's your requested implementation of the **Leetcode 528 variant** — where we select a **city based on its population proportionally** — rewritten in **Java** with:

* ✅ Telugu comments
* ✅ Multiple approaches (Binary Search with Prefix Sum + Linear Scan)
* ✅ Time and Space Complexity

---

## ✅ Problem Recap

> Given a list of `(city, population)`, pick a city randomly such that the probability of picking a city is proportional to its population.

---

## ✅ Approach 1: Prefix Sum + Binary Search (Efficient - `O(log n)` pick)

### 🔧 Java Code with Telugu Comments

```java
import java.util.*;

public class CityPicker {
    private final List<String> cities = new ArrayList<>();
    private final List<Integer> prefixSums = new ArrayList<>();
    private final Random rand = new Random();
    private int totalPopulation;

    // 🏗️ Constructor: Prefix Sum prepare cheyyadam
    public CityPicker(List<Pair<String, Integer>> cityPopulations) {
        totalPopulation = 0;

        for (Pair<String, Integer> entry : cityPopulations) {
            String city = entry.getKey();
            int population = entry.getValue();

            totalPopulation += population;
            cities.add(city);  // city names list lo store cheyyadam
            prefixSums.add(totalPopulation);  // cumulative sum prepare cheyyadam
        }
    }

    // 🔁 Random ga person pick cheyyali, and aa person ekkada padtado choodali
    public String pickCity() {
        int person = rand.nextInt(totalPopulation);  // 0 to total - 1
        int index = binarySearch(person);
        return cities.get(index);
    }

    // 🔍 Binary Search for person index in prefix sum
    private int binarySearch(int person) {
        int left = 0, right = prefixSums.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (person < prefixSums.get(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    // 🚀 Test code
    public static void main(String[] args) {
        List<Pair<String, Integer>> input = Arrays.asList(
            new Pair<>("US", 300),
            new Pair<>("VN", 100),
            new Pair<>("BR", 200)
        );

        CityPicker picker = new CityPicker(input);

        // Pick 10 samples
        Map<String, Integer> freq = new HashMap<>();
        for (int i = 0; i < 10000; i++) {
            String city = picker.pickCity();
            freq.put(city, freq.getOrDefault(city, 0) + 1);
        }

        System.out.println("City pick frequencies:");
        for (Map.Entry<String, Integer> entry : freq.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
```

🧱 You'll need a `Pair` class if you're not using JavaFX or javafx.util:

```java
class Pair<K, V> {
    private K key;
    private V value;

    public Pair(K k, V v) {
        this.key = k;
        this.value = v;
    }

    public K getKey() { return key; }
    public V getValue() { return value; }
}
```

---

## ✅ Approach 2: Linear Scan (Simpler but Slower - `O(n)` pick)

```java
public String pickCityLinear() {
    int person = rand.nextInt(totalPopulation);
    int sum = 0;

    for (int i = 0; i < prefixSums.size(); i++) {
        sum += (i == 0 ? prefixSums.get(i) : prefixSums.get(i) - prefixSums.get(i - 1));
        if (person < prefixSums.get(i)) {
            return cities.get(i);
        }
    }

    return null;
}
```

✅ Use `pickCityLinear()` if you don't want to use binary search but this is **less efficient**.

---

## 📊 Time & Space Complexity

| Operation        | PrefixSum + BinarySearch | Linear Scan |
| ---------------- | ------------------------ | ----------- |
| Constructor      | `O(n)`                   | `O(n)`      |
| pickCity()       | `O(log n)`               | `O(n)`      |
| Space Complexity | `O(n)`                   | `O(n)`      |

---

## 🧠 Real-World Interview Talking Points

🎤 Say this:

> “I precompute the **prefix sum of population**, and then generate a **random person number** to binary search where they fall. This ensures that the probability of landing in a city is exactly proportional to its population. For large lists, this approach is both time and memory efficient.”

---

## ✅ Possible Extensions (Interview Bonus Ideas)

| Extension                     | Notes                                               |
| ----------------------------- | --------------------------------------------------- |
| Add/Remove cities dynamically | Use TreeMap or Segment Trees                        |
| Floating-point weights        | Use `double` prefix sums                            |
| Track frequency of picks      | Add a `Map<String, Integer>` counter                |
| Weighted round-robin          | Use a Heap to cycle cities based on remaining quota |

---

Let me know if you'd like this as an **API class**, or extended to support **dynamic insert/delete** (e.g., real-time dashboards or load balancing)!
