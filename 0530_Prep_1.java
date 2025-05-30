package MYPow_50;

public class MyPOW_1 {

/*
    I couldn't find a clear explanation for an interative Log(n) solution so here's mine. The basic idea is to decompose the exponent into powers of 2, so that you can keep dividing the problem in half. For example, lets say

            N = 9 = 2^3 + 2^0 = 1001 in binary. Then:

    x^9 = x^(2^3) * x^(2^0)

    We can see that every time we encounter a 1 in the binary representation of N, we need to multiply the answer with x^(2^i) where i is the ith bit of the exponent. Thus, we can keep a running total of repeatedly squaring x - (x, x^2, x^4, x^8, etc) and multiply it by the answer when we see a 1.

    To handle the case where N=INTEGER_MIN we use a long (64-bit) variable. Below is solution:
*/

    public class Solution {
        public double MyPow(double x, int n) {
            double ans = 1;
            long absN = Math.abs((long) n);
            while (absN > 0) {
                if ((absN & 1) == 1) ans *= x;
                absN >>= 1;
                x *= x;
            }
            return n < 0 ? 1 / ans : ans;
        }
    }



    /* This is a simple solution based on divide and conquer */

    public class Solution1RecurSive {
        public double pow(double x, int m) {
            double temp = x;
            if (m == 0) return 1;
            temp = pow(x, m / 2);
            if (m % 2 == 0) return temp * temp;
            else {
                if (m > 0) return x * temp * temp;
                else return (temp * temp) / x;
            }

        }
    }


    public double pow(double x, int n) {
        if (n < 0) {
            n = -n;
            x = 1 / x;
        }
        double result = 1;
        for (double f = x; n > 0; n = n >> 1) {
            if (n % 2 == 1) {
                result *= f;
            }
            f = f * f;
        }
        return result;
    }

    class Solution2 {
        public double myPow(double x, int n) {
            long N = n;
            if (N < 0) {
                x = 1 / x;
                N = -N;
            }
            double ans = 1;
            for (long i = 0; i < N; i++)
                ans = ans * x;
            return ans;
        }
    }


    class Solution33 {
        private double fastPow(double x, long n) {
            if (n == 0) {
                return 1.0;
            }
            double half = fastPow(x, n / 2);
            if (n % 2 == 0) {
                return half * half;
            } else {
                return half * half * x;
            }
        }

        public double myPow(double x, int n) {
            long N = n;
            if (N < 0) {
                x = 1 / x;
                N = -N;
            }

            return fastPow(x, N);
        }
    }

    class Solution4 {
        public double myPow(double x, int n) {
            long N = n;
            if (N < 0) {
                x = 1 / x;
                N = -N;
            }
            double ans = 1;
            double current_product = x;
            for (long i = N; i > 0; i /= 2) {
                if ((i % 2) == 1) {
                    ans = ans * current_product;
                }
                current_product = current_product * current_product;
            }
            return ans;
        }
    }

}



Merge 3 sorted arrays - both positives and negatives


    import java.util.*;

public class MergeSortedArrays {
    static class Element {
        int value, arrayIndex, elementIndex;
        Element(int value, int arrayIndex, int elementIndex) {
            this.value = value;
            this.arrayIndex = arrayIndex;
            this.elementIndex = elementIndex;
        }
    }

    public static List<Integer> mergeSortedArrays(List<List<Integer>> arrays) {
        PriorityQueue<Element> minHeap = new PriorityQueue<>(Comparator.comparingInt(e -> e.value));
        List<Integer> result = new ArrayList<>();

        // Add first element from each array to heap
        for (int i = 0; i < arrays.size(); i++) {
            if (!arrays.get(i).isEmpty()) {
                minHeap.add(new Element(arrays.get(i).get(0), i, 0));
            }
        }

        while (!minHeap.isEmpty()) {
            Element current = minHeap.poll();
            result.add(current.value);

            int nextIndex = current.elementIndex + 1;
            if (nextIndex < arrays.get(current.arrayIndex).size()) {
                minHeap.add(new Element(arrays.get(current.arrayIndex).get(nextIndex), current.arrayIndex, nextIndex));
            }
        }

        return result;
    }

    public static void main(String[] args) {
        List<List<Integer>> arrays = Arrays.asList(
            Arrays.asList(-10, -1, 5, 9),
            Arrays.asList(-3, 0, 2, 11),
            Arrays.asList(-2, 4, 6, 8)
        );

        List<Integer> merged = mergeSortedArrays(arrays);
        System.out.println(merged); // Output: [-10, -3, -2, -1, 0, 2, 4, 5, 6, 8, 9, 11]
    }
}


import heapq

def merge_sorted_arrays(arrays):
    heap = []
    result = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    while heap:
        val, arr_idx, ele_idx = heapq.heappop(heap)
        result.append(val)

        if ele_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][ele_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, ele_idx + 1))

    return result

# Example usage:
arrays = [[-10, -1, 5, 9], [-3, 0, 2, 11], [-2, 4, 6, 8]]
print(merge_sorted_arrays(arrays))
# Output: [-10, -3, -2, -1, 0, 2, 4, 5, 6, 8, 9, 11]



    class Solution {
    public boolean validPalindrome(String s) {
             return isPalindromeWithChance(s, 0, s.length() - 1, true);
    }

    private boolean isPalindromeWithChance(String s, int left, int right, boolean canDelete) {
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                if (!canDelete) return false;
                // Try deleting one character: either left or right
                return isPalindromeWithChance(s, left + 1, right, false) ||
                       isPalindromeWithChance(s, left, right - 1, false);
            }
            left++;
            right--;
        }
        return true;
    }
}


class Solution {
    public boolean isPalindrome(String s) {
        // Get the words from the phrase. Remove all extra Chars. 
        int start = 0;
        int end = s.length() - 1;
        
        
        while (start <= end) {
            char charAtStart = s.charAt(start);
            char charAtEnd = s.charAt(end);
            if (!Character.isLetterOrDigit(charAtStart)) {
                start++;
            } else if (!Character.isLetterOrDigit(charAtEnd)) {
                end--;
            } else {
                if (Character.toLowerCase(charAtStart) != Character.toLowerCase(charAtEnd)) {
                    return false;
                }
                start++;
                end--;
            }
        }
        return true;
    }
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<int[]> nodeList = new ArrayList<>();
        traverse(root,0 ,0,nodeList);
        nodeList.sort((a,b) -> {
            if(a[0] != b[0])return a[0] - b[0];
            if(a[1] != b[1])return a[1] - b[1];
            else return a[2] - b[2];
        });

        List<List<Integer>> result = new ArrayList<>();
        int prev = Integer.MIN_VALUE;

        for(int i = 0 ; i < nodeList.size() ; i++){
            int[] entry = nodeList.get(i);
            int x = entry[0], val = entry[2];

            if(x != prev){
                result.add(new ArrayList<>());
                prev = x;
            }

            result.get(result.size() -1).add(val);
        }
        return result;
    }

    public void traverse(TreeNode root , int x , int y , List<int[]> nodeList){
        // y -> depth   x -> vertical order
        if(root == null)return;
        nodeList.add(new int[]{x,y,root.val});
        traverse(root.left,x-1,y+1,nodeList);
        traverse(root.right,x+1,y+1,nodeList);
    }
}




class Solution {

    private boolean[] visited;
    private boolean[] cycles;
    //private final ArrayList<Integer> result = new ArrayList<>();
    private int[] result;
    private int resultPointer;

    private List<Integer>[] buildGraph(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new List[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<Integer>();
        }
        for (int[] p : prerequisites) {
            graph[p[1]].add(p[0]);
        }
        return graph;
    }

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        var graph = buildGraph(numCourses, prerequisites);
        result = new int[numCourses];
        resultPointer = numCourses;
        visited = new boolean[numCourses];
        cycles = new boolean[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (hasCycleDFS(i, graph)) {
                return new int[0];
            }
        }
        return result;
    }

    public boolean hasCycleDFS(int current, List<Integer>[] graph) {
        if (cycles[current]) {
            return true;
        }
        if (visited[current]) {
            return false;
        }
        cycles[current] = true;
        visited[current] = true;
        
        for (int successor : graph[current]) {
            if (hasCycleDFS(successor, graph)) {
                return true;
            }
        }
        result[--resultPointer] = current;

        // Successors don't lead to cycles, so reset
        cycles[current] = false;
        return false;
    }
}

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // first task is to create graph..
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0 ; i < numCourses; i++){
            graph.add(new ArrayList<>());
        }
        for(int i = 0 ; i < prerequisites.length; i++){
            graph.get(prerequisites[i][1]).add(prerequisites[i][0]);
        }

        // create an indegree array for each node...
        int[] indegree = new int[numCourses];
        for(int i = 0; i < numCourses ; i++){
            for(int node : graph.get(i)){
                indegree[node]++;
            }
        }

        // now adding node to q, which have indegree 0...
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i < indegree.length; i++){
            if(indegree[i] == 0){
                q.add(i);
            }
        }


        // topological sorted array..
        int[] ts = new int[numCourses];
        int i = 0;
        
        while(!q.isEmpty()){
            int node = q.remove();
            ts[i++] = node;

            for(int nbr : graph.get(node)){
                indegree[nbr]--;
                if(indegree[nbr] == 0){
                    q.add(nbr);
                }
            }

        }
        if(i == 0 || i < numCourses) return new int[]{};
        return ts;
    }
}


class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // first task is to create graph..
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0 ; i < numCourses; i++){
            graph.add(new ArrayList<>());
        }
        for(int i = 0 ; i < prerequisites.length; i++){
            graph.get(prerequisites[i][1]).add(prerequisites[i][0]);
        }

        // create an indegree array for each node...
        int[] indegree = new int[numCourses];
        for(int i = 0; i < numCourses ; i++){
            for(int node : graph.get(i)){
                indegree[node]++;
            }
        }

        // now adding node to q, which have indegree 0...
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i < indegree.length; i++){
            if(indegree[i] == 0){
                q.add(i);
            }
        }


        // topological sorted array..
        int[] ts = new int[numCourses];
        int i = 0;
        
        while(!q.isEmpty()){
            int node = q.remove();
            ts[i++] = node;

            for(int nbr : graph.get(node)){
                indegree[nbr]--;
                if(indegree[nbr] == 0){
                    q.add(nbr);
                }
            }

        }
        if(i == 0 || i < numCourses) return new int[]{};
        return ts;
    }
}





