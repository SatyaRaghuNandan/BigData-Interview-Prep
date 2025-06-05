Python/LeetCode/Meta/Easy/938-Range-Sum-of-BST.py

"""
1. Problem Summary
   - Given a BST and a range [low, high], find the sum of all node values within that range
   - Key concepts: Binary Search Tree, DFS/BFS traversal, Tree manipulation

2. Meta Expectations
   - Time Complexity: O(n) where n is number of nodes
   - Space Complexity: O(h) where h is height of tree (due to recursion stack)
   - Clean code with proper type hints
   - Efficient use of BST properties
   - Clear variable naming and comments

3. Pythonic Solution
"""

# https://leetcode.com/problems/range-sum-of-bst/

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Example 1:

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# Example 2:

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper function to create a tree from a list representation."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Find sum of all node values within [low, high] range.
        
        Args:
            root: Root of the BST
            low: Lower bound of range
            high: Upper bound of range
            
        Returns:
            Sum of all node values in range
        """
        def dfs(root):
            nonlocal sum
            if not root:
                return 0

            # Add current node if in range
            if low <= root.val <= high:
                sum += root.val

            # Only traverse left if current value > low
            if low < root.val:
                dfs(root.left)
            # Only traverse right if current value < high
            if high > root.val:
                dfs(root.right)

        sum = 0
        dfs(root)
        return sum

"""
4. Step-by-Step Walkthrough
   Example: root = [10,5,15,3,7,None,18], low = 7, high = 15
   
   Initial state: sum = 0
   1. Start at root (10): 10 is in range, sum = 10
   2. Check left (5): 5 < low, skip
   3. Check right (15): 15 is in range, sum = 25
   4. Check right's left (None): skip
   5. Check right's right (18): 18 > high, skip
   6. Back to 5's right (7): 7 is in range, sum = 32
   Final result: 32

5. Variants and Follow-ups
   - Count nodes in range instead of summing
   - Find all values in range (not just sum)
   - Handle invalid ranges (low > high)
   - Optimize for very large trees
   - Handle duplicate values

6. Python Deep Dive
   - Optional type hints for nullable values
   - List comprehension for tree creation
   - Nonlocal keyword for nested function scope

7. Pitfalls to Avoid
   - Not using BST properties to optimize traversal
   - Forgetting to handle None/empty tree case
   - Not considering edge cases (single node, all nodes in range)

8. Reversal Practice
   - Find nodes outside the range
   - Find the range that contains exactly k nodes
   - Find the smallest range that contains all nodes
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        {
            "values": [10,5,15,3,7,None,18],
            "low": 7,
            "high": 15,
            "expected": 32
        },
        {
            "values": [10,5,15,3,7,13,18,1,None,6],
            "low": 6,
            "high": 10,
            "expected": 23
        }
    ]
    
    solution = Solution()
    for i, test in enumerate(test_cases, 1):
        root = create_tree(test["values"])
        result = solution.rangeSumBST(root, test["low"], test["high"])
        print(f"Test {i}:")
        print(f"Input: values={test['values']}, low={test['low']}, high={test['high']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Passed: {result == test['expected']}\n")
        

            

Python/LeetCode/Meta/Easy/125-Valid-Palindrome.py


"""
Problem Summary:
---------------
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
A palindrome reads the same forward and backward.

Input/Output Constraints:
- Input: String s (0 <= s.length <= 2 * 10^5)
- Output: Boolean indicating if s is a palindrome
- Edge Cases: Empty string, single character, non-alphanumeric characters

Meta Expectations:
----------------
- Time Complexity: O(n) where n is the length of the string
- Space Complexity: O(1) for two-pointer approach, O(n) for filtered string
- Coding Standards:
  * Clean, readable code
  * Proper type hints
  * Clear variable names
- Error Handling:
  * Handle empty strings
  * Handle non-alphanumeric characters

Pythonic Solution:
----------------
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a string is a palindrome, considering only alphanumeric characters.
        
        Args:
            s: Input string to check
            
        Returns:
            bool: True if the string is a palindrome, False otherwise
        """
        # Filter and convert to lowercase
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Two-pointer approach
        left, right = 0, len(filtered_s) - 1
        
        while left < right:
            if filtered_s[left] != filtered_s[right]:
                return False
            left += 1
            right -= 1
        
        return True

"""
Step-by-Step Walkthrough:
------------------------
1. Filter the string:
   - Remove all non-alphanumeric characters
   - Convert remaining characters to lowercase
   Example: "A man, a plan, a canal: Panama" -> "amanaplanacanalpanama"

2. Two-pointer approach:
   - Start with pointers at both ends
   - Compare characters and move pointers inward
   - Return False if characters don't match
   - Return True if pointers meet

Variants and Follow-ups:
-----------------------
1. Case-sensitive palindrome:
   - Don't convert to lowercase
   - Compare original characters

2. Strict palindrome:
   - Consider all characters (including spaces and punctuation)
   - No filtering needed

3. Longest palindromic substring:
   - Find the longest substring that is a palindrome
   - Requires different approach (expand around center)

Python Deep Dive:
---------------
- String methods used:
  * isalnum(): Check if character is alphanumeric
  * lower(): Convert to lowercase
  * join(): Concatenate characters
- List comprehension for filtering
- Two-pointer technique for efficient comparison

Pitfalls to Avoid:
----------------
1. Not handling empty strings
2. Case sensitivity issues
3. Not considering non-alphanumeric characters
4. Inefficient string concatenation
5. Not using two-pointer approach for O(1) space

Reversal Practice:
----------------
1. Find all palindromic substrings
2. Count palindromic substrings
3. Find shortest palindrome that can be formed by adding characters
4. Check if string can be rearranged to form a palindrome

Testing Strategy:
---------------
1. Basic cases:
   - Simple palindromes
   - Non-palindromes
2. Edge cases:
   - Empty string
   - Single character
   - All non-alphanumeric
3. Complex cases:
   - Mixed case and special characters
   - Long strings
   - Strings with spaces

Implementation Checklist:
-----------------------
- [x] Input validation
- [x] Edge case handling
- [x] Error handling
- [x] Type hints
- [x] Documentation
- [x] Test cases
- [x] Performance optimization
- [x] Code style compliance
- [x] Memory management
- [x] Time complexity analysis

Common Interview Questions:
-------------------------
1. How would you handle Unicode characters?
2. Can you solve this without creating a new string?
3. How would you modify the solution for case-sensitive comparison?
4. What's the time/space complexity of your solution?
5. How would you handle very long strings?

Learning Resources:
-----------------
1. LeetCode Problem: https://leetcode.com/problems/valid-palindrome/
2. Python String Methods: https://docs.python.org/3/library/stdtypes.html#string-methods
3. Two Pointer Technique: https://leetcode.com/articles/two-pointer-technique/
"""

def test_solution():
    """Test cases for the solution."""
    test_cases = [
        {
            "input": {"s": "A man, a plan, a canal: Panama"},
            "expected": True,
            "description": "Complex palindrome with spaces and punctuation"
        },
        {
            "input": {"s": "race a car"},
            "expected": False,
            "description": "Non-palindrome"
        },
        {
            "input": {"s": ""},
            "expected": True,
            "description": "Empty string"
        },
        {
            "input": {"s": "a"},
            "expected": True,
            "description": "Single character"
        },
        {
            "input": {"s": ".,"},
            "expected": True,
            "description": "Only non-alphanumeric characters"
        }
    ]
    
    solution = Solution()
    for i, test in enumerate(test_cases, 1):
        try:
            result = solution.isPalindrome(**test["input"])
            assert result == test["expected"], \
                f"Test {i} failed: {test['description']}. Expected {test['expected']}, got {result}"
            print(f"Test {i} passed: {test['description']}")
        except Exception as e:
            print(f"Test {i} failed: {test['description']}. Error: {str(e)}")

if __name__ == "__main__":
    test_solution()

Python/LeetCode/Meta/Easy/25-Valid-Palindrome.py
"""
1. Problem Summary
   - Check if a string is a palindrome after removing non-alphanumeric characters
   - Case-insensitive comparison
   - Key concepts: Two pointers, String manipulation

2. Meta Expectations
   - Time Complexity: O(n) where n is string length
   - Space Complexity: O(1) for in-place solution
   - Clean code with proper type hints
   - Efficient string manipulation
   - Clear variable naming and comments

3. Pythonic Solution
"""

# https://leetcode.com/problems/valid-palindrome/

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

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if string is palindrome after removing non-alphanumeric chars.
        
        Args:
            s: Input string to check
            
        Returns:
            True if string is palindrome, False otherwise
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True

"""
4. Step-by-Step Walkthrough
   Example: s = "A man, a plan, a canal: Panama"
   
   Initial state: left = 0, right = 30
   Step 1: Compare 'A' and 'a' -> match
   Step 2: Compare 'm' and 'm' -> match
   Step 3: Skip ',' and ':' -> compare 'a' and 'a' -> match
   ... continues until middle
   Final result: True

5. Variants and Follow-ups
   - Handle different character sets
   - Find longest palindromic substring
   - Count number of palindromes
   - Check if string can be rearranged into palindrome
   - Handle Unicode characters

6. Python Deep Dive
   - String methods: isalnum(), lower()
   - Two-pointer technique
   - String indexing and slicing

7. Pitfalls to Avoid
   - Not handling empty strings
   - Case sensitivity issues
   - Not considering non-alphanumeric characters
   - Off-by-one errors in indices
   - Not handling Unicode characters

8. Reversal Practice
   - Find non-palindromic parts
   - Make string palindrome with minimum changes
   - Find all palindromic substrings
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        {
            "input": "A man, a plan, a canal: Panama",
            "expected": True
        },
        {
            "input": "race a car",
            "expected": False
        },
        {
            "input": " ",
            "expected": True
        },
        {
            "input": "0P",
            "expected": False
        }
    ]
    
    solution = Solution()
    for i, test in enumerate(test_cases, 1):
        result = solution.isPalindrome(test["input"])
        print(f"Test {i}:")
        print(f"Input: {test['input']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Passed: {result == test['expected']}\n")


Python/LeetCode/Meta/Easy/408-Valid-Word-Abbreviation.py
"""
1. Problem Summary
   - Check if a word can be abbreviated according to given rules
   - Abbreviation rules: replace consecutive characters with their count
   - Key concepts: String parsing, Two pointers, Edge cases

2. Meta Expectations
   - Time Complexity: O(n) where n is length of word
   - Space Complexity: O(1) for in-place solution
   - Clean code with proper type hints
   - Efficient string parsing
   - Clear variable naming and comments

3. Pythonic Solution
"""

# https://leetcode.com/problems/valid-word-abbreviation/

# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The length of the abbreviation is the sum of these lengths.

# Note that abbr contains only lowercase letters and digits.

# Given a string word and an abbreviation abbr, return whether the string matches with the given abbreviation.

# A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:

# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true
# Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n" -> "i nternational iz atio n" after replacing the first "i" with 1 and "s" with 4).

# Example 2:

# Input: word = "apple", abbr = "a2e"
# Output: false
# Explanation: We cannot replace the first 'a' with 2 since the abbreviation is "a2e", not "2e".


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        Check if abbreviation is valid for the word.
        
        Args:
            word: Original word
            abbr: Abbreviation to check
            
        Returns:
            True if abbreviation is valid, False otherwise
        """
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':  # Leading zeros not allowed
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
                
        return i == len(word) and j == len(abbr)

"""
4. Step-by-Step Walkthrough
   Example: word = "internationalization", abbr = "i12iz4n"
   
   Initial state: i = 0, j = 0
   Step 1: 'i' matches 'i' -> i = 1, j = 1
   Step 2: '12' -> skip 12 chars in word -> i = 13, j = 3
   Step 3: 'i' matches 'i' -> i = 14, j = 4
   Step 4: 'z' matches 'z' -> i = 15, j = 5
   Step 5: '4' -> skip 4 chars in word -> i = 19, j = 6
   Step 6: 'n' matches 'n' -> i = 20, j = 7
   Final result: True

5. Variants and Follow-ups
   - Generate all possible abbreviations
   - Find shortest valid abbreviation
   - Handle multiple abbreviations
   - Validate against dictionary
   - Handle special characters

6. Python Deep Dive
   - String methods: isdigit()
   - Integer parsing
   - String indexing
   - Edge case handling

7. Pitfalls to Avoid
   - Not handling leading zeros
   - Not checking string lengths
   - Not handling empty strings
   - Not validating number ranges
   - Not handling invalid characters

8. Reversal Practice
   - Generate word from abbreviation
   - Find all possible abbreviations
   - Find shortest valid abbreviation
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        {
            "word": "internationalization",
            "abbr": "i12iz4n",
            "expected": True
        },
        {
            "word": "apple",
            "abbr": "a2e",
            "expected": False
        },
        {
            "word": "a",
            "abbr": "01",
            "expected": False
        },
        {
            "word": "hi",
            "abbr": "2i",
            "expected": False
        }
    ]
    
    solution = Solution()
    for i, test in enumerate(test_cases, 1):
        result = solution.validWordAbbreviation(test["word"], test["abbr"])
        print(f"Test {i}:")
        print(f"Input: word='{test['word']}', abbr='{test['abbr']}'")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Passed: {result == test['expected']}\n")

Python/LeetCode/Meta/Easy/543-diameter-of-binary-tree.py

"""
1. Problem Summary
   - Find the diameter (longest path between any two nodes) of a binary tree
   - Path length is measured by number of edges
   - Key concepts: Binary Tree, DFS, Tree traversal

2. Meta Expectations
   - Time Complexity: O(n) where n is number of nodes
   - Space Complexity: O(h) where h is height of tree
   - Clean code with proper type hints
   - Efficient tree traversal
   - Clear variable naming and comments

3. Pythonic Solution
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Helper function to create a tree from a list representation."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Find the diameter of a binary tree.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Length of the longest path between any two nodes
        """
        diameter = 0

        def dfs(root):
            nonlocal diameter
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Update diameter if current path is longer
            diameter = max(diameter, left + right)
            
            # Return max depth of current node
            return max(left, right) + 1
        
        dfs(root)
        return diameter

"""
4. Step-by-Step Walkthrough
   Example: root = [1,2,3,4,5]
   
   Initial state: diameter = 0
   Step 1: Start at root (1)
   Step 2: DFS left subtree (2)
   Step 3: DFS left of 2 (4) -> return 1
   Step 4: DFS right of 2 (5) -> return 1
   Step 5: At node 2: diameter = max(0, 1+1) = 2
   Step 6: DFS right subtree (3) -> return 1
   Step 7: At root: diameter = max(2, 1+1) = 2
   Final result: 3

5. Variants and Follow-ups
   - Find diameter of n-ary tree
   - Find all paths with maximum diameter
   - Find diameter with weighted edges
   - Find diameter with negative weights
   - Find diameter with cycles

6. Python Deep Dive
   - Optional type hints
   - Nonlocal keyword
   - Tree node class
   - Recursive DFS

7. Pitfalls to Avoid
   - Not handling empty tree
   - Not considering all paths
   - Not updating diameter correctly
   - Not handling single node
   - Not considering edge cases

8. Reversal Practice
   - Find shortest path between nodes
   - Find all paths with given length
   - Find nodes with maximum distance
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        {
            "values": [1,2,3,4,5],
            "expected": 3
        },
        {
            "values": [1,2],
            "expected": 1
        },
        {
            "values": [1],
            "expected": 0
        },
        {
            "values": [1,2,3,4,5,6,7],
            "expected": 4
        }
    ]
    
    solution = Solution()
    for i, test in enumerate(test_cases, 1):
        root = create_tree(test["values"])
        result = solution.diameterOfBinaryTree(root)
        print(f"Test {i}:")
        print(f"Input: values={test['values']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Passed: {result == test['expected']}\n")


Python/LeetCode/Meta/Easy/88-Merge-Sorted-Array.py
"""
1. Problem Summary
   - Merge two sorted arrays nums1 and nums2 into nums1
   - nums1 has extra space at the end to accommodate nums2
   - Key concepts: Two pointers, In-place array manipulation

2. Meta Expectations
   - Time Complexity: O(m + n) where m and n are lengths of arrays
   - Space Complexity: O(1) as we modify in-place
   - Clean code with proper type hints
   - Efficient use of two-pointer technique
   - Clear variable naming and comments

3. Pythonic Solution
"""

# https://leetcode.com/problems/merge-sorted-array/

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

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place.
        
        Args:
            nums1: First sorted array with extra space
            m: Number of elements in nums1
            nums2: Second sorted array
            n: Number of elements in nums2
        """
        while n > 0:
            if m > 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1

"""
4. Step-by-Step Walkthrough
   Example: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
   
   Initial state:
   nums1 = [1,2,3,0,0,0], m = 3
   nums2 = [2,5,6], n = 3
   
   Step 1: Compare 3 and 6
   nums1 = [1,2,3,0,0,6], m = 3, n = 2
   
   Step 2: Compare 3 and 5
   nums1 = [1,2,3,0,5,6], m = 3, n = 1
   
   Step 3: Compare 3 and 2
   nums1 = [1,2,3,3,5,6], m = 2, n = 1
   
   Step 4: Compare 2 and 2
   nums1 = [1,2,2,3,5,6], m = 2, n = 0
   
   Final result: [1,2,2,3,5,6]

5. Variants and Follow-ups
   - Merge k sorted arrays
   - Merge with no extra space
   - Handle duplicate elements differently
   - Merge with custom comparison function
   - Merge with stability requirements

6. Python Deep Dive
   - List slicing and in-place modification
   - Type hints for array parameters
   - Python's list operations

7. Pitfalls to Avoid
   - Not handling empty arrays
   - Modifying array while iterating
   - Not considering edge cases (all elements in one array)
   - Not using the extra space efficiently

8. Reversal Practice
   - Split a sorted array into two sorted arrays
   - Find the kth element in two sorted arrays
   - Merge with alternating elements
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        {
            "nums1": [1,2,3,0,0,0],
            "m": 3,
            "nums2": [2,5,6],
            "n": 3,
            "expected": [1,2,2,3,5,6]
        },
        {
            "nums1": [1],
            "m": 1,
            "nums2": [],
            "n": 0,
            "expected": [1]
        },
        {
            "nums1": [0],
            "m": 0,
            "nums2": [1],
            "n": 1,
            "expected": [1]
        }
    ]
    
    solution = Solution()
    for i, test in enumerate(test_cases, 1):
        nums1 = test["nums1"].copy()  # Create a copy to preserve original
        solution.merge(nums1, test["m"], test["nums2"], test["n"])
        print(f"Test {i}:")
        print(f"Input: nums1={test['nums1']}, m={test['m']}, nums2={test['nums2']}, n={test['n']}")
        print(f"Output: {nums1}")
        print(f"Expected: {test['expected']}")
        print(f"Passed: {nums1 == test['expected']}\n")


Python/LeetCode/Meta/Easy/938-Range-Sum-of-BST.py

"""
1. Problem Summary
   - Given a BST and a range [low, high], find the sum of all node values within that range
   - Key concepts: Binary Search Tree, DFS/BFS traversal, Tree manipulation

2. Meta Expectations
   - Time Complexity: O(n) where n is number of nodes
   - Space Complexity: O(h) where h is height of tree (due to recursion stack)
   - Clean code with proper type hints
   - Efficient use of BST properties
   - Clear variable naming and comments

3. Pythonic Solution
"""

# https://leetcode.com/problems/range-sum-of-bst/

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Example 1:

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# Example 2:

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper function to create a tree from a list representation."""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Find sum of all node values within [low, high] range.
        
        Args:
            root: Root of the BST
            low: Lower bound of range
            high: Upper bound of range
            
        Returns:
            Sum of all node values in range
        """
        def dfs(root):
            nonlocal sum
            if not root:
                return 0

            # Add current node if in range
            if low <= root.val <= high:
                sum += root.val

            # Only traverse left if current value > low
            if low < root.val:
                dfs(root.left)
            # Only traverse right if current value < high
            if high > root.val:
                dfs(root.right)

        sum = 0
        dfs(root)
        return sum

"""
4. Step-by-Step Walkthrough
   Example: root = [10,5,15,3,7,None,18], low = 7, high = 15
   
   Initial state: sum = 0
   1. Start at root (10): 10 is in range, sum = 10
   2. Check left (5): 5 < low, skip
   3. Check right (15): 15 is in range, sum = 25
   4. Check right's left (None): skip
   5. Check right's right (18): 18 > high, skip
   6. Back to 5's right (7): 7 is in range, sum = 32
   Final result: 32

5. Variants and Follow-ups
   - Count nodes in range instead of summing
   - Find all values in range (not just sum)
   - Handle invalid ranges (low > high)
   - Optimize for very large trees
   - Handle duplicate values

6. Python Deep Dive
   - Optional type hints for nullable values
   - List comprehension for tree creation
   - Nonlocal keyword for nested function scope

7. Pitfalls to Avoid
   - Not using BST properties to optimize traversal
   - Forgetting to handle None/empty tree case
   - Not considering edge cases (single node, all nodes in range)

8. Reversal Practice
   - Find nodes outside the range
   - Find the range that contains exactly k nodes
   - Find the smallest range that contains all nodes
"""

if __name__ == "__main__":
    # Test cases
    test_cases = [
        {
            "values": [10,5,15,3,7,None,18],
            "low": 7,
            "high": 15,
            "expected": 32
        },
        {
            "values": [10,5,15,3,7,13,18,1,None,6],
            "low": 6,
            "high": 10,
            "expected": 23
        }
    ]
    
    solution = Solution()
    for i, test in enumerate(test_cases, 1):
        root = create_tree(test["values"])
        result = solution.rangeSumBST(root, test["low"], test["high"])
        print(f"Test {i}:")
        print(f"Input: values={test['values']}, low={test['low']}, high={test['high']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Passed: {result == test['expected']}\n")
        

            











