Here are the **Java equivalents** of both the **Original** and the **Variant** versions of the `canFinish` method for **Course Schedule (Leetcode 207)**, with clean structure and inline comments.

---

## ✅ Original Java Version

> Input: `int numCourses`, `int[][] prerequisites`

```java
import java.util.*;

public class CourseScheduleOriginal {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // Step 1: Create graph and indegree array
        List<List<Integer>> graph = new ArrayList<>();
        int[] indegree = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        // Build graph: prerequisite[0] = course, prerequisite[1] = pre-req
        for (int[] pair : prerequisites) {
            int course = pair[0];
            int pre = pair[1];
            graph.get(pre).add(course);
            indegree[course]++;
        }

        // Step 2: Add all courses with indegree 0 into the queue
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        // Step 3: Process courses in topological order
        int visited = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            visited++;

            for (int neighbor : graph.get(course)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        // Step 4: Check if all courses were visited
        return visited == numCourses;
    }
}
```

---

## ✅ Variant Java Version

> Input: `List<List<Integer>> graph` (Adjacency List already built)

```java
import java.util.*;

public class CourseScheduleVariant {
    public boolean canFinish(List<List<Integer>> graph) {
        int numCourses = graph.size();
        int[] indegree = new int[numCourses];

        // Step 1: Build indegree array directly from the given graph
        for (List<Integer> neighbors : graph) {
            for (int neighbor : neighbors) {
                indegree[neighbor]++;
            }
        }

        // Step 2: Add all courses with indegree 0 into the queue
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        // Step 3: Process courses in topological order
        int visited = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            visited++;

            for (int neighbor : graph.get(course)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        // Step 4: Return true if all courses were visited
        return visited == numCourses;
    }
}
```

---

## 🧠 Summary Table

| Version  | Input Format                            | Builds Graph? | Builds Indegree? | Use Case                           |
| -------- | --------------------------------------- | ------------- | ---------------- | ---------------------------------- |
| Original | `int numCourses, int[][] prerequisites` | ✅ Yes         | ✅ Yes            | Leetcode 207                       |
| Variant  | `List<List<Integer>> graph`             | ❌ No          | ✅ Yes            | Leetcode 210 or Graph is pre-built |

---

Would you like test cases or helper methods to convert from prerequisites to graph?



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
