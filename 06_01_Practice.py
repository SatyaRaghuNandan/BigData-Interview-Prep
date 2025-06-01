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


