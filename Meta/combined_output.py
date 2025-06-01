# ---- File: 1004. Max Consecutive Ones III\longestOnes.py ----
# https://leetcode.com/problems/max-consecutive-ones-iii/

# https://www.youtube.com/watch?v=OPV49AuP9lQ

# https://www.youtube.com/watch?v=97oTiOCuxho

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

 

# Constraints:

#     1 <= nums.length <= 105
#     nums[i] is either 0 or 1.
#     0 <= k <= nums.length

from typing import List

# Approach 1:

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLen = 0

        for right, num in enumerate(nums):
            k -= 1 - num
            if k < 0:
                k += 1 - nums[left]
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen


# Approach 2:
    
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1

                left += 1

            right += 1
        return right - left


# ---- File: 1047. Remove All Adjacent Duplicates In String\removeDuplicates.py ----
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# https://www.youtube.com/watch?v=Ec2SJvjxYEs

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

# Example 1:

# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

# Example 2:

# Input: s = "azxxzy"
# Output: "ay"

 

# Constraints:

#     1 <= s.length <= 105
#     s consists of lowercase English letters.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if not stack or char != stack[-1]:
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)
    
    # T and S : O(N)
    

# ---- File: 1091. Shortest Path in Binary Matrix\shortestPathBinaryMatrix.py ----
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

# https://www.youtube.com/watch?v=Y2F8EGP3OA4

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

#     All the visited cells of the path are 0.
#     All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 2

# Example 2:

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1

 

# Constraints:

#     n == grid.length
#     n == grid[i].length
#     1 <= n <= 100
#     grid[i][j] is 0 or 1

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        queue = [(0, 0, 1)]  # row, column, and length
        grid[0][0] = 1

        for r, c, l in queue:
            if r == n - 1 and c == n - 1:
                return l

            directions = [
                (r - 1, c), (r - 1, c - 1), (r - 1, c + 1),
                (r, c - 1), (r, c + 1),
                (r + 1, c), (r + 1, c - 1), (r + 1, c + 1)
            ]

            for x, y in directions:
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    queue.append([x, y, l + 1])
        return -1

# T - O(N)
# S - O(N)
    
# Follow-up: If asked to print the path, rather than the length:
    
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        if grid[0][0] or grid[n - 1][n - 1]:
            return []

        queue = [(0, 0, [(0, 0)])]  # row, column, and path
        grid[0][0] = 1

        while queue:
            r, c, path = queue.pop(0)

            if r == n - 1 and c == n - 1:
                return path

            directions = [
                (r - 1, c), (r - 1, c - 1), (r - 1, c + 1),
                (r, c - 1), (r, c + 1),
                (r + 1, c), (r + 1, c - 1), (r + 1, c + 1)
            ]

            for x, y in directions:
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    queue.append((x, y, path + [(x, y)]))

        return []

# ---- File: 1249. Minimum Remove to Make Valid Parentheses\minRemoveToMakeValid.py ----
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# https://www.youtube.com/watch?v=FTo1kDyE-h4

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

#     It is the empty string, contains only lowercase characters, or
#     It can be written as AB (A concatenated with B), where A and B are valid strings, or
#     It can be written as (A), where A is a valid string.

 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

 

# Constraints:

#     1 <= s.length <= 105
#     s[i] is either'(' , ')', or lowercase English letter.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        S = list(s)

        for i in range(len(S)):
            if S[i] == "(":
                stack.append(i)
            elif S[i] == ")":
                if stack:
                    stack.pop()
                else:
                    S[i] = ""

        for j in stack:
            S[j] = ""

        return "".join(S)


# ---- File: 125. Valid Palindrome\#1 isPalindrome.py ----
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

 

# Constraints:

#     1 <= s.length <= 2 * 105
#     s consists only of printable ASCII characters.

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)

        s_reversed = s[::-1]

        if (s == s_reversed):
            return True
        return False

# ---- File: 125. Valid Palindrome\#2 isPalindrome.py ----
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

 

# Constraints:

#     1 <= s.length <= 2 * 105
#     s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""

        for c in s:
            if c.isalnum():
                s_new += c.lower()
        return s_new == s_new[::-1]


# ---- File: 125. Valid Palindrome\#3 isPalindrome.py ----
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

 

# Constraints:

#     1 <= s.length <= 2 * 105
#     s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the beginning and end of the string
        l, r = 0, len(s) - 1

        # Iterate until the two pointers meet
        while l < r:
            # Move the left pointer to the next alphanumeric character
            while l < r and not self.isAlphaNum(s[l]):
                l += 1

            # Move the right pointer to the next alphanumeric character
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1

            # Check if the corresponding characters are equal (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False

            # Move the pointers towards each other
            l += 1
            r -= 1

        # If the loop completes, the string is a palindrome
        return True

    def isAlphaNum(self, c):
        # Check if a character is alphanumeric (letters or digits)
        return (
            ord('A') <= ord(c) <= ord('Z')
            or ord('0') <= ord(c) <= ord('9')
            or ord('a') <= ord(c) <= ord('z')
        )


# ---- File: 129. Sum Root to Leaf Numbers\sumNumbers.py ----
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# https://www.youtube.com/watch?v=Jk16lZGFWxE

# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

#     For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

 

# Example 1:

# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Example 2:

# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

 

# Constraints:

#     The number of nodes in the tree is in the range [1, 1000].
#     0 <= Node.val <= 9
#     The depth of the tree will not exceed 10.

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(curr, sum):
            if not curr:
                return 0

            sum = sum * 10 + curr.val

            if not curr.left and not curr.right:
                return sum

            left = dfs(curr.left, sum)
            right = dfs(curr.right, sum)

            return left + right

        return dfs(root, 0)


# ---- File: 133. Clone Graph\cloneGraph.py ----
# https://leetcode.com/problems/clone-graph/

# https://www.youtube.com/watch?v=vXkT2nYSde0

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

# Example 1:

# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Example 2:

# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

# Example 3:

# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.

 

# Constraints:

#     The number of nodes in the graph is in the range [0, 100].
#     1 <= Node.val <= 100
#     Node.val is unique for each node.
#     There are no repeated edges and no self-loops in the graph.
#     The Graph is connected and all nodes can be visited starting from the given node.

import collections

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Using BFS, #T and #S: O(N)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # 1st: It maps old value to new cloned values
        # 2nd: Also acts as a visited set
        cloned_map = {}
        cloned_map[node] = Node(node.val, [])

        queue = collections.deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in cloned_map:
                    cloned_map[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                cloned_map[curr].neighbors.append(cloned_map[neighbor]) # initially [] empty
        return cloned_map[node]

# ---- File: 138. Copy List with Random Pointer\copyRandomList.py ----
# https://leetcode.com/problems/copy-list-with-random-pointer/

# https://www.youtube.com/watch?v=g7U-FPBR_gQ

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

#     val: an integer representing Node.val
#     random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

# Your code will only be given the head of the original linked list.

 

# Example 1:

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:

# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:

# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

 

# Constraints:

#     0 <= n <= 1000
#     -104 <= Node.val <= 104
#     Node.random is null or is pointing to some node in the linked list.


from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Mid-Efficient approach would be using a Hashmap (O(N) space) and do two passes:
# i) generate a new list / has old -> new
# ii) update the new list with new nodes for random

# Efficient Approach : O(1) Space - USING INTERWEAVING NODES
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        dummy.next = head
        curr = head

        # Step One: Interweave (Connect) Nodes
        while curr:
            tmp = Node(curr.val)
            tmp.next = curr.next
            curr.next = tmp
            curr = tmp.next
        curr = head

        # Step Two: Update Random
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = dummy
        old = head
        # Step Three: Remove Old Nodes
        while old:
            curr.next = old.next
            curr = old
            old = curr.next
        return dummy.next

# ---- File: 146. LRU Cache\LRUCache.py ----
# https://leetcode.com/problems/lru-cache/description/

# https://www.youtube.com/watch?v=7ABFKPK2hD4

# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

#     LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#     int get(int key) Return the value of the key if the key exists, otherwise return -1.
#     void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

 

# Constraints:

#     1 <= capacity <= 3000
#     0 <= key <= 104
#     0 <= value <= 105
#     At most 2 * 105 calls will be made to get and put.

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key to node (not val, it's a reference)

        # left = LRU, right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    # remove node from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # add node to the right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # to check if it exceeds capacity
        if len(self.cache) > self.cap:
            # remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ---- File: 15. 3Sum\threeSum.py ----
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

 

# Constraints:

#     3 <= nums.length <= 3000
#     -105 <= nums[i] <= 105

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


# ---- File: 1539. Kth Missing Positive Number\findKthPositive.py ----
# https://leetcode.com/problems/kth-missing-positive-number/

# https://www.youtube.com/watch?v=R15876l3tSE

# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

 

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

# Example 2:

# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

 

# Constraints:

#     1 <= arr.length <= 1000
#     1 <= arr[i] <= 1000
#     1 <= k <= 1000
#     arr[i] < arr[j] for 1 <= i < j <= arr.length

 

# Follow up:

# Could you solve this problem in less than O(n) complexity?

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] != 1:
            if arr[0] - 1 >= k:
                return k
            else: # decrement k by however many numbers are missing
                k -= arr[0] - 1
        
        i = 0

        while i < len(arr) - 1:
            diff = arr[i + 1] - arr[i]

            if diff != 1:
                for num in range(arr[i] + 1, arr[i + 1]):
                    k -= 1

                    if not k:
                        return num
            i += 1
        
        if k:
            return arr[-1] + k
        
        # T : O(N)
        # S : O(1)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Initialize the left and right pointers
        left, right = 0, len(arr) - 1
        
        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2
            
            # Calculate the number of missing positive integers before mid
            missing_before_mid = arr[mid] - mid - 1
            
            # Adjust the pointers based on the missing count
            if missing_before_mid < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # Return the kth missing positive integer
        return left + k

        # T : O(logn)
        # S : O(1)


# ---- File: 1570. Dot Product of Two Sparse Vectors\solution.py ----
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/

# https://www.youtube.com/watch?v=sQNN4xKC1mA

# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

#     SparseVector(nums) Initializes the object with the vector nums
#     dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

 

# Example 1:

# Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

# Example 2:

# Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
# Output: 0
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

# Example 3:

# Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
# Output: 6

 

# Constraints:

#     n == nums1.length == nums2.length
#     1 <= n <= 10^5
#     0 <= nums1[i], nums2[i] <= 100

from typing import List

# 1st Solution: Naive Approach - Loop through each vector and formulate dot product
# 2nd Solution: Non-Naive but not best as well - Use HashMap to store non-zero values in the form : non-zero index: value

# 3rd Solution(Below): Use Tuples since HashMap's can be terrible sometimes and interviewer may expect a more efficient solution with a follow-up question. Tuple is the answer:

class SparseVector:
    def __init__(self, nums: List[int]):

        self.nums = []

        for i, num in enumerate(nums):
            if num:
                self.nums.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:

        resProduct = 0
        i = j = 0

        while i < len(self.nums) and j < len(vec.nums):
            i_idx, i_val = self.nums[i]
            j_idx, j_val = vec.nums[j]

            if i_idx == j_idx:
                resProduct += i_val * j_val
                i += 1
                j += 1
            elif i_idx > j_idx:
                j += 1
            else:
                i += 1
        return resProduct
    
# T and S - O(N + M)
# If Follow up is asked in an interview: the answer is use Binary Search


# ---- File: 162. Find Peak Element\findPeakElement.py ----
# https://leetcode.com/problems/find-peak-element/description/

# https://www.youtube.com/watch?v=GAJITCneCPE

# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

 

# Constraints:

#     1 <= nums.length <= 1000
#     -231 <= nums[i] <= 231 - 1
#     nums[i] != nums[i + 1] for all valid i.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + ((r - l)) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l # or return r, doesn't matter

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]: #Time-Complexity: O(log(m) * n
                                                               #Space-Complexity: O(1)
        
        #Approach: You can think of this problem in two ways! Either column-based or row-based! 
        
        #Idea is that we perform binary search on mat grid and utilize search space on rows. ROW BASED
        #for the current middle row we are on, find the maximum element, as it will be bigger than
        #both of its left and right neighboring elements. To verify this element is a peak, we need
        #to make sure that it is also bigger than the immediate top and bottom neighboring elements!
        
        #however, we need to be careful of the bottom and top neighboring elements being out of bounds!
        #in this case, the current peak candidate will always be bigger than such elements since
        #all elements within mat are guaranteed to be positive numbers!
        #Right when we find peak element, we should return its position immediately!
        
        #define my search space by row!
        L, H = 0, len(mat) - 1
        #as long as we have at least one row left to consider, continue binary search!
        while L <= H:
            mid = (L + H) // 2
            mid_row = mat[mid]
            #initialize max_pos and store column pos later!
            max_pos = None
            max_val = float(-inf)
            #iterate linearly through the row since it's not sorted and find the maximum element as well
            #as its position!
            for j in range(len(mid_row)):
                if(mid_row[j] > max_val):
                    max_val = mid_row[j]
                    max_pos = j
                    continue
            #once we have max_pos, then we have to compare relative to top and bottom neighbors!
            top_val = -1 if mid - 1 < 0 else mat[mid-1][max_pos]
            bottom_val = -1 if mid + 1 >= len(mat) else mat[mid+1][max_pos]
            #then it's a peak!
            if(top_val < max_val and bottom_val < max_val):
                return [mid, max_pos]
            #top neighboring element is bigger! -> it has better chance to be peak element!
            if(top_val >= max_val):
                H = mid - 1 
                continue
            if(bottom_val >= max_val):
                L = mid + 1
                continue


# ---- File: 1644. Lowest Common Ancestor of a Binary Tree II\lowestCommonAncestor.py ----
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

# https://www.youtube.com/watch?v=7csj-Elpmmo&t=755s

# Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

 

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.

# Example 3:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
# Output: null
# Explanation: Node 10 does not exist in the tree, so return null.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_found = False
        self.q_found = False

        ans = self.dfs(root, p, q)

        if self.p_found and self.q_found:
            return ans
        return None # return null if p or q doesn't exist in the tree

    # do a post-order traversal: left -> right -> node to first check p_found and q_found are true
    # then return the LCA value if both are true and there
    def dfs(self, node, p, q):
        if not node:
            return None
        
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)

        if node == p or node == q:
            if node == p:
                self.p_found = True
            else:
                self.q_found = True
            return node

        if left and right:
            return node
        else:
            return left or right 

        # T : O(N)
        # S : O(N)


# ---- File: 1650. Lowest Common Ancestor of a Binary Tree III\lowestCommonAncestor.py ----
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

# https://www.youtube.com/watch?v=vZxxksAP8yk

# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

# Each node will have a reference to its parent node. The definition for Node is below:

# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }

# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.

# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1

 

# Constraints:

#     The number of nodes in the tree is in the range [2, 105].
#     -109 <= Node.val <= 109
#     All Node.val are unique.
#     p != q
#     p and q exist in the tree.

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Naive Approach - Using Extra Space (Set) to store seen nodes : O(N)

        seenNodes = set()

        while p:
            seenNodes.add(p)
            p = p.parent
        
        while q:
            if q in seenNodes:
                return q
            else:
                q = q.parent

# ----
                
class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        # Efficient Approach - Using p_copy and q_copy : O(1) Space

        p_copy = p
        q_copy = q

        while p_copy != q_copy:
            if p_copy:
                p_copy = p_copy.parent
            else:
                p_copy = q

            if q_copy:
                q_copy = q_copy.parent
            else:
                q_copy = p
        return p_copy


# ---- File: 1762. Buildings With an Ocean View\findBuildings.py ----
# https://leetcode.com/problems/buildings-with-an-ocean-view/

# https://www.youtube.com/watch?v=0UdQeXMjAFk

# There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

# Example 1:

# Input: heights = [4,2,3,1]
# Output: [0,2,3]
# Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

# Example 2:

# Input: heights = [4,3,2,1]
# Output: [0,1,2,3]
# Explanation: All the buildings have an ocean view.

# Example 3:

# Input: heights = [1,3,2,4]
# Output: [3]
# Explanation: Only building 3 has an ocean view.

 

# Constraints:

#     1 <= heights.length <= 105
#     1 <= heights[i] <= 109

from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = [len(heights) - 1]
        max_height = heights[-1]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_height:
                stack.append(i)
                max_height = heights[i]
        return stack[::-1]


# ---- File: 199. Binary Tree Right Side View\rightSideView.py ----
# https://leetcode.com/problems/binary-tree-right-side-view/description/

# https://www.youtube.com/watch?v=op8-7RWwL1A

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]

# Example 3:

# Input: root = []
# Output: []

 

# Constraints:

#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        res = []

        while queue:
            levelLen = len(queue)

            for i in range(levelLen):
                node = queue.popleft()

                if i == levelLen - 1: # 0 if asked left side view
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

# T - O(N), S - O(N)

# ---- File: 200. Number of Islands\numIslands.py ----
# https://leetcode.com/problems/number-of-islands/description/

# https://www.youtube.com/watch?v=BJ8KHYx_hXc

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

 

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 300
#     grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def island_to_zero(grid, r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                grid[r][c] = "0"

                for row_inc, col_inc in directions:
                    island_to_zero(grid, r + row_inc, c + col_inc)

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    island_count += 1
                    island_to_zero(grid, row, column)
        return island_count

        # T = O(R * C)
        # S = O(R * C), O(1) if not counting stack frames

# ---- File: 215. Kth Largest Element in an Array\findKthLargest.py ----
# https://leetcode.com/problems/kth-largest-element-in-an-array/

# https://www.youtube.com/watch?v=AzDs7qV1ugA&t=336s

# https://www.youtube.com/watch?v=XEmy13g1Qxc

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

 

# Constraints:

#     1 <= k <= nums.length <= 105
#     -104 <= nums[i] <= 104

import heapq
from typing import List

# Efficient Approach using Heap/Priority Queue:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                if num > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
        return min_heap[0]

        # Time Complexity = O(Nlogk)
        # Space Complexity = O(k)

# ----
    
# Inefficient approach in worst case - Quick Select:
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)


# ---- File: 227. Basic Calculator II\calculate.py ----
# https://leetcode.com/problems/basic-calculator-ii/description/

# https://www.youtube.com/watch?v=W3Rg4HVSZ9k&t=15s

# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7

# Example 2:

# Input: s = " 3/2 "
# Output: 1

# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5

 

# Constraints:

#     1 <= s.length <= 3 * 105
#     s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
#     s represents a valid expression.
#     All the integers in the expression are non-negative integers in the range [0, 231 - 1].
#     The answer is guaranteed to fit in a 32-bit integer.

class Solution:
    def calculate(self, s: str) -> int:
        currOp = "+"
        curr = prev = res = 0
        i = 0

        while i < len(s):
            currChar = s[i]

            if currChar.isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                i -= 1

                if currOp == "+":
                    res += curr
                    prev = curr
                elif currOp == "-":
                    res -= curr
                    prev = -curr
                elif currOp == "*":
                    res -= prev
                    res += prev * curr
                    prev = prev * curr
                elif currOp == "/":
                    res -= prev
                    res += int(prev / curr)
                    prev = int(prev / curr)
                
                curr = 0

            elif currChar != " ":
                currOp = currChar
            
            i += 1
        return res
    
# For * and / : rp, rpc, ppc

# ---- File: 23. Merge k Sorted Lists\mergeKLists.py ----
# https://leetcode.com/problems/merge-k-sorted-lists/

# https://www.youtube.com/watch?v=RCuBc4Zl-oY

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:

# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []

 

# Constraints:

#     k == lists.length
#     0 <= k <= 104
#     0 <= lists[i].length <= 500
#     -104 <= lists[i][j] <= 104
#     lists[i] is sorted in ascending order.
#     The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # add first elements of all the lists to the min heap
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i))
        
        dummy = curr = ListNode(0)

        while min_heap:
            val, i = heapq.heappop(min_heap) # pop the current smallest element from the heap
            curr.next = ListNode(val) # add to our output list
            if lists[i].next: # add the next element from the list where it's element was popped from heap to add in heap
                heapq.heappush(min_heap, (lists[i].next.val, i))
                lists[i] = lists[i].next
            curr = curr.next
        return dummy.next
        
        # Time Complexity: O(N log k)
        # Space Complexity: O(k)
    
    # Follow-up: If asked merge k sorted arrays instead of linked lists:

def merge_k_sorted_arrays(arrays):
    # Min heap to store tuples (element, array index, index within array)
    min_heap = []
    
    # Initialize the heap with the first element from each array
    for i, array in enumerate(arrays):
        if array:
            heapq.heappush(min_heap, (array[0], i, 0))

    result = []

    while min_heap:
        val, array_idx, idx_within_array = heapq.heappop(min_heap)
        result.append(val)

        # Move to the next element in the same array
        if idx_within_array + 1 < len(arrays[array_idx]):
            heapq.heappush(min_heap, (arrays[array_idx][idx_within_array + 1], array_idx, idx_within_array + 1))

    return result

    # Time Complexity: O(N log k)
    # Space Complexity: O(k)

# Example usage:
arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

result = merge_k_sorted_arrays(arrays)
print(result)

    
    

# ---- File: 236. Lowest Common Ancestor of a Binary Tree\lowestCommonAncestor.py ----
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# https://www.youtube.com/watch?v=WO1tfq2sbsI

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1

 

# Constraints:

#     The number of nodes in the tree is in the range [2, 105].
#     -109 <= Node.val <= 109
#     All Node.val are unique.
#     p != q
#     p and q will exist in the tree.

# Check left and right root nodes, check who returns non-none values, return l or r. If both return non-none values, root is the LCA

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right


# ---- File: 246. Strobogrammatic Number\isStrobogrammatic.py ----
# https://leetcode.com/problems/strobogrammatic-number/description/


# Given a string num which represents an integer, return true if num is a strobogrammatic number.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

# Example 1:

# Input: num = "69"
# Output: true

# Example 2:

# Input: num = "88"
# Output: true

# Example 3:

# Input: num = "962"
# Output: false

 

# Constraints:

#     1 <= num.length <= 50
#     num consists of only digits.


class Solution:
    def isStrobogrammatic(self, num):
        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        i,j = 0, len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in maps:
                return False
            i += 1
            j -= 1
        return True
        

# ---- File: 249. Group Shifted Strings\groupStrings.py ----
# https://leetcode.com/problems/group-shifted-strings/

# https://www.youtube.com/watch?v=g_CWHtPSQmQ&t=69s

# We can shift a string by shifting each of its letters to its successive letter.

#     For example, "abc" can be shifted to be "bcd".

# We can keep shifting the string to form a sequence.

#     For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

# Example 1:

# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

# Example 2:

# Input: strings = ["a"]
# Output: [["a"]]

 

# Constraints:

#     1 <= strings.length <= 200
#     1 <= strings[i].length <= 50
#     strings[i] consists of lowercase English letters.

import collections
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        # Idea is to create a map of:
        # key : tuple of difference between character values in each string
        # value : that specific string value

        grouping_dict = collections.defaultdict(list)

        for string in strings:
            if len(string) == 1:
                grouping_dict[(-1)].append(string)
            else:
                char_diff = []

                i = 1

                while i < len(string):
                    char_diff.append((ord(string[i]) - ord(string[i - 1])) % 26)
                    i += 1

                grouping_dict[tuple(char_diff)].append(string)

        return grouping_dict.values()

        # T: O(N * K), N = number of string in strings, K = length of longest string in strings
        # S: O(N * K)


# ---- File: 253. Meeting Rooms II\minMeetingRooms.py ----
# https://leetcode.com/problems/meeting-rooms-ii/

# https://www.youtube.com/watch?v=h_Ej3FFfnek

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

 

# Constraints:

#     1 <= intervals.length <= 104
#     0 <= starti < endi <= 106

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda i: i[0])

        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])

        for i in intervals[1:]:
            if i[0] >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, i[1])

        return len(min_heap)

        # T - O(nlogn)
        # S - O(N)


# ---- File: 270. Closest Binary Search Tree Value\closestValue.py ----
# https://leetcode.com/problems/closest-binary-search-tree-value/description/

# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

 

# Example 1:

# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4

# Example 2:

# Input: root = [1], target = 4.428571
# Output: 1

 

# Constraints:

#     The number of nodes in the tree is in the range [1, 104].
#     0 <= Node.val <= 109
#     -109 <= target <= 109

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_value = float("inf")
        curr = root

        while curr:
            if curr.val == target:
                return curr.val
            if abs(curr.val - target) < abs(closest_value - target):
                closest_value = curr.val
            if abs(curr.val - target) == abs(closest_value - target):
                closest_value = min(curr.val, closest_value)

            if curr.val > target:
                curr = curr.left
            else:
                curr = curr.right
        return closest_value


# ---- File: 283. Move Zeroes\moveZeroes.py ----
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]

 

# Constraints:

#     1 <= nums.length <= 104
#     -231 <= nums[i] <= 231 - 1

 
# Follow up: Could you minimize the total number of operations done?

from ast import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                tmp = nums[i]
                nums.pop(i)
                nums.append(tmp)
                n -= 1
            else:
                i += 1


# ---- File: 31. Next Permutation\nextPermutation.py ----
# https://leetcode.com/problems/next-permutation/description/

# https://www.youtube.com/watch?v=JDOXKqF60RQ

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

#     For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

#     For example, the next permutation of arr = [1,2,3] is [1,3,2].
#     Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
#     While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]

 

# Constraints:

#     1 <= nums.length <= 100
#     0 <= nums[i] <= 100

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)

        # find the first adacent pair/breakpoint from right side where left is smaller than right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        # if you dont find such a pair, reverse the whole array
        if index == -1:
            return nums.reverse()

        # swap the left element in the pair with the smallest element greater than that to its right
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        # sort the sub array from the point of swap (after the left element in the pair - index + 1) till the end
        nums[index + 1 :] = sorted(nums[index + 1 :])


# ---- File: 314. Binary Tree Vertical Order Traversal\verticalOrder.py ----
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# https://www.youtube.com/watch?v=_Froy1yUCWw&t=11s

# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

# Example 2:

# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]

# Example 3:

# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]

 

# Constraints:

#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100

# 1: Create a dictionary to store, column value : to their key's value
# 2: Queue for BFS and popping the first element and adding in to the dict_nodes
# 3: Sort the dictionary by keys (lowest col values) since we traverse left through right and append the respective key's value to the result list

import collections
from typing import List, Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dict_nodes = collections.defaultdict(list)
        queue = [(root, 0)]
        result = []

        while queue:
            curr, col = queue.pop(0)
            dict_nodes[col].append(curr.val)

            if curr.left:
                queue.append((curr.left, col - 1))
            if curr.right:
                queue.append((curr.right, col + 1))

        for key in sorted(dict_nodes.keys()):
            result.append(dict_nodes[key])
        return result



# ---- File: 339. Nested List Weight Sum\depthSum.py ----
# https://leetcode.com/problems/nested-list-weight-sum/description/

# https://www.youtube.com/watch?v=jR2UC4K-q2U

# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

# Return the sum of each integer in nestedList multiplied by its depth.

 

# Example 1:

# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

# Example 2:

# Input: nestedList = [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.

# Example 3:

# Input: nestedList = [0]
# Output: 0

 

# Constraints:

#     1 <= nestedList.length <= 50
#     The values of the integers in the nested list is in the range [-100, 100].
#     The maximum depth of any integer is less than or equal to 50.

# add the elements of nestedList in a queue
# if it's a single integer, multiple its value to the depth and add it to the result
# if it's a list, append the elements of the list (not the whole list) to end of the queue by using queue.extend(curr.getList())
# increase depth += 1 each round

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


from collections import deque

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        depth = 1
        result = 0

        queue = deque(nestedList)

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr.isInteger():
                    result += curr.getInteger() * depth
                else:
                    queue.extend(curr.getList())

            depth += 1
        return result


# ---- File: 346. Moving Average from Data Stream\MovingAverage.py ----
# https://leetcode.com/problems/moving-average-from-data-stream/description/

# https://www.youtube.com/watch?v=tje1ViST5Qk

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

#     MovingAverage(int size) Initializes the object with the size of the window size.
#     double next(int val) Returns the moving average of the last size values of the stream.

 

# Example 1:

# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

 

# Constraints:

#     1 <= size <= 1000
#     -105 <= val <= 105
#     At most 104 calls will be made to next.

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.stream = []

    def next(self, val: int) -> float:
        self.stream.append(val)

        avg = 0
        div = 0

        if len(self.stream) >= self.size:
            div = self.size
        else:
            div = len(self.stream)

        avg = sum(self.stream[-self.size :]) / div

        return avg

# ---- File: 347. Top K Frequent Elements\topKFrequent.py ----
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

 

# Constraints:

#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#     k is in the range [1, the number of unique elements in the array].
#     It is guaranteed that the answer is unique.

 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Bucket Sort solution : O(n) time and O(n) space (slightly better than use heap w/heapify where time complexity is O(klogn))

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        countMap = {}  # map to keep track of count - key: num, value: count of num in array nums
        freq = [[] for i in range(n + 1)]  # frequency array to keep track of elements for their certain count, eg. [[], [], [], ...]

        # add nums with their counts to hashmap
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1

        # append num's to the frequency array to their respective count indices
        for num, count in countMap.items():
            freq[count].append(num)

        result = []
        # loop from end of the frequency array to append top k frequent elements to the result array
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
            if len(result) == k:
                return result
            
        # Time Complexity: O(N + K log N)
        # Space Complexity: O(N) for the countMap and freq arrays


# ---- File: 383. Ransom Note\canConstruct.py ----
# https://leetcode.com/problems/ransom-note/description/

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

 

# Constraints:

#     1 <= ransomNote.length, magazine.length <= 105
#     ransomNote and magazine consist of lowercase English letters.

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)

        for char in magazine:
            if r_counter[char]:
                r_counter[char] -= 1
                if r_counter[char] == 0:
                    del r_counter[char]
        if not r_counter:
            return True
        return False


# ---- File: 398. Random Pick Index\solution.py ----
# https://leetcode.com/problems/random-pick-index/

# https://www.youtube.com/watch?v=HXRN8ZfAQOI

# Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

# Implement the Solution class:

#     Solution(int[] nums) Initializes the object with the array nums.
#     int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.

 

# Example 1:

# Input
# ["Solution", "pick", "pick", "pick"]
# [[[1, 2, 3, 3, 3]], [3], [1], [3]]
# Output
# [null, 4, 0, 2]

# Explanation
# Solution solution = new Solution([1, 2, 3, 3, 3]);
# solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.

 

# Constraints:

#     1 <= nums.length <= 2 * 104
#     -231 <= nums[i] <= 231 - 1
#     target is an integer from nums.
#     At most 104 calls will be made to pick.

import random
from typing import List

# Use concept of Reservoir Sampling 

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = pickIndex = 0

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1

                if random.randint(1, count) == count:
                    pickIndex = i
        return pickIndex

# T - O(N)
# S - O(1)


# ---- File: 408. Valid Word Abbreviation\validWordAbbreviation.py ----
# https://leetcode.com/problems/valid-word-abbreviation/

# https://www.youtube.com/watch?v=Sut-F029biM

# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

# For example, a string such as "substitution" could be abbreviated as (but not limited to):

#     "s10n" ("s ubstitutio n")
#     "sub4u4" ("sub stit u tion")
#     "12" ("substitution")
#     "su3i1u2on" ("su bst i t u ti on")
#     "substitution" (no substrings replaced)

# The following are not valid abbreviations:

#     "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
#     "s010n" (has leading zeros)
#     "s0ubstitution" (replaces an empty substring)

# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.

 
# Example 1:

# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true
# Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

# Example 2:

# Input: word = "apple", abbr = "a2e"
# Output: false
# Explanation: The word "apple" cannot be abbreviated as "a2e".

 

# Constraints:

#     1 <= word.length <= 20
#     word consists of only lowercase English letters.
#     1 <= abbr.length <= 10
#     abbr consists of lowercase English letters and digits.
#     All the integers in abbr will fit in a 32-bit integer.

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordPtr = abbrPtr = 0

        while wordPtr < len(word) and abbrPtr < len(abbr):
            if abbr[abbrPtr].isdigit():
                steps = 0

                if abbr[abbrPtr] == "0":
                    return False

                while abbrPtr < len(abbr) and abbr[abbrPtr].isdigit():
                    steps = steps * 10 + int(abbr[abbrPtr])
                    abbrPtr += 1

                wordPtr += steps
            else:
                if word[wordPtr] != abbr[abbrPtr]:
                    return False

                abbrPtr += 1
                wordPtr += 1
        return wordPtr == len(word) and abbrPtr == len(abbr)


# ---- File: 415. Add Strings\addStrings.py ----
# https://leetcode.com/problems/add-strings/

# https://www.youtube.com/watch?v=q1RR8gk47Cg

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"

 

# Constraints:

#     1 <= num1.length, num2.length <= 104
#     num1 and num2 consist of only digits.
#     num1 and num2 don't have any leading zeros except for the zero itself.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0:
            if i >= 0:
                curr_i = int(num1[i])
            else:
                curr_i = 0
            
            if j >= 0:
                curr_j = int(num2[j])
            else:
                curr_j = 0
            
            curr_sum = carry + curr_i + curr_j

            result.append(str(curr_sum % 10))

            carry = curr_sum // 10

            i -= 1
            j -= 1
        
        if carry:
            result.append(str(carry))
        
        return "".join(reversed(result))

        # T: O(N + M)
        # S: O(N + M)

# ---- File: 426. Convert Binary Search Tree to Sorted Doubly Linked List\treeToDoublyList.py ----
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

# https://www.youtube.com/watch?v=l1hSUOaXLxc

# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

 

# Example 1:

# Input: root = [4,2,5,1,3]


# Output: [1,2,3,4,5]

# Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

# Example 2:

# Input: root = [2,1,3]
# Output: [1,2,3]

 

# Constraints:

#     The number of nodes in the tree is in the range [0, 2000].
#     -1000 <= Node.val <= 1000
#     All the values of the tree are unique.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None

        self.first = None
        self.last = None

        self.inorder_link(root)

        self.first.left = self.last
        self.last.right = self.first

        return self.first

    # helper method for inorder traversal: left -> node -> right
    def inorder_link(self, node):
        if node:
            # traverse to the left
            self.inorder_link(node.left)

            # if it's the leftmost (smallest) node
            if not self.last:
                self.first = node
            # if we have seen a node prior, left done, now it's parent node, then:
            else:
                node.left = self.last
                self.last.right = node

            self.last = node

            # after left and parent node steps are done, now traverse to the right
            self.inorder_link(node.right)

# T - O(N)
# S - O(LogN) in best case but generally, O(N)

# ---- File: 50. Pow(x, n)\myPow.py ----
# https://leetcode.com/problems/powx-n/description/

# https://www.youtube.com/watch?v=g9YQyYi4IQQ

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

 

# Constraints:

#     -100.0 < x < 100.0
#     -231 <= n <= 231-1
#     n is an integer.
#     Either x is not zero or n > 0.
#     -104 <= xn <= 104

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0

            res = helper(x, n // 2)
            res = res * res
            if n % 2 == 0:
                return res
            return x * res

        res = helper(x, abs(n))
        if n < 0:
            return 1 / res
        return res


# ---- File: 523. Continuous Subarray Sum\checkSubarraySum.py ----
# https://leetcode.com/problems/continuous-subarray-sum/

# https://www.youtube.com/watch?v=OKcrLfR-8mE

# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

#     its length is at least two, and
#     the sum of the elements of the subarray is a multiple of k.

# Note that:

#     A subarray is a contiguous part of the array.
#     An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false

 

# Constraints:

#     1 <= nums.length <= 105
#     0 <= nums[i] <= 109
#     0 <= sum(nums[i]) <= 231 - 1
#     1 <= k <= 231 - 1

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderMap = collections.defaultdict(int)
        # We add it to handle case where subarray starting from 0 is divisible by k.
        remainderMap[0] = -1 # remainder key : index value
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainderMap:
                remainderMap[r] = i
            elif i - remainderMap[r] > 1:
                return True
        return False

    # T - O(N)
    # S - O(N)

# ---- File: 528. Random Pick with Weight\solution.py ----
# https://leetcode.com/problems/random-pick-with-weight/description/

# https://www.youtube.com/watch?v=7x7Ydq2Wfvw

# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

#     For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

 

# Example 1:

# Input
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output
# [null,0]

# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

# Example 2:

# Input
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output
# [null,1,1,1,1,0]

# Explanation
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

# Since this is a randomization problem, multiple answers are allowed.
# All of the following outputs can be considered correct:
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......
# and so on.

 

# Constraints:

#     1 <= w.length <= 104
#     1 <= w[i] <= 105
#     pickIndex will be called at most 104 times.

import random
from typing import List

class Solution:
    # Time Complexity = O(N) 
    # Space Complexity = O(N)
    def __init__(self, w: List[int]):
        self.prefixSums = []
        total = 0

        for weight in w:
            total += weight
            self.prefixSums.append(total)

        self.total = total

    # Time Complexity = O(logN) due to binary search [efficient since the naive approach is O(N)]
    # Space Complexity = O(1)
    def pickIndex(self) -> int:
        left = 0
        right = len(self.prefixSums)
        target = random.uniform(0, self.total)

        while left < right:
            middle = left + ((right - left) // 2)

            if self.prefixSums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left



# ---- File: 543. Diameter of Binary Tree\diameterOfBinaryTree.py ----
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:

# Input: root = [1,2]
# Output: 1

 

# Constraints:

#     The number of nodes in the tree is in the range [1, 104].
#     -100 <= Node.val <= 100

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right) # 2 + is not required
            return 1 + max(left, right)

        dfs(root)
        return res[0]
    
    # T - O(N)
    # S - O(H)



# ---- File: 56. Merge Intervals\merge.py ----
# https://leetcode.com/problems/merge-intervals/description/

# https://www.youtube.com/watch?v=44H3cEC2fFM

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

 

# Constraints:

#     1 <= intervals.length <= 104
#     intervals[i].length == 2
#     0 <= starti <= endi <= 104

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = result[-1][1]

            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])
        return result

# Possible Follow up Q) 57. Insert Interval

# ---- File: 560. Subarray Sum Equals K\subarraySum.py ----
# https://leetcode.com/problems/subarray-sum-equals-k/description/

# https://www.youtube.com/watch?v=xvNwoz-ufXA

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

 

# Constraints:

#     1 <= nums.length <= 2 * 104
#     -1000 <= nums[i] <= 1000
#     -107 <= k <= 107

import collections
from typing import List

# Intuition for O(N) efficient approach:
# 1) Initialize Hashmap to start with "0: 1 ( prefixSum: count )"
# 2) Do prefix sum as you loop through the input array, and check whether remove = (prefixSum - k) is in our map. 
# 3) If yes, increment the count of remove and add to count/result (line 48)
# 4) If not, add in map (line 49)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_counts = collections.defaultdict(int)
        prefix_sum_counts[0] = 1
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            remove = prefix_sum - k
            count += prefix_sum_counts[remove]
            prefix_sum_counts[prefix_sum] += 1
        return count


# ---- File: 57. Insert Interval\insert.py ----
# https://leetcode.com/problems/insert-interval/description/

# https://www.youtube.com/watch?v=_1jHnaovdpo

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

 

# Constraints:

#     0 <= intervals.length <= 104
#     intervals[i].length == 2
#     0 <= starti <= endi <= 105
#     intervals is sorted by starti in ascending order.
#     newInterval.length == 2
#     0 <= start <= end <= 105

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)
        i = 0

        # non-merging intervals
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # merging intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        result.append(newInterval)

        # append remaining integers
        while i < n:
            result.append(intervals[i])
            i += 1
        return result


# ---- File: 670. Maximum Swap\maximumSwap.py ----
# https://leetcode.com/problems/maximum-swap/description/

# https://www.youtube.com/watch?v=PALPz9r2Q4A

# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

 

# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.

 

# Constraints:

#     0 <= num <= 108

from collections import deque

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 11:
            return num

        num_as_list = deque([])

        # adding num in sequence wise to our num_as_list using queue
        while num:
            num_as_list.appendleft(num % 10)
            num //= 10

        max_num_seen = -1  # 1
        max_num_at = len(num_as_list)  # 2
        i = len(num_as_list) - 1

        # traverse right to left to give max_num_seen (#1) and max_num_at (#2) indexes
        while i >= 0:
            curr_num = num_as_list[i]
            num_as_list[i] = (curr_num, max_num_seen, max_num_at)  # add # 1 and # 2 to our nums_as_list[i] value

            if curr_num > max_num_seen:
                max_num_seen = curr_num
                max_num_at = i
            i -= 1

        i = 0
        # traverse left to right to swap
        while i < len(num_as_list):
            curr_num, max_to_right, max_num_at = num_as_list[i]

            if max_to_right > curr_num:
                num_as_list[i], num_as_list[max_num_at] = num_as_list[max_num_at], num_as_list[i]
                break
            i += 1

        # converting our final num_as_list to number
        number = 0
        for num, _, _ in num_as_list:
            number = number * 10 + num
        return number


# ---- File: 680. Valid Palindrome II\validPalindrome.py ----
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true

# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:

# Input: s = "abc"
# Output: false

 

# Constraints:

#     1 <= s.length <= 105
#     s consists of lowercase English letters.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skipLeft = s[left + 1 : right + 1]
                skipRight = s[left:right]

                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
            left += 1
            right -= 1
        return True


# ---- File: 708. Insert into a Sorted Circular Linked List\insert.py ----
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

# https://www.youtube.com/watch?v=XN9OsmP2YTk

# Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

# If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

# If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

 

# Example 1:

 

# Input: head = [3,4,1], insertVal = 2
# Output: [3,4,1,2]
# Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.



# Example 2:

# Input: head = [], insertVal = 1
# Output: [1]
# Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.

# Example 3:

# Input: head = [1], insertVal = 0
# Output: [1,0]

 

# Constraints:

#     The number of nodes in the list is in the range [0, 5 * 104].
#     -106 <= Node.val, insertVal <= 106


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# Four Edge Cases to Solve:
# 1) Head is Null
# 2) Insert into the LL
# 3) Insert Edge
# 4) Univalue Nodes

class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        # 1) Head is Null
        if not head:
            new_head_node = Node(insertVal)
            new_head_node.next = new_head_node

            return new_head_node

        curr = head
        while curr.next != head:
            # 2) Insert into the LL
            if curr.val <= insertVal <= curr.next.val:
                new_node = Node(insertVal, curr.next)
                curr.next = new_node

                return head

            # 3) Insert Edge
            elif curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    new_node = Node(insertVal, curr.next)
                    curr.next = new_node

                    return head

            curr = curr.next

        # 4) Univalue Nodes
        new_node = Node(insertVal, curr.next)
        curr.next = new_node
        return head
         # T : O(N), S : O(1)

# ---- File: 71. Simplify Path\simplifyPath.py ----
# https://leetcode.com/problems/simplify-path/description/

# https://www.youtube.com/watch?v=4e1gVeQ0AEs

# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

# The canonical path should have the following format:

#     The path starts with a single slash '/'.
#     Any two directories are separated by a single slash '/'.
#     The path does not end with a trailing '/'.
#     The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

# Return the simplified canonical path.

 

# Example 1:

# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.

# Example 2:

# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

# Example 3:

# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

 

# Constraints:

#     1 <= path.length <= 3000
#     path consists of English letters, digits, period '.', slash '/' or '_'.
#     path is a valid absolute Unix path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_items = path.split("/")

        for item in path_items:
            if item == "." or not item:
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return "/" + "/".join(stack)


# ---- File: 766. Toeplitz Matrix\isToeplitzMatrix.py ----
# https://leetcode.com/problems/toeplitz-matrix/description/

# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

# Example 1:

# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.

# Example 2:

# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.

 

# Constraints:

#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 20
#     0 <= matrix[i][j] <= 99

 
# Follow up:

#     What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
#     What if the matrix is so large that you can only load up a partial row into the memory at once?

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        for r in range(row - 1):
            for c in range(col - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True

        # T - O(M * N) in worst case
        # S - O(1)

# Follow-ups:
    
# 1) Matrix Stored on Disk with Limited Memory:
    
# In this scenario, you can iterate through the matrix one row at a time. Load the current row into memory and compare it with the next row. 
# This way, you only need to keep two rows in memory at any given time. 
# Continue this process until you reach the end of the matrix.
    
# 2) Matrix So Large Partial Row Fits in Memory:

# If the matrix is so large that you can only load a partial row into memory at once, you can still use a sliding window approach. 
# Load a portion of the current row into memory, compare it with the corresponding portion of the next row, and slide the window through the entire row.
# Repeat this process for each row.

# ---- File: 791. Custom Sort String\customSortString.py ----
# https://leetcode.com/problems/custom-sort-string/description/

# https://www.youtube.com/watch?v=rrWsOBDybZE

# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

 

# Example 1:

# Input: order = "cba", s = "abcd"

# Output: "cbad"

# Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".

# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

# Example 2:

# Input: order = "bcafg", s = "abcd"

# Output: "bcad"

# Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.

# Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "bacd" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.

 

# Constraints:

#     1 <= order.length <= 26
#     1 <= s.length <= 200
#     order and s consist of lowercase English letters.
#     All the characters of order are unique.

# --- #

# 1) Mid-Efficient Approach : T - O(N * M), S - O(N)
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = [""] * len(s)
        orderList = list(order)

        for char in s:
            if char in orderList:
                i = orderList.index(char)
                res[i] += char
            else:
                res[-1] += char
        return "".join(res)


# 2) Efficient Approach using String Builder w/Dictionary : T - O(N + M) = O(N), S - O(N)
from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counts = Counter(s)

        string_builder = []

        for char in order:
            if char in s_counts:
                string_builder.extend([char] * s_counts[char])
                del s_counts[char]

        for char, count in s_counts.items():
            string_builder.extend([char] * count)

        return "".join(string_builder)


# ---- File: 88. Merge Sorted Arrays\merge.py ----
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

 

# Constraints:

#     nums1.length == m + n
#     nums2.length == n
#     0 <= m, n <= 200
#     1 <= m + n <= 200
#     -109 <= nums1[i], nums2[j] <= 109

 

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for last index of nums 1
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n-=1
            last -= 1
        
        # fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            last -= 1
            n -= 1
        
# If asked to merge three sorted arrays:    
def merge3sorted(A, B, C):
	(l1, l2, l3) = (len(A), len(B), len(C))
	i = j = k = 0

	# Destination array
	ans = []

	while (i < l1 or j < l2 or k < l3):

		# Assigning a, b, c with max values so that if
		# any value is not present then also we can sort
		# the array
		a = 9999
		b = 9999
		c = 9999

		# a, b, c variables are assigned only if the
		# value exist in the array.
		if (i < l1):
			a = A[i]
		if (j < l2):
			b = B[j]
		if (k < l3):
			c = C[k]

		# Checking if 'a' is the minimum
		if (a <= b and a <= c):
			ans.append(a)
			i += 1

		# Checking if 'b' is the minimum
		elif (b <= a and b <= c):
			ans.append(b)
			j += 1

		# Checking if 'c' is the minimum
		elif (c <= a and c <= b):
			ans.append(c)
			k += 1

	return ans

     # T and S : O(M + N + O) = O(N)

 # If asked to merge three sorted arrays but without duplicates:

def merge_three_sorted_arrays_no_duplicates(arr1, arr2, arr3):
    result = []  # Initialize the result array to store the merged and deduplicated values
    i = j = k = 0  # Initialize pointers for each array

    while i < len(arr1) or j < len(arr2) or k < len(arr3):
        # Extract values at current pointers (or use infinity if pointers are out of bounds)
        val1 = arr1[i] if i < len(arr1) else float('inf')
        val2 = arr2[j] if j < len(arr2) else float('inf')
        val3 = arr3[k] if k < len(arr3) else float('inf')

        # Find the minimum value among the three arrays
        min_val = min(val1, val2, val3)

        # Move the pointers based on the minimum value
        if min_val == val1:
            i += 1
        elif min_val == val2:
            j += 1
        else:
            k += 1

        # Append the distinct value to the result (avoid duplicates)
        if not result or min_val != result[-1]:
            result.append(min_val)

    return result

    # T and S : O(N)


# ---- File: 921. Minimum Add to Make Parentheses Valid\minAddToMakeValid.py ----
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

# https://www.youtube.com/watch?v=LzcyBJRMhSw

# A parentheses string is valid if and only if:

#     It is the empty string,
#     It can be written as AB (A concatenated with B), where A and B are valid strings, or
#     It can be written as (A), where A is a valid string.

# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

#     For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

# Return the minimum number of moves required to make s valid.

 

# Example 1:

# Input: s = "())"
# Output: 1

# Example 2:

# Input: s = "((("
# Output: 3

 

# Constraints:

#     1 <= s.length <= 1000
#     s[i] is either '(' or ')'.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = added = 0

        for char in s:
            if char == "(":
                left += 1
            else:
                if right < left:
                    right += 1
                else:
                    added += 1

        added += left - right
        return added


# ---- File: 938. Range Sum of BST\rangeSumBST.py ----
# https://leetcode.com/problems/range-sum-of-bst/

# Iterative : https://www.youtube.com/watch?v=6dT3ZWhgDAU

# Recursive: https://www.youtube.com/watch?v=uLVG45n4Sbg

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Example 1:

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# Example 2:

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

# Constraints:

#     The number of nodes in the tree is in the range [1, 2 * 104].
#     1 <= Node.val <= 105
#     1 <= low <= high <= 105
#     All Node.val are unique.

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Iterative Solution (preferred, in case recursive since recursion can result in stack overflow in real-world problems - if asked in an interview)
        # T : O(N)
        # S : O(N)

        if not root:
            return 0

        result = 0
        stack = [root]

        while stack:
            curr = stack.pop()

            if curr:
                if low <= curr.val and curr.val <= high:
                    result += curr.val

                if curr.val > low:
                    stack.append(curr.left)

                if curr.val < high:
                    stack.append(curr.right)
        return result

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Recursive Solution
        # T : O(N)
        # S : O(N)

        if not root:
            return 0

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )


# ---- File: 973. K Closest Points to Origin\kClosest.py ----
# https://leetcode.com/problems/k-closest-points-to-origin/description/

# https://www.youtube.com/watch?v=rI2EBUEMfTk

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

# Example 1:

# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.

 

# Constraints:

#     1 <= k <= points.length <= 104
#     -104 <= xi, yi <= 104

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            dist = (x**2) + (y**2)
            min_heap.append([dist, x, y])

        heapq.heapify(min_heap)
        result = []

        while k > 0:
            dist, x, y = heapq.heappop(min_heap)
            result.append([x, y])
            k -= 1
        return result

        # T - O(klogN)
        # S - O(N)


# ---- File: 986. Interval List Intersections\intervalIntersection.py ----
# https://leetcode.com/problems/interval-list-intersections/description/

# https://www.youtube.com/watch?v=ZjxhxTiahBQ

# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

# Example 1:

# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

# Example 2:

# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []

 

# Constraints:

#     0 <= firstList.length, secondList.length <= 1000
#     firstList.length + secondList.length >= 1
#     0 <= starti < endi <= 109
#     endi < starti+1
#     0 <= startj < endj <= 109 
#     endj < startj+1

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        p1 = p2 = 0
        result = []

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            if start1 > end2:
                p2 += 1
            elif start2 > end1:
                p1 += 1
            else:
                result.append([max(start1, start2), min(end1, end2)])

                if end1 > end2:
                    p2 += 1
                else:
                    p1 += 1
        return result


# ---- File: 987. Vertical Order Traversal of a Binary Tree\verticalTraversal.py ----
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

# Return the vertical order traversal of the binary tree.

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Column -1: Only node 9 is in this column.
# Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
# Column 1: Only node 20 is in this column.
# Column 2: Only node 7 is in this column.

# Example 2:

# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# Column -2: Only node 4 is in this column.
# Column -1: Only node 2 is in this column.
# Column 0: Nodes 1, 5, and 6 are in this column.
#           1 is at the top, so it comes first.
#           5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
# Column 1: Only node 3 is in this column.
# Column 2: Only node 7 is in this column.

# Example 3:

# Input: root = [1,2,3,4,6,5,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# This case is the exact same as example 2, but with nodes 5 and 6 swapped.
# Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.

 

# Constraints:

#     The number of nodes in the tree is in the range [1, 1000].
#     0 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dict_nodes = collections.defaultdict(list)
        queue = deque([(root, 0, 0)])
        result = []

        while queue:
            curr, row, col = queue.popleft()
            dict_nodes[col].append((row, curr.val))

            if curr.left:
                queue.append((curr.left, row + 1, col - 1))
            if curr.right:
                queue.append((curr.right, row + 1, col + 1))

        for key in sorted(dict_nodes.keys()):
            sorted_values = [val for _, val in sorted(dict_nodes[key])]
            result.append(sorted_values)
        return result

