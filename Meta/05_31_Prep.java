class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        """
        Converts a sentence to 'Goat Latin' based on the following rules:
        1. If a word starts with a vowel, append "ma" to the end.
        2. If a word starts with a consonant, move the first letter to the end, then append "ma".
        3. Add one 'a' for the first word, two 'a's for the second word, and so on.
        """

        # Step 1: Split the sentence into individual words
        words = sentence.split()

        # Step 2: Define the set of vowels (both lowercase and uppercase)
        vowels = set('aeiouAEIOU')

        # Step 3: Prepare an empty list to collect transformed words
        result = []

        # Step 4: Word position counter (starts from 1 as per rules)
        i = 1

        # Step 5: Loop through each word in the list
        for word in words:
            if word[0] in vowels:
                # Case 1: Word starts with a vowel
                newword = word + "ma"
            else:
                # Case 2: Word starts with a consonant
                # Move the first letter to the end, then add "ma"
                newword = word[1:] + word[0] + "ma"

            # Step 6: Add 'a' repeated 'i' times to the end of the word
            newword += 'a' * i

            # Step 7: Add the transformed word to the result list
            result.append(newword)

            # Step 8: Increment the counter for the next word
            i += 1

        # Step 9: Join all the transformed words into a single string separated by spaces
        return ' '.join(result)



class Solution {
    public char[][] updateBoard(char[][] board, int[] click) {
        // If the clicked cell is a mine, reveal it as 'X' and end the game
        if (board[click[0]][click[1]] == 'M') {
            board[click[0]][click[1]] = 'X';
            return board;
        }

        // Otherwise, recursively reveal the board
        reveal(board, click[0], click[1]);
        return board;
    }

    private void reveal(char[][] board, int i, int j) {
        // If the indices are out of bounds or the cell is already revealed, return
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length || board[i][j] != 'E') {
            return;
        }

        // Temporarily mark as '0' to count adjacent mines
        board[i][j] = '0';

        // All 8 possible directions from the current cell
        int[][] neighbors = {
            {i - 1, j - 1}, {i - 1, j}, {i - 1, j + 1},
            {i, j - 1},               {i, j + 1},
            {i + 1, j - 1}, {i + 1, j}, {i + 1, j + 1}
        };

        // Count number of adjacent mines
        for (int[] neighbor : neighbors) {
            int x = neighbor[0], y = neighbor[1];
            if (x >= 0 && y >= 0 && x < board.length && y < board[0].length) {
                if (board[x][y] == 'M') {
                    board[i][j]++;  // Implicitly increments from '0' to '1', '2', etc.
                }
            }
        }

        // If any mines are adjacent, leave the digit and stop recursion
        if (board[i][j] != '0') {
            return;
        }

        // If no adjacent mines, mark as 'B' and continue revealing neighbors
        board[i][j] = 'B';
        for (int[] neighbor : neighbors) {
            reveal(board, neighbor[0], neighbor[1]);
        }
    }
}



from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        self.reveal(board, click[0], click[1])
        return board

    def reveal(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'E':
            return

        board[i][j] = '0'
        neighbors = [
            (i-1, j-1), (i-1, j), (i-1, j+1),
            (i, j-1),           (i, j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1)
        ]

        for x, y in neighbors:
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'M':
                board[i][j] = chr(ord(board[i][j]) + 1)

        if board[i][j] != '0':
            return

        board[i][j] = 'B'
        for x, y in neighbors:
            self.reveal(board, x, y)

# Test
board = [
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'M', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'E']
]
click = [3, 0]

sol = Solution()
updated = sol.updateBoard(board, click)

for row in updated:
    print(row)


from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Initialize graph and indegree
        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        # Step 2: Build graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""  # Invalid prefix case
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        # Step 3: BFS Topological Sort (Kahn's Algorithm)
        queue = deque([c for c in indegree if indegree[c] == 0])
        result = []

        while queue:
            c = queue.popleft()
            result.append(c)
            for neighbor in graph[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If result doesn't include all letters, graph has a cycle
        if len(result) != len(indegree):
            return ""

        return ''.join(result)



import java.util.*;

class Solution {
    public String alienOrder(String[] words) {
        // Graph: key is a char, value is set of next chars (outgoing edges)
        Map<Character, Set<Character>> graph = new HashMap<>();
        // Indegree map to help with topological sort
        Map<Character, Integer> indegree = new HashMap<>();

        // Initialize graph with all characters
        for (String word : words) {
            for (char c : word.toCharArray()) {
                graph.putIfAbsent(c, new HashSet<>());
                indegree.putIfAbsent(c, 0);
            }
        }

        // Build the graph based on order differences between adjacent words
        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i];
            String w2 = words[i + 1];
            // Invalid prefix case: e.g., "abc", "ab"
            if (w1.length() > w2.length() && w1.startsWith(w2)) {
                return "";
            }
            int len = Math.min(w1.length(), w2.length());
            for (int j = 0; j < len; j++) {
                char c1 = w1.charAt(j), c2 = w2.charAt(j);
                if (c1 != c2) {
                    // Add edge only if not already present
                    if (graph.get(c1).add(c2)) {
                        indegree.put(c2, indegree.get(c2) + 1);
                    }
                    break;
                }
            }
        }

        // Topological Sort using BFS (Kahn's Algorithm)
        Queue<Character> queue = new LinkedList<>();
        for (char c : indegree.keySet()) {
            if (indegree.get(c) == 0) queue.offer(c);
        }

        StringBuilder result = new StringBuilder();
        while (!queue.isEmpty()) {
            char current = queue.poll();
            result.append(current);
            for (char neighbor : graph.get(current)) {
                indegree.put(neighbor, indegree.get(neighbor) - 1);
                if (indegree.get(neighbor) == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        // If not all characters are in the result, there's a cycle
        if (result.length() != indegree.size()) return "";

        return result.toString();
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



class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]

        def partition(A, l, r):
            pivot = A[r]
            p = l
            for i in range(l, r):
                if A[i] < pivot:
                    A[i], A[p] = A[p], A[i]
                    p += 1
            A[p], A[r] = A[r], A[p]
            return p

        def quickselect(A, l, r):
            if l < r:
                p = partition(A, l, r)
                if p < k:
                    quickselect(A, p + 1, r)
                elif p > k:
                    quickselect(A, l, p - 1)

        quickselect(heap, 0, len(heap) - 1)
        top_k = sorted(heap[:k])
        return [word for _, word in top_k]

from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        # ప్రతి పదానికి గణన (frequency) లెక్కించటం
        count = Counter(words)

        # (frequency ని negative గా తీసుకుని, పదం) format లో లిస్ట్ తయారుచేస్తాం
        # దీని వల్ల మనం descending order లో sort చేయగలం
        heap = [(-freq, word) for word, freq in count.items()]

        # partition function: Quickselect కోసం array ని భాగాలుగా విడగొట్టటం
        def partition(arr, left, right):
            pivot = arr[right]
            i = left
            for j in range(left, right):
                # pivot కంటే చిన్నదైతే, ఎడమ వైపుకి మార్చటం
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            # pivot ని సరైన స్థానం లో పెట్టటం
            arr[i], arr[right] = arr[right], arr[i]
            return i

        # Quickselect function: top-k elements ని ముందుగా తెస్తుంది
        def quickselect(arr, left, right):
            if left < right:
                pivot_index = partition(arr, left, right)
                if pivot_index < k:
                    quickselect(arr, pivot_index + 1, right)
                elif pivot_index > k:
                    quickselect(arr, left, pivot_index - 1)
                # pivot_index == k అయితే, ముందున్నవి top-k

        # Quickselect ని ఉపయోగించి top-k elements ముందు తీసుకొస్తాం
        quickselect(heap, 0, len(heap) - 1)

        # మొదటి k elements ని sort చేసి ఫలితాన్ని తయారుచేస్తాం
        top_k = sorted(heap[:k])

        # ప్రతి tuple నుండి పదాన్ని మాత్రమే తీసుకొని final list return చేయటం
        return [word for _, word in top_k]

      
