Perfect! Here's how you can build both test cases and helper methods to convert prerequisites to a graph for **both versions**.

---

## ✅ Helper Method: Convert `prerequisites[][]` to `Adjacency List`

Useful for the **Variant version**, where you're given the graph as a list.

```java
public class GraphBuilder {
    public static List<List<Integer>> buildAdjacencyList(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] pair : prerequisites) {
            int course = pair[0];
            int pre = pair[1];
            graph.get(pre).add(course); // pre → course
        }

        return graph;
    }
}
```

---

## ✅ Sample Test Driver for Both Versions

```java
public class CourseScheduleTest {
    public static void main(String[] args) {
        int numCourses = 4;
        int[][] prerequisites = {
            {1, 0},
            {2, 0},
            {3, 1},
            {3, 2}
        };

        // ✅ Test for Original Version
        CourseScheduleOriginal originalSolver = new CourseScheduleOriginal();
        boolean result1 = originalSolver.canFinish(numCourses, prerequisites);
        System.out.println("Original Version: Can finish all courses? " + result1);

        // ✅ Convert prerequisites to graph for Variant Version
        List<List<Integer>> graph = GraphBuilder.buildAdjacencyList(numCourses, prerequisites);

        // ✅ Test for Variant Version
        CourseScheduleVariant variantSolver = new CourseScheduleVariant();
        boolean result2 = variantSolver.canFinish(graph);
        System.out.println("Variant Version: Can finish all courses? " + result2);
    }
}
```

---

## 🧪 Sample Outputs

Given this test case:

```java
int[][] prerequisites = {
    {1, 0},
    {2, 0},
    {3, 1},
    {3, 2}
};
```

There are **no cycles**, so output will be:

```
Original Version: Can finish all courses? true
Variant Version: Can finish all courses? true
```

---

## ❗ Bonus Test Case with Cycle

Try this instead:

```java
int[][] prerequisites = {
    {1, 0},
    {0, 1}  // ← cycle
};
```

Output:

```
Original Version: Can finish all courses? false
Variant Version: Can finish all courses? false
```

---

Let me know if you'd like to add **topological sort order** for Leetcode 210 or convert this into a reusable class-based structure for interviews.
