# ---- File: 1004_max_consecutive_ones_3\python\first_variant_1004_python.py ----
from typing import List

def longestOnes_first_variant_1004_python(days: List[str], pto: int) -> int:
    max_vacation = 0
    left = 0
    for right in range(len(days)):
        if days[right] == 'W':
            pto -= 1

        while pto < 0:
            if days[left] == 'W':
                pto += 1
            left += 1

        max_vacation = max(max_vacation, right - left + 1)
    return max_vacation

if __name__ == '__main__':
    days = ['W', 'H', 'H', 'W', 'W', 'H', 'W']
    pto = 2
    assert longestOnes_first_variant_1004_python(days, pto) == 5

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 0
    assert longestOnes_first_variant_1004_python(days, pto) == 2

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 5
    assert longestOnes_first_variant_1004_python(days, pto) == 7

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 10
    assert longestOnes_first_variant_1004_python(days, pto) == 7

    days = ['H', 'H', 'H', 'H', 'H', 'H', 'H']
    pto = 0
    assert longestOnes_first_variant_1004_python(days, pto) == 7

    days = ['W', 'H', 'W', 'W', 'W', 'H', 'W', 'H']
    pto = 1
    assert longestOnes_first_variant_1004_python(days, pto) == 3


# ---- File: 1004_max_consecutive_ones_3\python\fourth_variant_decimal_pto.py ----
from typing import List

class Variant:
    def getMaxVacations(self, days: List[str], pto: float) -> float:
        max_vacation = 0.0
        whole_pto, partial_pto = int(pto), pto - int(pto)
        left = 0
        for right in range(len(days)):
            if days[right] == 'W':
                whole_pto -= 1

            while whole_pto < 0:
                if days[left] == 'W':
                    whole_pto += 1
                left += 1

            extension = 0.0
            if left > 0 and days[left - 1] == 'W' or \
               right < len(days) - 1 and days[right + 1] == 'W':
               extension = partial_pto

            max_vacation = max(max_vacation, right - left + 1 + extension)

        return max_vacation

# ---- File: 1004_max_consecutive_ones_3\python\original_1004_python.py ----
from typing import List

def longestOnes_1004_python(nums: List[int], k: int) -> int:
    max_ = 0
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1

        while k < 0:
            if nums[left] == 0:
                k += 1
            left += 1

        max_ = max(max_, right - left + 1)
    return max_

# ---- File: 1004_max_consecutive_ones_3\python\second_variant_1004_python.py ----
from typing import List

def longestOnes_second_variant_1004_python(year: List[bool], pto: int) -> int:
    max_vacation = 0
    left = 0
    for right in range(len(year)):
        if not year[right]:
            pto -= 1

        while pto < 0:
            if not year[left]:
                pto += 1
            left += 1

        max_vacation = max(max_vacation, right - left + 1)
    return max_vacation

if __name__ == '__main__':
    year = [False, True, True, False, False, True, False]
    pto = 2
    assert longestOnes_second_variant_1004_python(year, pto) == 5

    year = [False, False, True, True, False, False, False]
    pto = 0
    assert longestOnes_second_variant_1004_python(year, pto) == 2

    year = [False, False, True, True, False, False, False]
    pto = 5
    assert longestOnes_second_variant_1004_python(year, pto) == 7

    year = [False, False, True, True, False, False, False]
    pto = 10
    assert longestOnes_second_variant_1004_python(year, pto) == 7

    year = [True, True, True, True, True, True, True]
    pto = 0
    assert longestOnes_second_variant_1004_python(year, pto) == 7

    year = [False, True, False, False, False, True, False, True]
    pto = 1
    assert longestOnes_second_variant_1004_python(year, pto) == 3


# ---- File: 1004_max_consecutive_ones_3\python\third_variant_2d_matrix_1004.py ----
from typing import List

class Variant:
    def shrink_window(self, days: List[List[str]], left: List[int]) -> List[int]:
        row, col = left[0], left[1]
        if col == len(days[0]) - 1:
            return [row + 1, 0]
        return [row, col + 1]

    def getMaxVacations(self, days: List[List[str]], pto: int) -> int:
        max_vacation = 0
        curr_vacation = 0
        left = [0, 0]
        for row in range(len(days)):
            for col in range(len(days[0])):
                if days[row][col] == 'W':
                    pto -= 1
                curr_vacation += 1

                while pto < 0:
                    if days[left[0]][left[1]] == 'W':
                        pto += 1
                    left = self.shrink_window(days, left)
                    curr_vacation -= 1

                max_vacation = max(curr_vacation, max_vacation)

        return max_vacation

# ---- File: 1047_remove_all_adjacent_duplicates_in_string\python\original_1047_python.py ----
def removeDuplicates(s):
    result = []
    for ch in s:
        if not result or result[-1] != ch:
            result.append(ch)
        else:
            result.pop()

    return ''.join(result)


# ---- File: 1047_remove_all_adjacent_duplicates_in_string\python\variant_remove_all_1047_python.py ----
def remove_all_adjacent_duplicates_variant_1047_python(s):
    letters = []
    for ch in s:
        if not letters:
            letters.append({'val': ch, 'freq': 1})
            continue
        if letters[-1]['val'] == ch:
            letters[-1]['freq'] += 1
            continue

        if letters[-1]['freq'] > 1:
            letters.pop()

        if not letters or letters[-1]['val'] != ch:
            letters.append({'val': ch, 'freq': 1})
        elif letters[-1]['val'] == ch:
            letters[-1]['freq'] += 1

    if letters and letters[-1]['freq'] > 1:
        letters.pop()

    result = ''.join([letter['val'] for letter in letters])
    return result

if __name__ == '__main__':
    s = "azxxxzy"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "ay"

    s = "abbaxx"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aabbccdd"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aaabbaad"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "d"

    s = "abcdefg"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "abcdefg"

    s = "abbcddeff"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "ace"

    s = "abcdeffedcba"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aabccddeeffbbbbbbbbbf"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "f"

    s = "abbbacca"; # Cannot pick and choose duplicates in the middle to delete first
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "a"


# ---- File: 121_best_time_to_buy_and_sell_stock\python\original_121_python.py ----
def maxProfit(prices):
    min_buying_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_buying_price)
        
        if price < min_buying_price:
            min_buying_price = price
    
    return max_profit


# ---- File: 121_best_time_to_buy_and_sell_stock\python\variant_121_python.py ----
def find_cheapest_tickets(departures, returns):
    min_departure_cost = departures[0]
    min_cost = float('inf')
    
    for i in range(1, len(departures)):
        min_cost = min(min_cost, min_departure_cost + returns[i])

        if departures[i] < min_departure_cost:
            min_departure_cost = departures[i]
    
    return min_cost

if __name__ == "__main__":
    departures = [8, 3, 6, 10]
    returns = [10, 9, 5, 8]
    assert find_cheapest_tickets(departures, returns) == 8

    departures = [10, 3, 10, 9, 3]
    returns = [4, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 9

    departures = [1, 3, 10, 9, 3]
    returns = [1, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [1, 3, 10, 9, 3]
    returns = [1, 1, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 2

    departures = [1, 3, 10, 9, 3]
    returns = [10, 9, 8, 7, 6]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [12, 33, 44, 9, 23]
    returns = [100, 90, 80, 70, 15]
    assert find_cheapest_tickets(departures, returns) == 24

    departures = [4, 3, 5, 11, 2]
    returns = [1, 6, 10, 2, 9]
    assert find_cheapest_tickets(departures, returns) == 5

# ---- File: 125_valid_palindrome\mock\mock_125.py ----
def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True

# ---- File: 125_valid_palindrome\python\original_125.py ----
class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = [c for c in s.lower() if c.isalnum()]
        left, right = 0, len(d) - 1
        while left < right:
            if d[left] != d[right]:
                return False
            left += 1
            right -= 1
        return True


# ---- File: 125_valid_palindrome\python\variant_125.py ----
class Solution:
    def isPalindrome(self, s: str, include: list[str]) -> bool:
        include_set = set(include)
        left, right = 0, len(s) - 1
        while left < right:
            while s[left] not in include_set and left < right:
                left += 1
            while s[right] not in include_set and left < right:
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    assert not solution.isPalindrome("racecarX", ["r", "X"])
    assert solution.isPalindrome("Yo, banana boY!", ["Y", "o", "b", "a", "n"])
    assert solution.isPalindrome("yo banana boy!", ["y", "o", "b", "a", "n"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", " ", "b", "c", "d", "e"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", "b", "c", "d", "e"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", "b", "e"])
    assert not solution.isPalindrome("Wow", ["W", "o", "w"])
    assert solution.isPalindrome("WwoWWWWWWWWWWWWWow", ["o", "w"])
    assert solution.isPalindrome("__________________", ["1", "2"])
    assert not solution.isPalindrome("________133__________", ["1", "3"])
    assert not solution.isPalindrome("____1____133_______________", ["1", "3", "_"])
    assert solution.isPalindrome("", ["1", "3", "_"])
    assert solution.isPalindrome("", [])
    assert solution.isPalindrome("MadaM", [])
    assert solution.isPalindrome("MadaM", ["z", "M", "d"])
    assert not solution.isPalindrome("MadaMM", ["z", "M", "d"])
    assert not solution.isPalindrome("racecarX", ["r", "X"])


# ---- File: 129_sum_root_to_leaf_nodes\python\first_variant_129.py ----
from typing import Optional

class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def getPlaces(num: int):
            if not num:
                return 10
                
            places = 1
            while num > 0:
                num = num // 10
                places *= 10
            return places
        
        def preorder(node: Solution.TreeNode, curr_number: int):
            nonlocal root_to_leaf
            if node:
                places = getPlaces(node.val)
                curr_number = (curr_number * places) + node.val
                if not (node.left or node.right):
                    root_to_leaf += curr_number
                preorder(node.left, curr_number)
                preorder(node.right, curr_number)

        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf


if __name__ == "__main__":
    solution = Solution()
    root = Solution.TreeNode(3)
    root.left = Solution.TreeNode(79, right=Solution.TreeNode(111))
    root.right = Solution.TreeNode(2)
    assert solution.sumNumbers(root) == 379143

    root = Solution.TreeNode(1)
    root.left = Solution.TreeNode(2)
    root.left.left = Solution.TreeNode(90)
    root.right = Solution.TreeNode(42)
    root.right.left = Solution.TreeNode(511)
    assert solution.sumNumbers(root) == 1290 + 142511

    root = Solution.TreeNode(1)
    root.left = Solution.TreeNode(2)
    root.left.left = Solution.TreeNode(912)
    root.left.left.left = Solution.TreeNode(3)
    root.left.left.right = Solution.TreeNode(4)
    root.right = Solution.TreeNode(46)
    root.right.left = Solution.TreeNode(5)
    root.right.right = Solution.TreeNode(61)
    assert solution.sumNumbers(root) == 129123 + 129124 + 1465 + 14661

    root = Solution.TreeNode(1)
    root.left = Solution.TreeNode(2)
    root.right = Solution.TreeNode(3)
    assert solution.sumNumbers(root) == 12 + 13

    root = Solution.TreeNode(10)
    root.left = Solution.TreeNode(200)
    root.right = Solution.TreeNode(3000)
    assert solution.sumNumbers(root) == 10200 + 103000

    root = Solution.TreeNode(10)
    root.left = Solution.TreeNode(0)
    root.right = Solution.TreeNode(0)
    assert solution.sumNumbers(root) == 200

    root = None
    assert solution.sumNumbers(root) == 0


# ---- File: 129_sum_root_to_leaf_nodes\python\original_129.py ----
from typing import Optional

from ...utils.treenode import TreeNode

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(node: TreeNode, curr_number: int):
            nonlocal root_to_leaf
            if node:
                curr_number = curr_number * 10 + node.val
                if not (node.left or node.right):
                    root_to_leaf += curr_number

                preorder(node.left, curr_number)
                preorder(node.right, curr_number)

        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf

# ---- File: 129_sum_root_to_leaf_nodes\python\second_variant_129.py ----
class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node, curr_sum, num_negatives):
            if node is None:
                return 0

            curr_sum = (curr_sum * 10) + abs(node.val)
            if node.val < 0:
                num_negatives += 1

            if node.left is None and node.right is None:
                sign = -1 if num_negatives % 2 == 1 else 1
                return curr_sum * sign

            left_sum = helper(node.left, curr_sum, num_negatives)
            right_sum = helper(node.right, curr_sum, num_negatives)

            return left_sum + right_sum

        return helper(root, 0, 0)


if __name__ == "__main__":
    solution = Solution()
    root = Solution.TreeNode(1, 
            left=Solution.TreeNode(-2), 
            right=Solution.TreeNode(3))
    assert solution.sumNumbers(root) == 1

    root = Solution.TreeNode(-1, 
            left=Solution.TreeNode(-2, 
                left=Solution.TreeNode(-9)), 
            right=Solution.TreeNode(4, 
                left=Solution.TreeNode(-5)))
    assert solution.sumNumbers(root) == -129 + 145

    root = Solution.TreeNode(-1, 
            left=Solution.TreeNode(-2, 
                left=Solution.TreeNode(-9, 
                    left=Solution.TreeNode(3), 
                        right=Solution.TreeNode(-3))),
            right=Solution.TreeNode(4, 
                left=Solution.TreeNode(-5), 
                    right=Solution.TreeNode(6)))
    assert solution.sumNumbers(root) == -1293 + 1293 + 145 + -146

    root = Solution.TreeNode(1, 
            left=Solution.TreeNode(2), 
            right=Solution.TreeNode(3))
    assert solution.sumNumbers(root) == 12 + 13

    root = Solution.TreeNode(-1, 
            left=Solution.TreeNode(-2), 
            right=Solution.TreeNode(-3))
    assert solution.sumNumbers(root) == 12 + 13

    root = Solution.TreeNode(-1, 
            left=Solution.TreeNode(-2, 
                left=Solution.TreeNode(-3)))
    assert solution.sumNumbers(root) == -123

    root = None
    assert solution.sumNumbers(root) == 0

# ---- File: 138_copy_list_with_random_pointer\python\original_138.py ----
from typing import Optional

class Solution:
    class Node:
        def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
            self.val = int(x)
            self.next = next
            self.random = random

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        visited = {}

        def dfs(head):
            if head is None:
                return None
            if head in visited:
                return visited[head]
            node = Node(head.val)
            visited[head] = node
            node.next = dfs(head.next)
            node.random = dfs(head.random)
            return node

        return dfs(head)


# ---- File: 138_copy_list_with_random_pointer\python\variant_138.py ----
from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: "Optional[Node]") -> "Optional[NodeCopy]":
        visited = {}

        def dfs(root) -> "Optional[NodeCopy]":
            if root is None:
                return None
            if root in visited:
                return visited[root]
            copy = NodeCopy(root.val)
            visited[root] = copy
            copy.left = dfs(root.left)
            copy.right = dfs(root.right)
            copy.random = dfs(root.random)
            return copy

        return dfs(root)


# ---- File: 1570_dot_product_of_two_sparse_vectors\python\original_1570.py ----
from collections import namedtuple

class SparseVector:
    def __init__(self, nums: list[int]):
        Pair = namedtuple("Pair", "index value")
        self.pairs = [Pair(index, value) for index, value in enumerate(nums) if value != 0]

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        i, j = 0, 0
        while i < len(self.pairs) and j < len(vec.pairs):
            if self.pairs[i].index == vec.pairs[j].index:
                result += self.pairs[i].value * vec.pairs[j].value
                i += 1
                j += 1
            elif self.pairs[i].index < vec.pairs[j].index:
                i += 1
            else:
                j += 1
        return result

# ---- File: 1570_dot_product_of_two_sparse_vectors\python\variant_binary_search_1570.py ----
from collections import namedtuple
from bisect import bisect_left


class SparseVectorVariant:
    def __init__(self, nums: list[int]):
        Pair = namedtuple("Pair", "index value")
        self.pairs = [
            Pair(index, value) for index, value in enumerate(nums) if value != 0
        ]

    def dotProduct(self, vec: "SparseVectorVariant") -> int:
        result = 0
        shorter, longer = (
            (self.pairs, vec.pairs)
            if len(self.pairs) < len(vec.pairs)
            else (vec.pairs, self.pairs)
        )
        for pair in shorter:
            matched_idx = bisect_left(longer, (pair.index,))
            if matched_idx >= len(longer) or longer[matched_idx].index != pair.index:
                continue
            result += pair.value * longer[matched_idx].value

        return result


# ---- File: 162_find_peak_element\python\original_162_python.py ----
def findPeakElement_python(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right - left) // 2 + left

        if (mid == len(nums) - 1 or nums[mid + 1] < nums[mid]) and \
           (mid == 0 or nums[mid - 1] < nums[mid]):
            return mid

        if nums[mid + 1] > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Unreachable


# ---- File: 162_find_peak_element\python\variant_find_valley_element_162_python.py ----
def findValleyElement(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right - left) // 2 + left

        if (mid == len(nums) - 1 or nums[mid + 1] > nums[mid]) and \
           (mid == 0 or nums[mid - 1] > nums[mid]):
            return mid

        if nums[mid + 1] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Unreachable

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    assert findValleyElement(nums) == 0  # Left pos infinity yields valley

    nums = [1, 2, 3, 5, 3, 4, 3, 1, 6]
    assert findValleyElement(nums) == 4

    nums = [3, 2, 3, 4, 3, 2]
    assert findValleyElement(nums) == 1

    nums = [1, 2, 3, 4, 3, 2]
    assert findValleyElement(nums) == 0

    nums = [1, 2, 3, 2, 1, 0]
    assert findValleyElement(nums) == 5  # Right pos infinity yields valley

    nums = [1, 2, 3, 2, 1, 6]
    assert findValleyElement(nums) == 4

# ---- File: 163_missing_ranges\python\original_163.py ----
class Solution:
    def findMissingRanges(
        self, nums: list[int], lower: int, upper: int
    ) -> list[list[int]]:
        n = len(nums)
        missing_ranges = []
        if n == 0:
            missing_ranges.append([lower, upper])
            return missing_ranges

        # Check for any missing numbers between the lower bound and nums[0].
        if lower < nums[0]:
            missing_ranges.append([lower, nums[0] - 1])

        # Check for any missing numbers between successive elements of nums.
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue
            missing_ranges.append([nums[i] + 1, nums[i + 1] - 1])

        # Check for any missing numbers between the last element of nums and the upper bound.
        if upper > nums[-1]:
            missing_ranges.append([nums[-1] + 1, upper])

        return missing_ranges


# ---- File: 163_missing_ranges\python\variant_163.py ----
class Solution:
    def findMissingRangesVariant(self, nums, lower, upper):
        curr_lower = lower
        missing_ranges = []
        nums.append(upper + 1)
        
        for num in nums:
            if num - curr_lower > 2:
                missing_ranges.append(f"{curr_lower}-{num - 1}")
            elif num - curr_lower == 2:
                missing_ranges.append(str(curr_lower))
                missing_ranges.append(str(curr_lower + 1))
            elif num - curr_lower == 1:
                missing_ranges.append(str(curr_lower))
            
            curr_lower = num + 1
        
        return missing_ranges


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 2, 87) == [
        "2-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-87",
    ]

    solution = Solution()
    # Empty vector cases
    assert solution.findMissingRangesVariant([], 0, 0) == ["0"]
    assert solution.findMissingRangesVariant([], 5, 35) == ["5-35"]
    assert solution.findMissingRangesVariant([], 0, 35) == ["0-35"]

    # Valid cases
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 2, 87) == [
        "2-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-87",
    ]

    # Upper bound with dash
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 800) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-800",
    ]

    # Upper bound with one missing number
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 21) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
    ]

    # Upper bound with two missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 22) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
        "22",
    ]

    # Upper bound with no missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 20) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # No missing ranges with one element
    assert solution.findMissingRangesVariant([0], 0, 0) == []

    # No missing ranges with one element V2
    assert solution.findMissingRangesVariant([6], 6, 6) == []

    # Lower bound with dash
    assert solution.findMissingRangesVariant([0, 8, 9, 15, 16, 18, 20], 0, 20) == [
        "1-7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with no missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 5, 20) == [
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with two missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 3, 20) == [
        "3",
        "4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with one missing number
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 4, 20) == [
        "4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Upper bound with no dash
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 5, 22) == [
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
        "22",
    ]

    # One element with two ranges missing
    assert solution.findMissingRangesVariant([10], 5, 22) == ["5-9", "11-22"]


# ---- File: 199_binary_tree_right_side_view\python\first_variant_left_right_side_view_199.py ----
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leftRightSideViewVariant(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        left_side = []
        right_side = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()

                if i == 0:
                    left_side.append(node.val)
                if size == i + 1:
                    right_side.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        result = []
        result.extend(reversed(left_side))
        result.extend(right_side[1:])
        return result


if __name__ == "__main__":
    solution = Solution()
    # Test Case 1: Based on the example in the problem
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    /     \
    #   5       4
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(5)
    root1.right.right = TreeNode(4)
    assert solution.leftRightSideViewVariant(root1) == [5, 2, 1, 3, 4]
    # Test Case 2: Based on the second example
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    assert solution.leftRightSideViewVariant(root2) == [4, 2, 1, 3, 5]

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.right = TreeNode(7)
    root1.right.left = TreeNode(6)
    root1.right.right.left = TreeNode(8)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    assert solution.leftRightSideViewVariant(root1) == [8, 4, 2, 1, 3, 7, 8]

    root2 = TreeNode(1)
    assert solution.leftRightSideViewVariant(root2) == [1]

    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    assert solution.leftRightSideViewVariant(root3) == [3, 2, 1, 2, 3]

    root4 = None
    assert solution.leftRightSideViewVariant(root4) == []

    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)
    root5.right.left = TreeNode(5)
    root5.right.left.right = TreeNode(6)
    root5.right.left.right.right = TreeNode(7)
    root5.left.right = TreeNode(4)
    assert solution.leftRightSideViewVariant(root5) == [7, 6, 4, 2, 1, 3, 5, 6, 7]


# ---- File: 199_binary_tree_right_side_view\python\original_199.py ----
from ...utils.treenode import TreeNode
from typing import Optional
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        rightside = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                curr = queue.popleft()
                if i == level_length - 1:
                    rightside.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return rightside


# ---- File: 199_binary_tree_right_side_view\python\second_variant_print_left_right_side_views_199.py ----
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leftRightSideViewVariantPrint(self, root: Optional[TreeNode]):
        if not root:
            return []

        left_side = []
        right_side = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()

                if i == 0:
                    left_side.append(node.val)
                if size == i + 1:
                    right_side.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        for left_value in left_side[-1:0:-1]:
            print(left_value)
        for right_value in right_side:
            print(right_value)


if __name__ == "__main__":
    solution = Solution()
    # Test Case 1: Based on the example in the problem
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    /     \
    #   5       4
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(5)
    root1.right.right = TreeNode(4)
    solution.leftRightSideViewVariantPrint(root1)  # Should print 5, 2, 1, 3, 4 in order
    print("-")
    # Test Case 2: Based on the second example
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    solution.leftRightSideViewVariantPrint(root2)  # Should print 4, 2, 1, 3, 5 in order
    print("-")

    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    /     \
    #   5       4
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(5)
    root1.right.right = TreeNode(4)
    solution.leftRightSideViewVariantPrint(root1)  # Expected output: 5 2 1 3 4
    print("-")

    root2 = TreeNode(1)
    solution.leftRightSideViewVariantPrint(root2)  # Expected output: 1
    print("-")

    root3 = None
    solution.leftRightSideViewVariantPrint(root3)  # Expected output: (nothing)
    print("-")

    # Tree structure:
    #       1
    #      /
    #     2
    #    /
    #   3
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    solution.leftRightSideViewVariantPrint(root4)  # Expected output: 3 2 1 2 3


# ---- File: 19_remove_nth_node_from_end\python\original_19.py ----
from utils.ListNode import ListNode

class Solution_19:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head

        r = dummy
        for _ in range(n):
            r = r.next

        l = dummy
        while r.next is not None:
            r = r.next
            l = l.next

        l.next = l.next.next
        return dummy.next


# ---- File: 19_remove_nth_node_from_end\python\variant_19_ith_from_beginning.py ----
from utils.ListNode import ListNode

class Solution_19_Variant:
    def removeIthFromBeginning(self, head, n):
        dummy = ListNode()
        dummy.next = head

        i = dummy
        for _ in range(n):
            if i.next is None:
                return dummy.next
            i = i.next

        if i.next is None:
            return dummy.next

        i.next = i.next.next
        return dummy.next

# ---- File: 215_kth_largest_element\python\first_variant_kth_largest_215.py ----
from heapq import heappush, heappop

class Solution:
    def findKthPluseOneLargest(self, nums: list[int], k: int) -> int:
        if k + 1 > len(nums):
            return 0
        k = k + 1
        min_heap = []
        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)
        return min_heap[0]

if __name__ == "__main__":
    solution = Solution()
    # Distinct elements in nums
    nums = [1, 2, 3, 4, 5]
    k = 0
    assert solution.findKthPluseOneLargest(nums, k) == 5
    k = 1
    assert solution.findKthPluseOneLargest(nums, k) == 4
    k = 2
    assert solution.findKthPluseOneLargest(nums, k) == 3
    k = 3
    assert solution.findKthPluseOneLargest(nums, k) == 2
    k = 4
    assert solution.findKthPluseOneLargest(nums, k) == 1
    
    nums = [1]
    k = 0
    assert solution.findKthPluseOneLargest(nums, k) == 1
    
    # Out of range indices
    nums = [1, 2, 3, 4, 5]
    try:
        solution.findKthPluseOneLargest(nums, 5)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass
    try:
        solution.findKthPluseOneLargest(nums, 50)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass

    nums = [1]
    k = 1
    try:
        solution.findKthPluseOneLargest(nums, k)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass

    # Edge Case: Empty list
    nums = []
    k = 0
    try:
        solution.findKthPluseOneLargest(nums, k)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass
    
    k = 1
    try:
        solution.findKthPluseOneLargest(nums, k)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass

    k = 2
    try:
        solution.findKthPluseOneLargest(nums, k)
        assert False, "Expected an out_of_range exception"
    except AssertionError:
        pass

# ---- File: 215_kth_largest_element\python\original_215.py ----
from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)
        return min_heap[0]


# ---- File: 215_kth_largest_element\python\second_variant_kth_smallest_215.py ----
from heapq import heappush, heappop


class Solution:
    def findKthSmallest(self, nums: list[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heappush(max_heap, -num)
            if len(max_heap) > k:
                heappop(max_heap)
        return -max_heap[0]


if __name__ == "__main__":
    solution = Solution()
    assert solution.findKthSmallest([2, 10, 8, 3, 7, 9], 2) == 3
    assert solution.findKthSmallest([2, 10, 8, 3, 7, 9], 4) == 8

    assert solution.findKthSmallest([3, 8, 4, 1, 10], 1) == 1
    assert solution.findKthSmallest([3, 8, 4, 1, 10], 2) == 3
    assert solution.findKthSmallest([3, 8, 4, 1, 10], 3) == 4
    assert solution.findKthSmallest([3, 8, 4, 1, 10], 4) == 8
    assert solution.findKthSmallest([3, 8, 4, 1, 10], 5) == 10

    assert solution.findKthSmallest([1, 1, 1, 1, 2], 1) == 1
    assert solution.findKthSmallest([1, 1, 1, 1, 2], 2) == 1
    assert solution.findKthSmallest([1, 1, 1, 1, 2], 3) == 1
    assert solution.findKthSmallest([1, 1, 1, 1, 2], 4) == 1
    assert solution.findKthSmallest([1, 1, 1, 1, 2], 5) == 2

    assert solution.findKthSmallest([-1, -5, -2, -3, -4], 1) == -5
    assert solution.findKthSmallest([-1, -5, -2, -3, -4], 2) == -4
    assert solution.findKthSmallest([-1, -5, -2, -3, -4], 3) == -3
    assert solution.findKthSmallest([-1, -5, -2, -3, -4], 4) == -2
    assert solution.findKthSmallest([-1, -5, -2, -3, -4], 5) == -1


# ---- File: 21_merge_two_sorted_lists\python\first_variant_21_python.py ----
from typing import List

def merge_3_sorted_lists_first_variant_21_python(listA: List[int], 
                                                 listB: List[int], 
                                                 listC: List[int]) -> List[int]:
    result = []
    a, b, c = 0, 0, 0
    while a < len(listA) or b < len(listB) or c < len(listC):
        a_val = listA[a] if a < len(listA) else float('inf')
        b_val = listB[b] if b < len(listB) else float('inf')
        c_val = listC[c] if c < len(listC) else float('inf')

        min_val = min(a_val, b_val, c_val)
        result.append(min_val)

        if a_val == min_val:
            a += 1
        elif b_val == min_val:
            b += 1
        else:
            c += 1

    return result

if __name__ == '__main__':
    a = [1, 1, 1, 3, 4, 5]
    b = [3, 3, 4, 5, 6]
    c = [1, 1, 3, 3, 8, 8, 8, 10]
    expected = [1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6, 8, 8, 8, 10]
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)

    a = []
    b = [3, 3, 4, 5, 6]
    c = [1, 1, 3, 3, 8, 8, 8, 10]
    expected = [1, 1, 3, 3, 3, 3, 4, 5, 6, 8, 8, 8, 10]
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)

    a = []
    b = []
    c = []
    expected = []
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)

    a = [1]
    b = [2]
    c = [3, 4, 5, 6, 7]
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)

    a = [1, 2, 3]
    b = [1, 2, 3]
    c = [1, 2, 3]
    expected = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)

    a = [2, 2]
    b = [2]
    c = [0]
    expected = [0, 2, 2, 2]
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)

# ---- File: 21_merge_two_sorted_lists\python\second_variant_21_python.py ----
from typing import List

def merge_3_sorted_lists_second_variant_21(listA: List[int], 
                                           listB: List[int], 
                                           listC: List[int]) -> List[int]:
    result = []
    a, b, c = 0, 0, 0
    while a < len(listA) or b < len(listB) or c < len(listC):
        a_val = listA[a] if a < len(listA) else float('inf')
        b_val = listB[b] if b < len(listB) else float('inf')
        c_val = listC[c] if c < len(listC) else float('inf')

        min_val = min(a_val, b_val, c_val)

        if not result or result[-1] != min_val:
            result.append(min_val)

        if a_val == min_val:
            a += 1
        elif b_val == min_val:
            b += 1
        else:
            c += 1

    return result

if __name__ == '__main__':
    a = [1, 1, 1, 3, 4, 5]
    b = [3, 3, 4, 5, 6]
    c = [1, 1, 3, 3, 8, 8, 8, 10]
    expected = [1, 3, 4, 5, 6, 8, 10]
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)

    a = []
    b = [3, 3, 4, 5, 6]
    c = [1, 1, 3, 3, 8, 8, 8, 10]
    expected = [1, 3, 4, 5, 6, 8, 10]
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)

    a = []
    b = []
    c = []
    expected = []
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)

    a = [1]
    b = [2]
    c = [3, 4, 5, 6, 7]
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)

    a = [1, 2, 3]
    b = [1, 2, 3]
    c = [1, 2, 3]
    expected = [1, 2, 3]
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)

    a = [2, 2]
    b = [2]
    c = [0]
    expected = [0, 2]
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)


# ---- File: 236_lowest_common_ancestor\python\first_variant_236_nary_tree.py ----
class TreeNode:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        parent = {root: None}
        stack = [root]
        while p not in parent or q not in parent:
            node = stack.pop()
            for child in node.children:
                parent[child] = node
                stack.append(child)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q


if __name__ == "__main__":
    # Tree structure:
    #       1
    #    /  |  \
    #   3   2   4
    #  / \
    # 5   6
    root1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    root1.children = [node3, node2, node4]
    node3.children = [node5, node6]
    solution = Solution()
    assert solution.lowestCommonAncestor(root1, node5, node2) == root1
    assert solution.lowestCommonAncestor(root1, node5, node6) == node3

    # Test Case 2: More complex tree
    # Tree structure:
    #        10
    #     /  |  \  \
    #    5   1   7  8
    #   / \  |      |
    #  2  4  3      9
    #    /
    #   6
    root2 = TreeNode(10)
    node5_2 = TreeNode(5)
    node1 = TreeNode(1)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node2_2 = TreeNode(2)
    node4_2 = TreeNode(4)
    node3_2 = TreeNode(3)
    node9 = TreeNode(9)
    node6_2 = TreeNode(6)

    root2.children = [node5_2, node1, node7, node8]
    node5_2.children = [node2_2, node4_2]
    node1.children = [node3_2]
    node8.children = [node9]
    node4_2.children = [node6_2]
    assert solution.lowestCommonAncestor(root2, node6_2, node3_2) == root2
    assert solution.lowestCommonAncestor(root2, node6_2, node2_2) == node5_2

    # Tree structure:
    #       1
    #    /  |  \
    #   2   3   4
    #  / \     / | \
    # 5   6   7  8  9
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    root.children = [node2, node3, node4]
    node2.children = [node5, node6]
    node4.children = [node7, node8, node9]
    solution = Solution()
    # Root as the LCA
    assert solution.lowestCommonAncestor(root, node5, node7) == root
    assert solution.lowestCommonAncestor(root, node5, node8) == root
    assert solution.lowestCommonAncestor(root, node5, node9) == root
    assert solution.lowestCommonAncestor(root, node6, node7) == root
    assert solution.lowestCommonAncestor(root, node6, node8) == root
    assert solution.lowestCommonAncestor(root, node6, node9) == root

    assert solution.lowestCommonAncestor(root, node2, node9) == root

    assert solution.lowestCommonAncestor(root, node2, node4) == root
    assert solution.lowestCommonAncestor(root, node2, node3) == root

    # Node 4 as the LCA
    assert solution.lowestCommonAncestor(root, node7, node8) == node4
    assert solution.lowestCommonAncestor(root, node7, node9) == node4

    # Node 2 as the LCA
    assert solution.lowestCommonAncestor(root, node5, node6) == node2

    # Same tree structure for the second test case:
    #       1
    #    /  |  \
    #   2   3   4
    #  / \     / | \
    # 5   6   7  8  9
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    root.children = [node2, node3, node4]
    node2.children = [node5, node6]
    node4.children = [node7, node8, node9]

    solution = Solution()
    # Root as the LCA
    assert solution.lowestCommonAncestor(root, root, node2) == root
    assert solution.lowestCommonAncestor(root, root, node3) == root
    assert solution.lowestCommonAncestor(root, root, node4) == root
    assert solution.lowestCommonAncestor(root, root, node5) == root
    assert solution.lowestCommonAncestor(root, root, node6) == root
    assert solution.lowestCommonAncestor(root, root, node7) == root
    assert solution.lowestCommonAncestor(root, root, node8) == root
    assert solution.lowestCommonAncestor(root, root, node9) == root

    # Node 4 as the LCA
    assert solution.lowestCommonAncestor(root, node4, node8) == node4
    assert solution.lowestCommonAncestor(root, node4, node9) == node4

    # Node 2 as the LCA
    assert solution.lowestCommonAncestor(root, node2, node6) == node2


# ---- File: 236_lowest_common_ancestor\python\original_236.py ----
from ...utils.treenode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent = {root: None}
        stack = [root]
        while p not in parent or q not in parent:
            curr = stack.pop()
            if curr.left:
                parent[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                parent[curr.right] = curr
                stack.append(curr.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q


# ---- File: 31_next_permutation\python\original_31.py ----
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        valley = None
        for i in range(len(nums) - 1, 0, -1):
            # Iterate from end
            if nums[i - 1] < nums[i]:
                valley = i - 1
                break

        if valley is None:
            nums.reverse()
            return

        next_higher = len(nums) - 1
        while nums[next_higher] <= nums[valley]:
            next_higher -= 1

        nums[valley], nums[next_higher] = nums[next_higher], nums[valley]

        left = valley + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# ---- File: 31_next_permutation\python\variant_31_previous_permutation.py ----
class Solution:
    def previousPermutation(self, nums: list[int]) -> None:
        peak = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] > nums[i]:
                peak = i - 1
                break

        if peak is None:
            nums.reverse()
            return

        next_lower = len(nums) - 1
        while nums[next_lower] >= nums[peak]:
            next_lower -= 1

        nums[peak], nums[next_lower] = nums[next_lower], nums[peak]

        left = peak + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    # Basic cases
    solution = Solution()
    nums = [9, 4, 8, 3, 5, 5, 8, 9]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 5, 3]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 3, 5]
    nums = [3, 2, 1]
    solution.previousPermutation(nums)
    assert nums == [3, 1, 2]
    nums = [1, 2, 3]
    solution.previousPermutation(nums)
    assert nums == [3, 2, 1]
    nums = [9, 6, 5, 4, 3, 2]
    solution.previousPermutation(nums)
    assert nums == [9, 6, 5, 4, 2, 3]
    nums = [4, 5, 1, 1, 3, 7]
    solution.previousPermutation(nums)
    assert nums == [4, 3, 7, 5, 1, 1]
    nums = [1, 5, 8, 5, 1, 3, 4, 6, 7]
    solution.previousPermutation(nums)
    assert nums == [1, 5, 8, 4, 7, 6, 5, 3, 1]
    nums = [9, 4, 8, 3, 5, 5, 8, 9]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 5, 3]

    # Single digit case
    nums = [5]
    solution.previousPermutation(nums)
    assert nums == [5]

    # Duplicate digits case
    nums = [1, 1, 1]
    solution.previousPermutation(nums)
    assert nums == [1, 1, 1]

    # Already smallest case (loops around)
    nums = [1, 2, 3, 4, 5, 6]
    solution.previousPermutation(nums)
    assert nums == [6, 5, 4, 3, 2, 1]


# ---- File: 339_nested_list_weight_sum\python\original_339.py ----
from typing import List
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       The result is undefined if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       The result is undefined if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            sum = 0
            for nested in nestedList:
                if nested.isInteger():
                    sum += nested.getInteger() * depth
                else:
                    sum += dfs(nested.getList(), depth + 1)
            return sum
        
        return dfs(nestedList, 1)

# ---- File: 339_nested_list_weight_sum\python\variant_339_bfs.py ----
from collections import deque
from typing import List, Union

# VARIANT: What if you had to define your own schema for NestedList and implement BFS?
class Object:
    def __init__(self):
        self.value: List['Object' | int]

class Solution:
    def depthSum(self, objs: List[Object]) -> int:
        queue = deque(objs)
        level = 1
        sum = 0
        while queue:
            for _ in range(len(queue)):
                obj = queue.popleft()
                if isinstance(obj, int):
                    sum += obj * level
                else:
                    queue.extend(obj.value)
            level += 1

        return sum

# ---- File: 339_nested_list_weight_sum\python\variant_339_dfs.py ----
from collections import deque
from typing import List, Union

# VARIANT: What if you had to define your own schema for NestedList and implement DFS?
class Object:
    def __init__(self):
        self.value: List['Object' | int]

class Solution:
    def depthSum(self, objs: List[Object]) -> int:
        def dfs(objs, depth):
            sum = 0
            for obj in objs:
                if isinstance(obj, int):
                    sum += obj * depth
                else:
                    sum += dfs(obj.value, depth + 1)
            return sum
        return dfs(objs, 1)

# ---- File: 346_moving_average_from_data_stream\python\original_346_python.py ----
from queue import Queue

class MovingAverage_346:
    def __init__(self, size: int):
        self.size = size
        self.queue = Queue()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.window_sum += val
        self.queue.put(val)

        if self.queue.qsize() > self.size:
            self.window_sum -= self.queue.get()

        return self.window_sum / self.queue.qsize()

# ---- File: 346_moving_average_from_data_stream\python\variant_sliding_window_346_python.py ----
from typing import List
def compute_running_sum_variant_346(nums: List[int], size: int) -> List[int]:
    result = []
    window_sum = 0
    for right in range(len(nums)):
        window_sum += nums[right]

        left = right - size
        if left >= 0:
            window_sum -= nums[left]

        if right >= size - 1:
            result.append(window_sum // size)

    return result

if __name__ == '__main__':
    nums = [5, 2, 8, 14, 3]
    size = 3
    assert compute_running_sum_variant_346(nums, size) == [5, 8, 8]

    nums = [6]
    size = 1
    assert compute_running_sum_variant_346(nums, size) == [6]

    nums = [1, 2, 3]
    size = 1
    assert compute_running_sum_variant_346(nums, size) == [1, 2, 3]

    nums = [2, 4, 6, 8, 10, 12]
    size = 2
    assert compute_running_sum_variant_346(nums, size) == [3, 5, 7, 9, 11]

    nums = [2, 4, 6, 8, 10, 12]
    size = 6
    assert compute_running_sum_variant_346(nums, size) == [(2+4+6+8+10+12)/size]

    nums = [1, 2, 3, 4, 5]
    size = 4
    assert compute_running_sum_variant_346(nums, size) == [2, 3]

    nums = [1, 2, 1, 2]
    size = 2
    assert compute_running_sum_variant_346(nums, size) == [1, 1, 1]






# ---- File: 34_find_first_and_last_position_of_element_in_array\python\first_variant_34.py ----
class Solution:
    def countElements(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if target > nums[-1] or target < nums[0]:
            return 0

        def upper(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        def lower(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        first = lower(nums, target)
        if nums[first] != target:
            return 0
        last = upper(nums, target)
        return last - first + 1

if __name__ == "__main__":
    # Valid cases
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    assert solution.countElements(nums, target) == 2
    target = 6
    assert solution.countElements(nums, target) == 0
    nums = [2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12]
    target = 9
    assert solution.countElements(nums, target) == 5
    target = 2
    assert solution.countElements(nums, target) == 2
    target = 3
    assert solution.countElements(nums, target) == 3
    target = 10
    assert solution.countElements(nums, target) == 1
    target = 12
    assert solution.countElements(nums, target) == 2
    nums = [1, 2, 3, 4, 5]
    target = 1
    assert solution.countElements(nums, target) == 1
    target = 2
    assert solution.countElements(nums, target) == 1
    target = 3
    assert solution.countElements(nums, target) == 1
    target = 4
    assert solution.countElements(nums, target) == 1
    target = 5
    assert solution.countElements(nums, target) == 1
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    target = 1
    assert solution.countElements(nums, target) == 9
    nums = [-3, -2, -1, 0, 1, 2, 3]
    target = -3
    assert solution.countElements(nums, target) == 1
    target = -2
    assert solution.countElements(nums, target) == 1
    target = -1
    assert solution.countElements(nums, target) == 1
    target = 0
    assert solution.countElements(nums, target) == 1
    target = 1
    assert solution.countElements(nums, target) == 1
    target = 2
    assert solution.countElements(nums, target) == 1
    target = 3
    assert solution.countElements(nums, target) == 1

    # Target not found cases
    nums = [5, 7, 7, 8, 8, 10]
    target = 9  # Not Found
    assert solution.countElements(nums, target) == 0
    target = 6  # Not Found
    assert solution.countElements(nums, target) == 0
    target = -5  # Too low
    assert solution.countElements(nums, target) == 0
    target = 60  # Too high
    assert solution.countElements(nums, target) == 0

    nums = []  # Empty list
    target = -5  # Empty vector
    assert solution.countElements(nums, target) == 0
    target = 50  # Empty vector
    assert solution.countElements(nums, target) == 0

    nums = [2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12]
    target = 1  # Too low
    assert solution.countElements(nums, target) == 0
    target = 4  # Not found
    assert solution.countElements(nums, target) == 0
    target = 15  # Too high
    assert solution.countElements(nums, target) == 0

    nums = [1, 2, 3, 4, 5]
    target = 0
    assert solution.countElements(nums, target) == 0
    target = 6
    assert solution.countElements(nums, target) == 0

# ---- File: 34_find_first_and_last_position_of_element_in_array\python\original_34.py ----
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]
        if target > nums[-1] or target < nums[0]:
            return [-1, -1]

        def upper(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        def lower(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        first = lower(nums, target)
        if nums[first] != target:
            return [-1, -1]
        last = upper(nums, target)
        return [first, last]


# ---- File: 34_find_first_and_last_position_of_element_in_array\python\second_variant_34.py ----
class Solution:
    def countUnique(self, nums: list[int]) -> int:
        # Should run in O(k * log(N)) complexity, where k is # of unique elements
        if len(nums) == 0:
            return 0

        def upper(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        start = 0
        count = 0
        while start < len(nums):
            end = upper(nums, nums[start])
            start = end + 1
            count += 1

        return count


if __name__ == "__main__":
    solution = Solution()
    # Nonzero Count cases
    nums = [2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12]
    assert solution.countUnique(nums) == 5
    nums = [-3, -2, -1, 0, 1, 2, 3]
    assert solution.countUnique(nums) == 7
    nums = [-3, -3, -3, -2, -2, -2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    assert solution.countUnique(nums) == 7
    nums = [1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 7, 7, 8, 8, 10]
    assert solution.countUnique(nums) == 6
    nums = [19, 19, 19, 19]
    assert solution.countUnique(nums) == 1
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert solution.countUnique(nums) == 1
    nums = [9001]
    assert solution.countUnique(nums) == 1
    nums = [5, 7, 7, 8, 8, 10]
    assert solution.countUnique(nums) == 4
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert solution.countUnique(nums) == 10

    # Zero Count case
    nums = []
    assert solution.countUnique(nums) == 0


# ---- File: 415_add_strings\python\original_415.py ----
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        p1, p2 = len(num1) - 1, len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord("0") if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord("0") if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        return "".join(str(x) for x in res[::-1])


# ---- File: 415_add_strings\python\variant_415.py ----
class Solution:
    def add_string_decimals_415(self, num1: str, num2: str) -> str:
        nums1 = num1.split('.')
        nums2 = num2.split('.')
        decimals1 = nums1[1] if len(nums1) > 1 else ''
        decimals2 = nums2[1] if len(nums2) > 1 else ''

        max_len = max(len(decimals1), len(decimals2))
        decimals1 = decimals1.ljust(max_len, '0')
        decimals2 = decimals2.ljust(max_len, '0')

        carry = [0]
        result = []
        
        def add_strings_415(num1: str, num2: str, carry: list) -> str:
            n1 = len(num1) - 1
            n2 = len(num2) - 1
            result = []
            while n1 >= 0 or n2 >= 0:
                sum = 0
                if n1 >= 0:
                    sum += int(num1[n1])
                    n1 -= 1
                if n2 >= 0:
                    sum += int(num2[n2])
                    n2 -= 1
                sum += carry[0]

                result.append(str(sum % 10))
                carry[0] = sum // 10
            
            return ''.join(result)

        result.append(add_strings_415(decimals1, decimals2, carry))

        if decimals1 or decimals2:
            result.append('.')
        
        result.append(add_strings_415(nums1[0], nums2[0], carry))
        if carry[0]:
            print(carry)
            result.append(str(carry[0]))
        return "".join(result)[::-1]


if __name__ == "__main__":
    solution = Solution()
    # Only Whole Numbers
    assert solution.add_string_decimals_415("11", "123") == "134"
    assert solution.add_string_decimals_415("456", "77") == "533"
    assert solution.add_string_decimals_415("0", "0") == "0"
    assert solution.add_string_decimals_415("0", "2983435243982343") == "2983435243982343"
    assert solution.add_string_decimals_415("99999999", "2983435243982343") == "2983435343982342"
    assert solution.add_string_decimals_415("99999999", "99999999999") == "100099999998"

    # Both Decimals With And Without Carry
    assert solution.add_string_decimals_415("123.53", "11.2") == "134.73"
    assert solution.add_string_decimals_415("687345.3434321", "389457248.24374657243") == "390144593.58717867243"
    assert solution.add_string_decimals_415(".56", ".12") == ".68"
    assert solution.add_string_decimals_415(".5995495049556", ".12") == ".7195495049556"
    assert solution.add_string_decimals_415(".9479823748932", ".716400040030") == "1.6643824149232"
    assert solution.add_string_decimals_415(".00009479823748932", ".000000716400040030") == ".000095514637529350"
    assert solution.add_string_decimals_415(".00009479823748932", ".00000071640004003000000") == ".00009551463752935000000"
    assert solution.add_string_decimals_415("110.12", "9.") == "119.12"
    assert solution.add_string_decimals_415("111111110.0013430430433434454001", "9.") == "111111119.0013430430433434454001"
    assert solution.add_string_decimals_415("111111110.0013430430433434454001", "993483400013438854.") == "993483400124549964.0013430430433434454001"
    assert solution.add_string_decimals_415("910.99999", "999.9999") == "1910.99989"
    assert solution.add_string_decimals_415("999999.99999", "999999.9999") == "1999999.99989"
    assert solution.add_string_decimals_415("123.525", "11.2") == "134.725"
    assert solution.add_string_decimals_415("1234540458475845.", "8348736.") == "1234540466824581"

    # # One Decimal, One Whole Number
    assert solution.add_string_decimals_415("110.75", "9") == "119.75"
    assert solution.add_string_decimals_415("110.75", "9999999") == "10000109.75"
    assert solution.add_string_decimals_415("150423434.00000000000", "9999999.") == "160423433.00000000000"
    assert solution.add_string_decimals_415("150423434.0000009184837483", "9999999.") == "160423433.0000009184837483"
    assert solution.add_string_decimals_415("110.9010479382798527", "9999999.") == "10000109.9010479382798527"


# ---- File: 50_pow_x_n\python\follow_up_50.py ----
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = abs(n)

        result = 1.0
        doubling_val = x
        while n != 0:
            if n % 2 == 1:
                result *= doubling_val
            doubling_val *= doubling_val
            n //= 2

        return result

# ---- File: 50_pow_x_n\python\original_50.py ----
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0 / self.myPow(x, abs(n))
        if n == 0:
            return 1

        result = self.myPow(x, n // 2)

        if n % 2 == 1:
            return x * result * result
        return result * result


# ---- File: 543_diameter_of_a_binary_tree\python\original_543.py ----
from ...utils.treenode import TreeNode

def getDiameter(root: TreeNode | None):
    diameter = 0
    def longestPath(root: TreeNode | None):
        nonlocal diameter
        if not root:
            return 0
        right = longestPath(root.right)
        left = longestPath(root.left)
        diameter = max(diameter, left + right)
        return max(left, right) + 1
    longestPath(root)
    return diameter

# ---- File: 543_diameter_of_a_binary_tree\python\variant_543.py ----
from typing import Optional, List

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def longest_path(node: 'Node'):
            if node is None:
                return 0

            max_height = 0
            second_max_height = 0
            for child in node.children:
                height = longest_path(child)
                if height > max_height:
                    second_max_height = max_height
                    max_height = height
                elif height > second_max_height:
                    second_max_height = height
            nonlocal diameter
            diameter = max(diameter, max_height + second_max_height)
            return max_height + 1

        longest_path(root)

        return diameter

# ---- File: 560_subarray_sum_equals_k\mock\mock_560.py ----
class Solution:
    def has_valid_subarray(self, nums: list[int], target: int) -> bool:
        left = 0
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]

            while sum > target:
                sum -= nums[left]
                left += 1

            if sum == target:
                return True

        return False
    
if __name__ == "__main__":
    solution = Solution()
    assert solution.has_valid_subarray([1, 1, 1], 2)
    assert solution.has_valid_subarray([1, 2, 3], 3)
    # SubarraySum_SecondVariant True
    assert solution.has_valid_subarray([1, 1, 1], 2) == True
    assert solution.has_valid_subarray([1, 2, 3], 3) == True
    assert solution.has_valid_subarray([1, 2, 3, 1, 1, 1], 5) == True
    assert solution.has_valid_subarray([1, 2, 3, 1, 1, 1], 9) == True
    assert solution.has_valid_subarray([5], 5) == True
    assert solution.has_valid_subarray([5], 10) == False
    assert solution.has_valid_subarray([23, 5, 4, 7, 2, 11], 20) == True
    assert solution.has_valid_subarray([1, 3, 5, 23, 2], 8) == True
    assert solution.has_valid_subarray([4, 2, 5, 2, 6, 1], 9) == True
    assert solution.has_valid_subarray([1, 1, 1, 1, 1, 1], 1) == True
    assert solution.has_valid_subarray([1], 1) == True

    # SubarraySum_SecondVariant False
    assert solution.has_valid_subarray([1, 1, 1], 4) == False
    assert solution.has_valid_subarray([1, 2, 3, 4, 5, 6, 7], 100) == False
    assert solution.has_valid_subarray([100, 101, 102, 103], 2) == False
    assert solution.has_valid_subarray([1, 3, 5, 23, 2], 7) == False


# ---- File: 560_subarray_sum_equals_k\python\first_variant_560.py ----
class Solution:
    def subarraySumExists(self, nums: list[int], k: int) -> bool:
        cumulative = 0
        prefix_sums = set([0])
        for num in nums:
            cumulative += num
            if (cumulative - k) in prefix_sums:
                return True
            prefix_sums.add(cumulative)
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.subarraySumExists([1, 1, 1], 2)
    assert not solution.subarraySumExists([1, 4, 7], 3)

    # SubarraySum_FirstVariant True
    assert solution.subarraySumExists([1, 1, 1], 2) == True
    assert solution.subarraySumExists([-1, 2, 3, -4], 0) == True
    assert solution.subarraySumExists([1, 2, 3, 1, 1, 1], 5) == True
    assert solution.subarraySumExists([1, 2, 3, 1, 1, 1], 9) == True
    assert solution.subarraySumExists([3, 4, 7, 2, -3, 1, 4, 2, 1, -14], 7) == True
    assert solution.subarraySumExists([1, 2, 3, -3, 1, 1], 0) == True
    assert solution.subarraySumExists([1, -3, 3, -3, 3, -3], 0) == True
    assert solution.subarraySumExists([1, -3, 3, -6, 8, -3, 4, 5, 6], 8) == True
    assert solution.subarraySumExists([1, -3, 3, -6, 8, -3, 4, 5, 6], -1) == True
    assert solution.subarraySumExists([5], 5) == True
    assert solution.subarraySumExists([5], 10) == False
    assert solution.subarraySumExists([-1, -2, -3, -4], -5) == True
    assert solution.subarraySumExists([-1, -2, -3, -4], -10) == True
    assert solution.subarraySumExists([0, 0, 0, 0, 0], 0) == True
    assert solution.subarraySumExists([8, 3, 6, 1, -5, 10], 10) == True

    # SubarraySum_FirstVariant False
    assert solution.subarraySumExists([1, 1, 1], 4) == False
    assert solution.subarraySumExists([3, 4, 7, 2, -3, 1, 4, 2, 1, -14], -10) == False
    assert solution.subarraySumExists([-1, -2, -3, -4], -15) == False


# ---- File: 560_subarray_sum_equals_k\python\original_560.py ----
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count, cumulative = 0, 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        for num in nums:
            cumulative += num
            if (cumulative - k) in prefix_sums:
                count += prefix_sums[cumulative - k]
            prefix_sums[cumulative] += 1
        return count


# ---- File: 560_subarray_sum_equals_k\python\second_variant_560.py ----
class Solution:
    def subarraySumExistsPositiveNums(self, nums: list[int], k: int) -> bool:
        left, right = 0, 0
        window_sum = 0
        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum > k:
                window_sum -= nums[left]
                left += 1

            if window_sum == k:
                return True
            
        return False

if __name__ == "__main__":
    solution = Solution()
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 2)
    assert solution.subarraySumExistsPositiveNums([1, 2, 3], 3)

    # SubarraySum_SecondVariant True
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 2) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3], 3) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 1, 1, 1], 5) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 1, 1, 1], 9) == True
    assert solution.subarraySumExistsPositiveNums([5], 5) == True
    assert solution.subarraySumExistsPositiveNums([5], 10) == False
    assert solution.subarraySumExistsPositiveNums([23, 5, 4, 7, 2, 11], 20) == True
    assert solution.subarraySumExistsPositiveNums([1, 3, 5, 23, 2], 8) == True
    assert solution.subarraySumExistsPositiveNums([4, 2, 5, 2, 6, 1], 9) == True
    assert solution.subarraySumExistsPositiveNums([1, 1, 1, 1, 1, 1], 1) == True
    assert solution.subarraySumExistsPositiveNums([1], 1) == True

    # SubarraySum_SecondVariant False
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 4) == False
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 4, 5, 6, 7], 100) == False
    assert solution.subarraySumExistsPositiveNums([100, 101, 102, 103], 2) == False
    assert solution.subarraySumExistsPositiveNums([1, 3, 5, 23, 2], 7) == False


# ---- File: 56_merge_intervals\python\original_56_python.py ----
from typing import List

def merge_56_python(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])

    result = []
    for curr_interval in intervals:
        if not result or curr_interval[0] > result[-1][1]:
            result.append(curr_interval)
        else:
            result[-1][1] = max(curr_interval[1], result[-1][1])

    return result

# ---- File: 56_merge_intervals\python\variant_merge_two_lists_56_python.py ----
from typing import List

def try_merge(result: List[List[int]], curr_interval: List[int]):
    if not result or curr_interval[0] > result[-1][1]:
        result.append(curr_interval)
    else:
        result[-1][1] = max(curr_interval[1], result[-1][1])

def merge_2_interval_lists_56_variant_python(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    result = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i][0] <= B[j][0]:
            curr_interval = A[i]
            i += 1
        else:
            curr_interval = B[j]
            j += 1

        try_merge(result, curr_interval)

    if i < len(A):
        while i < len(A):
            try_merge(result, A[i])
            i += 1
    else:
        while j < len(B):
            try_merge(result, B[j])
            j += 1

    return result

if __name__ == "__main__":
    A = [[3, 11], [14, 15], [18, 22], [23, 24], [25, 26]]
    B = [[2, 8], [13, 20]]
    expected = [[2, 11], [13, 22], [23, 24], [25, 26]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

    A = []
    B = [[2, 8], [13, 20]]
    expected = [[2, 8], [13, 20]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

    A = [[1, 5], [10, 15], [20, 25]]
    B = [[5, 10], [15, 20]]
    expected = [[1, 25]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

    A = [[1, 5], [11, 15], [21, 25]]
    B = [[6, 10], [16, 20]]
    expected = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

# ---- File: 65_valid_number\python\original_65.py ----
class Solution(object):
    def isNumber(self, s: str):
        seen_digit, seen_dot, seen_exponent = [False, False, False]
        for i in range(len(s)):
            if s[i].isdigit():
                seen_digit = True
            elif s[i] in {"+", "-"}:
                if i != 0 and s[i - 1] not in {"E", "e"}:
                    return False
            elif s[i] == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif s[i] in {"e", "E"}:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            else:
                return False

        if not seen_digit:
            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isNumber("0089")
    assert solution.isNumber("-0.1")
    assert solution.isNumber("+3.14")
    assert solution.isNumber("4.")
    assert solution.isNumber("-.9")
    assert solution.isNumber("2e10")
    assert solution.isNumber("-90E3")
    assert solution.isNumber("3e+7")
    assert solution.isNumber("+6e-1")
    assert solution.isNumber("53.5e93")
    assert solution.isNumber("-123.456e789")
    assert not solution.isNumber("abc")
    assert not solution.isNumber("1a")
    assert not solution.isNumber("1e")
    assert not solution.isNumber("e3")
    assert not solution.isNumber("99e2.5")
    assert not solution.isNumber("--6")
    assert not solution.isNumber("-+3")
    assert not solution.isNumber("95a54e53")


# ---- File: 65_valid_number\python\variant_65.py ----
class Solution(object):
    def isNumber(self, s: str):
        seen_digit, seen_dot = [False, False]
        for i in range(len(s)):
            if s[i].isdigit():
                seen_digit = True
            elif s[i] in {"+", "-"}:
                if i != 0:
                    return False
            elif s[i] == ".":
                if seen_dot:
                    return False
                seen_dot = True
            else:
                return False

        if not seen_digit:
            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isNumber("0089")
    assert solution.isNumber("-0.1")
    assert solution.isNumber("+3.14")
    assert solution.isNumber("4.")
    assert solution.isNumber("-.9")
    assert solution.isNumber("420")
    assert solution.isNumber("+3")
    assert solution.isNumber("-10")
    assert solution.isNumber("2")
    # Exponents not valid anymore
    assert not solution.isNumber("3e+7")
    assert not solution.isNumber("+6e-1")
    assert not solution.isNumber("53.5e93")
    assert not solution.isNumber("-123.456e789")
    assert not solution.isNumber("abc")
    assert not solution.isNumber("2e10")
    assert not solution.isNumber("-90E3")
    assert not solution.isNumber("1a")
    assert not solution.isNumber("1e")
    assert not solution.isNumber("e3")
    assert not solution.isNumber("99e2.5")
    assert not solution.isNumber("--6")
    assert not solution.isNumber("-+3")
    assert not solution.isNumber("95a54e53")
    assert not solution.isNumber("7..")
    assert not solution.isNumber(".")
    assert not solution.isNumber("3-")
    assert not solution.isNumber("+7e5")
    assert not solution.isNumber("7E5")
    assert not solution.isNumber("7ee")
    assert not solution.isNumber("7e")
    assert not solution.isNumber("8e1.2")
    assert not solution.isNumber("+20e-5")
    assert not solution.isNumber("Abc")


# ---- File: 670_maximum_swap\python\original_670.py ----
class Solution:
    def maximumSwap(self, num: int) -> int:
        right_most = [-1 for _ in range(10)]
        n = list(str(num))

        for i, dig in enumerate(n):
            right_most[int(dig)] = i

        for i, dig in enumerate(n):
            for j in range(9, int(dig), -1):
                if right_most[j] > i:
                    n[right_most[j]], n[i] = n[i], n[right_most[j]]
                    return int("".join(n))

        return num


# ---- File: 670_maximum_swap\python\variant_670.py ----
class Solution:
    def buildSecondLargestNumber(self, num: list[int]) -> list[int]:
        if not num or len(num) == 1:
            return []
        
        freqs = [0 for _ in range(10)]
        for digit in num:
            freqs[digit] += 1

        largest_num = []
        for i in range(9, -1, -1):
            for _ in range(freqs[i]):
                largest_num.append(i)

        for i in range(len(largest_num) - 1, 0, -1):
            if largest_num[i - 1] != largest_num[i]:
                largest_num[i - 1], largest_num[i] = largest_num[i], largest_num[i - 1]
                return largest_num

        return []


if __name__ == "__main__":
    solution = Solution()
    assert solution.buildSecondLargestNumber([2, 7, 3, 6]) == [7, 6, 2, 3]
    assert solution.buildSecondLargestNumber([1, 2, 1, 1, 1]) == [1, 2, 1, 1, 1]

    # MaximumSwap_Variant_BuildSecondLargest True
    assert solution.buildSecondLargestNumber([]) == []
    assert solution.buildSecondLargestNumber([1]) == []
    assert solution.buildSecondLargestNumber([2]) == []
    assert solution.buildSecondLargestNumber([3]) == []
    assert solution.buildSecondLargestNumber([4]) == []
    assert solution.buildSecondLargestNumber([5]) == []
    assert solution.buildSecondLargestNumber([6]) == []
    assert solution.buildSecondLargestNumber([7]) == []
    assert solution.buildSecondLargestNumber([8]) == []
    assert solution.buildSecondLargestNumber([9]) == []
    assert solution.buildSecondLargestNumber([0]) == []

    # Distinct Digits And One Swap
    assert solution.buildSecondLargestNumber([2, 7, 3, 6]) == [7, 6, 2, 3]
    assert solution.buildSecondLargestNumber([2, 3, 4, 1, 8]) == [8, 4, 3, 1, 2]

    # All Duplicate Digits Cannot Build Second Largest
    assert solution.buildSecondLargestNumber([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == []
    assert solution.buildSecondLargestNumber([2, 2]) == []
    assert solution.buildSecondLargestNumber([0, 0, 0, 0, 0, 0]) == []

    # Duplicate Digits And Looped Swap
    assert solution.buildSecondLargestNumber([1, 2, 1, 1, 1]) == [1, 2, 1, 1, 1]
    assert solution.buildSecondLargestNumber([5, 9, 7, 6, 6, 3, 9, 6, 6]) == [9, 9, 7, 6, 6, 6, 6, 3, 5]
    assert solution.buildSecondLargestNumber([5, 9, 7, 6, 6, 3, 9, 6, 6, 3, 3]) == [9, 9, 7, 6, 6, 6, 6, 3, 5, 3, 3]
    assert solution.buildSecondLargestNumber([4, 4, 4, 4, 9, 9, 9, 9, 9]) == [9, 9, 9, 9, 4, 9, 4, 4, 4]

    # Zeroes
    assert solution.buildSecondLargestNumber([0, 0, 0, 0, 0, 6, 0]) == [0, 6, 0, 0, 0, 0, 0]
    assert solution.buildSecondLargestNumber([0, 0, 1, 2, 3, 3]) == [3, 3, 2, 0, 1, 0]
    assert solution.buildSecondLargestNumber([0, 0, 8, 4, 9, 9, 6, 7]) == [9, 9, 8, 7, 6, 0, 4, 0]

# ---- File: 680_valid_palindrome_2\python\original_680_python.py ----

def validPalindrome(s: str) -> bool:
    def check_remaining(s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            return False

        return True

    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue

        return check_remaining(s, left, right - 1) or check_remaining(s, left + 1, right)

    return True



# ---- File: 71_simplify_path\python\first_variant_cwd_cd_71.py ----
class Solution:
    def changeDirectory(self, cwd: str, cd: str) -> str:
        if not cd:
            return cwd
        
        if cd[0] == '/':
            cwd = ''
        
        tokens = []
        for token in cwd.split('/'):
            if token:
                tokens.append(token)
        
        for token in cd.split('/'):
            if not token:
                continue
            if token == '.':
                continue
            elif token == '..':
                if tokens:
                    tokens.pop()
            else:
                tokens.append(token)
        
        if not tokens:
            return '/'
        
        return '/' + '/'.join(tokens)

if __name__ == "__main__":
    solution = Solution()
    assert solution.changeDirectory("/a/b/c", "/d/./e") == "/d/e"
    assert solution.changeDirectory("", "/d/./e") == "/d/e"
    assert solution.changeDirectory("/a/b/c", "") == "/a/b/c"
    assert solution.changeDirectory("/a/b", ".//c/../../d/f") == "/a/d/f"
    assert solution.changeDirectory("/", "foo") == "/foo"
    assert solution.changeDirectory("/", "foo/bar/././xyz///") == "/foo/bar/xyz"
    assert solution.changeDirectory("/baz", "/bar") == "/bar"
    assert solution.changeDirectory("/foo/bar", "../../../../..") == "/"
    assert solution.changeDirectory("/x/y", "../p/../q") == "/x/q"
    assert solution.changeDirectory("/x/y", "/p/./q") == "/p/q"
    assert solution.changeDirectory("/facebook/anin", "../abc/def") == "/facebook/abc/def"
    assert solution.changeDirectory("/facebook/instagram", "../../../../.") == "/"


# ---- File: 71_simplify_path\python\original_71.py ----
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for directory in path.split("/"):
            if directory == "..":
                if len(stack) > 0:
                    stack.pop()
            elif directory and directory != ".":
                stack.append(directory)
        return "/" + "/".join(stack)


# ---- File: 721_accounts_merge\python\original_721.py ----
from typing import List

from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Create adjacency list
        adj = defaultdict(list)
        for account in accounts:
            emails = account[1:]
            canonical = emails[0]
            for email in emails[1:]:
                adj[canonical].append(email)
                adj[email].append(canonical)

        visited = set()

        def dfs(email, same_emails: List[str]):
            visited.add(email)
            same_emails.append(email)
            for nei in adj[email]:
                if nei not in visited:
                    dfs(nei, same_emails)

        # Merge
        merged = []
        for account in accounts:
            emails = account[1:]
            if emails[0] in visited:
                continue
            same_emails = []
            dfs(emails[0], same_emails)
            merged.append([account[0]] + sorted(same_emails))

        return merged


# ---- File: 721_accounts_merge\python\variant_721.py ----
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        def dfs_variant_721(adjs, email_to_id, visited, curr_email, id):
            visited.add(curr_email)
            email_to_id[curr_email] = id
            for adj in adjs.get(curr_email, []):
                if adj not in visited:
                    dfs_variant_721(adjs, email_to_id, visited, adj, id)

        # Create adjacency list
        adjs = {}
        for id, emails in accounts.items():
            first_email = emails[0]
            for email in emails[1:]:
                if first_email not in adjs:
                    adjs[first_email] = []
                if email not in adjs:
                    adjs[email] = []
                adjs[first_email].append(email)
                adjs[email].append(first_email)

        # Helper structures
        email_to_id = {}
        visited = set()
        result = {}

        # Perform DFS and group by connected components
        for id, emails in accounts.items():
            first_email = emails[0]
            if first_email in visited:
                same_id = email_to_id[first_email]
                if same_id not in result:
                    result[same_id] = []
                result[same_id].append(id)
            else:
                result[id] = []
                dfs_variant_721(adjs, email_to_id, visited, first_email, id)

        # Prepare result as a list of lists
        result_v2 = []
        for id, same_ids in result.items():
            same = [id] + same_ids
            result_v2.append(same)

        return result_v2


if __name__ == "__main__":
    # Happy Case
    solution = Solution()
    input_data = {
        "C1": ["a", "b"],
        "C2": ["c"],
        "C3": ["b", "d"],
        "C4": ["d"],
        "C5": ["e"],
        "C6": ["c"],
        "C7": ["a"]
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 3
    assert sorted(result[0]) == sorted(["C1", "C3", "C7", "C4"])
    assert sorted(result[1]) == sorted(["C6", "C2"])
    assert sorted(result[2]) == sorted(["C5"])

    # Actual Email Strings
    input_data = {
        "ID1": ["aa@gmail.com", "bb@gmail.com"],
        "ID2": ["cc@gmail.com"],
        "ID3": ["bb@gmail.com", "dd@gmail.com"],
        "ID4": ["dd@gmail.com"],
        "ID5": ["ee@gmail.com"],
        "ID6": ["cc@gmail.com"],
        "ID7": ["aa@gmail.com"]
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 3
    assert sorted(result[0]) == sorted(["ID3", "ID7", "ID4", "ID1"])
    assert sorted(result[1]) == sorted(["ID2", "ID6"])
    assert sorted(result[2]) == sorted(["ID5"])

    # No Edges
    input_data = {
        "C1": ["a", "b"],
        "C2": ["c"],
        "C3": ["d", "e", "f"],
        "C4": ["g"],
        "C5": ["h"],
        "C6": ["i"],
        "C7": ["j", "k", "l", "m", "n"]
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 7
    assert sorted(result[0]) == sorted(["C1"])
    assert sorted(result[1]) == sorted(["C2"])
    assert sorted(result[2]) == sorted(["C3"])
    assert sorted(result[3]) == sorted(["C4"])
    assert sorted(result[4]) == sorted(["C5"])
    assert sorted(result[5]) == sorted(["C6"])
    assert sorted(result[6]) == sorted(["C7"])

    # One Connected Component Via One Email
    input_data = {
        "C1": ["a", "b"],
        "C2": ["a"],
        "C3": ["d", "a", "f"],
        "C4": ["a"],
        "C5": ["a"],
        "C6": ["a"],
        "C7": ["j", "a", "l", "m", "n"]
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C6", "C1", "C5", "C3", "C7", "C2", "C4"])

    # One Connected Component Via Two Emails
    input_data = {
        "C1": ["a", "b"],
        "C2": ["a"],
        "C3": ["d", "a", "f"],
        "C4": ["a", "x", "y", "z"],
        "C5": ["a"],
        "C6": ["a", "o", "p", "b"],
        "C7": ["j", "a", "l", "m", "n"]
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C6", "C1", "C5", "C3", "C7", "C2", "C4"])

    # One Id One Email
    input_data = {
        "C1": ["a"]
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C1"])

    # One Id Multiple Emails
    input_data = {
        "C1": ["a@gmail.com", "b@gmail.com", "c@gmail.com"]
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C1"])

    # Separate Connected Components
    input_data = {
        "C1": ["a", "b", "c", "d"],
        "C2": ["q", "r", "s", "t"],
        "C10": ["x", "y", "z"]
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 3
    assert sorted(result[0]) == sorted(["C1"])
    assert sorted(result[1]) == sorted(["C2"])
    assert sorted(result[2]) == sorted(["C10"])



# ---- File: 791_custom_sort_string\python\follow_up_791.py ----
class Solution:
    def customSortString(self, order: list[str], s: str) -> str:
        freqs = [0] * 26
        for ch in s:
            freqs[ord(ch) - ord('a')] += 1
        
        result = ""
        for ch in order:
            result += ch * freqs[ord(ch) - ord('a')]
            freqs[ord(ch) - ord('a')] = 0
        
        for i in range(26):
            result += chr(i + ord('a')) * freqs[i]
        
        return result


# ---- File: 791_custom_sort_string\python\original_791.py ----
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        result = []
        for char in order:
            if char in freq:
                result.extend([char] * freq[char])
                freq[char] = 0

        for remaining_char, f in freq.items():
            if f > 0:
                result += [remaining_char] * f

        return "".join(result)


# ---- File: 791_custom_sort_string\python\variant_791.py ----
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = [0 for _ in range(26)]

        def get_index(char: str):
            """Returns index in freq"""
            return ord(char) - ord("a")

        for char in s:
            freq[get_index(char)] += 1

        result = []
        for char in order:
            i = get_index(char)
            if freq[i] > 0:
                result.extend([char] * freq[i])
                freq[i] = 0

        for i, f in enumerate(freq):
            if f > 0:
                result += [chr(ord("a") + i)] * f

        return "".join(result)


# ---- File: 88_merged_sorted_array\python\original_88.py ----
class Solution:
    def mergeSortedArray(self, nums1: list[int], nums2: list[int], m: int, n: int):
        p1 = m - 1
        p2 = n - 1
        for p in range(m + n - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1


# ---- File: 88_merged_sorted_array\python\variant_without_sizes_88.py ----
class Solution:
    def mergeSortedArray(self, nums1: list[int], nums2: list[int]):
        a = len(nums1) // 2 - 1
        b = len(nums2) - 1
        i = len(nums1) - 1
        
        while b >= 0:
            if a >= 0 and nums1[a] >= nums2[b]:
                nums1[i] = nums1[a]
                a -= 1
            else:
                nums1[i] = nums2[b]
                b -= 1
            i -= 1

if __name__ == "__main__":
    solution = Solution()
    list_a = [1, 3, 0, 0]
    list_b = [4, 10]
    expected = [1, 3, 4, 10]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected

    list_a = [5, 6, 7, 8, 0, 0, 0, 0]
    list_b = [1, 2, 3, 4]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected

    list_a = [0]
    list_b = [99]
    expected = [99]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected

    list_a = [1, 10, 0, 0]
    list_b = [2, 11]
    expected = [1, 2, 10, 11]
    solution.mergeSortedArray(list_a, list_b)
    assert list_a == expected


# ---- File: 921_minimum_add_to_make_parentheses_valid\python\original_921.py ----
class Solution:
    def minimumAddToMakeValid(self, s: str) -> int:
        extra_right = 0
        left_open = 0
        for c in s:
            if c == '(':
                left_open += 1
            elif c == ')':
                if left_open == 0:
                    extra_right += 1
                    continue
                left_open -= 1
        return left_open + extra_right


# ---- File: 921_minimum_add_to_make_parentheses_valid\python\variant_921.py ----
class Solution:
    def minimumAddToMakeValid(self, s: str) -> str:
        result = []
        extra_opens = 0
        for c in s:
            if c == '(':
                extra_opens += 1
            elif c == ')':
                if extra_opens == 0:
                    result.append("(")
                else:
                    extra_opens -= 1
            result.append(c)

        
        result += [')'] * extra_opens
        return "".join(result)
    
if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumAddToMakeValid("(())((") == "(())(())"
    assert solution.minimumAddToMakeValid("))(") == "()()()"
    assert solution.minimumAddToMakeValid(")))") == "()()()"
    assert solution.minimumAddToMakeValid("(((") == "((()))"
    assert solution.minimumAddToMakeValid("") == ""
    assert solution.minimumAddToMakeValid("(())") == "(())"
    assert solution.minimumAddToMakeValid(")))(((") == "()()()((()))"
    assert solution.minimumAddToMakeValid("abcxyz") == "abcxyz"
    assert solution.minimumAddToMakeValid("(()()))((") == "(()())()(())"
    assert solution.minimumAddToMakeValid("((a)()))((xyz") == "((a)())()((xyz))"

# ---- File: 938_range_of_sum_bst\python\first_variant_average_938.py ----
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeAverageBST(self, root: Optional[TreeNode], low: int, high: int) -> float:
        result = 0
        count = 0
        stack = [root]
        while stack:
            curr = stack.pop()
            if low <= curr.val <= high:
                result += curr.val
                count += 1
            if curr.right and curr.val < high:
                stack.append(curr.right)
            if curr.left and curr.val > low:
                stack.append(curr.left)
        return result / count

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)

    root.right = TreeNode(15)
    root.right.right = TreeNode(18)

    assert solution.rangeAverageBST(root, 7, 15) == 32.0 / 3.0
    assert solution.rangeAverageBST(root, 0, 9000) == 58.0 / 6.0
    assert solution.rangeAverageBST(root, 7, 7) == 7.0
    assert solution.rangeAverageBST(root, 14, 18) == 33.0 / 2.0
    assert solution.rangeAverageBST(root, 3, 6) == 4.0

# ---- File: 938_range_of_sum_bst\python\original_938.py ----
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        stack = [root]
        while stack:
            curr = stack.pop()
            if low <= curr.val <= high:
                result += curr.val
            if curr.right and curr.val < high:
                stack.append(curr.right)
            if curr.left and curr.val > low:
                stack.append(curr.left)
        return result


# ---- File: 938_range_of_sum_bst\python\second_variant_many_invocations_938.py ----
from typing import Optional
from itertools import accumulate
from bisect import bisect_left


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, root):
        self.vals = []
        self.prefix_sums = []
        self.inorder(root)
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.vals.append(root.val)
        if not self.prefix_sums:
            self.prefix_sums.append(root.val)
        else:
            self.prefix_sums.append(self.prefix_sums[-1] + root.val)
        self.inorder(root.right)
    
    def find_right_boundary(self, left, right, upper):
        while left <= right:
            mid = (right - left) // 2 + left
            if self.vals[mid] <= upper:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    def find_left_boundary(self, left, right, lower):
        while left <= right:
            mid = (right - left) // 2 + left
            if self.vals[mid] >= lower:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def calculate(self, lower, upper):
        right_boundary = self.find_right_boundary(0, len(self.vals) - 1, upper)
        left_boundary = self.find_left_boundary(0, len(self.vals) - 1, lower)
        
        if left_boundary == 0:
            return self.prefix_sums[right_boundary]
        
        return self.prefix_sums[right_boundary] - self.prefix_sums[left_boundary - 1]


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(1)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(6)

    root.right = TreeNode(15)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(18)

    solution = Solution(root)
    assert solution.calculate(5, 16) == 56
    assert solution.calculate(0, 9000) == 1 + 3 + 5 + 6 + 7 + 10 + 13 + 15 + 18
    assert solution.calculate(7, 7) == 7
    assert solution.calculate(14, 18) == 33
    assert solution.calculate(3, 6) == 14

# ---- File: Unknowns\1_draw_circle\python\1_draw_circle.py ----
import math

class DrawCircle:
    def draw_circle(self, radius, n):
        result = []
        steps = n // 2

        for i in range(steps):
            x = (i / steps) * radius
            y = math.sqrt(radius**2 - x**2)

            x = round(x, 2)
            y = round(y, 2)

            result.extend([
                (x, y),
                (x, -y)
            ])

        if n % 2 == 1:
            result.append((radius, 0))
            
        return result

# ---- File: Unknowns\2_skip_list\python\2_skip_list.py ----
from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.top = None
        self.bottom = None

class SkipList:
    def search(self, root: Optional['Node'], target: int) -> bool:
        if root is None:
            return False
        if root.val == target:
            return True
        
        c = root
        while c is not None:
            while c.next is not None and c.next.val <= target:
                c = c.next
                if c.val == target:
                    return True
            c = c.bottom

        return False

# ---- File: Unknowns\2_skip_list\python\2_skip_list_variant.py ----
from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.top = None
        self.bottom = None

class SkipList:
    def search_closest(self, root: Optional['Node'], target: int) -> Optional['Node']:
        if root is None:
            return None
        if root.val == target:
            return root

        c = root
        while c.bottom is not None:
            while c.next is not None and c.next.val <= target:
                c = c.next
                if c.val == target:
                    return c
            c = c.bottom

        while c.next is not None and c.next.val <= target:
            c = c.next
        return c

# ---- File: Unknowns\3_digitsums\python\3_digitsums.py ----
import heapq

class KthSmallestDigitSums:
    def compute(self, num):
        digit_sum = 0
        while num != 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def kth_smallest_digit_sums(self, nums, k):
        max_heap = []

        for num in nums:
            digit_sum = self.compute(num)
            heapq.heappush(max_heap, (-digit_sum, num))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        result = []
        while max_heap:
            _, num = heapq.heappop(max_heap)
            result.append(num)
        return result

# ---- File: Unknowns\3_digitsums\python\3_digitsums_followup.py ----
import heapq

# FOLLOW-UP: What if the order in the output array mattered? It should be sorted in ascending order
# In the case of a tiebreak (of equal digit sums), prioritize the number with the lower index
class KthSmallestDigitSumsFollowup:
    def compute(self, num):
        digit_sum = 0
        while num != 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum
    
    def kth_smallest_digit_sums(self, nums, k):
        max_heap = []

        for index, num in enumerate(nums):
            digit_sum = self.compute(num)
            heapq.heappush(max_heap, (-digit_sum, -index, num))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        result = []
        while max_heap:
            _, _, num = heapq.heappop(max_heap)
            result.append(num)
        result.reverse()
        return result

# ---- File: utils\ListNode.py ----
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ---- File: utils\treenode.py ----
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

