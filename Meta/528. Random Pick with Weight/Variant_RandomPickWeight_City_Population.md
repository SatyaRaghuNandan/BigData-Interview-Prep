# // VARIANT: What if you had to return the city that a person lives in? The input is given very differently.

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
