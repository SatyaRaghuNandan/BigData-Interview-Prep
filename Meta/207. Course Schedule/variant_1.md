
import java.util.*;

public class CourseScheduleVariant {

    public boolean canFinish(List<List<Integer>> graph) {
        int numCourses = graph.size();

        // Telugu: In-degrees calculate cheyyadam
        int[] indegrees = new int[numCourses];
        for (List<Integer> neighbors : graph) {
            for (int sequel : neighbors) {
                indegrees[sequel]++;
            }
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegrees[i] == 0) {
                queue.offer(i);
            }
        }

        int visited = 0;

        while (!queue.isEmpty()) {
            int course = queue.poll();
            visited++;

            for (int neighbor : graph.get(course)) {
                indegrees[neighbor]--;
                if (indegrees[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        return visited == numCourses;
    }
}
