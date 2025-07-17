Here’s how you can implement a solution in **Java** to randomly pick a city **proportionally to its population**:

---

### ✅ **Java Solution: City Picker Based on Population**

```java
import java.util.*;

public class CityPicker {
    private List<String> cities = new ArrayList<>();
    private int[] prefixSums;
    private int totalPopulation;
    private Random random = new Random();

    public CityPicker(Map<String, Integer> cityPopulations) {
        prefixSums = new int[cityPopulations.size()];
        int i = 0;
        int runningSum = 0;

        for (Map.Entry<String, Integer> entry : cityPopulations.entrySet()) {
            cities.add(entry.getKey());
            runningSum += entry.getValue();
            prefixSums[i++] = runningSum;
        }

        totalPopulation = runningSum;
    }

    public String pickCity() {
        int target = random.nextInt(totalPopulation); // 0 to totalPopulation - 1
        int index = binarySearch(target);
        return cities.get(index);
    }

    private int binarySearch(int target) {
        int left = 0, right = prefixSums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target < prefixSums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    // Main method for testing
    public static void main(String[] args) {
        Map<String, Integer> cityPopulations = new LinkedHashMap<>();
        cityPopulations.put("NY", 5_000_000);
        cityPopulations.put("CA", 10_000_000);
        cityPopulations.put("WS", 2_000_000);

        CityPicker picker = new CityPicker(cityPopulations);

        // Frequency map for testing randomness
        Map<String, Integer> freq = new HashMap<>();
        for (int i = 0; i < 100_000; i++) {
            String city = picker.pickCity();
            freq.put(city, freq.getOrDefault(city, 0) + 1);
        }

        System.out.println("Sampling distribution over 100k trials:");
        for (Map.Entry<String, Integer> entry : freq.entrySet()) {
            System.out.printf("%s → %.2f%%\n", entry.getKey(), (entry.getValue() / 100000.0) * 100);
        }
    }
}
```

---

### 🧠 Key Notes

| Step             | Description                                   |
| ---------------- | --------------------------------------------- |
| Input            | `Map<String, Integer>` with city → population |
| Prefix Sum Array | Stores cumulative populations                 |
| Binary Search    | Finds city for a random number                |
| `pickCity()`     | O(log n) lookup                               |

---

### 📊 Sample Output (approximate)

```
Sampling distribution over 100k trials:
NY → 29.41%
CA → 58.83%
WS → 11.76%
```

*(Based on proportion: NY: 5M, CA: 10M, WS: 2M → Total: 17M)*

---

Let me know if you want this in **Python**, or if you want to make it thread-safe or support dynamic updates!


Here is the **Java version** of your Kotlin program using the **same approach** — `City` class with `population`, prefix sum array, and binary search to pick a city based on its population weight.

---

### ✅ Java Program: Pick Random City by Population

```java
import java.util.*;

public class RandomCityPicker {

    // ✅ City class to hold name and population
    static class City {
        String name;
        int population;

        public City(String name, int population) {
            this.name = name;
            this.population = population;
        }

        @Override
        public String toString() {
            return name + " (pop=" + population + ")";
        }
    }

    // ✅ RandomCity class handles prefix sum + weighted random pick
    static class RandomCity {
        private final List<City> cities;
        private final int[] prefixSums;
        private final int totalPopulation;
        private final Random random;

        public RandomCity(List<City> cities) {
            this.cities = cities;
            this.prefixSums = new int[cities.size()];
            this.random = new Random();

            int sum = 0;
            for (int i = 0; i < cities.size(); i++) {
                sum += cities.get(i).population;
                prefixSums[i] = sum;
            }
            this.totalPopulation = sum;
        }

        public City getRandomCity() {
            if (cities.isEmpty()) return null;

            double rand = random.nextDouble() * totalPopulation;
            int left = 0, right = prefixSums.length;

            while (left < right) {
                int mid = left + (right - left) / 2;
                if (rand >= prefixSums[mid]) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            return cities.get(left);
        }
    }

    // ✅ Test the logic
    public static void main(String[] args) {
        List<City> input = Arrays.asList(
                new City("NYC", 5),
                new City("LA", 10),
                new City("Moscow", 20),
                new City("SF", 30)
        );

        RandomCity picker = new RandomCity(input);

        System.out.println("Randomly picked cities:");
        for (int i = 0; i < 10; i++) {
            System.out.println(picker.getRandomCity());
        }
    }
}
```

---

### 🔍 Sample Output (varies every time):

```
Randomly picked cities:
SF (pop=30)
LA (pop=10)
SF (pop=30)
Moscow (pop=20)
SF (pop=30)
SF (pop=30)
LA (pop=10)
Moscow (pop=20)
```

---

### 🧠 Remember This Pattern

| Step | Logic                                      |
| ---- | ------------------------------------------ |
| 1    | Build prefix sum of populations            |
| 2    | Generate random `target` in `[0, total)`   |
| 3    | Binary search for smallest prefix ≥ target |
| 4    | Return that city                           |

---

Let me know if you want:

* Unit tests
* Frequency simulation
* Real-world JSON parser for city population file

This code is ready for interview or production.

