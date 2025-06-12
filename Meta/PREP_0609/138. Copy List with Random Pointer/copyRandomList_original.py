from typing import Optional

class Solution:
    class Node:
        def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
            self.val = int(x)
            self.next = next
            self.random = random

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        visited = {}  # Original node → new node mapping store cheyyali

        def dfs(head):
            if head is None:
                return None  # Base case: None node ki None return cheyyali

            if head in visited:
                return visited[head]  
                # Already copy chesina node unte, direct ga return cheyyali 
                # (to handle cycles and shared randoms)

            # Node create cheyyadam (val copy cheyyadam)
            node = Solution.Node(head.val)

            # Mapping maintain cheyyali: original → copy
            visited[head] = node

            # Recursive call for next and random pointers
            node.next = dfs(head.next)      # Next node ki copy
            node.random = dfs(head.random)  # Random node ki copy

            return node  # Final ga new node return cheyyadam

        return dfs(head)  # DFS ni original head nundi start cheddam



