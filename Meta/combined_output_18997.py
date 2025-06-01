# ---- File: lc_1004.py ----
'''
https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
'''
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Finds the longest contiguous subarray that contains only 1s
        after flipping at most `k` 0s.

        :param nums: List of binary integers (0s and 1s)
        :param k: Maximum number of 0s that can be flipped
        :return: Length of the longest contiguous subarray with at most k flips
        """
        
        left = 0  # Left pointer for the sliding window
        
        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1  # Use one of the available flips
            
            # If k goes below 0, it means we have used more than allowed flips
            if k < 0:
                # If the left pointer is at a zero, recover one flip when moving past it
                if nums[left] == 0:
                    k += 1  
                left += 1  # Move the left pointer forward to reduce the window size
        
        # The length of the longest valid subarray is (right - left + 1)
        return right - left + 1


# ---- File: lc_1011.py ----
'''
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

Time Complexity: O(n * log W)

n is the number of packages (len(weights)).

W is the sum of all weights (sum(weights)), which defines the upper bound of the binary search range.

The algorithm performs a binary search over possible capacities in the range [max(weights), sum(weights)], which takes log W steps.

For each binary search step, the canShip() function runs in O(n) time to simulate the shipping process.

So, the total time complexity is O(n * log W).

Space Complexity: O(1)

The solution uses only a constant amount of extra space (for variables like left, right, mid, current_load, etc.).

No additional data structures are used that grow with input size.



'''

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Finds the minimum ship capacity to ship all packages within the given number of days.
        Uses binary search between the heaviest single package and the total weight.
        """

        # The minimum possible capacity must be at least the heaviest package
        left = max(weights)

        # The maximum possible capacity is the total weight (if we ship everything in one day)
        right = sum(weights)

        # Perform binary search to find the minimum feasible capacity
        while left < right:
            mid = (left + right) // 2  # Candidate capacity to test
            if self.canShip(weights, mid, days):
                right = mid  # Try a smaller capacity
            else:
                left = mid + 1  # Need a larger capacity

        # When left == right, we've found the smallest feasible capacity
        return left

    def canShip(self, weights: List[int], capacity: int, days: int) -> bool:
        """
        Helper function to check if all weights can be shipped within `days`
        using the given `capacity`.
        """
        days_needed = 1
        current_load = 0

        for weight in weights:
            current_load += weight

            # If current load exceeds capacity, we need an extra day
            if current_load > capacity:
                days_needed += 1       # Increment day count
                current_load = weight  # Start new day with current package

        # Return True if we can do it within the allowed number of days
        return days_needed <= days


# ---- File: lc_1091.py ----
'''
✅ Time Complexity: O(n^2)
Let n be the number of rows/columns in the n x n grid (as per problem constraints).

In the worst case, every cell in the grid is traversable (value 0), and each cell is visited once.

For each cell, we consider its 8 neighbors, so operations per cell are constant: O(1).

👉 Therefore, total operations = O(n^2) for visiting each cell once.

✅ Space Complexity: O(n^2)
Version 1 (Solution class):

It modifies the grid in-place to store distance instead of using a separate visited structure.

Queue stores up to O(n^2) cells in the worst case.

So total auxiliary space is O(n^2) (dominated by the queue).

Version 2 (Solution2 class):

Uses an explicit visited set, which can grow up to O(n^2) in size.

The queue can also hold up to O(n^2) elements.

Therefore, space complexity is O(n^2) as well.
'''
from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        
        # Possible 8-directional moves (up, down, left, right, diagonals)
        directions = [(-1,-1), (-1,0), (1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1)]

        # Function to get valid neighbors for BFS traversal
        def get_neighbors(row, col):
            for row_d, col_d in directions:
                new_row = row + row_d
                new_col = col + col_d
                
                # Check if the new position is within bounds
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                
                # Skip if the cell is blocked (not zero)
                if grid[new_row][new_col] != 0:
                    continue
                
                # Yield valid neighbor coordinates
                yield (new_row, new_col)

        # If the starting or ending cell is blocked, return -1 (no valid path)
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        # Initialize a queue for BFS (row, col)
        queue = deque()
        queue.append((0, 0))
        
        # Mark the starting point as visited with distance 1
        grid[0][0] = 1

        # Perform BFS traversal
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]  # Get the current distance from start
            
            # If we reached the bottom-right cell, return the distance
            if (row, col) == (max_row, max_col):
                return distance
            
            # Explore all valid neighbors
            for neighbor_row, neighbor_col in get_neighbors(row, col):
                grid[neighbor_row][neighbor_col] = distance + 1  # Mark visited with distance
                queue.append((neighbor_row, neighbor_col))  # Add to BFS queue
        
        # If no path is found, return -1
        return -1

    
class Solution2:
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:  
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        current_distance = 1
        
        # Do the BFS.
        while queue:
            # Process all nodes at current_distance from the top-left cell.
            nodes_of_current_distance = len(queue)
            for _ in range(nodes_of_current_distance):
                row, col = queue.popleft()
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in get_neighbours(row, col):
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    queue.append(neighbour)
            # We'll now be processing all nodes at current_distance + 1
            current_distance += 1
                    
        # There was no path.
        return -1 

# ---- File: lc_11.py ----
'''
https://leetcode.com/problems/container-with-most-water/

Time Complexity: O(n), where n is the number of elements in the height list.

Explanation: The algorithm uses a two-pointer approach, starting from both ends of the list and moving inward. In each iteration, at least one pointer moves closer to the other, so there are at most n iterations. Each step does constant-time operations, leading to an overall linear time complexity.

Space Complexity: O(1) since the algorithm uses only a fixed amount of extra space regardless of the input size.
'''

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0  # Stores the maximum water found so far

        # Initialize two pointers at both ends of the array
        left, right = 0, len(height) - 1

        # Loop while the two pointers haven't crossed
        while left < right:
            # Calculate the height and width of the current container
            # Height is determined by the shorter of the two lines
            # Width is the distance between the two lines
            water = min(height[left], height[right]) * (right - left)

            # Update maximum water if this container holds more
            max_water = max(max_water, water)

            # Move the pointer pointing to the shorter line inward
            # This is a greedy step: we want to try and find a taller line
            # because increasing the shorter line might increase area
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                # If both heights are equal, moving either is fine
                # So we move both inward to explore new pairs
                left += 1
                right -= 1

        # Return the maximum area found
        return max_water


# ---- File: lc_1249.py ----
'''
1249. Minimum Remove to Make Valid Parentheses
Solved
Medium
Topics
Companies
Hint
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Given a string `s` containing letters and parentheses, remove the 
        minimum number of parentheses to make the string valid.
        
        A valid string means that:
        - Open '(' parentheses must have a corresponding closing ')' parentheses.
        - Parentheses must be properly nested.
        """
        
        # Stack to store indices of unmatched '(' parentheses
        extraParentheses = []
        
        # Convert string to list to modify characters easily
        s = list(s)
        
        # First pass: Identify invalid ')' parentheses
        for index, ch in enumerate(s):
            if ch == '(':
                # Store index of '(' for future matching
                extraParentheses.append(index)
            elif ch == ')':
                if extraParentheses:
                    # Valid pair found, remove matched '(' from stack
                    extraParentheses.pop()
                else:
                    # No matching '(', mark ')' for removal
                    s[index] = ''

        # Second pass: Remove unmatched '(' parentheses
        while extraParentheses:
            s[extraParentheses.pop()] = ''

        # Return the final valid string
        return ''.join(s)


# ---- File: lc_127.py ----
'''
https://leetcode.com/problems/word-ladder/description/

✅ Time Complexity: O(N × M × 26) → Simplifies to O(N × M)
Where:

N is the number of words in the wordList

M is the length of each word

🔍 Explanation:
For each word processed in the BFS queue, you:

Loop through each character position in the word → M

Try replacing it with every letter from 'a' to 'z' → 26 letters

For each transformation, you check if it exists in the dictionary (O(1) due to the set)

So per word:
O(M × 26) = O(M) work

In the worst case, you may explore up to all N words from the dictionary, giving:
👉 Total time = O(N × M)

✅ Space Complexity: O(N × M)
Why:

dictionary_set stores up to N words, each of length M → O(N × M)

visited set also stores up to N words → O(N × M)

queue can store up to N words → O(N × M)

No additional complex data structures used

🧠 Summary:
Time: O(N × M)

Space: O(N × M)

Your solution is efficient because it:

Generates neighbors directly (no need to compare word pairs)

Uses BFS with O(1) lookups via a set
'''

from typing import List
from collections import deque

class Solution:
    def ladderLength(self, start: str, end: str, wordList: List[str]) -> int:
        """
        Given a `start` word and an `end` word, and a list of valid words (`wordList`),
        find the shortest transformation sequence from `start` to `end`,
        where:
        - Each transformed word must exist in `wordList`.
        - Only one letter can be changed at a time.
        - Return the length of the shortest transformation sequence. Return 0 if no sequence exists.
        """

        # Step 1: Convert wordList to a set for O(1) lookup time
        dictionary_set = set(wordList)

        # If `end` word is not in the dictionary, transformation is impossible
        if end not in dictionary_set:
            return 0
        
        # If start and end words are the same, the shortest path is just one step
        if start == end:
            return 1

        # Step 2: BFS Setup
        lower_case_alphabet = "abcdefghijklmnopqrstuvwxyz"  # Letters for transformation
        queue = deque([start])  # Initialize queue for BFS
        visited = set([start])  # Track visited words to prevent cycles
        dist = 0  # Distance counter (number of transformation steps)

        # Step 3: BFS Traversal
        while queue:
            dist += 1  # Increment transformation step count
            
            # Process all words at the current level before moving to the next
            for _ in range(len(queue)):
                curr_word = queue.popleft()  # Get the current word

                # If we reach the end word, return the total transformation steps
                if curr_word == end:
                    return dist
                
                # Step 4: Generate all possible one-letter transformations
                for i in range(len(curr_word)):
                    for c in lower_case_alphabet:
                        # Generate a new word by replacing one character
                        next_word = curr_word[:i] + c + curr_word[i+1:]

                        # If the new word exists in dictionary and is not visited, add to queue
                        if next_word in dictionary_set and next_word not in visited:
                            queue.append(next_word)
                            visited.add(next_word)  # Mark as visited to avoid reprocessing

        # Step 5: If BFS completes without finding `end`, return 0 (no transformation possible)
        return 0


# ---- File: lc_129.py ----
'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

✅ Time Complexity: O(n), where n is the number of nodes in the binary tree.
Explanation:

Each node is visited exactly once during the depth-first traversal.

At each node, constant-time operations are performed (multiplication, addition, pushing to stack).

Therefore, the total time is proportional to the number of nodes: O(n)

✅ Space Complexity: O(h), where h is the height of the tree.
Explanation:

The space used by the stack depends on the depth of the recursion (or stack) at any time.

In the worst case:

For a skewed tree (like a linked list), the height is n, so space = O(n)

For a balanced tree, height = log n, so space = O(log n)

Therefore, space complexity is O(h), where h is the height of the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Computes the sum of all root-to-leaf numbers in a binary tree.
        
        Each root-to-leaf path represents a number formed by concatenating node values.
        The sum of all such numbers is returned.

        :param root: Root node of the binary tree
        :return: Sum of all root-to-leaf numbers
        """
        
        # Stack for iterative depth-first traversal (node, current number)
        stack = [(root, 0)]
        
        # Variable to store the sum of all root-to-leaf numbers
        root_to_leaf = 0 
        
        # Iterate using DFS (Depth-First Search)
        while stack:
            root, curr_number = stack.pop()  # Get the current node and its accumulated value
            
            if root is not None:
                # Update the current number by shifting left (multiplying by 10) and adding node value
                curr_number = curr_number * 10 + root.val

                # If it's a leaf node, add the current number to the total sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    # Push the right child first (so left is processed first in DFS order)
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))

        return root_to_leaf  # Return the sum of all root-to-leaf numbers

# ---- File: lc_138.py ----
'''
https://leetcode.com/problems/copy-list-with-random-pointer/description/

Time Complexity: O(n), where n is the number of nodes in the linked list.

Explanation:

Each node in the original list is visited exactly once.

For each node, you:

Create a copy,

Recursively visit its .next and .random pointers.

The visitedHash dictionary ensures no node is visited or copied more than once.

Therefore, the total work is proportional to the number of nodes: O(n).

Space Complexity: O(n)

Explanation:

A hash map (visitedHash) is used to store a mapping from original nodes to their copies. It stores one entry per node → O(n) space.

Additionally, recursive calls consume stack space. In the worst case (if the list is a single chain), the recursion stack could go up to n levels → O(n) space.

So, the overall space complexity is O(n).

'''

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # HashMap (Dictionary) to keep track of visited nodes and avoid duplicates
        visitedHash = {}

        def helper(node: 'Optional[Node]') -> 'Optional[Node]':
            nonlocal visitedHash  # Use the shared dictionary to track copied nodes
            
            # Base case: If node is None, return None
            if not node:
                return None
            
            # If the node is already copied, return the copied node from the hash map
            if node in visitedHash:
                return visitedHash[node]
            
            # Create a new node with the same value, but without setting next or random yet
            newNode = Node(node.val, None, None)
            
            # Store this newly created node in the hash map before recursion
            visitedHash[node] = newNode

            # Recursively copy the next node and random node
            newNode.next = helper(node.next)
            newNode.random = helper(node.random)
            
            return newNode  # Return the copied node
        
        # Start the recursion with the head node
        newHead = helper(head)
        return newHead


# ---- File: lc_139.py ----
'''
https://leetcode.com/problems/word-break/description/

✅ Time Complexity: O(n²), where n is the length of the input string s.

Explanation:

For each index start in the queue (at most n different positions), you may check up to n - start substrings by varying end from start + 1 to n.

Checking if s[start:end] is in the dictionary takes O(1) (thanks to the set).

Since each end index is processed only once (due to seen), the total number of substring checks is bounded by O(n²).

✅ Space Complexity: O(n + m), where:

n is the length of the input string s,

m is the total number of characters in wordDict.

Explanation:

words set takes O(m) space to store the dictionary.

queue and seen sets can store up to n indices → O(n).

No extra space proportional to substrings or a DP table is used.

🧠 Summary:
Time: O(n²)

Space: O(n + m)
'''
from typing import List
from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determines if the string `s` can be segmented into a sequence of one or more dictionary words.
        Uses BFS to explore all valid segmentations.
        """

        words = set(wordDict)       # Convert wordDict to set for O(1) lookup
        queue = deque([0])          # BFS queue holds starting indices to explore
        seen = set()                # Tracks visited indices to prevent re-processing

        while queue:
            start = queue.popleft()  # Get the current start index to explore from

            if start == len(s):      # Reached the end of the string with valid segmentations
                return True

            # Try every possible substring starting from `start`
            for end in range(start + 1, len(s) + 1):
                # Skip if we've already visited this end position
                if end in seen:
                    continue

                # If substring from start to end exists in dictionary
                if s[start:end] in words:
                    queue.append(end)   # Add new start index to queue
                    seen.add(end)       # Mark end index as visited

        # If we've explored all options and found no valid break
        return False


# ---- File: lc_140.py ----
'''
https://leetcode.com/problems/word-break-ii/description/

✅ Time Complexity:
Let:

n be the length of the string s

k be the average number of valid words that can start at each position

L be the average length of the result sentences

Time Complexity (Worst Case): O(2^n × L)
Explanation:

At each character position in the string, we can either break or not (depending on word matches), leading to up to 2^n recursive paths (just like generating all subsets).

For each valid path (sentence), joining words into a string takes O(L), where L is the sentence length.

So total time can be up to O(2^n × L).

Note: In practice, we may use memoization (caching results for subproblems) to reduce redundant recomputation, improving performance significantly.

✅ Space Complexity: O(n × L)
Explanation:

The recursion stack can go as deep as n in the worst case.

The result list may contain up to 2^n sentences, and each sentence takes O(L) space.

So the output space (not auxiliary) can also be O(2^n × L), but auxiliary space is mainly from recursion and temporary lists: O(n × L).


'''
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Returns all possible sentences by segmenting the string `s` into valid dictionary words.
        Each sentence is a sequence of words separated by spaces.
        """

        word_set = set(wordDict)  # Convert wordDict to a set for fast lookup
        result = []  # List to store all valid sentences

        def backtrack(s: str, current_sentence: List[str], start_index: int):
            """
            Recursive backtracking function to build valid word sequences.
            
            :param s: The input string
            :param current_sentence: List of words forming the current sentence
            :param start_index: The starting index in `s` to search for the next word
            """
            # Base case: if we've reached the end of the string, store the complete sentence
            if start_index == len(s):
                result.append(" ".join(current_sentence))  # Join the words with spaces
                return

            # Try every possible substring starting from start_index
            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]  # Current substring to test
                if word in word_set:
                    current_sentence.append(word)               # Choose the word
                    backtrack(s, current_sentence, end_index)   # Recurse with updated index
                    current_sentence.pop()                      # Backtrack: remove the last word

        # Start backtracking from index 0 with an empty sentence
        backtrack(s, [], 0)
        return result

'''
Time Complexity: Still up to O(2^n × L) in the worst case (if there are many overlapping subproblems and valid paths), but practically much faster due to avoiding repeated work.

Space Complexity: O(n × L) for recursion + memoization cache.
'''

from typing import List

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Returns all possible sentences by segmenting the string `s` into valid dictionary words.
        Each sentence is a sequence of words separated by spaces.
        """
        word_set = set(wordDict)  # Convert wordDict to a set for fast lookup
        memo = {}  # Dictionary for memoization

        def backtrack(start_index: int) -> List[str]:
            """
            Recursive backtracking function with memoization to build valid word sequences.

            :param start_index: The starting index in `s` to search for the next word
            :return: A list of sentences that can be built from start_index to end of s
            """
            if start_index in memo:
                return memo[start_index]

            if start_index == len(s):
                return [""]  # Base case: return list with empty string to build sentence

            sentences = []

            # Try every possible substring starting from start_index
            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]
                if word in word_set:
                    rest_sentences = backtrack(end_index)

                    for sentence in rest_sentences:
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)

            memo[start_index] = sentences
            return sentences

        return backtrack(0)


# ---- File: lc_1428.py ----
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#     def get(self, row: int, col: int) -> int:
#     def dimensions(self) -> list[]:
'''
✅ Time Complexity of leftMostColumnWithOne:
Let’s define:

m = number of rows in the binary matrix

n = number of columns in the binary matrix

⏱ Time Complexity: O(m * log n)
For each row (total m rows), the algorithm performs a binary search over the columns (n columns).

Binary search on n columns takes O(log n) time.

Thus, total time = m * O(log n) = O(m log n)

🧠 Space Complexity: O(1)
No extra space is used apart from a few variables (constant space).

'''

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()  # Get matrix dimensions
        smallest_index = cols  # Initialize to maximum possible column index
        
        for row in range(rows):
            lo = 0
            hi = cols - 1
            
            # Binary search for the leftmost 1 in the current row
            while lo <= hi:
                mid = (lo + hi) // 2
                if binaryMatrix.get(row, mid) == 0:
                    lo = mid + 1  # Search in the right half
                else:
                    hi = mid - 1  # Search in the left half
            
            # If a 1 is found, update smallest_index
            if lo < cols and binaryMatrix.get(row, lo) == 1:
                smallest_index = min(smallest_index, lo)
        
        # If smallest_index remains unchanged, no 1 was found
        return -1 if smallest_index == cols else smallest_index


# ---- File: lc_146.py ----
'''
https://leetcode.com/problems/lru-cache/description/

✅ Time Complexity:
get(key) → O(1)

put(key, value) → O(1)

Explanation:
Both get and put operations perform:

Hashmap lookups (e.g., self.hashmap[key]) → O(1)

Doubly Linked List operations (add_to_tail, remove_node) → O(1) because they only involve pointer adjustments.

So, every operation (get/put) completes in constant time → O(1).

This is the key design of an efficient LRU cache: combining a hashmap (for fast lookup) and a doubly linked list (for tracking usage order in constant time).

✅ Space Complexity: O(capacity)
Explanation:

The cache stores up to capacity nodes.

Each node is stored in both:

the hashmap (for key lookup),

and the doubly linked list (for usage ordering).

Therefore, space grows linearly with capacity.

🧠 Summary:
Operation	Time Complexity
get()	O(1)
put()	O(1)
Space Complexity: O(capacity)

Let me know if you'd like a visual diagram of how get and put work step-by-step!
'''
# Node definition for a doubly linked list
class DoublyLinkedListNode:
    def __init__(self, key: int, val: int):
        self.key = key                      # Store key for hashmap reference
        self.val = val                      # Value associated with the key
        self.next = self.prev = None        # Pointers for DLL navigation

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity            # Maximum number of entries in cache
        self.hashmap = {}                   # Hashmap to store key → node mapping for O(1) access
        # Create dummy head and tail nodes to simplify insert/remove logic
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node) -> None:
        """
        Add the given node just before the tail (most recently used position).
        """
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node

    def remove_node(self, node) -> None:
        """
        Disconnect the node from the doubly linked list.
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        """
        Return the value associated with the key if it exists.
        Move the node to the tail to mark it as recently used.
        """
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]
        self.remove_node(node)     # ✅ Remove from current position in DLL
        self.add_to_tail(node)     # ✅ Re-add to tail as most recently used
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Insert or update a key-value pair.
        If the key exists, update and move it to tail.
        If the cache exceeds capacity, evict the least recently used node.
        """
        if key in self.hashmap:
            # ✅ Remove the existing node before inserting the updated one
            self.remove_node(self.hashmap[key])
            del self.hashmap[key]

        node = DoublyLinkedListNode(key, value)
        self.hashmap[key] = node
        # If the cache is over capacity, remove the least recently used node (head.next)
        if len(self.hashmap) > self.capacity:
            lru_node = self.head.next
            self.remove_node(lru_node)          # Remove from DLL
            del self.hashmap[lru_node.key]      # Remove from hashmap

        self.add_to_tail(node)

# ---- File: lc_15.py ----
'''
https://leetcode.com/problems/3sum/description/

Time Complexity: O(n^2), where n is the number of elements in the input list nums.

Explanation:

First, the array is sorted in O(n log n) time.

Then, the algorithm uses a loop to fix one element and applies the two-pointer approach for the remaining two elements.

For each element, the two-pointer traversal takes O(n) time in the worst case, and this happens for n elements.

Hence, the overall time complexity is O(n^2).

Space Complexity: O(1) (excluding the output list).

The algorithm does not use any extra space for computation; it modifies pointers in-place after sorting.

However, the space required for the result list depends on the number of valid triplets found, which can vary based on the input.
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array `nums`, return all unique triplets [nums[i], nums[j], nums[k]]
        such that `nums[i] + nums[j] + nums[k] == 0`.
        """

        nums.sort()  # Step 1: Sort the array to allow two-pointer traversal
        res = []  # Stores the final list of unique triplets

        # Step 2: Iterate through the sorted list to find triplets
        for i, a in enumerate(nums):
            # Optimization: Since `nums` is sorted, if `nums[i] > 0`, no triplet can sum to zero.
            if a > 0:
                break  # No valid triplet exists beyond this point.

            # Skip duplicate values to avoid duplicate triplets in the result
            if i > 0 and a == nums[i - 1]:
                continue  # Skip processing the same number again

            # Step 3: Two-pointer approach to find pairs that sum to `-a`
            l, r = i + 1, len(nums) - 1  # Left and right pointers

            while l < r:
                threeSum = a + nums[l] + nums[r]  # Calculate sum of triplet
                
                if threeSum > 0:
                    r -= 1  # Move the right pointer left to decrease the sum
                elif threeSum < 0:
                    l += 1  # Move the left pointer right to increase the sum
                else:
                    # Found a valid triplet
                    res.append([a, nums[l], nums[r]])

                    # Move left pointer forward while skipping duplicate values
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  # Skip duplicate numbers to ensure unique triplets

        return res  # Return the list of unique triplets


# ---- File: lc_150.py ----
'''
https://leetcode.com/problems/merge-intervals/description/

✅ Time Complexity: O(n log n), where n is the number of intervals.
Explanation:

Sorting the list of intervals by their start time takes O(n log n).

Iterating through the sorted intervals and merging them takes O(n) time.

So the total time complexity is dominated by the sorting step: O(n log n).

✅ Space Complexity: O(n)
Explanation:

In the worst case (no overlapping intervals), all intervals are added to the merged list → O(n) space.

Although the sorting may be done in-place depending on the implementation, the output list still requires space.

🧠 Summary:
Time Complexity: O(n log n)

Space Complexity: O(n)
'''
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by the starting value of each interval
        # This ensures that overlapping intervals are adjacent in the list
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize an empty list to store merged intervals
        merged = []
        
        # Step 3: Start with the first interval as the `prev` interval to compare
        prev = intervals[0]

        # Step 4: Iterate through the rest of the intervals
        for interval in intervals[1:]:
            # If the current interval overlaps with `prev`, merge them
            if interval[0] <= prev[1]:  
                # Update the end time of `prev` to include the new interval
                prev[1] = max(prev[1], interval[1])
            else:
                # If no overlap, add `prev` to merged list and move to next interval
                merged.append(prev)
                prev = interval

        # Step 5: Add the last merged interval to the list
        merged.append(prev)
        
        # Step 6: Return the merged intervals list
        return merged


# ---- File: lc_1570.py ----
'''
https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/
'''

from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        """
        Initializes a sparse vector from a given list of integers.
        
        Instead of storing all elements, we store only the non-zero elements
        in a dictionary (`self.nums`), where:
        - Key: Index of the non-zero element
        - Value: The non-zero element itself

        This optimizes space complexity by ignoring zero elements.

        Time Complexity: O(N) where N is the length of `nums`
        Space Complexity: O(K) where K is the number of non-zero elements
        """
        self.nums = {i: n for i, n in enumerate(nums) if n}  # Store only non-zero elements

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Computes the dot product of two sparse vectors efficiently.

        The dot product formula is:
            dot_product = sum(A[i] * B[i]) for all i

        Since most values in a sparse vector are zero, we only multiply 
        the non-zero elements that exist in both vectors.

        Approach:
        - Iterate over the smaller dictionary (for efficiency).
        - Multiply matching indices from both dictionaries.
        - Sum up the products.

        Time Complexity: O(K1 + K2) where K1, K2 are the non-zero elements in each vector.
        Space Complexity: O(1) (no extra space used)
        
        Args:
            vec (SparseVector): Another sparse vector.

        Returns:
            int: The dot product of the two vectors.
        """
        result = 0  # Store the final dot product

        # Optimize by iterating over the smaller dictionary for efficiency
        if len(self.nums) < len(vec.nums):
            smaller, larger = self.nums, vec.nums
        else:
            smaller, larger = vec.nums, self.nums

        # Compute dot product only for indices that exist in both vectors
        for key in smaller.keys():
            if key in larger:  # If index exists in both vectors
                result += smaller[key] * larger[key]

        return result  # Return the computed dot product

# Usage example:
# v1 = SparseVector([1, 0, 0, 2, 3])
# v2 = SparseVector([0, 3, 0, 4, 0])
# ans = v1.dotProduct(v2)  # Expected output: 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8


# ---- File: lc_162.py ----
'''
https://leetcode.com/problems/find-peak-element/description/
✅ Time Complexity: O(log n), where n is the number of elements in the input list nums.
Explanation:

The function uses binary search, which reduces the search space by half in each iteration.

So even in the worst case, it performs at most log₂(n) comparisons.

This is much faster than a linear scan (O(n)) and meets the problem’s logarithmic time requirement.

✅ Space Complexity: O(1)
Explanation:

Only a few variables (lo, hi, mid) are used.

No extra space is used that scales with the input size.

🧠 Summary:
Time Complexity: O(log n)

Space Complexity: O(1)
'''
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Initialize the search space with low and high pointers
        lo, hi = 0, len(nums) - 1
        
        # Perform binary search
        while lo < hi:
            mid = (lo + hi) // 2  # Find the middle index
            
            # Compare the mid element with the next element
            if nums[mid] < nums[mid + 1]:
                # If mid is less than mid+1, peak must be on the right side
                lo = mid + 1
            else:
                # If mid is greater than or equal to mid+1, peak must be on the left side (including mid)
                hi = mid
        
        # Since lo and hi converge, return the peak index
        return lo


# ---- File: lc_1650.py ----
'''
1650. Lowest Common Ancestor of a Binary Tree III
Solved
Medium
Topics
Companies
Hint
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
"""
Find the depth of each pointer
Move the deeper pointer up until it is at the same level as the other pointer
Move each pointer up level-by-level until they meet
"""
class Solution:
    def get_depth(self, p):
        """
        Helper function to calculate the depth of a given node `p` in a tree.
        The depth is the distance from the node to the root.
        
        Args:
            p (Node): The node whose depth is to be calculated.
        
        Returns:
            int: Depth of the node in the tree.
        """
        depth = 0
        while p:  # Traverse upwards until the root node is reached
            p = p.parent
            depth += 1  # Increment depth counter
        return depth

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Finds the lowest common ancestor (LCA) of two nodes in a tree where nodes 
        have parent pointers.
        
        The approach:
        - Compute the depth of both nodes.
        - Move the deeper node up until both nodes are at the same level.
        - Move both nodes up together until they meet, which is the LCA.

        Args:
            p (Node): First node.
            q (Node): Second node.

        Returns:
            Node: The lowest common ancestor of p and q.
        """
        # Step 1: Compute the depth of both nodes
        p_depth = self.get_depth(p)
        q_depth = self.get_depth(q)

        # Step 2: Move the deeper node up so both nodes are at the same depth
        # If `p` is deeper, move `p` up
        for _ in range(p_depth - q_depth):
            p = p.parent

        # If `q` is deeper, move `q` up
        for _ in range(q_depth - p_depth):
            q = q.parent

        # Step 3: Move both nodes up simultaneously until they meet
        while p != q:
            p = p.parent
            q = q.parent

        # Step 4: Return the first common ancestor
        return p

        

        

        

# ---- File: lc_167.py ----
'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

🧠 Explanation:
Time Complexity: O(n) — Each pointer moves at most n times (once from each end), so it's linear.

Space Complexity: O(1) — No extra space is used beyond a few variables.

'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Assumes input list `nums` is sorted in non-decreasing order.
        Returns 1-based indices of two numbers that add up to the target.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        left, right = 0, len(nums) - 1  # Initialize two pointers

        # Loop until the two pointers meet
        while left < right:
            sumFound = nums[left] + nums[right]

            if sumFound < target:
                left += 1  # Move left pointer right to increase sum
            elif sumFound > target:
                right -= 1  # Move right pointer left to decrease sum
            else:
                # Found the pair; return 1-based indices
                return [left + 1, right + 1]

        # Return default value if no valid pair found
        return [-1, -1]


# ---- File: lc_1762.py ----
'''
1762. Buildings With an Ocean View
Solved
Medium
Topics
Companies
Hint
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 109
'''
from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        Given a list `heights` where `heights[i]` represents the height of a building,
        return a list of indices of buildings that have a clear ocean view.
        
        A building has an ocean view if all buildings to its right have a smaller height.
        
        Approach:
        - Use a **monotonic decreasing stack** to maintain indices of buildings with ocean views.
        - Iterate through the buildings **from left to right**.
        - Pop buildings from the stack that are **shorter or equal** to the current building.
        - Append the current building index to the stack.
        - The remaining buildings in the stack have ocean views.

        Time Complexity: O(N) (Each building is pushed and popped at most once)
        Space Complexity: O(N) (Stack stores at most N elements in the worst case)
        """
        
        stack = []  # Stack to store indices of buildings with ocean views

        # Step 1: Iterate through the buildings from left to right
        for i in range(len(heights)):
            # Step 2: Remove buildings that are blocked by the current building
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()  # Remove shorter or equal height buildings

            # Step 3: Append the current building index to the stack
            stack.append(i)

        # Step 4: Return the indices of buildings that have a clear ocean view
        return stack

# Left and Right View
class Solution2:
    def findBuildingsWithViews(self, heights: List[int]) -> List[int]:
        """
        Given a list `heights` where `heights[i]` represents the height of a building,
        return a list of indices of buildings that have either:
        - A left-side view (no taller building before it).
        - A right-side view (no taller building after it).
        
        Approach:
        - Use two monotonic stacks (one for the left view, one for the right view).
        - Merge results into a set and return sorted indices.
        
        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        def get_view_indices(heights: List[int], left_to_right: bool) -> List[int]:
            """ Helper function to compute left or right view indices using a stack. """
            stack = []
            indices = []
            n = len(heights)
            iterable = range(n) if left_to_right else range(n - 1, -1, -1)

            for i in iterable:
                while stack and heights[stack[-1]] <= heights[i]:
                    stack.pop()
                stack.append(i)
                indices.append(i)

            return set(indices)

        # Get buildings visible from the left and right
        left_view = get_view_indices(heights, left_to_right=True)
        right_view = get_view_indices(heights, left_to_right=False)

        # Combine both views and return sorted indices
        return sorted(left_view | right_view)


# ---- File: lc_179.py ----
'''
179. Largest Number
Solved
Medium
Topics
Companies
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109

✅ Time Complexity: O(n log n * k)
Where:

n = number of elements in nums

k = average length of the numbers (as strings)

Explanation:
String conversion of each number takes O(n * k), where k is the average digit length of the numbers.

Sorting takes O(n log n) comparisons.

Each comparison involves concatenating two strings (n1 + n2 and n2 + n1), which takes O(k) time.

So total sorting complexity is O(n log n * k)

Joining the strings at the end takes O(n * k) time.

So overall, the dominant term is O(n log n * k) due to the custom sort.

✅ Space Complexity: O(n * k)
Explanation:

You store all numbers as strings → O(n * k) space.

The sorted array and final joined string also take O(n * k) space.

🧠 Summary:
Time Complexity: O(n log n * k)

Space Complexity: O(n * k)
'''
from typing import List
from functools import cmp_to_key  # Import for custom sorting comparator

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert numbers to strings for lexicographical comparison
        array = list(map(str, nums))

        # Custom comparator function to determine sorting order
        def compare_num(n1, n2):
            # Compare concatenated numbers: (n1 + n2) vs (n2 + n1)
            if n1 + n2 > n2 + n1:
                return -1  # Place n1 before n2 (higher order)
            else:
                return 1   # Place n2 before n1 (higher order)

        # Sort using the custom comparator (descending order)
        array.sort(key=cmp_to_key(compare_num))

        # Edge case: If the largest number is "0", return "0" instead of "000..."
        if array[0] == "0":
            return "0"

        # Join the sorted elements to form the largest possible number
        largest = ''.join(array)

        return largest


# ---- File: lc_19.py ----
'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Time Complexity: O(L), where L is the length of the linked list.

Explanation:

The algorithm traverses the list in two phases:

Moving the leader pointer n steps ahead.

Moving both leader and trailer until the leader reaches the end.

Each phase takes at most O(L) time, so the total is linear with respect to the list length.

Space Complexity: O(1) because the algorithm uses only a constant amount of extra space, regardless of the input size.
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (e.g., removing the head)
        dummy = ListNode(-1)
        dummy.next = head

        # Initialize two pointers: leader will go ahead n steps
        trailer = leader = dummy

        # Move leader n steps ahead
        for _ in range(n):
            leader = leader.next
            # If n is longer than the list, return original head
            if not leader:
                return head

        # Move both pointers until leader reaches the end
        # After this, trailer will be right before the node to be removed
        while leader.next:
            leader = leader.next
            trailer = trailer.next

        # Skip the nth node from the end
        trailer.next = trailer.next.next

        # Return the head of the modified list
        return dummy.next


# ---- File: lc_1922.py ----
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        Given an integer `n`, count the number of "good" digit strings of length `n`.

        A "good" number:
        - Even indices (0-based) can be one of {0, 2, 4, 6, 8} (5 choices).
        - Odd indices (0-based) can be one of {2, 3, 5, 7} (4 choices).
        
        The task is to compute the total number of valid numbers of length `n` 
        under modulo `10^9 + 7`.
        """

        MOD = 10**9 + 7  # Large prime to prevent overflow
        
        # Step 1: Determine the count of even and odd positions
        if n % 2 == 0:
            ne = n // 2  # Number of even-indexed positions
        else:
            ne = (n + 1) // 2  # If odd length, there is one more even index than odd
        no = n // 2  # Number of odd-indexed positions

        # Step 2: Compute the total number of valid combinations
        # te = 5^ne (Choices for even-indexed positions)
        # tp = 4^no (Choices for odd-indexed positions)
        te = pow(5, ne, MOD)  # Fast modular exponentiation
        tp = pow(4, no, MOD)  # Fast modular exponentiation

        # Step 3: Compute the final result under modulo
        return (tp * te) % MOD  # Use modulo to prevent integer overflow


# ---- File: lc_1963.py ----
'''
1963. Minimum Number of Swaps to Make the String Balanced
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

 

Example 1:

Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".
Example 2:

Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".
Example 3:

Input: s = "[]"
Output: 0
Explanation: The string is already balanced.
 

Constraints:

n == s.length
2 <= n <= 106
n is even.
s[i] is either '[' or ']'.
The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.
'''
class Solution:
    def minSwaps(self, s: str) -> int:
        """
        Given a string `s` consisting of '[' and ']', determine the minimum number 
        of adjacent swaps needed to make the brackets balanced.

        A balanced string means that for every opening bracket '[', there is a 
        corresponding closing bracket ']' in the correct order.

        Approach:
        - Use a stack to track unmatched '[' brackets.
        - Count the number of unpaired '[' brackets at the end.
        - The number of swaps needed to fix them is (unpaired_count + 1) // 2.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        stack = []  # Stack to track unmatched '[' brackets

        # Step 1: Process the string to track unbalanced '[' brackets
        for c in s:
            if c == '[':
                # Push opening bracket to stack
                stack.append(c)
            elif stack and c == ']':
                # If there's a matching '[', remove it (balanced pair found)
                stack.pop()

        # Step 2: Compute the number of swaps needed
        # The remaining unpaired '[' count determines the number of swaps
        # Since each swap fixes 2 misplaced brackets, we use (len(stack) + 1) // 2
        return (len(stack) + 1) // 2


# ---- File: lc_2.py ----
'''
https://leetcode.com/problems/add-two-numbers/description/
O(max(n, m)), where n is the number of nodes in the first linked list l1, and m is the number of nodes in the second linked list l2.
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start the result list
        dummyNode = ListNode(0)
        curr = dummyNode  # Pointer to build the new list
        carry = 0         # Initialize carry to 0

        # Loop until both lists are exhausted and no carry remains
        while l1 or l2 or carry != 0:
            # Get the current values, defaulting to 0 if node is None
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # Compute the sum and carry
            currentSum = l1_val + l2_val + carry
            carry = currentSum // 10  # Update carry for next iteration

            # Create a new node with the digit (remainder after division by 10)
            newNode = ListNode(currentSum % 10)
            curr.next = newNode       # Append to the result list
            curr = newNode            # Move pointer forward

            # Move to next nodes in l1 and l2 if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the next node of dummy (skipping dummy head)
        return dummyNode.next


# ---- File: lc_200.py ----
'''
200. Number of Islands
Solved
Medium
Topics
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

🧠 Time and Space Complexity:
Time Complexity: O(m × n) — Each cell is visited once.

Space Complexity: O(m × n) — In the worst case, the visited set and recursion stack can grow to cover all land cells.
'''

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define possible movement directions (down, up, left, right)
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        
        # Get the number of rows and columns in the grid
        rows = len(grid)
        cols = len(grid[0])
        
        # Variable to count the number of islands
        island = 0
        
        # Depth-First Search (DFS) function to explore an island
        def dfs(i, j, visited):
            visited.add((i, j))  # Mark current cell as visited

            # Explore all 4 directions
            for dr, dc in directions:
                r, c = i + dr, j + dc
                if (
                    0 <= r < rows and
                    0 <= c < cols and
                    grid[r][c] == '1' and
                    (r, c) not in visited
                ):
                    dfs(r, c, visited)  # Recurse on connected land

        visited = set()  # Set to track visited cells

        # Iterate through all grid cells
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    island += 1           # Found a new island
                    dfs(i, j, visited)    # Explore the entire island

        return island  # Return total number of islands

         

        

# ---- File: lc_206.py ----
'''
https://leetcode.com/problems/reverse-linked-list/description/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize current node to head and previous node to None
        curr_node, prev_node = head, None

        # Traverse the list and reverse the links one by one
        while curr_node:
            next_node = curr_node.next   # Store the next node
            curr_node.next = prev_node   # Reverse the current node's pointer
            prev_node = curr_node        # Move prev_node one step forward
            curr_node = next_node        # Move curr_node one step forward

        # At the end, prev_node will be the new head of the reversed list
        return prev_node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node, return head
        if not head or not head.next:
            return head

        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)

        # Reverse the link: the next node should now point back to the current node
        head.next.next = head

        # Break the current node's next pointer to avoid cycles
        head.next = None

        # Return the new head of the reversed list
        return new_head


# ---- File: lc_207.py ----
'''
https://leetcode.com/problems/course-schedule/description/

✅ Time Complexity: O(n + p)
Where:

n is the number of courses (nodes in the graph),

p is the number of prerequisite pairs (edges in the graph).

Explanation:
Building the graph and in-degree list:
You iterate through each of the p prerequisites → O(p)

Initializing the queue:
You scan all n courses to check for zero in-degree → O(n)

Processing the queue (BFS):
Each course (node) is added and removed from the queue at most once → O(n)
For each node, you iterate through its neighbors (edges) → O(p)

So total: O(n + p)

✅ Space Complexity: O(n + p)
Explanation:

Adjacency list (graph) stores up to p edges → O(p)

In-degree array stores n values → O(n)

Queue can hold up to n courses in the worst case → O(n)


'''

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if it is possible to finish all courses given the prerequisite dependencies.
        Uses **Topological Sorting (Kahn's Algorithm)** to detect cycles in a directed graph.
        
        :param n: Number of courses (0 to n-1).
        :param prerequisites: List of prerequisite pairs [a, b] meaning "To take `b`, you must first complete `a`".
        :return: True if all courses can be completed, otherwise False.
        """

        # Step 1: Build the adjacency list representation of the graph
        graph = defaultdict(list)  # Graph adjacency list
        in_degrees = [0] * n  # `in_degrees[i]` represents the number of prerequisites for course `i`

        # Step 2: Populate the graph and in-degree array
        for prerequisite, course in prerequisites:
            graph[prerequisite].append(course)  # Add edge `prerequisite -> course`
            in_degrees[course] += 1  # Increment in-degree of `course`
        
        # Step 3: Initialize the queue with courses that have no prerequisites (in-degree = 0)
        queue = deque()
        for i in range(n):
            if in_degrees[i] == 0:  # If a course has no prerequisites, it can be taken immediately
                queue.append(i)
        
        # Step 4: Process courses in topological order
        enrolled_courses = 0  # Track the number of courses that can be completed
        while queue:
            node = queue.popleft()  # Take a course with no prerequisites
            enrolled_courses += 1  # Count this course as completed

            # Reduce the in-degree of dependent courses
            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1  # Reduce prerequisite count

                # If a dependent course now has no prerequisites, add it to the queue
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: If we could process all courses, return True, otherwise return False
        return enrolled_courses == n  # If we enrolled in all `n` courses, there's no cycle


# ---- File: lc_210.py ----
'''
https://leetcode.com/problems/course-schedule-ii/description/

✅ Time Complexity: O(n + p)
Where:

n is the number of courses,

p is the number of prerequisite pairs.

Explanation:
Graph Construction:

Looping through p prerequisite pairs to build the adjacency list and in_degrees array → O(p)

Queue Initialization:

Iterating through all n courses to enqueue those with zero in-degree → O(n)

Topological Sort Processing:

Each node (course) is dequeued at most once → O(n)

For each node, you loop over its neighbors (edges), and across all nodes, you process all p edges once → O(p)

So total time complexity = O(n + p)

✅ Space Complexity: O(n + p)
Explanation:

Adjacency list (graph) stores p edges → O(p)

In-degree array stores n values → O(n)

Queue can hold up to n elements → O(n)

Result list (course_order) stores up to n elements → O(n)

So total space complexity = O(n + p)

'''
from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Returns the order in which courses should be taken to complete all courses.
        Uses **Topological Sorting (Kahn's Algorithm)** to find a valid order.
        If it is not possible to complete all courses (cycle detected), return an empty list.
        
        :param n: Number of courses (0 to n-1).
        :param prerequisites: List of prerequisite pairs [course, prerequisite] 
                              meaning "To take `course`, you must first complete `prerequisite`".
        :return: A list representing the order of courses, or an empty list if not possible.
        """

        # Step 1: Build the graph and in-degree array
        graph = defaultdict(list)  # Adjacency list representation
        in_degrees = [0] * n  # Track number of prerequisites for each course

        # Step 2: Populate the graph and in-degree array
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)  # prerequisite → course (correct direction)
            in_degrees[course] += 1  # Increment in-degree of `course`
        
        # Step 3: Initialize the queue with courses that have no prerequisites (in-degree = 0)
        queue = deque()
        for i in range(n):
            if in_degrees[i] == 0:  # No prerequisites, can take immediately
                queue.append(i)
        
        # Step 4: Process courses in topological order
        course_order = []  # Store the order in which courses should be taken

        while queue:
            node = queue.popleft()  # Take a course with no prerequisites
            course_order.append(node)  # Append course to order list

            # Reduce the in-degree of dependent courses
            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1  # Remove the prerequisite requirement

                # If a dependent course now has no prerequisites, add it to the queue
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: If all courses are processed, return the order. Otherwise, return an empty list (cycle detected).
        return course_order if len(course_order) == n else []


# ---- File: lc_212.py ----
'''
https://leetcode.com/problems/word-search-ii/description/

✅ Time Complexity: O(m × n × 4^L)
Where:

m = number of rows in the board

n = number of columns in the board

L = maximum length of any word in words

Explanation:
Trie Construction (Preprocessing):

Inserting each word takes O(L), and there are k words in total → O(k × L) time.

DFS Traversal:

You initiate DFS from each cell in the board → m × n starting points.

From each starting cell, the DFS explores up to 4 directions recursively.

The depth of each DFS call stack is at most L (since word length is bounded by L).

In the worst case (no pruning), each DFS path can take up to O(4^L) time (like a 4-ary tree of depth L).

So total DFS traversal: O(m × n × 4^L)

⚠️ However, the Trie structure significantly prunes invalid paths early, making it much faster in practice than the theoretical upper bound.

✅ Space Complexity: O(k × L) + O(L)
Explanation:

Trie: Stores up to k × L nodes → O(k × L)

DFS recursion stack: Maximum depth = length of the longest word → O(L)

Result list (res) stores up to k words → O(k), but not counted as auxiliary space
'''

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}      # Maps character to TrieNode
        self.word = None        # Stores the complete word at the terminal node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build the Trie from the list of words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                # Create a new TrieNode if char not already a child
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark the end of a word in the Trie

        res = []  # Result list to store words found on the board

        def dfs(r: int, c: int, node: TrieNode):
            """
            Perform DFS from the board cell at (r, c), traversing Trie as we match characters.
            """
            # If this node marks the end of a word, collect it
            if node.word:
                res.append(node.word)
                node.word = None  # Avoid duplicate entries

            temp = board[r][c]
            board[r][c] = '#'  # Mark the current cell as visited

            # Define possible directions: up, left, down, right
            dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for dr, dc in dirs:
                next_r, next_c = r + dr, c + dc
                # Check bounds and whether next character is part of Trie path
                if (0 <= next_r < len(board) and 
                    0 <= next_c < len(board[0]) and 
                    board[next_r][next_c] in node.children):
                    dfs(next_r, next_c, node.children[board[next_r][next_c]])

            board[r][c] = temp  # Backtrack: unmark the visited cell

        # Step 2: Start DFS from every cell that matches a starting character in Trie
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.children:
                    dfs(r, c, root.children[board[r][c]])

        return res


# ---- File: lc_227.py ----
'''
https://leetcode.com/problems/basic-calculator-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

✅ Time Complexity: O(n), where n is the length of the input string s.
Explanation:

You loop through the entire string exactly once → O(n)

Each number and operator is processed once.

Stack operations (append, pop) are O(1) each.

Final sum(stack) runs in O(n) time (in the worst case, every digit forms a new number).

So overall:
O(n)

✅ Space Complexity: O(n) in the worst case.
Explanation:

The stack stores intermediate results.

In the worst case (e.g., only additions/subtractions), you push up to n values onto the stack → O(n) space.

currentNumber, operation, and loop variables take constant space.
'''

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = []               # Stack to store intermediate results
        currentNumber = 0        # Tracks the current number being parsed
        operation = '+'          # Default operation is addition

        for i, char in enumerate(s):
            # Build the current number if the character is a digit
            if char.isdigit():
                currentNumber = currentNumber * 10 + int(char)

            # If it's an operator (not digit and not space) or end of string
            # The reason we check this is to ensure that the very last number in the string is processed, even if it’s not followed by an operator.
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                # Apply the last stored operation to currentNumber
                if operation == '+':
                    stack.append(currentNumber)  # Add to stack as is
                elif operation == '-':
                    stack.append(-currentNumber) # Push negative number
                elif operation == '*':
                    stack.append(stack.pop() * currentNumber)  # Multiply with top of stack
                elif operation == '/':
                    prev = stack.pop()
                    # Use int() to truncate towards zero (like Java's integer division)
                    stack.append(int(prev / currentNumber))

                # Update operation and reset current number for next round
                operation = char
                currentNumber = 0

        # Final result is the sum of all values in the stack
        return sum(stack)


# ---- File: lc_23.py ----
'''
23. Merge k Sorted Lists
Solved
Hard
Topics
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

Time Complexity: O(N log k), where:

k is the number of linked lists,

N is the total number of nodes across all lists.

Explanation:

Each node is inserted into and removed from the min-heap exactly once.

Inserting or removing from a heap of size k takes O(log k) time.

Since there are N nodes in total, the overall time complexity is O(N log k).

Space Complexity: O(k)

Explanation:

The min-heap holds at most k nodes at any time (one from each list).

Aside from the heap and the output list (which doesn't count as extra space), no additional data structures are used.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min heap to store the smallest elements from k linked lists
        heap = []
        
        # Define a custom comparator for ListNode objects to allow heapq to work
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        # Push the head node of each linked list into the heap
        for head in lists:
            if head:  # Only push non-empty lists
                heapq.heappush(heap, head)

        # Dummy node to serve as the starting point of the merged linked list
        dummy = ListNode(-1)
        curr = dummy  # Pointer to track the current position in the merged list

        # Process the heap until all nodes are merged
        while heap:
            # Extract the smallest node from the heap
            smallest_node = heapq.heappop(heap)
            # Append it to the merged list
            curr.next = smallest_node
            curr = curr.next  # Move the pointer forward
            
            # If there are more nodes in the current list, push the next node into the heap
            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next)

        # Return the merged linked list (excluding the dummy node)
        return dummy.next

        

# ---- File: lc_232.py ----
'''
http://leetcode.com/problems/implement-queue-using-stacks/description/
🔧 push(x)
Time Complexity: O(1)

Why: Adding an element to the end of a Python list (append) takes constant time.

🔧 pop()
Time Complexity: Amortized O(1)
Worst-case: O(n)

Why:

If output stack is not empty, popping from it is O(1).

If output is empty, all elements from input are moved to output, which takes O(n) time only once for every n pushes.

Each element is moved from input to output only once, so across n operations, the total cost is O(n), resulting in amortized O(1) per operation.

🔧 peek()
Time Complexity: Amortized O(1)
Worst-case: O(n)

Why: Same reason as pop(). The transfer from input to output only happens once per element. Peeking the last element of a list is O(1).

🔧 empty()
Time Complexity: O(1)

Why: Simply checks if both stacks are empty using a logical and on two list checks.


'''

class MyQueue:

    def __init__(self):
        # Two stacks:
        # 'input' is used for enqueue (push) operations
        # 'output' is used for dequeue (pop/peek) operations
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        # Always push to the input stack
        self.input.append(x)

    def pop(self) -> int:
        # Ensure the output stack has the correct order
        self.peek()
        # Pop from the output stack (front of the queue)
        return self.output.pop()

    def peek(self) -> int:
        # If output stack is empty, move all elements from input to output
        # This reverses the order, making the oldest element accessible on top of output
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        # Return the element at the front of the queue
        return self.output[-1]

    def empty(self) -> bool:
        # Queue is empty only when both stacks are empty
        return not self.output and not self.input


# ---- File: lc_235.py ----
'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

✅ Time Complexity: O(h), where h is the height of the BST.
Explanation:

You traverse the tree starting from the root, going either left or right depending on the values of p and q.

In the best case (balanced BST), height h = log n, so time is O(log n).

In the worst case (unbalanced BST or skewed tree), height h = n, so time is O(n).

✅ Space Complexity:
Iterative version (your code): O(1)

You use no recursion and only a few variables — constant space.
Recursive version (if you used recursion): O(h) for the recursion stack.

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree (BST).

        The LCA of `p` and `q` in a BST is defined as the lowest node in the tree
        that has both `p` and `q` as descendants.

        Since it's a BST:
        - If both `p` and `q` are smaller than `root`, the LCA must be in the left subtree.
        - If both `p` and `q` are greater than `root`, the LCA must be in the right subtree.
        - If `p` and `q` are on different sides, `root` is the LCA.

        :param root: The root of the BST.
        :param p: First node in the BST.
        :param q: Second node in the BST.
        :return: The lowest common ancestor node of `p` and `q`.
        """
        
        while root:
            # If both `p` and `q` are smaller than `root`, move to the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left  

            # If both `p` and `q` are greater than `root`, move to the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right  

            # If `p` and `q` are on different sides, or one of them is `root`, we found the LCA
            else:
                return root  # This is the lowest common ancestor

        return None  # If no LCA is found (shouldn't happen in a valid BST)


# ---- File: lc_249.py ----
'''
https://leetcode.com/problems/group-shifted-strings/description/

Sure! Here's the time and space complexity explanation for your groupStrings function:

✅ Time Complexity: O(n × m)
Where:

n is the number of strings in the input list strings

m is the maximum length of any string

Explanation:
For each of the n strings:

The get_hash function iterates through the string (up to m - 1 character pairs) → O(m)

Hash key generation (including string concatenation) takes O(m) in practice because it handles up to m characters.

Adding strings to a dictionary and converting to list(groups.values()) are also O(n) operations in total.

So, the total time is:

text
Copy
Edit
O(n × m) → processing all n strings of length up to m
✅ Space Complexity: O(n × m)
Explanation:

The hash map stores all n strings grouped by their hash key.

In the worst case (no groups share a hash key), each string is stored once → O(n × m) space in total.

Each hash key (as a string) also takes up to O(m) space.


'''
from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        # Function to generate a unique hash key for each shift group
        def get_hash(string: str):
            key = []
            
            # Iterate through the string to calculate shift differences
            for i in range(1, len(string)):
                diff = ord(string[i]) - ord(string[i-1])  # Calculate difference between adjacent characters
                
                # If difference is negative, adjust for circular shift in alphabet
                if diff < 0:
                    diff += 26
                
                # Store the difference with a separator to create a unique pattern
                key.append(str(diff) + '#')
            
            # Append a special character to distinguish different shift groups
            key.append('.')
            
            # Return the generated hash key as a string
            return ''.join(key)

        # Dictionary to group strings by their computed hash keys
        groups = defaultdict(list)
        
        # Iterate over all strings in the input list
        for string in strings:
            hash_key = get_hash(string)  # Compute the unique shift-based hash
            groups[hash_key].append(string)  # Group the strings based on their hash
        
        # Return all the grouped values as a list of lists
        return list(groups.values())


# ---- File: lc_251.py ----
import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Partition function to rearrange elements around a pivot
        def partition(nums: List[int], left: int, right: int) -> int:
            # Choose a random pivot and move it to the end
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            pivot = nums[right]
            
            # Pointer for the next smaller-than-pivot position
            lo = left
            for i in range(left, right):
                # Push all smaller elements to the left
                if nums[i] < pivot:
                    nums[lo], nums[i] = nums[i], nums[lo]
                    lo += 1
            
            # Finally place pivot in its correct sorted position
            nums[lo], nums[right] = nums[right], nums[lo]
            return lo  # Return the pivot index

        # Quickselect to find the kth largest element
        def quickselect(nums: List[int], left: int, right: int, k: int) -> int:
            n = len(nums)
            # Base case: only one element
            if left >= right:
                return nums[left]

            # Partition and get pivot index
            pivot_index = partition(nums, left, right)

            # Target index for kth largest is (n - k)
            if pivot_index < n - k:
                # Recurse right
                return quickselect(nums, pivot_index + 1, right, k)
            elif pivot_index > n- k:
                return quickselect(nums, left, pivot_index - 1, k)
            else:
                return nums[pivot_index]
        
        return quickselect(nums, 0, len(nums) - 1, k)

# ---- File: lc_252.py ----
'''
https://leetcode.com/problems/meeting-rooms/

✅ Time Complexity: O(n log n)
Where:

n is the number of meeting intervals.

Explanation:
Sorting the intervals by start time → O(n log n)

Single pass through the intervals to check for overlaps → O(n)

So overall time complexity =
O(n log n)

✅ Space Complexity: O(1)
Explanation:

Sorting is done in-place (assuming Python’s Timsort).

No additional data structures that scale with input size are used.


'''

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Determines if a person can attend all meetings without any time overlap.

        :param intervals: List of meeting time intervals [start, end]
        :return: True if no meetings overlap, False otherwise
        """

        # Edge case: no meetings at all
        if not intervals:
            return True

        # Step 1: Sort all intervals based on start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize previous meeting to the first one
        prev = intervals[0]

        # Step 3: Iterate through the rest of the meetings
        for interval in intervals[1:]:
            # If the current meeting starts before the previous one ends, they overlap
            if interval[0] < prev[1]:
                return False  # Can't attend both meetings

            # Otherwise, update the previous meeting to current
            prev = interval

        # Step 4: If we never found an overlap, return True
        return True


# ---- File: lc_253.py ----
'''
https://leetcode.com/problems/meeting-rooms-ii/description/

✅ Time Complexity: O(n log n)
Where:

n is the number of meeting intervals.

Explanation:
Sorting intervals by start time:

Takes O(n log n) time.

Processing each interval:

Each heapq.heappush and heapq.heappop operation takes O(log k), where k is the size of the heap (≤ n).

In total, across all n intervals, heap operations take O(n log n) in the worst case.

So, overall time complexity:
O(n log n)

✅ Space Complexity: O(n)
Explanation:

In the worst case (all meetings overlap), you store all n end times in the min-heap.

So heap size can grow up to n → O(n) space.
'''

import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Returns the minimum number of meeting rooms required to accommodate all meetings.

        :param intervals: List of meeting time intervals [start, end]
        :return: Minimum number of meeting rooms needed
        """

        # Edge case: No meetings, no rooms needed
        if not intervals:
            return 0

        # Step 1: Sort all intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize a min heap to track meeting end times (rooms in use)
        # The heap stores the end times of meetings currently using a room
        free_rooms = []

        # Step 3: Add the end time of the first meeting to the heap
        # This means one meeting is using one room
        heapq.heappush(free_rooms, intervals[0][1])

        # Step 4: Process the remaining meetings
        for i in intervals[1:]:
            # If the earliest ending meeting ends before the current meeting starts
            # it means one room got free, we can reuse it
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)  # Free up the room

            # Push the current meeting's end time into the heap
            # This occupies a room (either reused or a new one)
            heapq.heappush(free_rooms, i[1])

        # Step 5: The size of the heap tells us how many rooms are in use at the peak
        return len(free_rooms)


# ---- File: lc_270.py ----
'''
https://leetcode.com/problems/closest-binary-search-tree-value/description/

✅ Solution 1: Inorder Traversal + Linear Search
Time Complexity: O(n)
Inorder traversal visits every node once → O(n)

Finding the closest value in the list using min(..., key=...) → O(n)

Total: O(n)

Space Complexity: O(n)
You store all node values in the values list → O(n)

Recursion stack (in worst case for unbalanced tree) → up to O(n)

✅ Solution 2: Optimized BST Traversal (Iterative)
Time Complexity: O(h), where h is the height of the BST
Each step of the traversal compares and moves either left or right, like binary search.

In a balanced BST, h = log n, so time is O(log n).

In a skewed BST, h = n, so time is O(n) in worst case.

Space Complexity: O(1)
No recursion or extra space used except a few variables.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        values = []  # List to store the inorder traversal values

        def inorder(node: Optional[TreeNode]):
            """Recursive function to perform inorder traversal (Left -> Root -> Right)."""
            nonlocal values  # Use nonlocal to modify the values list
            if node:
                inorder(node.left)   # Visit the left subtree
                values.append(node.val)  # Process the current node
                inorder(node.right)  # Visit the right subtree

        inorder(root)  # Start the inorder traversal
        
        # Find the value in the list that is closest to the target
        return min(values, key=lambda x: abs(target - x))  

    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val  # Initialize closest with the root value
        
        while root:
            # Check if the current node is a better candidate for "closest"
            if (
                # ✅ Case 1: current node is strictly closer to target than previous closest
                abs(root.val - target) < abs(closest - target)
                
                # ✅ Case 2: current node is equally close but numerically smaller
                or (
                    abs(root.val - target) == abs(closest - target)  # Same distance
                    and root.val < closest                           # Prefer smaller value
                )
            ):
                # ✅ Update closest to current node's value
                closest = root.val
            
            # Move left if target is smaller, right if target is larger
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest

        




# ---- File: lc_283.py ----
'''
283. Move Zeroes
Solved
Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all 0's to the end of the list while maintaining the relative order of the non-zero elements.
        Modifies the input list in-place.
        """
        left = 0  # Position to place the next non-zero element

        # Move all non-zero elements to the front
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


# ---- File: lc_304.py ----
'''
https://leetcode.com/problems/range-sum-query-2d-immutable/
✅ __init__ Method (Constructor)
Time Complexity: O(m × n)
Where m = number of rows, n = number of columns in the matrix.

You initialize the prefix sum matrix and compute prefix sums row by row.

Each cell is processed exactly once.

Space Complexity: O(m × n)
A new 2D array prefixSum of the same dimensions as the input matrix is created.

✅ sumRegion(row1, col1, row2, col2)
Time Complexity: O(r), where r = row2 - row1 + 1
For each row between row1 and row2, you compute a single subtraction to get the sum for that row segment.

This takes linear time in the number of rows spanned by the region.

⚠️ Note: This is not constant time since the query still loops over rows — it's fast, but not the optimal 2D prefix sum approach (which would be O(1)).

Space Complexity: O(1)
No additional space is used apart from a few variables.
'''
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        
        # Step 1: Initialize a 2D prefix sum matrix with the same dimensions
        self.prefixSum = [[0] * self.COLS for _ in range(self.ROWS)]

        # Step 2: Build row-wise prefix sums
        for row in range(self.ROWS):
            self.prefixSum[row][0] = matrix[row][0]  # First column is the same
            for col in range(1, self.COLS):
                # Add current matrix value to the running row sum
                self.prefixSum[row][col] = self.prefixSum[row][col - 1] + matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Compute the sum of elements within the rectangle from (row1, col1) to (row2, col2), inclusive.
        Only row-wise prefix sums are used, so each row is processed individually.
        """
        res = 0
        for row in range(row1, row2 + 1):  # Traverse from row1 to row2 inclusive
            if col1 > 0:
                # Use prefix sum: subtract left part (before col1)
                res += self.prefixSum[row][col2] - self.prefixSum[row][col1 - 1]
            else:
                # Start from beginning of row
                res += self.prefixSum[row][col2]

        return res


# ---- File: lc_31.py ----
'''
https://leetcode.com/problems/next-permutation/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

Time Complexity: O(n), where n is the length of the list nums.

Explanation:

Step 1: Scanning from right to left to find the first decreasing element takes at most O(n).

Step 2: Finding the next larger element to swap also takes at most O(n).

Step 3: Swapping two elements takes O(1).

Step 4: Reversing the sublist takes at most O(n).

All steps together are linear in time, so the total time complexity is O(n).

Space Complexity: O(1)

The algorithm modifies the input list in place and uses only a constant amount of extra space.
'''
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies the list 'nums' in-place to produce the next lexicographical permutation.
        If no such permutation exists (i.e., the list is in descending order), it transforms into the lowest possible order.

        :param nums: List of integers representing a permutation.
        :return: None (modifies 'nums' in-place).
        """
        
        n = len(nums)
        i = n - 2  # Start from the second last element
        
        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i+1] <= nums[i]:  
            i -= 1  # Keep moving left while the sequence is non-increasing
        
        if i >= 0:  # If a decreasing element was found
            j = n - 1  # Start from the last element
            
            # Step 2: Find the first element larger than nums[i] from the right
            while nums[j] <= nums[i]:
                j -= 1  
            
            # Step 3: Swap nums[i] and nums[j] to get the next larger permutation
            nums[i], nums[j] = nums[j], nums[i]  
        
        # Step 4: Reverse the sequence after index 'i' to get the next lexicographical order
        self.reverse(nums, i + 1)

    def reverse(self, nums: List[int], start: int) -> None:
        """
        Reverses the sublist nums[start:] in-place.

        :param nums: List of numbers.
        :param start: Starting index of the sublist to reverse.
        :return: None (modifies 'nums' in-place).
        """
        i, j = start, len(nums) - 1  # Start and end pointers
        
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]  # Swap elements
            i += 1
            j -= 1


# ---- File: lc_311.py ----
'''
https://leetcode.com/problems/sparse-matrix-multiplication/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

🔸 Time Complexity: O(nz1 + nz2 + z)
Where:

nz1 = number of non-zero elements in mat1

nz2 = number of non-zero elements in mat2

z = number of actual non-zero multiplications (i.e., shared non-zero indices between corresponding row in mat1 and column in mat2)

➡️ This is much better than the naive O(m1 * n1 * n2) time when matrices are sparse (contain lots of zeros).

🔸 Space Complexity: O(nz1 + nz2 + m1 * n2)
O(nz1) for storing sparse representation X of mat1

O(nz2) for storing sparse representation Y of mat2

O(m1 * n2) for storing the result matrix res (though it may contain many zeros, it's fully allocated)

➡️ The extra space for X and Y is still efficient for sparse matrices compared to storing full matrices.
'''

from collections import defaultdict

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # Dimensions
        m1, n1 = len(mat1), len(mat1[0])  # mat1: m1 x n1
        m2, n2 = len(mat2), len(mat2[0])  # mat2: m2 x n2

        # Initialize result matrix with zeros: shape m1 x n2
        res = [[0 for _ in range(n2)] for _ in range(m1)]

        # X[i][j] will store non-zero values of mat1 for row i
        X = [defaultdict(int) for _ in range(m1)]

        # Y[j][i] will store non-zero values of mat2 transposed: col j → row i
        Y = [defaultdict(int) for _ in range(n2)]

        # Build sparse representation of mat1
        for i in range(m1):
            for j in range(n1):
                if mat1[i][j] != 0:
                    X[i][j] = mat1[i][j]

        # Build sparse representation of mat2 (column-wise as row-wise)
        for i in range(m2):
            for j in range(n2):
                if mat2[i][j] != 0:
                    Y[j][i] = mat2[i][j]  # Notice: Y is accessed by [col][row] (transposed)

        # Multiply non-zero entries only
        for i in range(m1):          # For each row in mat1
            for j in range(n2):      # For each col in mat2
                for r in X[i]:       # For each non-zero col in mat1 row i
                    if r in Y[j]:    # If same index is non-zero in mat2 col j
                        res[i][j] += X[i][r] * Y[j][r]

        return res


# ---- File: lc_314.py ----
'''
314. Binary Tree Vertical Order Traversal
Solved
Medium
Topics
Companies
Hint
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]

📌 Final Time Complexity:
🟩 O(n) — where n is the number of nodes in the binary tree

All operations are linear in the number of nodes. There are no nested loops or redundant traversals.

🧠 Space Complexity (Bonus):
treeData: stores each node once → O(n)

q and cols: hold up to one level of nodes at a time → O(w) where w = max width of the tree (worst case: O(n))

res: stores all node values grouped → O(n)

➡️ Overall space complexity: O(n)
'''

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: If the tree is empty, return an empty list
        if not root:
            return []
        
        # Dictionary to store node values grouped by their column index
        treeData = defaultdict(list)

        # Queue to perform level-order traversal (BFS)
        q = deque([root])

        # Queue to track the column index corresponding to each node
        cols = deque([0])  # Root starts at column index 0

        # Variables to track the minimum and maximum column indices
        _min = 0
        _max = 0

        # Result list to store the vertical order traversal
        res = []

        # Perform BFS traversal
        while q:
            # Pop the node and its corresponding column index
            node = q.popleft()
            col = cols.popleft()

            # Store the node's value in the corresponding column index
            treeData[col].append(node.val)

            # If the node has a left child, add it to the queue with col - 1
            if node.left:
                q.append(node.left)
                cols.append(col - 1)
                _min = min(_min, col - 1)  # Update the minimum column index

            # If the node has a right child, add it to the queue with col + 1
            if node.right:
                q.append(node.right)
                cols.append(col + 1)
                _max = max(_max, col + 1)  # Update the maximum column index
            
        # Collect results in order of column indices from _min to _max
        for i in range(_min, _max + 1): 
            res.append(treeData.get(i))

        return res


# ---- File: lc_323.py ----
'''
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

✅ Time Complexity: O(E × α(n))
Where:

n = number of nodes

E = number of edges

α(n) = inverse Ackermann function — grows extremely slowly and is considered constant (≤ 5) in all practical scenarios.

Explanation:
find(x) uses path compression, and union(x, y) uses union by size.

These optimizations ensure that each union or find operation takes amortized O(α(n)) time.

You loop through each edge once → E calls to union().

So total time complexity:
✅ O(E × α(n)), which is practically linear time.

✅ Space Complexity: O(n)
Explanation:

You maintain two arrays:

parent[] of size n

size[] of size n

So total auxiliary space = O(n)
'''

from typing import List

# Union-Find (Disjoint Set) class
class UnionFind:
    def __init__(self, size: int):
        # Initialize each node as its own parent (self-loop)
        self.parent = [i for i in range(size)]
        # Track the size of each connected component
        self.size = [1] * size  

    def union(self, x: int, y: int) -> bool:
        """
        Merges two sets if they are disjoint.
        Returns False if they are already connected (i.e., cycle detected).
        """
        rep_x, rep_y = self.find(x), self.find(y)  # Find representatives (leaders)
        
        if rep_x == rep_y:
            return False  # If both nodes have the same representative, cycle detected

        # Union by size: attach the smaller tree under the larger tree
        if self.size[rep_x] > self.size[rep_y]:
            self.parent[rep_y] = rep_x  # Make rep_x the parent of rep_y
            self.size[rep_x] += self.size[rep_y]  # Update size of the component
        else:
            self.parent[rep_x] = rep_y  # Make rep_y the parent of rep_x
            self.size[rep_y] += self.size[rep_x]  # Update size of the component

        return True  # Successfully merged

        

    def find(self, x: int) -> int:
        """
        Finds the representative (leader) of the set that `x` belongs to.
        Uses **path compression** to flatten the tree, optimizing future queries.
        """
        if x == self.parent[x]:
            return x  # If `x` is its own parent, it is the root
        
        # Path Compression: directly connect node to its root representative
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def size(self, x:int) -> int:
        return self.size[self.find(x)]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n
        for u, v in edges:
            if uf.union(u,v):
                res -=1
        return res
        

# ---- File: lc_3371.py ----
'''
https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
'''

from typing import List

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        """
        Finds the largest outlier in the list.
        An outlier is defined as a number `num` such that removing `num` twice
        results in another number that already exists in the list.

        :param nums: List of integers
        :return: The largest valid outlier or float('-inf') if none exist.
        """
        
        # Step 1: Compute the total sum of all numbers
        total_sum = sum(nums)  

        # Step 2: Initialize variable to store the largest valid outlier
        largest_outlier = float('-inf')

        # Step 3: Build a frequency map to count occurrences of each number
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1  # Count each number
        
        # Step 4: Iterate through each unique number
        for num in freq_map.keys():
            # Compute the potential outlier using the formula:
            potential_outlier = total_sum - 2 * num  
            
            # Step 5: Check if potential_outlier exists in the frequency map
            if potential_outlier in freq_map:
                # Ensure validity:
                # - If potential_outlier is different from num, it's valid
                # - If potential_outlier == num, then num must appear at least twice
                if potential_outlier != num or freq_map[num] > 1:
                    # Corrected typo: Use largest_outlier instead of larget_outlier
                    largest_outlier = max(largest_outlier, potential_outlier)
        
        # Step 6: Return the largest outlier found (or -inf if none exist)
        return largest_outlier


# ---- File: lc_339.py ----
'''
https://leetcode.com/problems/nested-list-weight-sum/description/
339. Nested List Weight Sum
Solved
Medium
Topics
Companies
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

 

Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
Example 2:


Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
Example 3:

Input: nestedList = [0]
Output: 0

✅ Time Complexity: O(n)
Where:

n is the total number of elements in the entire nested structure, including both integers and lists.

Why?
You visit every element exactly once, whether it's:

an integer → multiply it by its depth

or a list → recursively traverse it

So the number of isInteger(), getInteger(), and getList() calls is proportional to the number of total elements → O(n)

✅ Space Complexity:
DFS version: O(d) — where d is the maximum depth of nesting

Comes from the recursion stack

BFS version: O(w) — where w is the maximum number of elements at any level

Comes from the queue
'''
from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#     def __init__(self, value=None):
#         """
#         If value is not specified, initializes an empty list.
#         Otherwise initializes a single integer equal to value.
#         """
#
#     def isInteger(self):
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         :rtype bool
#         """
#
#     def add(self, elem):
#         """
#         Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#         :rtype void
#         """
#
#     def setInteger(self, value):
#         """
#         Set this NestedInteger to hold a single integer equal to value.
#         :rtype void
#         """
#
#     def getInteger(self):
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         :rtype int
#         """
#
#     def getList(self):
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         :rtype List[NestedInteger]
#         """

class Solution:
    def depthSum(self, nestedList: List["NestedInteger"]) -> int:
        # Helper function to perform DFS (Depth-First Search)
        def helper(nested, depth):
            total = 0  # Local sum at this depth level
            
            # Iterate through each element in the nested list
            for item in nested:
                if item.isInteger():
                    # If it's an integer, multiply it by the depth and add to total
                    total += depth * item.getInteger()
                else:
                    # If it's a list, recursively call helper function with increased depth
                    total += helper(item.getList(), depth + 1)
            
            return total  # Return the accumulated sum at this level
        
        # Start the recursive function with depth 1
        return helper(nestedList, 1)

from typing import List
from collections import deque

'''
Time: O(n), where n is the total number of NestedInteger elements (including those nested)

Space: O(n) for the queue in the worst case


'''
class Solution2:
    def depthSum(self, nestedList: List['NestedInteger']) -> int:
        total = 0
        queue = deque([(item, 1) for item in nestedList])  # Each element is (NestedInteger, depth)

        while queue:
            current, depth = queue.popleft()

            if current.isInteger():
                total += current.getInteger() * depth
            else:
                for ni in current.getList():
                    queue.append((ni, depth + 1))  # Increase depth for nested list

        return total


# ---- File: lc_340.py ----
'''
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
'''

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right = 0, 0  # Sliding window boundaries
        char_freq = defaultdict(int)  # Frequency map of characters in the current window
        maxLen = 0  # Track the length of the longest valid substring

        # Expand the window to the right
        while right < len(s):
            right_char = s[right]
            char_freq[right_char] += 1  # Add current character to frequency map

            # Shrink the window from the left if we exceed k distinct characters
            while len(char_freq) > k:
                left_char = s[left]
                char_freq[left_char] -= 1  # Reduce count of the leftmost character
                if char_freq[left_char] == 0:
                    del char_freq[left_char]  # Remove it from map if frequency is 0
                left += 1  # Move the left boundary forward

            # Update maxLen if the current window is longer
            maxLen = max(maxLen, right - left + 1)
            right += 1  # Expand the right boundary

        return maxLen  # Return the maximum length found


# ---- File: lc_346.py ----
'''
https://leetcode.com/problems/moving-average-from-data-stream/

⏱ Time Complexity:
append: O(1)

sum(self.nums[start:]): O(k) where k = size
(slicing and summing the window takes linear time per call)

💾 Space Complexity: O(n)
The list self.nums stores all values received, even outside the window.
'''

class MovingAverage:

    def __init__(self, size: int):
        self.nums = []       # List to store all incoming values
        self.size = size     # Size of the moving window

    def next(self, val: int) -> float:
        self.nums.append(val)  # Add the new value to the list

        if len(self.nums) <= self.size:
            # If total values seen so far are fewer than window size
            return sum(self.nums) / len(self.nums)
        else:
            # Use only the last `size` values from the list
            start = len(self.nums) - self.size
            return sum(self.nums[start:]) / self.size



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

'''
⏱ Time Complexity:
append: O(1)

popleft: O(1)

sum is maintained incrementally → O(1) per next() call

💾 Space Complexity: O(k)
Only the most recent k = size values are stored in the queue.
'''

from collections import deque

class MovingAverage2:

    def __init__(self, size: int):
        self.sum = 0                    # Running sum of the current window
        self.size = size               # Maximum size of the window
        self.window = deque()          # Store only the last `size` elements

    def next(self, val: int) -> float:
        self.sum += val                # Add the new value to the sum
        self.window.append(val)        # Add to the sliding window

        if len(self.window) > self.size:
            # If window is full, remove the oldest value
            self.sum -= self.window.popleft()

        return self.sum / len(self.window)  # Return the average




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# ---- File: lc_35.py ----
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize the binary search boundaries
        left, right = 0, len(nums)  # Note: 'right' is exclusive

        # Perform binary search
        while left < right:
            # Find the middle index
            mid = (left + right) // 2

            # If the mid value is greater than or equal to target,
            # the target could be at mid or somewhere to the left
            if nums[mid] >= target:
                right = mid  # Shrink the search space to the left half (including mid)
            else:
                # If nums[mid] < target, the target must be to the right
                left = mid + 1  # Move left boundary to mid + 1

        # When loop exits, left == right and points to the correct insert position
        return left


# ---- File: lc_36.py ----
'''
https://leetcode.com/problems/valid-sudoku/

Time Complexity: O(1)

Explanation:

The board size is fixed at 9x9 (standard Sudoku), so the number of iterations is constant: 9 * 9 = 81 cells.

Each check and insertion into a set is done in constant time, O(1).

Since the input size does not grow beyond 81 cells, the entire algorithm runs in constant time.

Space Complexity: O(1)

Explanation:

Although we use sets to store seen values for rows, columns, and subgrids, each can hold at most 9 digits (1–9).

Thus, the total space used is constant and does not scale with input size.
'''

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track the seen digits for each row, column, and 3x3 subgrid
        row_sets = [set() for _ in range(9)]                 # One set per row
        col_sets = [set() for _ in range(9)]                 # One set per column
        subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]  # 3x3 grid of sets for subgrids

        # Traverse every cell of the board
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                # Skip empty cells
                if num == '.':
                    continue

                # Check if number already exists in the current row
                if num in row_sets[r]:
                    return False  # Invalid: duplicate in row

                # Check if number already exists in the current column
                if num in col_sets[c]:
                    return False  # Invalid: duplicate in column

                # Check if number already exists in the current 3x3 subgrid
                if num in subgrid_sets[r // 3][c // 3]:
                    return False  # Invalid: duplicate in subgrid

                # If valid so far, record the number in the appropriate sets
                row_sets[r].add(num)
                col_sets[c].add(num)
                subgrid_sets[r // 3][c // 3].add(num)

        # If we complete the loop with no conflicts, the board is valid
        return True


# ---- File: lc_39.py ----
'''
https://leetcode.com/problems/combination-sum/description/

Time Complexity: O(2^t), where t is the target value.

Explanation:

In the worst case, the recursion explores all possible combinations of numbers (including repeated use of the same number) that sum up to the target.

Since each number can be used multiple times, the recursion tree can grow exponentially with respect to the target.

The number of recursive calls is bounded by 2^t in the worst case (though pruning with total > target helps in practice).

The actual time also depends on the size of the result list, since each valid combination is copied into the result.

Space Complexity: O(t)

Explanation:

The maximum depth of the recursion tree is O(t) in the worst case (when repeatedly adding the smallest number until the sum reaches target).

Additionally, space is used to store the result list res, but that depends on the number of valid combinations and is not considered extra space for complexity analysis.
'''

from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in `nums` where the numbers sum to `target`.
        Each number in `nums` can be used an unlimited number of times.
        """
        res = []  # Stores all valid combinations

        def dfs(index: int, current_subset: List[int], total: int):
            """
            Depth-First Search (DFS) helper function to explore combinations.
            :param index: Current index in `nums` to consider.
            :param current_subset: The combination being built.
            :param total: Current sum of elements in `current_subset`.
            """
            # Base case: If the sum reaches the target, store the valid combination
            if total == target:
                res.append(current_subset[:])  # Append a copy to avoid reference issues
                return
            
            # Base case: If out of bounds or sum exceeds target, return
            if index >= len(nums) or total > target:
                return

            # Step 1: Include nums[index] and recurse (can use the same element again)
            current_subset.append(nums[index])  # Choose the current number
            dfs(index, current_subset, total + nums[index])  # Recurse with updated sum

            # Step 2: Exclude nums[index] and move to the next index
            current_subset.pop()  # Undo choice (backtrack)
            dfs(index + 1, current_subset, total)  # Move to next index
        
        # Start the DFS traversal from index 0 with an empty subset and total sum 0
        dfs(0, [], 0)

        return res  # Return the list of valid combinations


# ---- File: lc_398.py ----
'''
https://leetcode.com/problems/random-pick-index/description/

✅ __init__(self, nums: List[int])
Time Complexity: O(n)
Where n is the length of the input list nums.

You iterate through the list once and populate a hashmap (self.map) with indices for each number.

Space Complexity: O(n)
In the worst case (all elements are unique), each number has its own list of indices → total space = O(n).

✅ pick(self, target: int)
Time Complexity: O(1)
Dictionary lookup (self.map[target]) is O(1).

random.choice(indexes) is also O(1).

Space Complexity: O(1)
Only uses a few local variables; no additional space that grows with input.
'''
import random
from collections import defaultdict
from typing import List

class Solution:
    
    # Constructor: Preprocess the input list to store indices of each number
    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)  # Dictionary to store lists of indices for each number
        
        # Iterate through the list and store the indices of each number in the dictionary
        for i, num in enumerate(nums):
            self.map[num].append(i)  # Append index of `num` to its corresponding list

    # Function to pick a random index of the target number
    def pick(self, target: int) -> int:
        indexes = self.map[target]  # Retrieve the list of indices where `target` appears
        return random.choice(indexes)  # Randomly select one index from the list

# Example usage:
# nums = [1, 2, 3, 3, 3]
# obj = Solution(nums)
# print(obj.pick(3))  # Randomly returns an index of '3' (either 2, 3, or 4)


# ---- File: lc_4.py ----
'''
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
Time complexity: The time complexityof thefind_the_median_from_two_sorted_arays
 functionis becauseweperformbinarysearchoverthesmallerofthetwoinput 𝑂(𝑙𝑜𝑔(𝑚𝑖𝑛(𝑚,𝑛)))
 arrays.
 Spacecomplexity:Thespacecomplexityis .
'''

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to perform binary search on it
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        # Half of the total number of elements (used to partition the arrays)
        half_total_len = (m + n) // 2

        # Initialize binary search bounds
        left, right = 0, m - 1

        while True:
            # Binary search on nums1: pick middle index
            L1_index = (left + right) // 2
            # L2_index is derived to ensure left part has exactly half_total_len elements
            L2_index = half_total_len - (L1_index + 1) - 1

            # Get left and right values around the partition in nums1
            L1 = float('-inf') if L1_index < 0 else nums1[L1_index]
            R1 = float('inf') if L1_index >= m - 1 else nums1[L1_index + 1]

            # Get left and right values around the partition in nums2
            L2 = float('-inf') if L2_index < 0 else nums2[L2_index]
            R2 = float('inf') if L2_index >= n - 1 else nums2[L2_index + 1]

            # Binary search adjustment: too far right in nums1
            if L1 > R2:
                right = L1_index - 1
            # Too far left in nums1
            elif L2 > R1:
                left = L1_index + 1
            else:
                # Correct partition found
                if (m + n) % 2 == 0:
                    # If total length is even, return average of max of left and min of right
                    return (max(L1, L2) + min(R1, R2)) / 2.0
                else:
                    # If total length is odd, return min of right elements
                    return min(R1, R2)



# ---- File: lc_40.py ----
'''
https://leetcode.com/problems/combination-sum-ii/description/

Time Complexity: O(2^n), where n is the number of elements in the candidates list.

Explanation:

The solution uses backtracking to explore all subsets of the input list.

In the worst case, each number has two choices: include or exclude, leading to 2^n possible combinations.

Sorting the list takes O(n log n), but the dominant term is the recursive exploration.

Due to the pruning (if cur + candidates[i] > target) and skipping of duplicates, the actual number of recursive calls is much smaller in practice, but still exponential in the worst case.

Space Complexity: O(n)

Explanation:

The recursion stack can go as deep as n in the worst case (when building a long combination).

Aside from the result list res (which is not counted in auxiliary space), only the path list and recursion call stack contribute to space usage.

'''

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of `candidates` where the numbers sum to `target`.
        Each number in `candidates` can only be used once in a combination.
        """

        res = []  # Stores all valid unique combinations
        candidates.sort()  # Step 1: Sort the input array to handle duplicates efficiently

        def dfs(idx: int, path: List[int], cur: int):
            """
            Depth-First Search (DFS) helper function to explore combinations.
            :param idx: Current index in `candidates` to consider.
            :param path: The current combination being built.
            :param cur: The current sum of elements in `path`.
            """
            # Base case: If the sum reaches the target, store the valid combination
            if cur == target:
                res.append(path[:])  # Append a copy to avoid reference issues
                return

            # Step 2: Iterate through the candidates, starting from `idx`
            for i in range(idx, len(candidates)):
                # Step 3: Skip duplicate numbers (to avoid duplicate combinations)
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicate elements at the same recursion level
                
                # Step 4: Prune the search if the sum exceeds the target
                if cur + candidates[i] > target:
                    break  # Since `candidates` is sorted, all further values will also be too large
                
                # Step 5: Include `candidates[i]` in the combination and recurse
                path.append(candidates[i])  # Choose the current element
                dfs(i + 1, path, cur + candidates[i])  # Move to the next index (no reuse allowed)

                # Step 6: Backtrack - Remove the last element to explore other possibilities
                path.pop()

        # Start DFS traversal from index 0 with an empty subset and sum 0
        dfs(0, [], 0)

        return res  # Return the list of unique valid combinations


# ---- File: lc_408.py ----
'''
408. Valid Word Abbreviation
Solved
Easy
Topics
Companies
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.

🧠 Time and Space Complexity:
✅ Time Complexity: O(max(m, n))
m = length of word

n = length of abbr

You iterate through each character of abbr, and may also iterate over all characters in word.

In the worst case, each character in both strings is processed once → O(m + n) = O(max(m, n))

✅ Space Complexity: O(1)
Only a few pointers and variables are used.

No additional space is used that scales with input.
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0  # Pointers for `word` and `abbr`

        # Iterate through both `word` and `abbr`
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():  # If the current character in `abbr` is a digit
                if abbr[j] == '0':  
                    # Leading zeros are not allowed
                    return False

                shift = 0  # Stores the number of characters to skip in `word`

                # Build the full number (handle multiple digits)
                while j < len(abbr) and abbr[j].isdigit():
                    shift = shift * 10 + int(abbr[j])
                    j += 1
                
                i += shift  # Skip `shift` characters in the word

            else:
                # If characters don't match or word is too short
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        # Ensure both pointers reach the end of their respective strings
        return i == len(word) and j == len(abbr)



# ---- File: lc_424.py ----
'''
https://leetcode.com/problems/longest-repeating-character-replacement/
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}  # Dictionary to keep count of characters in the current window
        highest_freq = 0  # Highest frequency of a single character in the current window
        max_len = 0  # The length of the longest valid window found so far
        left = right = 0  # Sliding window pointers

        while right < len(s):
            # Expand the window by including the character at the 'right' pointer
            freqs[s[right]] = freqs.get(s[right], 0) + 1

            # Update the highest frequency character count seen in the current window
            highest_freq = max(highest_freq, freqs[s[right]])

            # Calculate how many characters need to be replaced to make all characters the same
            num_chars_to_replace = (right - left + 1) - highest_freq

            # If the number of replacements needed exceeds 'k', slide the window forward
            # by moving the left pointer to the right to maintain a valid window
            if num_chars_to_replace > k:
                # Decrease the count of the character at the left pointer as it's leaving the window
                freqs[s[left]] -= 1
                left += 1  

            # Update the maximum length of a valid window found so far
            max_len = max(max_len, right - left + 1)

            # Move the right pointer to expand the window
            right += 1

        return max_len


# ---- File: lc_426.py ----
'''
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Converts a Binary Search Tree (BST) into a circular doubly linked list
        using an in-order traversal.

        The left pointer acts as `prev`, and the right pointer acts as `next`.

        Approach:
        - Use an iterative **in-order traversal** with a stack.
        - Maintain a **`prevNode`** pointer to link nodes.
        - Keep track of the **firstNode (head)** and **lastNode (tail)**.
        - At the end, connect `firstNode` and `lastNode` to make it circular.

        Time Complexity: O(N) (each node is visited once)
        Space Complexity: O(N) (stack stores nodes during traversal)
        """

        if not root:
            return None  # Edge case: empty tree

        stack = []  # Stack for in-order traversal
        prevNode = None  # Previous node in in-order sequence
        currentNode = root  # Start traversal from root
        firstNode = None  # Head of the doubly linked list
        lastNode = None  # Tail of the doubly linked list

        # Step 1: Perform in-order traversal using a stack
        while stack or currentNode:
            # Traverse left subtree first (in-order)
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            
            # Pop the node from the stack (visit the node)
            node = stack.pop()

            # Step 2: Link the previous node (`prevNode`) to the current node
            node.left = prevNode  # Link current node's left to previous node
            if prevNode:
                prevNode.right = node  # Link previous node's right to current node
            
            # Update `prevNode` for the next iteration
            prevNode = node

            # Step 3: Set the first node (head) of the doubly linked list
            if not firstNode:
                firstNode = node  # The first node in in-order traversal is the head

            # Track the last node (tail)
            lastNode = node  # Keep updating the last node

            # Move to the right subtree
            currentNode = node.right

        # Step 4: Make the linked list circular
        firstNode.left = lastNode  # Connect head to tail
        lastNode.right = firstNode  # Connect tail to head

        # Step 5: Return the head (first node) of the circular doubly linked list
        return firstNode


        

# ---- File: lc_430.py ----
'''
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
Time Complexity: O(n)
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if not head:
            return None  # Return if the list is empty

        # Create a dummy node to simplify edge cases
        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead

        stack = [head]  # Use a stack for depth-first traversal

        while stack:
            curr = stack.pop()  # Pop the current node to process

            # Connect current node with the previous node
            prev.next = curr
            curr.prev = prev

            # If there is a next node, push it onto the stack.
            # It will be processed after the child node (if any)
            if curr.next:
                stack.append(curr.next)

            # If there is a child node, push it to the stack to be processed next
            # Set curr.child to None as it's flattened now
            if curr.child:
                stack.append(curr.child)
                curr.child = None  # Important to remove child reference

            # Move prev forward for the next iteration
            prev = curr

        # Detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next  # Return the flattened list starting from the real head



# ---- File: lc_435.py ----
'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

✅ Time Complexity: O(n log n)
Sorting the intervals by end time takes O(n log n)

One pass through the list: O(n)

Total: O(n log n)

✅ Space Complexity: O(1)
Sorting is done in-place.

Only a few variables used for tracking.
 
'''

from typing import List
from math import inf

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Returns the minimum number of intervals to remove to make the rest non-overlapping.

        Approach:
        - Use a greedy algorithm by always keeping the interval with the earliest end time.
        - Sort intervals by end time to maximize how many non-overlapping intervals can be kept.
        """

        # Step 1: Sort intervals based on their end times
        intervals.sort(key=lambda x: x[1])

        ans = 0         # Count of intervals to remove
        k = -inf        # End of the last non-overlapping interval

        # Step 2: Iterate through each interval
        for x, y in intervals:
            if x >= k:
                # Case 1: No overlap — we can keep this interval
                k = y  # Update the end of last kept interval
            else:
                # Case 2: Overlap — we must remove this interval
                ans += 1

        return ans


# ---- File: lc_445.py ----
'''
https://leetcode.com/problems/add-two-numbers-ii/description/

✅ Time Complexity: O(m + n)
Where:

m = length of linked list l1

n = length of linked list l2

Breakdown:
Reversing both lists:

reverse_list(l1) takes O(m)

reverse_list(l2) takes O(n)

Adding corresponding digits:

You iterate through both reversed lists once → up to O(max(m, n))

Total time:

scss
Copy
Edit
O(m + n) for reversal + O(max(m, n)) for addition
⇒ O(m + n)
✅ Space Complexity: O(m + n)
In the worst case, the sum may have one more digit than either input (e.g., 999 + 1 = 1000)

So, you create a new linked list of up to max(m, n) + 1 nodes → O(m + n)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Helper function to reverse a linked list
        def reverse_list(node: Optional[ListNode]) -> Optional[ListNode]:
            curr, prev = node, None
            while curr:
                next_node = curr.next  # Store next node
                curr.next = prev       # Reverse the pointer
                prev = curr            # Move prev to current
                curr = next_node       # Move to next node
            return prev  # New head of reversed list

        # Reverse both input lists to make addition easier from least significant digit
        r1 = reverse_list(l1)
        r2 = reverse_list(l2)

        carry = 0
        ans = None  # Initialize result list as empty

        # Loop until all nodes and carry are processed
        while r1 or r2 or carry:
            total_sum = carry  # Start with carry from previous addition

            # Add digit from first list if available
            if r1:
                total_sum += r1.val
                r1 = r1.next

            # Add digit from second list if available
            if r2:
                total_sum += r2.val
                r2 = r2.next

            # Update carry for next step
            carry = total_sum // 10

            # Create new node with current digit (mod 10)
            new_node = ListNode(total_sum % 10)

            # Prepend the new node to the result list
            new_node.next = ans
            ans = new_node

        # Return the head of the result list
        return ans 


# ---- File: lc_46.py ----
'''
htt
ps://leetcode.com/problems/permutations/description/
Time Complexity: O(n × n!), where n is the number of elements in the input list nums.

Explanation:

There are n! possible permutations of n unique elements.

For each permutation, you build a list of length n, and copying that list to the result takes O(n) time.

Therefore, the total time complexity is O(n × n!).

Space Complexity: O(n) (excluding the output list)

Explanation:

The recursion stack and the candidate list can each grow up to size n.

The used set also holds up to n elements.

The result list res will take O(n × n!) space to store all permutations, but that is typically not counted as auxiliary space.

'''

from typing import List, Set

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible permutations of the given list of numbers.
        
        :param nums: List of unique integers
        :return: List of all possible permutations
        """
        res = []  # List to store the final permutations
        self.helper(nums, [], set(), res)  # Call the recursive helper function
        return res

    def helper(self, nums: List[int], candidate: List[int], used: Set[int], res: List[List[int]]) -> None:
        """
        Recursive helper function to generate permutations using backtracking.
        
        :param nums: Original list of numbers
        :param candidate: Current permutation being built
        :param used: Set to track which numbers are already in `candidate`
        :param res: List to store all valid permutations
        """
        # Base case: If candidate contains all numbers, add a copy to results
        if len(candidate) == len(nums):
            res.append(candidate[:])  # Append a shallow copy to avoid modifications
            return  # Stop further recursion

        # Iterate over all numbers to build permutations
        for num in nums:
            if num not in used:  # Ensure we don’t reuse numbers in the same permutation
                candidate.append(num)  # Choose: Add num to the current permutation
                used.add(num)  # Mark num as used

                self.helper(nums, candidate, used, res)  # Recur with updated candidate

                candidate.pop()  # Undo choice (backtrack)
                used.remove(num)  # Unmark num as used


# ---- File: lc_47.py ----
'''
https://leetcode.com/problems/permutations-ii/

Time Complexity: O(n × n!) in the worst case, where n is the length of the input list nums.

Explanation:

Without duplicates, the number of permutations is n!, and building each permutation takes O(n) time, giving a total of O(n × n!).

With duplicates, the number of unique permutations is less than n! (depending on how many repeated elements exist), so the actual number of recursive calls is less — but in the worst case (all unique elements), it remains O(n × n!).

Space Complexity: O(n) (excluding the output list)

Explanation:

The recursion stack, used list, and the current candidates list can each grow up to size n.

The result list res is not included in the auxiliary space calculation, but it will take O(n × n!) space to store all permutations in the worst case.
'''

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []  # Stores all unique permutations
        nums.sort()  # Sorting ensures duplicates are adjacent
        used = [False] * len(nums)  # Track used numbers in the current recursion

        def backtrack(candidates: List[int]):
            # Base case: If current permutation is complete, add it to results
            if len(candidates) == len(nums):
                res.append(candidates[:])  # Append a copy of the current permutation
                return

            # Iterate over the numbers
            for i in range(len(nums)):
                # Skip used numbers
                if used[i]:
                    continue

                # Skip duplicate numbers (only pick the first occurrence in the same recursion level)
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Choose the number
                used[i] = True
                candidates.append(nums[i])

                # Recurse to build the rest of the permutation
                backtrack(candidates)

                # Backtrack: remove the last element and mark it as unused
                candidates.pop()
                used[i] = False

        # Start backtracking with an empty list
        backtrack([])

        return res  # Return all unique permutations


# ---- File: lc_485.py ----
'''
785. Is Graph Bipartite?
Solved
Medium
Topics
Companies
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

 

Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
Seen this question in a real interview before?
1/5

✅ Time Complexity: O(V + E)
Where:

V = number of vertices (nodes) in the graph

E = number of edges

Why?
Each node is visited once → O(V)

Each edge is explored once in an undirected graph → O(E)

So total traversal time is O(V + E)

✅ Space Complexity: O(V)
Explanation:

colors array takes O(V) space

Call stack (due to DFS) takes up to O(V) in the worst case (if the graph is connected and shaped like a chain)

So total auxiliary space: O(V)
'''

from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Array to store colors of nodes: 0 (unvisited), 1 (color A), -1 (color B)
        colors = [0] * len(graph)
        
        # Depth-First Search (DFS) function to check bipartiteness
        def dfs(node: int, color: int) -> bool:
            nonlocal colors
            # Color the current node
            colors[node] = color
            
            # Check all neighbors
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    # Conflict detected: neighbor has the same color
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    # If unvisited, recursively apply DFS with opposite color
                    return False
            
            return True

        # Loop through each node to ensure all components are checked
        for i in range(len(graph)):
            if colors[i] == 0:  # If the node is unvisited, start DFS
                if not dfs(i, 1):  # Try to color with 1, if fails return False
                    return False
        
        return True  # If no conflicts found, the graph is bipartite

        

# ---- File: lc_490.py ----
'''
https://leetcode.com/problems/the-maze/description/

✅ Time Complexity: O(m × n)
Where:

m = number of rows in the maze

n = number of columns

Explanation:
Each cell in the maze can be added to the queue at most once.

For each cell, you simulate rolling the ball in 4 directions, but:

The rolling continues until hitting a wall or boundary, not checking every cell repeatedly.

So although rolling may scan several cells per direction, the visited matrix prevents revisiting them.

➡️ Hence, even though you're scanning along paths, each cell is processed once → total time: O(m × n)

✅ Space Complexity: O(m × n)
visited matrix: O(m × n)

queue can hold up to O(m × n) positions in the worst case
'''

from collections import deque
from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])
        visited = [[False] * cols for _ in range(rows)]  # Tracks visited stopping positions
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]   # Right, Down, Up, Left

        queue = deque([start])  # Start BFS with the initial position
        visited[start[0]][start[1]] = True  # Mark the start as visited

        while queue:
            r, c = queue.popleft()  # Current position

            # Check if destination is reached
            if [r, c] == destination:
                return True

            # Explore all 4 directions
            for dr, dc in directions:
                # 🔁 Start rolling from current position
                # We use new_r, new_c to simulate rolling the ball without modifying r, c
                new_r, new_c = r, c

                # Roll until hitting a wall or boundary
                while (
                    0 <= new_r + dr < rows and
                    0 <= new_c + dc < cols and
                    maze[new_r + dr][new_c + dc] == 0
                ):
                    new_r += dr
                    new_c += dc

                # If the stopping position hasn't been visited yet, add it to the queue
                if not visited[new_r][new_c]:
                    visited[new_r][new_c] = True
                    queue.append([new_r, new_c])

        # If BFS completes and destination is never reached
        return False


# ---- File: lc_496.py ----
'''
496. Next Greater Element I
Solved
Easy
Topics
Companies
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 

Follow up: Could you find an O(nums1.length + nums2.length) solution?

✅ Time Complexity: O(m + n)
Where:

m = len(nums1)

n = len(nums2)

🔍 Step-by-step Breakdown:
Preprocessing nums2 with a stack: O(n)

python
Copy
Edit
for num in reversed(nums2):
Each element is pushed and popped at most once from the stack.

So even with the while stack: inside, the total work is linear in nums2.

The hashmap is filled with at most n entries — constant-time operations.

Building output for nums1: O(m)

python
Copy
Edit
for j in nums1:
    output.append(hashmap[j])
Each lookup in the hashmap is O(1).

✅ Total Time:
text
Copy
Edit
O(n) + O(m) = O(m + n)
✅ Space Complexity: O(n)
Stack: Can hold up to n elements → O(n)

Hashmap: Stores one mapping for each number in nums2 → O(n)

Output: Stores m results → O(m), but since it's returned, it's not counted as extra space.
'''
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Stack to keep track of next greater elements in nums2
        stack = []
        # Hashmap to store the next greater element for each number in nums2
        hashmap = {}
        # Output list to store the results for elements in nums1
        output = []

        # Iterate through nums2 in reverse order (right to left)
        for num in reversed(nums2):
            # Maintain a decreasing stack (pop elements smaller than current number)
            while stack:
                if stack[-1] > num:
                    # Store the next greater element in the hashmap
                    hashmap[num] = stack[-1]
                    # Push the current number onto the stack
                    stack.append(num)
                    break
                else:
                    # Pop smaller elements since they won't be needed anymore
                    stack.pop()
            
            # If stack is empty (no greater element found), store -1
            if not stack:
                hashmap[num] = -1
                stack.append(num)

        # Iterate over nums1 to retrieve results from the hashmap
        for j in nums1:
            output.append(hashmap[j])

        return output


# ---- File: lc_50.py ----
'''
https://leetcode.com/problems/powx-n/description/

🧮 Why Is This Efficient?
Instead of multiplying x by itself n times (which would take O(n) time), this algorithm uses recursion to cut the problem in half each time, which gives us a logarithmic depth of computation.

⏱️ Time Complexity: O(log n)
The recursion depth is proportional to log₂(n) since n is halved on each call.

Each recursive step performs a constant amount of work (O(1)), so the total time complexity is O(log n).

🧠 Space Complexity: O(log n) (for recursive stack)
The recursion stack will go as deep as log₂(n) in the worst case, so the space complexity is also O(log n).
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # Recursive helper function to compute x^n efficiently
        def helper(x, n):
            # Base case: If x is 0, any power of 0 is 0 (except 0^0 which is typically defined as 1)
            if x == 0: 
                return 0
            # Base case: Any number raised to the power 0 is 1
            if n == 0:
                return 1
            
            # Recursive divide-and-conquer: Compute power for n//2
            res = helper(x, n // 2)
            
            # Multiply result by itself (x^(n//2) * x^(n//2))
            res = res * res
            
            # If `n` is odd, multiply once more by `x`
            return x * res if n % 2 == 1 else res
        
        # Compute power using the absolute value of `n`
        ans = helper(x, abs(n))
        
        # If `n` is negative, take reciprocal of the result
        return ans if n >= 0 else 1 / ans


'''
Time Complexity : O(log n)
Space Complexity: O(1)
Say x = 2, n = 13 (binary: 1101)

We'll multiply:

2^1 (because the last bit is 1)

2^4 (because 3rd bit from right is 1)

2^8 (because 4th bit from right is 1)
'''
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponents
        N = abs(n)
        result = 1.0
        current_product = x

        while N > 0:
            # If the current bit is set, multiply result
            if N % 2 == 1:
                result *= current_product
            
            # Square the base
            current_product *= current_product
            # Move to the next bit
            N //= 2
        
        # If original exponent was negative, take reciprocal
        return result if n >= 0 else 1 / result


# ---- File: lc_503.py ----
'''
503. Next Greater Element II
Medium
Topics
Companies
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109

The second pass helps us simulate the circular nature of the array.

Instead of physically rotating the array or creating a new one of size 2n, we logically simulate this by:

Traversing the array twice, so that every element gets a chance to see what comes "after" it, even if that’s at the start of the array.
'''
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Initialize result array with -1, as default values (if no greater element is found)
        res = [-1] * len(nums)
        # Stack to store indices of elements (used for tracking next greater elements)
        stack = []
        
        # First pass: Traverse the array once to fill next greater elements for normal order
        for i, num in enumerate(nums):
            # Check if the current element is greater than the element at the top of the stack
            while stack and nums[stack[-1]] < num:
                # Update result array with next greater element
                res[stack.pop()] = num
            # Push the index onto the stack
            stack.append(i)

        # Second pass: Traverse again to handle the circular nature of the array
        for i, num in enumerate(nums):
            # Process only those elements left in the stack
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num

        return res



# ---- File: lc_523.py ----
'''
https://leetcode.com/problems/continuous-subarray-sum/description/

✅ Why Index -1?
This is a trick to handle subarrays starting from index 0.

Let’s say:

python
Copy
Edit
nums = [6, 1, 2], k = 6
The cumulative sum at index 0 is:

python
Copy
Edit
total = 6 → 6 % 6 = 0
So at index 0, remainder is 0.

Now check:

python
Copy
Edit
i - remainder[0] = 0 - (-1) = 1  ❌ (length < 2)
But by index 2:

sum = 6 + 1 + 2 = 9

9 % 6 = 3 → still no match

Now if another 3 appears later, it’ll check if a subarray of length ≥ 2 had the same remainder before.

So storing remainder 0 at index -1 ensures that:

Any subarray starting at index 0 is still valid

The length check still works: i - (-1) = i + 1, which is the full length from index 0 to i
'''
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the first occurrence of a remainder
        remainder = {0: -1}  # Initialize with remainder 0 at index -1 to handle edge cases where first element itself is multiple of k
        total = 0  # Variable to maintain the cumulative sum

        # Iterate through the array
        for i, n in enumerate(nums):
            total += n  # Update cumulative sum
            
            # Compute remainder of total sum when divided by k
            r = total % k

            # If this remainder has never been seen before, store the index
            if r not in remainder:
                remainder[r] = i  # Store first occurrence of this remainder
            
            # If we have seen this remainder before and the subarray size is at least 2
            if i - remainder[r] > 1:
                return True  # Found a valid subarray
            
        # If no valid subarray found, return False
        return False


# ---- File: lc_528.py ----
'''
528. Random Pick with Weight
Medium
Topics
Companies
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
 

Constraints:

1 <= w.length <= 104
1 <= w[i] <= 105
pickIndex will be called at most 104 times.

✅ Time Complexity:
__init__() method:
The constructor runs in O(n) time, where n is the length of the input list w.

Computing the sum of the list takes O(n)

Normalizing the weights takes O(n)

Building the prefix sum array takes O(n)

pickIndex() method:
In the worst case, pickIndex() takes O(n) time.

It generates a random number N in O(1)

Then performs a linear scan through the cumulative weights array to find the appropriate index, which can take up to O(n)

✅ Space Complexity:
The space complexity is O(n).

You store the modified cumulative weight array (in-place in self.w), which takes linear space.
'''
import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        """
        Preprocessing step to convert the given weights into a prefix sum 
        of probabilities, effectively creating a probability distribution.
        """
        self.w = w  # Store the weights list

        # Step 1: Calculate the total sum of weights
        denom = sum(self.w)

        # Step 2: Normalize the weights by converting them into probabilities
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / denom  # Convert each weight into a fraction of total weight

        # Step 3: Convert the probabilities into a cumulative sum (prefix sum)
        # This helps in determining the region each index occupies on a [0,1] range.
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        """
        Picks an index randomly based on weight distribution using a random
        number in the range [0,1] and checking where it falls in the cumulative sum.
        """
        # Generate a random number in the range [0,1]
        N = random.uniform(0, 1)

        # Initialize index and a flag for breaking the loop
        flag = 1
        index = -1

        # Iterate through the cumulative probability array to find the corresponding index
        while flag:
            index += 1

            # If N falls within the cumulative probability range, return the corresponding index
            if N <= self.w[index]:
                flag = 0  # Exit loop

        return index



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# ---- File: lc_536.py ----
'''
https://leetcode.com/problems/construct-binary-tree-from-string/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        def getNumber(index: int) -> (int, int):
            """
            Helper function to parse a number (including negative).
            Returns the parsed number and updated index.
            """
            is_negative = False
            if s[index] == '-':
                is_negative = True
                index += 1

            number = 0
            while index < len(s) and s[index].isdigit():
                number = number * 10 + int(s[index])
                index += 1

            return -number if is_negative else number, index

        if not s:
            return None  # Empty string → no tree

        root = TreeNode()  # Initially create a dummy root node
        stack = [root]     # Stack to track current processing nodes

        index = 0
        while index < len(s):
            node = stack.pop()  # Get current node from stack to process

            # Case 1: Current char is a digit or negative sign → parse number
            if s[index].isdigit() or s[index] == '-':
                value, index = getNumber(index)  # Parse the value
                node.val = value                 # Assign value to the current node

                # If more data exists and next char is '(', a left child starts
                if index < len(s) and s[index] == '(':
                    stack.append(node)              # Push current node back to stack
                    node.left = TreeNode()          # Prepare left child node
                    stack.append(node.left)         # Add left child to stack for further parsing

            # Case 2: Left child already filled, and next is '(' → begin right child
            elif node.left and s[index] == '(':
                stack.append(node)                  # Push current node back
                node.right = TreeNode()             # Prepare right child node
                stack.append(node.right)            # Add right child to stack

            index += 1  # Move to next character This next character could ')'

        # At the end, either stack has one last parent to return, or return root
        return stack.pop() if stack else root


# ---- File: lc_539.py ----
'''
539. Minimum Time Difference
Medium
Topics
Companies
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
'''

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Helper function to convert HH:MM time format to total minutes
        def convertToMins(timeStr: str) -> int:
            hours, mins = map(int, timeStr.split(":"))  # Split "HH:MM" and convert to integers
            return hours * 60 + mins  # Convert to total minutes (hours * 60 + minutes)

        # Convert all time strings to minutes
        minutes = [convertToMins(tp) for tp in timePoints]
        
        # Sort the times in ascending order
        minutes.sort()

        # Initialize min_diff to a large number
        min_diff = float('inf')

        # Compare adjacent time differences to find the minimum difference
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        # Handle circular time difference (difference between last and first time)
        circular_diff = 1440 - minutes[-1] + minutes[0]  # 1440 minutes in a day
        min_diff = min(min_diff, circular_diff)

        # Return the minimum time difference
        return min_diff


# ---- File: lc_54.py ----
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []  # This will store the elements in spiral order
        left, right = 0, len(matrix[0])  # Initialize left and right pointers for columns
        top, bottom = 0, len(matrix)     # Initialize top and bottom pointers for rows

        # Loop until the pointers cross each other
        while left < right and top < bottom:

            # Traverse from left to right on the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1  # Move the top boundary down

            # Traverse from top to bottom on the rightmost column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1  # Move the right boundary left

            # Check if we are still within valid boundaries after moving top and right
            if not (left < right and top < bottom):
                break  # If the matrix is fully traversed, exit the loop

            # Traverse from right to left on the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1  # Move the bottom boundary up

            # Traverse from bottom to top on the leftmost column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # Move the left boundary right

        return res  # Return the spiral order traversal


# ---- File: lc_543.py ----
'''
543. Diameter of Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

📌 Time Complexity: O(n)
Each node is visited exactly once.

Work done at each node (calculating height and updating diameter) is constant time.

Let n be the number of nodes in the tree → total time: O(n)

📌 Space Complexity:
O(h), where h is the height of the tree (due to recursion stack).

Best case (balanced tree): O(log n)

Worst case (completely unbalanced tree): O(n)


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Same as coding_2025/trees/max_path_sum.py
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize diameter to negative infinity to track the maximum path length
        diameter = float('-inf')

        def helper(node: TreeNode) -> int:
            nonlocal diameter  # Allow us to update the outer variable

            if not node:
                return 0  # Base case: no height from a null node

            # Recursively compute the height of left and right subtrees
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)

            # Diameter at current node = left height + right height
            # Update the global diameter if this path is longer
            diameter = max(diameter, left + right)

            # Return the height of the current node to the parent call
            return 1 + max(left, right)

        # Kick off the recursion from the root
        helper(root)

        return diameter


# ---- File: lc_56.py ----
'''
56. Merge Intervals
Solved
Medium
Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
Seen this question in a real interview before?
1/5

Time Complexity: O(n log n), where n is the number of intervals.

Explanation:

The list of intervals is sorted by start time, which takes O(n log n) time.

Then, we iterate through the sorted list once to merge intervals, which takes O(n) time.

Therefore, the total time complexity is dominated by the sorting step: O(n log n).

Space Complexity: O(n) in the worst case.

Explanation:

We use an additional list merged to store the merged intervals.

In the worst case (no overlaps), all intervals are added to the result, so the space used is O(n).

The sort operation may also take extra space depending on the sorting algorithm (but typically not counted as extra in-place space usage).
'''

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by the starting value of each interval
        # This ensures that overlapping intervals are adjacent in the list
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize an empty list to store merged intervals
        merged = []
        
        # Step 3: Start with the first interval as the `prev` interval to compare
        prev = intervals[0]

        # Step 4: Iterate through the rest of the intervals
        for interval in intervals[1:]:
            # If the current interval overlaps with `prev`, merge them
            if interval[0] <= prev[1]:  
                # Update the end time of `prev` to include the new interval
                prev[1] = max(prev[1], interval[1])
            else:
                # If no overlap, add `prev` to merged list and move to next interval
                merged.append(prev)
                prev = interval

        # Step 5: Add the last merged interval to the list
        merged.append(prev)
        
        # Step 6: Return the merged intervals list
        return merged

        
        

# ---- File: lc_560.py ----
'''
https://leetcode.com/problems/subarray-sum-equals-k/

✅ Time Complexity: O(n)
You iterate through the array once, updating the cumulative prefix sum and checking a hashmap (dictionary) for each element.

All operations inside the loop — dictionary lookups and updates — are O(1) on average.

So, for an input list of length n, total time is O(n).

✅ Space Complexity: O(n)
In the worst case, the prefix_sum_map stores a unique prefix sum for every index of the array (if all prefix sums are different).

Therefore, space used by the hashmap is O(n).
'''
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Counter for the number of subarrays that sum to `k`
        count = 0  
        
        # Dictionary to store the frequency of prefix sums
        prefix_sum_map = {0: 1}  # Initialize with sum 0 to handle cases where subarray starts at index 0
        
        # Variable to store the current prefix sum
        curr_prefix_sum = 0  
        
        # Iterate through the array to calculate prefix sums
        for num in nums:
            curr_prefix_sum += num  # Update the running prefix sum
            
            # Check if there exists a subarray that sums to `k`
            # A subarray sum is valid if (curr_prefix_sum - k) was seen before
            if curr_prefix_sum - k in prefix_sum_map:
                count += prefix_sum_map[curr_prefix_sum - k]  # Add the count of previous occurrences
            
            # Update prefix_sum_map with the current prefix sum
            # This keeps track of how many times each prefix sum appears
            prefix_sum_map[curr_prefix_sum] = prefix_sum_map.get(curr_prefix_sum, 0) + 1  
        
        # Return the total count of valid subarrays
        return count


# ---- File: lc_621.py ----
'''
https://leetcode.com/problems/task-scheduler/description/

Time Complexity: O(n × log k)

n is the total number of tasks

k is the number of unique tasks

Each task may be pushed to or popped from the heap (which takes O(log k) time)

In the worst case, we simulate up to n actual task executions plus possible idle slots

So, the overall time complexity is O(n × log k)

Space Complexity: O(k)

We use a max-heap to store frequencies of up to k unique tasks

We also use a queue to store tasks in the cooldown period, which can hold at most k tasks at any point

So, the overall space complexity is O(k)
'''

import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Given a list of CPU tasks and a cooldown period `n`,
        find the minimum time required to complete all tasks
        following the given constraints.
        """
        
        # Step 1: Count the frequency of each task
        count = Counter(tasks)  # Stores task frequencies
        
        # Step 2: Use a Max Heap (negate values to use Python's min-heap as a max-heap)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)  # Convert list into a heap
        
        # Step 3: Use a queue to track cooling tasks with their next available execution time
        queue = deque()  # Format: [remaining_count, next_available_time]
        
        time = 0  # Tracks the total time taken
        
        # Step 4: Process tasks using a heap and cooldown queue
        while maxHeap or queue:  # Continue until all tasks are completed
            time += 1  # Increment time at each step
            
            if maxHeap:  # If there are available tasks to process
                cnt = 1 + heapq.heappop(maxHeap)  # Process task (increment since we store negative counts)
                
                if cnt:  # If there are more instances of this task left
                    queue.append([cnt, time + n])  # Add it to cooldown queue with next available time
            
            # Step 5: If a task has finished its cooldown, reinsert it into the heap
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
                
        return time  # Return total time taken to complete all tasks


# ---- File: lc_636.py ----
'''
https://leetcode.com/problems/exclusive-time-of-functions/description/
'''

from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n                # Result array to store exclusive time for each function ID
        stack = []                   # Stack to keep track of currently running functions
        prev = 0                     # Keeps the timestamp of the last processed log

        for log in logs:
            # Split the log into function ID, type ("start"/"end"), and timestamp
            fn_id, typ, time = log.split(':')
            fn_id, time = int(fn_id), int(time)

            if typ == "start":
                # If there's already a running function on top of the stack,
                # calculate how much time it ran until this new function started
                if stack:
                    # Add the elapsed time since prev to the current running function
                    res[stack[-1]] += time - prev

                # Push the new function onto the stack (start running it)
                stack.append(fn_id)
                prev = time  # Update prev to current start time

            else:  # typ == "end"
                # The function at the top of the stack ends now
                last_fn_id = stack.pop()

                # Add the time this function was running to its result
                # (from prev to current time, inclusive → +1)
                res[last_fn_id] += time - prev + 1

                # Update prev to time just after this function ends
                prev = time + 1

        return res


# ---- File: lc_65.py ----
'''
Algorithm

Now that we have laid out the rules, let's iterate over the input. For each character, determine what group it belongs to, and verify that it follows the rules.

Declare 3 variables seenDigit, seenExponent, and seenDot. Set all of them to false.

Iterate over the input.

If the character is a digit, set seenDigit = true.

If the character is a sign, check if it is either the first character of the input, or if the character before it is an exponent. If not, return false.

If the character is an exponent, first check if we have already seen an exponent or if we have not yet seen a digit. If either is true, then return false. Otherwise, set seenExponent = true, and seenDigit = false. We need to reset seenDigit because after an exponent, we must construct a new integer.

If the character is a dot, first check if we have already seen either a dot or an exponent. If so, return false. Otherwise, set seenDot = true.

If the character is anything else, return false.

At the end, return seenDigit. This is one reason why we have to reset seenDigit after seeing an exponent - otherwise an input like "21e" would be incorrectly judged as valid.
https://leetcode.com/problems/valid-number/
'''

class Solution:
    def isNumber(self, s: str) -> bool:
        # Flags to track occurrences of digits, exponent, and decimal point
        digitSeen, exponentSeen, dotSeen = False, False, False
        
        for i, c in enumerate(s):
            if c in ['e', 'E']:  # Check if the character is an exponent
                # Exponent should appear only once and must be preceded by a number
                if exponentSeen or not digitSeen:
                    return False
                exponentSeen = True  # Mark that an exponent has been seen
                digitSeen = False  # Reset digitSeen because there must be digits after 'e' or 'E'

            elif c == '.':  # Check if the character is a decimal point
                # A decimal point cannot appear after an exponent and should appear only once
                if dotSeen or exponentSeen:
                    return False
                dotSeen = True  # Mark that a decimal point has been seen

            elif c in ['+', '-']:  # Check if the character is a sign ('+' or '-')
                # The sign should appear only at the beginning or right after an exponent
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False

            elif c.isdigit():  # If the character is a digit
                digitSeen = True  # Mark that a digit has been seen

            else:  # If an invalid character is encountered
                return False

        # A valid number must contain at least one digit
        return digitSeen


# ---- File: lc_670.py ----
'''
https://leetcode.com/problems/maximum-swap/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
You're allowed to swap two digits at most once in a number to make it as large as possible.

The greedy strategy is:

For each digit, check if there's a larger digit later in the number.
If so, swap with the rightmost occurrence of that larger digit (to maximize the number).
'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Finds the maximum number that can be obtained by swapping two digits at most once.

        :param num: An integer
        :return: The maximum possible number after at most one swap
        """

        # Convert the integer to a list of characters (digits)
        nums = list(str(num))
        n = len(nums)

        # Array to store the index of the maximum digit to the right for each position
        max_right_index = [0] * n  
        max_right_index[n-1] = n-1  # The last digit is the maximum in its position

        # Populate max_right_index with the rightmost max digit for each position
        for i in range(n-2, -1, -1):
            # Store the index of the max digit on the right (or itself if it's larger)
            max_right_index[i] = i if nums[i] > nums[max_right_index[i+1]] else max_right_index[i+1]
        
        # Iterate through the digits and find the first instance where a swap improves the number
        for i in range(n):
            if nums[i] < nums[max_right_index[i]]:  # If a larger digit exists to the right
                # Swap the current digit with the rightmost maximum digit
                nums[i], nums[max_right_index[i]] = nums[max_right_index[i]], nums[i]
                return int(''.join(nums))  # Convert back to integer and return
        
        # If no swap was made, return the original number
        return num

class Solution2:
    def maximumSwap(self, num: int) -> int:
        """
        Finds the maximum number that can be obtained by swapping two digits at most once.

        :param num: An integer
        :return: The maximum possible number after at most one swap
        """

        # Convert the number to a list of digits (characters)
        nums = list(str(num))  

        # Variables to track the maximum digit seen from the right
        max_num = "0"  # Stores the maximum digit encountered (initialized to '0')
        max_i = -1  # Stores the index of the maximum digit encountered
        swap_i, swap_j = -1, -1  # Indices of digits to be swapped

        # Traverse the digits from right to left (reversed order)
        for i in reversed(range(len(nums))):
            if nums[i] > max_num:  # Update max_num and its index if a larger digit is found
                max_num = nums[i]
                max_i = i
            if nums[i] < max_num:  # If a smaller digit is found before max_num, mark it for swap
                swap_i, swap_j = i, max_i  

        # If a swap is possible, perform the swap
        if swap_i != -1:
            nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]  

        # Convert the list back to an integer and return
        return int(''.join(nums))


# ---- File: lc_680.py ----
'''
680. Valid Palindrome II
Solved
Easy
Topics
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = 1  # Maximum number of deletions allowed
        
        def verify(s: str, left, right, deleted):
            """
            Recursive function to check if a substring is a valid palindrome 
            with at most one deletion.
            """
            while left < right:
                if s[left] != s[right]:  # Mismatch found
                    if deleted == n:
                        return False  # Already deleted one character, cannot delete again
                    else:
                        # Try deleting either the left or right character and check if it's a palindrome
                        return verify(s, left+1, right, deleted+1) or verify(s, left, right-1, deleted+1)
                else:
                    # Continue checking next characters
                    left += 1
                    right -= 1
            return True  # If loop completes, it is a valid palindrome

        return verify(s, 0, len(s) - 1, 0)  # Start with the full string

# Iterative
class Solution2:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, left, right):
            """Helper function to check if a substring is a palindrome"""
            while left < right:
                if s[left] != s[right]:
                    return False  # Mismatch found, not a palindrome
                left += 1
                right -= 1
            return True  # If loop completes, it is a palindrome

        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:  # Mismatch found
                # Try skipping one character (either left or right) and check if the rest is a palindrome
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
            left += 1
            right -= 1
        
        return True  # String is already a palindrome


# ---- File: lc_684.py ----
'''
https://leetcode.com/problems/redundant-connection/description/

✅ Time Complexity: O(n * α(n))
Where:

n is the number of nodes (or edges, since this is a connected graph)

α(n) is the inverse Ackermann function, which grows extremely slowly and is practically constant for all realistic values of n (even up to billions)

Why?
You loop through each of the n edges → O(n)

Each call to union() involves two find() operations

With path compression, each find() takes O(α(n))

So each union takes O(α(n)) in the worst case

➡️ Total = O(n * α(n)) → considered almost linear

✅ Space Complexity: O(n)
The Union-Find structure uses:

parent[] array of size n + 1

size[] array of size n + 1

So the overall space used is O(n)
'''

from typing import List

# Union-Find (Disjoint Set) class
class UnionFind:
    def __init__(self, size: int):
        # Initialize each node as its own parent (self-loop)
        self.parent = [i for i in range(size)]
        # Track the size of each connected component
        self.size = [1] * size  

    def union(self, x: int, y: int) -> bool:
        """
        Merges two sets if they are disjoint.
        Returns False if they are already connected (i.e., cycle detected).
        """
        rep_x, rep_y = self.find(x), self.find(y)  # Find representatives (leaders)
        
        if rep_x == rep_y:
            return False  # If both nodes have the same representative, cycle detected

        # Union by size: attach the smaller tree under the larger tree
        if self.size[rep_x] > self.size[rep_y]:
            self.parent[rep_y] = rep_x  # Make rep_x the parent of rep_y
            self.size[rep_x] += self.size[rep_y]  # Update size of the component
        else:
            self.parent[rep_x] = rep_y  # Make rep_y the parent of rep_x
            self.size[rep_y] += self.size[rep_x]  # Update size of the component

        return True  # Successfully merged

        

    def find(self, x: int) -> int:
        """
        Finds the representative (leader) of the set that `x` belongs to.
        Uses **path compression** to flatten the tree, optimizing future queries.
        """
        if x == self.parent[x]:
            return x  # If `x` is its own parent, it is the root
        
        # Path Compression: directly connect node to its root representative
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def size(self, x:int) -> int:
        return self.size[self.find(x)]

# Main solution class
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Finds the redundant edge in a given undirected graph that, if removed,
        results in a tree (i.e., an acyclic connected graph).
        """
        size = len(edges) + 1  # Total nodes (1-based indexing)
        union_find = UnionFind(size)  # Initialize Union-Find structure

        for n1, n2 in edges:
            # If the union operation fails, it means this edge creates a cycle
            if not union_find.union(n1, n2):
                return [n1, n2]  # Return the redundant edge
        
        return []  # Default return (should never reach this point)


# ---- File: lc_708.py ----
'''
https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        # Case 1: If the list is empty, create a new node that points to itself (circular list)
        if head is None:
            newNode = Node(insertVal)
            newNode.next = newNode  # Point to itself to maintain circular structure
            return newNode
        
        prev, curr = head, head.next  # Initialize two pointers
        insertFlag = False  # Flag to indicate whether insertion position is found

        while True:
            # Case 2: Insert between two nodes in a sorted manner (normal case)
            if prev.val <= insertVal <= curr.val:
                insertFlag = True

            # Case 3: Handling the wrap-around case (largest to smallest in circular list)
            elif prev.val > curr.val:
                # Insert if the value is either the new maximum or the new minimum in the list
                if insertVal >= prev.val or insertVal <= curr.val:
                    insertFlag = True
            
            # Insert the new node if a valid position is found
            if insertFlag:
                prev.next = Node(insertVal, curr)
                return head

            # Move to the next pair of nodes
            prev, curr = curr, curr.next

            # Case 4: If we have traversed the entire list and found no valid position
            if prev == head:
                break
        
        # Case 5: If all values in the list are the same or no valid position was found, insert anywhere
        prev.next = Node(insertVal, curr)
        return head


# ---- File: lc_71.py ----
'''
https://leetcode.com/problems/simplify-path/

Time Complexity: O(n), where n is the length of the input string path.

Explanation:

Splitting the string by '/' takes O(n) time.

Iterating through each token and performing operations (push/pop) on the stack takes O(n) in total because each directory name is processed at most once.

Joining the stack to form the result also takes O(n) in the worst case.

So, the overall time complexity is O(n).

Space Complexity: O(n)

Explanation:

In the worst case, all parts of the path are valid directory names and get stored in the stack, which takes O(n) space.

The final output string (resulting simplified path) also requires O(n) space to store.
'''
from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize a deque (stack) to store valid directory names
        stack = deque()
        
        # Split the path by '/' to get individual directory names or special symbols
        tokens = path.split('/')
        
        # Iterate through each token
        for token in tokens:
            if stack and token == '..':  
                # '..' means move up one directory, so pop from the stack if not empty
                stack.pop()
            elif not token == "" and not token == '.' and not token == '..':
                # If token is a valid directory name, push it onto the stack
                stack.append(token)

        # If the stack is empty, return root "/"
        if not stack:
            return '/'
        
        # Join the stack elements to form the final simplified path
        return '/' + '/'.join(stack)


# ---- File: lc_721.py ----
'''

✅ Time Complexity: O(N * M * log M)
Where:

N is the number of accounts

M is the average number of emails per account
O(N * M) for graph construction
+ O(V + E) for DFS traversal
+ O(M log M) for sorting
⇒ O(N * M + M log M)

✅ Space Complexity: O(N * M)
Graph storage (adjacency list): O(M)

Visited set: O(M)

Recursive DFS call stack: up to O(M) in worst case

Result storage: O(N * M)

'''

from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accountList: List[List[str]]) -> List[List[str]]:
        """
        Merges accounts that share common emails using DFS traversal.
        
        :param accountList: List of accounts, where each account consists of a name 
                            and multiple email addresses.
        :return: Merged list of accounts with unique emails sorted alphabetically.
        """
        
        # Step 1: Build an adjacency list (Graph representation)
        adjacent = defaultdict(list)  # Stores connections between emails

        for account in accountList:
            accountFirstEmail = account[1]  # First email in the account
            for j in range(2, len(account)):  # Connect all emails in the account
                accountEmail = account[j]
                # Since emails are bidirectionally connected, add edges in both directions
                adjacent[accountFirstEmail].append(accountEmail)
                adjacent[accountEmail].append(accountFirstEmail)

        # Step 2: Use DFS to find connected components (merged accounts)
        mergedAccounts = []  # Stores the final merged accounts
        visited = set()  # Keeps track of visited emails

        def dfs(mergedAccount: List[str], email: str):
            """
            Depth-First Search (DFS) to collect all connected emails.
            
            :param mergedAccount: The list that stores all emails belonging to one merged account
            :param email: The current email being processed in DFS
            """
            mergedAccount.append(email)  # Add the email to the current account
            visited.add(email)  # Mark email as visited
            
            # Explore all neighboring emails (connected emails)
            for neighbor in adjacent[email]:
                if neighbor not in visited:
                    dfs(mergedAccount, neighbor)  # Recursively visit connected emails

        # Step 3: Process each account and merge connected emails
        for account in accountList:
            accountName = account[0]  # Extract account holder's name
            accountFirstEmail = account[1]  # Get the first email in the account

            # If the first email hasn't been visited, start DFS from it
            if accountFirstEmail not in visited:
                mergedAccount = [accountName]  # Start with the account name
                dfs(mergedAccount, accountFirstEmail)  # DFS collects all emails
                mergedAccount[1:] = sorted(mergedAccount[1:])  # Sort emails
                mergedAccounts.append(mergedAccount)  # Store the merged account

        return mergedAccounts


# ---- File: lc_73.py ----
'''
https://leetcode.com/problems/set-matrix-zeroes/description/
'''

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modifies the input matrix in-place:
        If any element is 0, sets its entire row and column to 0.
        Uses first row and column as markers to achieve O(1) space.
        """
        m, n = len(matrix), len(matrix[0])

        # Flag to remember if the first row has any zero
        first_row_has_zero = False
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        # Flag to remember if the first column has any zero
        first_col_has_zero = False
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break

        # Use first row and first column to mark zeros
        # If matrix[i][j] == 0, mark matrix[i][0] and matrix[0][j] as 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0  # Mark column
                    matrix[i][0] = 0  # Mark row

        # Set elements to 0 based on the markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # If first row originally had a zero, zero out the whole row
        if first_row_has_zero:
            for c in range(n):
                matrix[0][c] = 0

        # If first column originally had a zero, zero out the whole column
        if first_col_has_zero:
            for r in range(m):
                matrix[r][0] = 0


# ---- File: lc_74.py ----
'''
https://leetcode.com/problems/search-a-2d-matrix/description/
Time complexity: The time complexity of matrix_search is
 binary searchoverasearchspaceofsize
 𝑚 · 𝑛
 Spacecomplexity:Thespacecomplexityis
 .
 𝑂(1)
 .
 𝑂(𝑙𝑜𝑔(𝑚 · 𝑛))
 becauseitperformsa
'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get matrix dimensions
        m, n = len(matrix), len(matrix[0])
        
        # Apply binary search on the virtual 1D array from index 0 to m*n - 1
        left, right = 0, m * n - 1
        
        while left <= right:
            # Mid index in the virtual 1D array
            mid = (left + right) // 2

            # Convert 1D index to 2D row and column
            r, c = mid // n, mid % n

            # Check the target value at the calculated position
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                # Target is in the left half
                right = mid - 1
            else:
                # Target is in the right half
                left = mid + 1
        
        # Target not found
        return False


# ---- File: lc_78.py ----
'''
https://leetcode.com/problems/subsets/description/

Time Complexity: O(2^n), where n is the number of elements in the input list nums.

Explanation:

Each element in the list has two choices: include or exclude.

This results in 2^n total subsets (the size of the power set).

Each subset is constructed in O(n) time (due to copying the list), but since we only copy when reaching the base case, and we have 2^n such cases, the total time complexity is O(2^n).

Space Complexity: O(n) (excluding the output)

Explanation:

The recursion stack and the current subset curr_subset can grow up to size n.

The result list res stores 2^n subsets, but that is not counted as auxiliary space — it's part of the required output.
'''

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible subsets (the power set) of a given list of numbers.
        Uses backtracking to explore both inclusion and exclusion of each element.
        """
        res = []  # Stores all subsets

        def helper(i: int, curr_subset: List[int]):
            """
            Recursive helper function to build subsets.
            :param i: Current index in `nums`
            :param curr_subset: The subset being built in this recursion path
            """
            # Base case: If we reach the end of the list, add the current subset to results
            if i == len(nums):
                res.append(curr_subset[:])  # Append a shallow copy of the subset
                return

            # Step 1: Include nums[i] in the subset
            curr_subset.append(nums[i])  # Add current element
            helper(i + 1, curr_subset)   # Recurse with the next index

            # Step 2: Exclude nums[i] from the subset (backtrack)
            curr_subset.pop()  # Remove last element (undo inclusion)
            helper(i + 1, curr_subset)  # Recurse without the current element
        
        # Start backtracking from index 0 with an empty subset
        helper(0, [])

        return res  # Return the final list of subsets


# ---- File: lc_79.py ----
'''
https://leetcode.com/problems/word-search/description/
O(m × n × 4^L) where:
m × n = total number of cells
L = length of the word
Each DFS call can go in 4 directions for each character.
'''
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Returns True if the given `word` exists in the `board`.
        The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically).
        Same cell cannot be used more than once in a word path.
        """
        ROWS, COLS = len(board), len(board[0])  # Dimensions of the board
        path = set()  # Set to track visited cells in the current DFS path
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 4 directions: down, right, up, left

        def dfs(r: int, c: int, i: int) -> bool:
            """
            Performs DFS to match the `i`th character of `word` starting from board[r][c]
            """
            # Base case: all characters matched
            if i == len(word):
                return True

            # Check boundaries, visited, and character mismatch
            if (
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r, c) in path or 
                board[r][c] != word[i]
            ):
                return False

            # Mark current cell as visited
            path.add((r, c))

            # Explore all 4 directions
            for dr, dc in dirs:
                next_r, next_c = r + dr, c + dc
                if dfs(next_r, next_c, i + 1):
                    return True  # If any path returns True, we're done

            # Backtrack: remove cell from visited path
            path.remove((r, c))
            return False

        # Try starting DFS from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # If DFS finds the word, return True
                    return True

        # If no path matched the word
        return False


# ---- File: lc_791.py ----
'''
https://leetcode.com/problems/custom-sort-string/description/
'''

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Given a custom character order `order` and a string `s`, reorder `s`
        such that characters appear in the order given in `order`. 
        Characters not present in `order` should appear at the end in any order.
        
        Approach:
        - Use a frequency map to count occurrences of characters in `s`.
        - Construct the result string by following the order in `order`.
        - Append remaining characters from `s` that are not in `order`.

        Time Complexity: O(N + M), where N is the length of `s` and M is the length of `order`.
        Space Complexity: O(N) for the frequency map.
        """

        # Step 1: Build frequency map for characters in `s`
        s_freq_map = {}  # Dictionary to store character counts in `s`
        for c in s:
            s_freq_map[c] = s_freq_map.get(c, 0) + 1  # Count occurrences

        result = ''  # Result string to store sorted characters

        # Step 2: Add characters in the order specified by `order`
        for char in order:
            if char in s_freq_map:  # If character exists in `s`
                result += char * s_freq_map[char]  # Append it repeated by its count
                del s_freq_map[char]  # Remove it from the map

        # Step 3: Append remaining characters that were not in `order`
        for k, v in s_freq_map.items():
            result += k * v  # Append remaining characters in any order

        return result  # Return the final sorted string


# ---- File: lc_814.py ----
'''
https://leetcode.com/problems/binary-tree-pruning/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(node: TreeNode) -> bool:
            if not node:
                return False
            
            # Check if any node in the left subtree contains a 1.
            left_contains_one = helper(node.left)
            
            # Check if any node in the right subtree contains a 1.
            right_contains_one = helper(node.right)

              # If the left subtree does not contain a 1, prune the subtree.
            if not left_contains_one: 
                node.left = None
                
            # If the right subtree does not contain a 1, prune the subtree.
            if not right_contains_one: 
                node.right = None
            
            return node.val or left_contains_one or right_contains_one

        # Return the pruned tree if the tree contains a 1, otherwise return None.
        return root if helper(root) else None
        

# ---- File: lc_863.py ----
'''
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

✅ Time Complexity: O(n)
Where n is the number of nodes in the tree.

Breakdown:
build_graph() visits each node once → O(n)

BFS also visits each node once → O(n)

Each node and edge is processed once

Appending and checking nodes in graph and visited set: O(1) average

✅ Total time = O(n)

✅ Space Complexity: O(n)
Breakdown:
graph dictionary stores up to 2 * (n - 1) edges → O(n)

visited set: O(n)

queue stores nodes level by level → O(n) in worst case

answer list: O(n) in the worst case (e.g. all nodes are k-distance away)

✅ Total space = O(n)
'''
from collections import defaultdict, deque
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Finds all nodes that are exactly `k` distance away from the target node in a binary tree.
        
        :param root: The root of the binary tree.
        :param target: The target node whose distance-k neighbors are to be found.
        :param k: Distance from the target node.
        :return: A list of node values that are exactly `k` distance from the target node.
        """

        # Step 1: Convert the Binary Tree into an Undirected Graph
        graph = defaultdict(list)  # Adjacency list representation of the tree

        def build_graph(cur: TreeNode, parent: TreeNode):
            """
            Constructs an adjacency list from the binary tree.
            This allows bidirectional traversal between parent and child nodes.
            
            :param cur: The current node in the tree.
            :param parent: The parent node of `cur`.
            """
            if not cur:
                return

            if parent:
                graph[cur.val].append(parent.val)  # Add parent connection
                graph[parent.val].append(cur.val)  # Add child connection

            # Recursively build the graph for left and right subtrees
            build_graph(cur.left, cur)
            build_graph(cur.right, cur)

        # Build the graph starting from the root node
        build_graph(root, None)

        # Step 2: BFS Traversal from Target Node
        answer = []  # Stores nodes at exactly `k` distance
        visited = set([target.val])  # Set to track visited nodes
        queue = deque([(target.val, 0)])  # BFS queue initialized with (target, distance)

        while queue:
            cur, distance = queue.popleft()

            # If the current node is exactly `k` distance away, add it to the answer list
            if distance == k:
                answer.append(cur)
                continue  # No need to explore further from this node
            
            # Explore all neighbors (children and parent)
            for neighbor in graph[cur]:
                if neighbor not in visited:  # Avoid revisiting nodes
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))  # Move to next level

        # Step 3: Return the collected nodes at distance `k`
        return answer


# ---- File: lc_875.py ----
'''
Koko Eating Bananas
Solved
Medium
Topics
Companies
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

Time Complexity: O(n log m)
'''

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Given an array `piles` representing the number of bananas in each pile and
        `h` representing the number of hours available, find the minimum eating speed
        (bananas per hour) such that all bananas can be eaten within `h` hours.
        
        The problem is solved using **Binary Search** to find the optimal speed.
        """
        
        # Set the search space between 1 (slowest) and max(piles) (fastest)
        left, right = 1, max(piles)

        # Apply binary search to find the minimum feasible eating speed
        while left < right:
            mid = (left + right) // 2  # Middle speed
            if self.is_feasible(piles, mid, h):  
                # If it is possible to eat all bananas within h hours, try a slower speed
                right = mid
            else:
                # If not feasible, increase the speed
                left = mid + 1
        
        return left  # The minimum feasible eating speed
    

    def is_feasible(self, piles: List[int], mid: int, h: int) -> bool:
        """
        Helper function to check if a given speed `mid` allows us to eat all
        the bananas within `h` hours.
        """
        total_hours = 0  # Total hours required at this speed

        # Calculate the number of hours needed for each pile
        for pile in piles:
            # Using math.ceil(pile/mid) but rewritten to avoid import
            hour = (pile + mid - 1) // mid  # This is equivalent to ceil(pile/mid)
            total_hours += hour  # Accumulate total hours needed
        
        # Return True if the total hours required is within the allowed time h
        return total_hours <= h



# ---- File: lc_938.py ----
'''
938. Range Sum of BST
Solved
Easy
Topics
Companies
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

✅ Time Complexity: O(n)
Where n is the number of nodes in the tree.

Why?
In the worst case, the function may need to visit every node in the tree.

Even though it prunes subtrees using the BST property, the pruning only happens when the node's value is clearly outside the range.

So in the worst-case scenario (e.g., all nodes fall inside [low, high]), the function visits every node.

🚀 Best-case time complexity:
If most nodes are outside the range, the pruning reduces the number of nodes visited.

For example, if low = 50 and all nodes are < 50, you only traverse the rightmost path.

So best case is O(log n) for a balanced BST.

But overall, we say worst-case is O(n).

✅ Space Complexity: O(h)
Where h is the height of the tree.

Why?
This is a recursive solution, so it uses the call stack.

In the worst case (unbalanced tree), the recursion can go as deep as n → O(n).

In the best case (balanced BST), the recursion depth is log n → O(log n)

So,

Worst case (unbalanced BST) → O(n)

Best case (balanced BST) → O(log n)


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Recursively calculates the sum of all nodes within the range [low, high].
        Uses BST properties to prune unnecessary branches.
        """
        if not root:
            return 0  # Base case: return 0 if node is None

        elif root.val < low:
            # If current node is less than the low value, search only in the right subtree
            return self.rangeSumBST(root.right, low, high)

        elif root.val > high:
            # If current node is greater than high value, search only in the left subtree
            return self.rangeSumBST(root.left, low, high)

        # If current node is within range, include its value and explore both subtrees
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


# Using DFS
class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Uses Depth-First Search (DFS) to calculate the sum of nodes within the range [low, high].
        """
        res = 0  # Stores the sum of nodes in the range

        # Helper function to perform DFS
        def dfs(node: TreeNode) -> None:
            nonlocal res  # Use the outer `res` variable
            if not node:
                return  # Base case: return if node is None

            # If node is within range, add its value to the sum
            if low <= node.val <= high:
                res += node.val

            # If node value is greater than low, explore the left subtree
            if low < node.val:
                dfs(node.left)

            # If node value is less than high, explore the right subtree
            if node.val < high:
                dfs(node.right)

        dfs(root)  # Start DFS traversal from the root
        return res


# ---- File: lc_973.py ----
'''
https://leetcode.com/problems/k-closest-points-to-origin/
'''
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k closest points to the origin (0,0) using a Min Heap.
        """
        minHeap = []  # Min-Heap to store distances along with points
        
        # Step 1: Compute squared distance and store in minHeap
        for x, y in points:
            dist = x**2 + y**2  # Squared Euclidean distance to avoid floating point calculations
            minHeap.append([dist, x, y])  # Store distance along with point coordinates
        
        # Convert the list into a heap in O(N) time
        heapq.heapify(minHeap)

        res = []  # Stores k closest points
        
        # Step 2: Extract k closest points
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)  # Extract the closest point (smallest distance)
            res.append([x, y])  # Store the point in the result list
            k -= 1  # Decrease the count
        
        return res  # Return the list of k closest points

'''
✅ Time Complexity: O(n log k)
Where:

n is the total number of points in the input

k is the number of closest points to return

✅ Space Complexity: O(k)
You maintain a heap of size at most k → O(k)

Result array res also stores k points → O(k)


'''

class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k closest points to the origin (0,0) using a Max Heap.
        This approach is efficient when k is much smaller than the total number of points.
        """
        maxHeap = []  # Max Heap (simulated using negative values)
        
        # Step 1: Process each point and maintain a max heap of size k
        for x, y in points:
            dist = -(x**2 + y**2)  # Compute negative squared Euclidean distance
            heapq.heappush(maxHeap, [dist, x, y])  # Push distance with point
            
            # If the heap size exceeds k, remove the farthest point (largest negative value)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)  # Remove the point with the smallest negative distance (farthest point)
        
        res = []  # Stores the k closest points
        
        # Step 2: Extract the k closest points from the heap
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)  # Pop elements from the heap
            res.append([x, y])  # Append the point to the result
        
        return res  # Return the final list of k closest points


# ---- File: lc_986.py ----
'''
https://leetcode.com/problems/interval-list-intersections/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

✅ Time Complexity: O(n + m)
Where:

n is the length of firstList

m is the length of secondList

🔍 Why?
You're iterating through both interval lists using two pointers (i for firstList and j for secondList).

In each iteration, at least one of the pointers is incremented (either i or j), based on which interval ends earlier.

So the total number of iterations is at most n + m.

No nested loops, no sorting — just a single linear scan of both lists.

✅ Space Complexity: O(k)
Where k is the number of overlapping intervals added to the result list.

You only store the intersections found in the result list.

No additional memory is used other than for the result.
'''
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Finds the intersection of two lists of intervals.
        
        :param firstList: List of intervals [[start1, end1], [start2, end2], ...]
        :param secondList: List of intervals [[startA, endA], [startB, endB], ...]
        :return: A list of intervals representing the intersection of both input lists.
        """
        
        # If either list is empty, return an empty list (no intersection possible)
        if not firstList or not secondList:
            return []
        
        i, j = 0, 0  # Pointers for firstList and secondList
        result = []  # Stores the intersection intervals

        # Traverse both lists until one of them is fully processed
        while i < len(firstList) and j < len(secondList):
            # Calculate the overlapping interval
            startMax = max(firstList[i][0], secondList[j][0])  # Start of the intersection
            endMin = min(firstList[i][1], secondList[j][1])  # End of the intersection
            
            # If the interval is valid (start <= end), add it to the result
            if endMin >= startMax:
                result.append([startMax, endMin])
            
            # Move the pointer for the interval that ends first (to find new intersections)
            if firstList[i][1] == endMin:
                i += 1
            if secondList[j][1] == endMin:
                j += 1
        
        return result  # Return the list of intersected intervals


# ---- File: lc_987.py ----
'''
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
Let n be the number of nodes in the binary tree.

1. BFS Traversal:
Each node is visited once → O(n)

2. Appending to column_map:
Each node appends a tuple to a column list → O(1) per node → total O(n)

3. Sorting Columns:
Worst case: all nodes are in one column → sort n items: O(n log n)

In general: sum of all k log k across columns is bounded by O(n log n)

4. Building Result:
Extracting values from each sorted column: O(n)

✅ Total Time Complexity:
O(n log n) — due to sorting the rows within each column

🧮 Space Complexity Analysis:
column_map: stores each node once → O(n)

queue: stores nodes during BFS → up to O(n) in worst case

result: final output with all node values → O(n)

✅ Total Space Complexity:
O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to store column index -> list of (row, value)
        column_map = defaultdict(list)

        # Track leftmost and rightmost column indices
        leftmost_column = rightmost_column = 0

        # BFS queue: (node, row, column)
        queue = deque([(root, 0, 0)])

        # Perform BFS traversal while tracking (row, col)
        while queue:
            node, row, column = queue.popleft()

            # Append (row, value) into the corresponding column list
            column_map[column].append((row, node.val))

            # Update column boundaries
            leftmost_column = min(leftmost_column, column)
            rightmost_column = max(rightmost_column, column)

            # Queue left child with updated row and column
            if node.left:
                queue.append((node.left, row + 1, column - 1))

            # Queue right child with updated row and column
            if node.right:
                queue.append((node.right, row + 1, column + 1))

        # Step 2: Extract and sort values from column_map
        result = []

        for col in range(leftmost_column, rightmost_column + 1):
            # Sort first by row, then by value
            sorted_column = sorted(column_map[col])
            # Extract just the values from sorted (row, value) pairs
            result.append([val for row, val in sorted_column])

        return result


# ---- File: lc_994.py ----
'''
https://leetcode.com/problems/rotting-oranges/

✅ Time Complexity: O(m × n)
Where:

m is the number of rows in the grid.

n is the number of columns.

🔍 Why?
Grid Traversal (Initialization)

You traverse the entire grid once to:

Count fresh oranges.

Add all rotten oranges to the queue.

This takes O(m × n).

BFS Traversal

In the worst case, every cell with a fresh orange gets visited exactly once and turned rotten.

So again, BFS will process each cell at most once → O(m × n).

Hence, the overall time complexity is:

✅ O(m × n)

✅ Space Complexity: O(m × n)
In the worst case, the queue can hold all the rotten oranges → up to O(m × n).

You also use a few variables like ones, seconds, and a directions list of constant size, which is negligible.

So:

✅ Space Complexity = O(m × n)

'''

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Directions for moving up, down, left, and right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque()  # Queue for BFS traversal
        ones = 0  # Count of fresh oranges (1s)
        seconds = 0  # Timer to count minutes

        # Helper function to check if a cell is within grid bounds
        def is_within_bounds(r: int, c: int):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        # Step 1: Count fresh oranges and enqueue all rotten ones
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:  # Fresh orange found
                    ones += 1
                elif grid[r][c] == 2:  # Rotten orange found
                    queue.append((r, c))  # Add to BFS queue

        # Step 2: Perform BFS to spread rot
        while queue and ones > 0:  # Continue while there are fresh oranges
            seconds += 1  # Increase time as each minute passes

            # Process all currently rotten oranges in queue
            for _ in range(len(queue)):
                r, c = queue.popleft()  # Get the next rotten orange
                
                # Try all 4 possible directions (up, down, left, right)
                for d in dirs:
                    next_r, next_c = r + d[0], c + d[1]

                    # Check if the next cell is within bounds and has a fresh orange
                    if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == 1:
                        grid[next_r][next_c] = 2  # Make it rotten
                        queue.append((next_r, next_c))  # Add to queue for next round
                        ones -= 1  # Reduce count of fresh oranges

        # Step 3: If no fresh oranges are left, return elapsed time; otherwise, return -1
        return seconds if ones == 0 else -1

        
