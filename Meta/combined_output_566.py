# ---- File: 1004_max_consecutive_ones_3.py ----
from collections import defaultdict

class Solution:
    def longestOnes(self, nums, k: int) -> int:
        count = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            while count[0] > k:
                count[nums[left]] -= 1
                left += 1
            res = max(right - left + 1, res)

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
    print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

# Sliding window where the number of 0s within it is always less than or equal to k, find max window size

# ---- File: 1011_capacity_to_ship_packages_in_d_days.py ----
class Solution:
    def can_ship(self, weights, days, cap):
        total = 0
        weight_so_far = 0
        for weight in weights:
            if weight_so_far + weight > cap:
                total += 1
                weight_so_far = 0
            weight_so_far += weight
        return total + 1 <= days
    
    def shipWithinDays(self, weights, days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if self.can_ship(weights, days, mid):
                right = mid

            else:
                left = mid + 1

        return left
    
# Binary search between max weights and sum of weights to get the first capacity number that allows shipment within D days

# ---- File: 103_binary_tree_zigzag.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        cur_level = 0
        queue = [(root, 0)]
        res = []
        level_list = []
        while queue:
            node, level = queue.pop(0)
            if level != cur_level:
                res.append(level_list)
                level_list = []
                cur_level = level
            level_list.append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        res.append(level_list)

        for i in range(len(res)):
            if i % 2 != 0:
                res[i] = res[i][::-1]
        return res
    
# Traverse the binary tree by level
# For every odd level, reverse the list


# ---- File: 1060_missing_element_in_sorted_array.py ----
class Solution:
    def missingElement(self, nums, k: int) -> int:
        def missing(idx):
            return nums[idx] - nums[0] - idx

        if k > missing(len(nums) - 1):
            return nums[-1] + k - missing(len(nums) - 1)
            
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if missing(mid) >= k:
                right = mid
            else:
                left = mid + 1
            
        return nums[left - 1] + k - missing(left - 1)
    
# Do binary search to find the first element where the number of missing elements before it >= k. Then the missing element
# is between it and the element before it. Since this previous num has j elements before it missing, and we need to find the kth,
# add k - j to it to get the missing elem.
# Edge case: if k > missing(-1), that means the element is to the right of the array, so account for that.

# ---- File: 1089_duplicate_zeros.py ----
class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.duplicateZeros([1,0,2,3,0,4,5,0]))
# First keep track of the number of 0s in the array.
# Iterate through the array backwards. The number of 0s behind a number is how many positions it's gonna get pushed forward.
# If there's a 0 then we subtract the count and repeat the same process to emulate the duplication

# ---- File: 1091_shortest_path_binary_matrix.py ----
from collections import deque

class Solution:
    def valid(self, grid, r, c):
        n = len(grid)
        return 0 <= r < n and 0 <= c < n
    
    def shortestPathBinaryMatrix(self, grid) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        queue = deque([])
        n = len(grid)
        queue.append((0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, -1), (-1, 1)]
        grid[0][0] = 1
        while queue:
            r, c = queue.popleft()
            if r == n - 1 and c == n - 1:
                return grid[-1][-1]
            for dr, dc in directions:
                new_r = dr + r
                new_c = dc + c
                if self.valid(grid, new_r, new_c) and grid[new_r][new_c] == 0:
                    grid[new_r][new_c] = grid[r][c] + 1
                    queue.append((new_r, new_c))
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPathBinaryMatrix([[0,1],[1,0]]))
    print(sol.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
    print(sol.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
    print(sol.shortestPathBinaryMatrix([[0,0,1,0,1,1],[1,0,0,1,0,0],[0,1,0,1,0,0],[1,0,1,0,0,0],[0,1,0,1,0,0],[0,0,0,0,0,0]]))

# Do BFS to find the shortest path. For each step of the path, mark the square we traverse to the length of the path to get to it to avoid revisiting.

# ---- File: 10_regular_expression_matching.py ----
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.cache = {}
        def dfs(i, j):
            if (i, j) in self.cache: return self.cache[(i, j)]
            if i >= len(s) and j >= len(p): return True
            if j >= len(p): return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                self.cache[(i, j)] = (match and dfs(i + 1, j)) or dfs(i, j + 2)

            elif match:
                self.cache[(i, j)] = dfs(i + 1, j + 1)

            else:
                self.cache[(i, j)] = False
            
            return self.cache[(i, j)]
        
        return dfs(0, 0)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a"))
    print(sol.isMatch("aa", "a*"))
    print(sol.isMatch("ab", ".*"))

# (i, j) represents if we can match the string up to indices i for s and j for p
# We first check if s[i] == p[j] first and mark a flag accordingly.
# Next, we see if p[j + 1] == "*" so we can decide whether to use multiple or none of p[j]
# We only use p[j] if s[i] == p[j]. And if we use it, we move the i pointer forward and keep j because we might match more of p[j]
# If we don't use the *, we move the j pointer forward by 2 to go to the next character.

# If p[j + 1] != "*" then we move both pointers forward since the current characters are equal already
# If none of this happens we return false

# ---- File: 1106_parsing_a_boolean_expression.py ----
class Solution:
    def __init__(self):
        self.index = 0

    def parse(self, expression):
        t_count = f_count = 0
        while self.index < len(expression) and expression[self.index] != ")":
            if expression[self.index] in "&!|":
                operation = expression[self.index]
                self.index += 1
                inner_t, inner_f = self.parse(expression)
                if operation == "&":
                    if inner_f > 0: f_count += 1
                    else: t_count += 1
                elif operation == "!":
                    if inner_f > 0: t_count += 1
                    else: f_count += 1
                else:
                    if inner_t > 0: t_count += 1
                    else: f_count += 1
            elif expression[self.index] == "t":
                t_count += 1
            elif expression[self.index] == "f":
                f_count += 1

            self.index += 1
        return [t_count, f_count]
    def parseBoolExpr(self, expression: str) -> bool:
        if expression == "t" or expression == "f":
            return True if expression == "t" else False
        inner_t, inner_f = self.parse(expression)
        return True if inner_t else False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.parseBoolExpr("&(|(f))"))
    sol = Solution()
    print(sol.parseBoolExpr("|(f,f,f,t)"))
    sol = Solution()
    print(sol.parseBoolExpr("!(&(f,t))"))

# When evaluating an expression, keep track of the number of ts and fs within that expression, so that we may update their number in the outer expression.
# If our operation is & then we evaluate to true if f_count == 0 and false otherwise, for instance

# ---- File: 1110_delete_nodes_and_return_forest.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = set()
        delete = set(to_delete)

        def dfs(root):
            if not root: return None

            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in delete:
                if root.left:
                    roots.add(root.left)
                
                if root.right:
                    roots.add(root.right)

                return None

            return root

        dfs(root)
        if root.val not in delete: roots.add(root)
        return list(roots)
    
# Store final roots in a set. Do postorder traversal so we can get the left and right children before deleting a node.
# If the current node should be deleted, add the left and right children into the roots set if they're not null, then return null so the parent can have the accurate right/left pointers

# ---- File: 113_path_sum_2.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, sum, path):
        if not root: return
        
        sum -= root.val
        path.append(root.val)
        if not sum and not root.left and not root.right:
            self.res.append(list(path))
     
        self.dfs(root.left, sum, path)
        self.dfs(root.right, sum, path)
        
        path.pop()
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.res = []
        self.dfs(root, targetSum, [])
        return self.res

# ---- File: 114_flatten_binary_tree_to_linked_list.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return None
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left:
            left.right = root.right
            root.right = root.left
            root.left = None
        return right or left or root
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)

# After flattening the left subtree, we want to take its tail and connect it to the first node of the right subtree
# After connecting, return the flattened right subtree's tail so that it may be connected. If the right subtree doesn't exist
# then return the left subtree's tail. If neither exists then the root itself is the tail.
        

# ---- File: 116_populating_next_right_pointers.py ----
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        cur_level = 0
        prev = None
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)

            if level != cur_level:
                prev = None
                cur_level = level

            node.next = prev
            prev = node

            if node.right:
                queue.append((node.right, level + 1))
            
            if node.left:
                queue.append((node.left, level + 1))

        return root

# Do BFS traversal and store a previous node indicating the previous node we processed on the same level.
# Every time we traverse to a new level, have prev = None
# Have node.next = prev every time we process a new node, and traverse from right to left on each level so that the rightmost node points to None


# ---- File: 1197_minimum_knight_moves.py ----
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = [(0, 0, 0)]
        directions = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        visited = set()
        visited.add((0, 0))
        while True:
            r, c, dist = queue.pop(0)

            if r == x and c == y:
                return dist

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if (new_r, new_c) in visited:
                    continue

                visited.add((new_r, new_c))
                queue.append((new_r, new_c, dist + 1))

# BFS on the knight

# ---- File: 1209_remove_all_adjacent_duplicates.py ----
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or char != stack[-1][0]:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        return "".join(c * count for c, count in stack)
            
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates("abcd", 2))
    print(sol.removeDuplicates("deeedbbcccbdaa", 3))

# Store the characters and their counts so far in the stack.
# If the stack is empty or the current character is different from the top then add it to the stack
# Otherwise, increment the count. If the count reaches k then pop the stack
# At the end, the string is all of the characters in the stack times their counts


# ---- File: 1216_valid_palindrome_3.py ----
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for d in range(1, n):
            for i in range(n - d):
                j = d + i
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1] >= len(s) - k
    
# It's longest palindromic subsequence but ensure that dp[0][-1] >= len(s) - k, since you can only remove at most k characters from it.

# ---- File: 121_best_time_to_buy_and_sell_stock.py ----
class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n == 1: return 0
        if n == 2: return max(0, prices[1] - prices[0])
        dp = [[-1e9]*2 for i in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return max(dp[-1])
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))
    

# Variables: dp(i, k) being the maximum profit on day i, k = 0 is when you sell the stock on day i, k = 1 is when you buy it.
    
# Base case: dp(0, 0) = 0, dp(0, 1) = -prices[0]
    
# Recurrence relation:
    # dp(i, 0) = max(dp(i-1, 0), dp(i-1, 1) + prices[i])
    # dp(i, 1) = max(dp(i-1, 1), -prices[i]) 

# If you choose to sell the stock, the max profit would be the max of the previous time you sold the stock and the previous time you bought the stock plus the current stock price
# Otherwise, the max profit would be the max of the previous time you bought the stock and your profit if you buy the stock now.

    

# ---- File: 1233_remove_subfolders_from_file_system.py ----
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder):
        root = TrieNode()
        res = set()
        for subfolder in folder:
            cur = root
            directories = subfolder.split("/")
            for ch in directories:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                
                cur = cur.children[ch]

            cur.is_end = True
        
        for subfolder in folder:
            cur = root
            directories = subfolder.split("/")
            path = []
            for ch in directories:
                cur = cur.children[ch]
                path.append(ch)
                if cur.is_end:
                    res.add("/".join(path))
                    break
        return list(res)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))

# ---- File: 1249_min_remove_valid_parentheses.py ----
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_indices = set()
        for (i, ch) in enumerate(s):
            if ch == "(":
                stack.append((ch, i))
            elif ch == ")":
                if not stack:
                    remove_indices.add(i)
                else:
                    stack.pop()
        while stack:
            remove_indices.add(stack.pop()[1])

        res = [s[i] for i in range(len(s)) if i not in remove_indices]
        return "".join(res)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(sol.minRemoveToMakeValid("a)b(c)d"))
    print(sol.minRemoveToMakeValid("))(("))
    
# Use a set to store which indices we don't want to include in our final string.
# Use a stack to store open brackets and their indices. Every time we encounter a closing bracket, it would be paired with the top of the stack,
# which is the closest opening bracket. We pop the opening bracket.
# If the stack is empty, that means there aren't anymore valid opening brackets before the current closing bracket, so we do not want to include it in the final string
# If the stack is still non-empty after iterating through the original string, that means there are some opening brackets that don't have their closing brackets. We
# don't want to include those in the final string either.
# Thus, with all of those indices in consideration, don't include them in the final string

# ---- File: 124_binary_tree_max_path_sum.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res

            if not root: return 0
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)

            res = max(res, root.val + left_max + right_max)

            return root.val + max(left_max, right_max)

        dfs(root)
        return res
    
# At each node, calculate the max path sum of the left and right subtrees.
# We also update the result by maximizing it vs. the sum from combining both paths + the root. However, we discard negative paths
# We return the sum of the root + the max path because when we go to the parent, we cannot account for going through both paths, only 1.

# ---- File: 126_word_ladder_2.py ----
from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList: return []

        L = len(beginWord)
        all_word_combo = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(L):
                inter = word[:i] + "*" + word[i+1:]

                all_word_combo[inter].append(word)
        seen = set()
        seen.add(endWord)
        dq = deque([(endWord, 1)])
        min_paths = defaultdict(int)

        while dq:
            word, distance = dq.popleft()
            for i in range(L):
                inter = word[:i] + "*" + word[i+1:]
                
                for neighbor in all_word_combo[inter]:
                    if neighbor in seen:
                        continue

                    seen.add(neighbor)
                    min_paths[neighbor] = distance + 1
                    dq.append((neighbor, distance + 1))
        
        if beginWord not in min_paths: return []
        visited = set()
        visited.add(beginWord)
        paths = defaultdict(list)
        
        def backtracking(word, path):
            
            if word == endWord:
                paths[len(path)].append(path[:])
                return
            
            for i in range(L):
                inter = word[:i] + "*" + word[i+1:]

                for neighbor in all_word_combo[inter]:
                    if neighbor in visited:
                        continue

                    if len(path) + min_paths[neighbor] > min_paths[beginWord]:
                        continue
                    path.append(neighbor)
                    visited.add(neighbor)
                    backtracking(neighbor, path)
                    path.pop()
                    visited.remove(neighbor)
        
        backtracking(beginWord, [beginWord])
        return paths[min_paths[beginWord]]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(sol.findLadders("cet", "ism", ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim"]))

# For each word, store words it can transform to in a hash table, like a template. For example, abc, abd are stored in ab* together, but not a*c
# Use BFS with the endWord as the starting node, add all words it can transform into in a queue, then find the minimum steps it takes for the neighbor to become endWord

# Do backtracking from beginWord. Avoid using a neighbor where its min steps + the current path length > the min steps of the beginWord

# ---- File: 127_word_ladder.py ----
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        seen = set()
        dq = deque([(beginWord, 1)])
        
        while dq:
            word, distance = dq.popleft()
            if word == endWord: return distance
            for i in range(L):
                inter = word[:i] + "*" + word[i+1:]
                
                for neighbor in all_combo_dict[inter]:
                    if neighbor in seen:
                        continue

                    seen.add(neighbor)
                    dq.append((neighbor, distance + 1))
        return 0
            
# For each word, store words it can transform to in a hash table, like a template. For example, abc, abd are stored in ab* together, but not a*c
# Use BFS with the word as the starting node, add all words it can transform into in a queue, end when we find the endWord

# ---- File: 128_longest_consecutive_sequence.py ----
from collections import defaultdict

class DSU:
    def __init__(self, nums):
        self.size = defaultdict(int)
        self.parent = defaultdict(int)
        for num in nums:
            self.parent[num] = num
            self.size[num] = 1

    def find(self, u):
        if self.parent[u] == u: return u
        return self.find(self.parent[u])
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u != v:
            if self.size[u] > self.size[v]:
                self.parent[v] = u
                self.size[u] += self.size[v]

            else:
                self.parent[u] = v
                self.size[v] += self.size[u]

class Solution:
    def longestConsecutive_B(self, nums) -> int:
        if not nums: return 0
        count = set(nums)
        uf = DSU(nums)
        for num in nums:
            if num + 1 in count:
                uf.union(num, num + 1)
            if num - 1 in count:
                uf.union(num, num - 1)
        res = uf.size.values()
        return max(res)
    
    def longestConsecutive(self, nums) -> int:
        if not nums: return 0
        res = 0
        num_set = set(nums)
        for num in num_set:
            streak = 0
            if num - 1 not in num_set:
                while num in num_set:
                    num += 1
                    streak += 1
                res = max(res, streak)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive([1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3]))

# Do DSU to connect 2 consecutive elements together and find the largest connected component

# Or iterate through every number, check if number - 1 is not in the array, that means it's the start of the consecutive sequence.
# Increment the number until it's not in the array anymore. Find the largest number of times you can increment

# ---- File: 129_sum_root_to_leaf_numbers.py ----
class Solution:
    def dfs(self, root, sum_path):
        if not root: return
        if not root.left and not root.right:
            self.sum += sum_path * 10 + root.val
            return
        
        sum_path = sum_path * 10 + root.val
        self.dfs(root.left, sum_path)
        self.dfs(root.right, sum_path)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.dfs(root, 0)
        return self.sum
    
# The sum path for each node would be the sum path of its parent * 10 + itself. If we reach a leaf node we update the global sum value

# ---- File: 131_palindrome_partitioning.py ----
class Solution:
    def partition(self, s: str):
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True

        for d in range(2, n):
            for i in range(n - d):
                j = i + d
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

        res = []
        def backtracking(index, part):
            if index == len(s):
                res.append(part[:])

            for i in range(index, len(s)):
                if dp[index][i]:
                    part.append(s[index:i + 1])
                    backtracking(i + 1, part)
                    part.pop()
        backtracking(0, [])
        return res

#Do DP to find all of the valid palindromes within s. dp(i, j) = True when s[i:j + 1] is a palindrome
# Do backtracking based on that DP. Only do backtracking based on a substring if the substring is a palindrome


# ---- File: 133_clone_graph.py ----
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, node, visited):
        visited.add(node)
        for neighbor in node.neighbors:
            self.neighbors[node.val].append(neighbor.val)
            if neighbor not in visited:
                self.dfs(neighbor, visited)
            

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        if not node.neighbors: return Node(node.val)
        self.neighbors = defaultdict(list)
        self.dfs(node, set())
        nodes = {key: Node(key) for key in self.neighbors}
        for cur in nodes:
            cur_node = nodes[cur]
            for neighbor in self.neighbors[cur]:
                cur_node.neighbors.append(nodes[neighbor])
        return nodes[node.val]
    
# First we use dfs to store all of the nodes and their neighbors in an easily accessible hash table
# Next, we create new nodes for each key in the hash table
# After that, iterate through each one of those nodes, get its value, and add all of its neighbors to it based on the neighbors hash table

# ---- File: 1344_angle_between_hands_on_a_clock.py ----
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_min_angle = 6
        one_hour_angle = 30
        
        minutes_angle = one_min_angle * minutes
        hour_angle = (hour % 12 + minutes / 60) * one_hour_angle
        
        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)
    
# For every minute, the minute hand goes on 6 degrees
# For every hour, it goes on 30 degrees ontop of the fraction of the minute hand divided by 60, to signify how far along it's gone in an hour.
# Return the absolute minimum difference, including 360 - diff.

# ---- File: 134_gas_station.py ----
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        total = res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1

        return res
    
# The only case where there isn't a solution is where sum(gas) < sum(cost), because you won't have enough to traverse the entire circle
# When gas < cost, we can't go to the next station so we don't want to start at the current. Every time that happens, consider the next station as a potential
# starting point. If we reach the end of the list, the result is the starting station we last updated

# ---- File: 1367_linked_list_in_binary_tree.py ----
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root: return False
        return self.check_path(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def check_path(self, head, root):
        if not head: return True
        if not root: return False

        if head.val != root.val: return False
        return self.check_path(head.next, root.left) or self.check_path(head.next, root.right)
    
# Do DFS starting from every node as the potential start of the linked list. If node.val == head.val then we advance the linked list node. If the list node
# is null then we reached the end of the linked list, so we return true. If they're not equal then that is the end of this traversal.
# If we reach the end of the tree while the linked list is still going then return false


# ---- File: 136_single_number.py ----
class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res
        
# XOR of 2 of the same numbers = 0

# ---- File: 1371_longest_substring_even_vowels.py ----
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        res = 0
        mask = 0
        mask_index = {0: -1}
        for (i, ch) in enumerate(s):
            if ch in vowels:
                mask ^= vowels[ch]
            
            if mask in mask_index:
                res = max(res, i - mask_index[mask])
            else:
                mask_index[mask] = i
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheLongestSubstring("eleetminicoworoep"))
    print(sol.findTheLongestSubstring("leetcodeisgreat"))
    print(sol.findTheLongestSubstring("bcbcbc"))

# Use a bitmask of length 5 to represent the state of a prefix.
# The bitmask represents if the prefix has an even count for each vowel, with 0 being odd and 1 being even. For example, 00001 means "a" has an odd count and the rest have even counts.
# Ideally, we want to find the longest subarray with bitmask 00000
# Otherwise, if there are 2 prefixes with the same bitmask, then the middle subarray has bitmask 00000.

# ---- File: 137_single_number_2.py ----
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Initialize seen_once and seen_twice to 0
        seen_once = seen_twice = 0

        # Iterate through nums
        for num in nums:
            # Update using derived equations
            seen_once = (seen_once ^ num) & (~seen_twice)
            seen_twice = (seen_twice ^ num) & (~seen_once)

        # Return integer which appears exactly once
        return seen_once
    
# Keep track of 2 bitmasks: seen_once and seen_twice, to track the number of times a number has appeared.
# Every time we see a number, xor its bits with seen_once. If it's the first time we see that number then its bits
# will be 1 in seen_once. If it's the second time then they will be 0, and seen_twice would reflect that.
# If it's the third, both seen_once and seen_twice would be 0 for those bits. We and them with the inverse of the other mask
# so that the bits only appear once in either mask.

# ---- File: 138_copy_list_random_pointer.py ----
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def clone(self, node):
        if node:
            if node not in self.visited:
                self.visited[node] = Node(node.val, None, None)
            return self.visited[node]
        return None
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        old = head
        new = Node(old.val, None, None)
        self.visited = {old: new}

        while old:
            new_next = self.clone(old.next)
            new_random = self.clone(old.random)

            new.next = new_next
            new.random = new_random

            new = new.next
            old = old.next
        return self.visited[head]
    
# For each node in the original list, we store the new node with the old as the key in a hash table
# Each time we clone the old node, we want to potentially create 2 new nodes corresponding to its next and random pointers.
# We store these nodes in the hash table as well, and have the next and random pointers of the new node point to them.


# ---- File: 139_word_break.py ----
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False]*n

        for i in range(n):
            for word in wordDict:
                if i + 1 - len(word) < 0: continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1:i+1] == word:
                        dp[i] = True
                        break

        return dp[-1]
    
    def wordBreak_trie(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False]*n
        root = TrieNode()
        for word in wordDict:
            cur = root
            for i in range(len(word)):
                ch = word[i]
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()

                cur = cur.children[ch]
            cur.is_end = True
            
        for i in range(n):
            if i == 0 or dp[i - 1]:
                cur = root
                for j in range(i, n):
                    ch = s[j]

                    if ch not in cur.children:
                        break

                    cur = cur.children[ch]

                    if cur.is_end:
                        dp[j] = True
        
        print(dp)
        return dp[-1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak_trie("leetcode", ["leet","code"]))

# DP without trie:
# DP(i) = whether you can segment s[:i + 1] into words in the dictionary.
# If we reach i, we check every word in the dictionary and subtract its length from i. If we were able to segment without that word included, then DP(i) = true.
# DP(i) = DP(i - word_len) for word in wordDict if s[i - word_len + 1:i + 1] == word

# With trie:
# If we reach i, we traverse the trie staring from s[i]. If we're able to reach the end of the trie, that means the substring from s[i] to some s[j] can be segmented.
# Thus, DP(j) = true. We only traverse the trie if DP(i - 1) = true because then, s[i] could be the start of the next valid segment.


# ---- File: 140_word_break_2.py ----
class Solution:
    def wordBreak(self, s, wordDict):
        res = []
        def backtracking(start, sentence):
            if start == len(s):
                res.append(" ".join(sentence))
                return
            
            for i in range(start, len(s)):
                substring = s[start:i + 1]
                if substring in wordDict:
                    sentence.append(substring)

                    backtracking(i + 1, sentence)
                    sentence.pop()

        backtracking(0, [])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
    print(sol.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
        
# Do backtracking. For every start index, attempt to expand the end index and see if the formed word is within the dictionary.
# If so, add the word into the sentence and move the start index to be after the end index
# If start == len(s) then we reached the end of s and all of the previously added words are part of the dictionary, so we add the sentence into result

# ---- File: 1424_diagonal_traverse_2.py ----
class Solution:
    def findDiagonalOrder(self, nums):
        queue = []
        queue.append((0, 0))
        visited = set((0, 0))
        res = []
        while queue:
            r, c = queue.pop(0)
            res.append(nums[r][c])

            for dr, dc in [(1,0), (0, 1)]:
                new_r = r + dr
                new_c = c + dc

                if new_r < len(nums) and new_c < len(nums[new_r]) and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))


# Do BFS traversal but add the cell below before adding the cell to the right.

# ---- File: 142_linked_list_cycle_2.py ----
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findIntersection(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        intersect = self.findIntersection(head)
        if not intersect: return None

        p1 = head
        p2 = intersect
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
    
# Use the tortoise and hare algorith mto see if there's a cycle, if yes then return the point in which they meet in the cycle
# Call this point x
# Say that before entering the cycle, the tortoise walks A steps, and walks another B before meeting the hare. In the cycle, the hare walks A + B + k*c steps, 
# with k being the number of times it goes through the cycle, and c being the cycle length
# Since the tortoise walked A + B steps, the hare walked 2(A + B) steps since it's twice as fast, and 2(A + B) = A + B + k * c  <-> A + B = k * c
# Currently the tortoise is B steps away from the cycle entrance, so it needs to walk A more steps to make it back to the cycle entrance because A + B = k * c
# Thus, we move the hare back to the beginning, and have it walk A steps as well to meet the tortoise again. The point they meet is the cycle entrance 

# ---- File: 1438_longest_cont_subarray_absolute_diff.py ----
import heapq
from collections import deque

class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        max_heap = []
        min_heap = []
        removed = set()

        left = 0
        res = 1
        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))

            while (-max_heap[0][0] - min_heap[0][0]) > limit:
                removed.add(left)
                left += 1
                while max_heap and max_heap[0][1] in removed:
                    heapq.heappop(max_heap)

                while min_heap and min_heap[0][1] in removed:
                    heapq.heappop(min_heap)
            
            res = max(right - left + 1, res)

        return res
    
    def longestSubarray(self, nums, limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        res = 1
        for right in range(len(nums)):
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()

            max_deque.append(right)

            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()

            min_deque.append(right)
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque and max_deque[0] == left:
                    max_deque.popleft()
                
                if min_deque and min_deque[0] == left:
                    min_deque.popleft()
                left += 1
                
            
            res = max(right - left + 1, res)

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubarray([8,2,4,7], 4))
    print(sol.longestSubarray([10,1,2,4,7,2], 5))
    print(sol.longestSubarray([4,2,2,2,4,4,2,2], 0))

# Similar to Sliding Window Maximum, keep mono increasing + decreasing deques to store the max/min for a sliding window.
# Increase the window size until the difference between the front of these 2 deques is larger than the limit.
# Then, move the left pointer rightward and pop the deques if the left index matches the fronts

# ---- File: 143_reorder_list.py ----
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        first = head
        second = prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

# Do the tortoise and hare node trick
# The intuition is that the final list is the first half intertwined with the second half reversed
# So we go to the halfway point of the list, and reverse the second half.
# The tail of the first half is still connected to its next node, which is now the tail of the second half.
# Iterate through the lists to set the appropriate next pointer. We do not need to worry about the second half's tail since either
# the first half's tail or the second half's tail's before woul be connected to it still, depending on the length of the linked list.

# ---- File: 146_lru_cache.py ----
from collections import defaultdict

class DoublyLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoublyLinkedList(0, 0)
        self.tail = DoublyLinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = defaultdict(int)
    
    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)


    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node: return -1
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)

        if not node:
            new_node = DoublyLinkedList(key, value)
            self.cache[key] = new_node
            self.add_node(new_node)
            self.capacity -= 1
            if self.capacity < 0:
                last = self.tail.prev
                self.remove_node(last)
                self.cache.pop(last.key)
                self.capacity += 1
        else:
            node.val = value
            self.move_to_head(node)
        
# Use a doubly linked list to store the usage of the keys. Head means most recently used, tail means least recently used.
# Use a hash table to store the nodes for retrieval in O(1).

# Each time a node is interacted with, it gets moved to the front of the linked list
# For the get function, we check if the node exists first. If so, move it to the head, otherwise return -1
# For the put function, we check if the node exists first. If so, update its value and move it to the head.
# Otherwise, create a new node, store it in the hash map. If adding the node exceeds the capacity, pop the tail node.


# ---- File: 1497_array_pairs_divisible_by_k.py ----
from collections import defaultdict

class Solution:
    def canArrange(self, arr, k: int) -> bool:
        mod_freq = defaultdict(int)
        for num in arr:
            mod_freq[num % k] += 1
        for i in range(1, k):
            if mod_freq[i] != mod_freq[k - i]: return False
        if 0 in mod_freq: return mod_freq[0] % 2 == 0
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.canArrange([1,2,3,4,5,10,6,7,8,9], 5))
    print(sol.canArrange([1,2,3,4,5,6], 7))
    print(sol.canArrange([1,2,3,4,5,6], 10))

# Store all the modulos by k for each number in a hash table. If freq[i] != freq[k - i] then return false because all of those numbers are supposed to be paired with each other.
# If 0 is a modulo then we can't compare with freq[k], so we have to see if it's even or not.


# ---- File: 150_evaluate_reverse_polish_notation.py ----
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for ch in tokens:
            if ch in "+-/*":
                num1 = stack.pop()
                num2 = stack.pop()
                if ch == "+":
                    result = num1 + num2
                elif ch == "-":
                    result = num2 - num1
                elif ch == "*":
                    result = num1 * num2
                else:
                    result = int(num2 / num1)

                stack.append(result)
            else:
                stack.append(int(ch))

        return stack.pop()

if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["2","1","+","3","*"]))
    print(sol.evalRPN(["4","13","5","/","+"]))

# Store the results in a stack. Every time we see an operation, pop the 2 elements at the top and do the appropriate operation, and push into stack.


# ---- File: 152_maximum_product_subarray.py ----
class Solution:
    def maxProduct(self, nums) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        res = max_prod
        for num in nums[1:]:
            max_prod, min_prod = max(num, max_prod*num, min_prod*num), min(num, min_prod*num, max_prod*num)
            res = max(max_prod, res)
        return res
    
# Similar to Kadane's algo, have 2 variables saving the maximum and minimum products
# The maximum product is the max of the current num, the previous max product * the current num, and the previous min product * the current num
# Current num: the previous product could be negative whereas the current is positive, so the current num would be the best pick
# Max product * cur num: the previous product is positive and cur is positive, so we could maximize
# Min product * cur_num: the previous product is negative and cur is negative, so we could maximize

# ---- File: 1539_kth_missing_positive_number.py ----
class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            missing = arr[mid] - mid - 1

            if missing >= k:
                right = mid
            else:
                left = mid + 1
        missing = arr[left] - left - 1
        if missing < k:
            return k + left + 1

        return k + left

# To do this in less than O(N), use binary search to find the lowest M such that the number of missing integers to the left of arr[M] >= k. missing[M] = arr[M] - M - 1
# If the number of missing integers to the left of a number is less than k then we need to check the right part of the array, and left otherwise.
# Once we have M, the missing integer is either between M - 1 and M or after M
# We compare the missing integers to the left of M with k. If k is larger, then it's after M.
# The formula is arr[M] + (k - missing[M - 1]) = arr[M] + (k - arr[M] + M + 1) = k + M + 1
# If k is smaller then it's before M. The formula is arr[M - 1] + (k - missing[M - 1]) = arr[M - 1] + (k - arr[M - 1] + M + 1 - 1) = k + M


# ---- File: 153_find_min_in_rotated_sorted_array.py ----
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
    
# Find the smallest k such that nums[k] <= nums[-1]

# ---- File: 1545_find_kth_bit_in_nth_binary_string.py ----
reverse = {"0": "1", "1": "0"}

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        length = 2 ** n
        if k == length // 2:
            return "1"
        
        if k < length // 2:
            return self.findKthBit(n - 1, k)
        
        mirrored_k = length - k
        rev = reverse[self.findKthBit(n - 1, mirrored_k)]
        return rev
        

# For every bit, its mirror through the center point of the string would be its inverse
# We can utilize this to account for previous results
# If a bit is on the left half of the string, find its position in the n - 1 string.
# If a bit is on the right half, return the inverse of its mirror position in the n - 1 string.
# If a bit is in the middle, return "1".
# If n == 1, return "0"

# ---- File: 1570_dot_product_sparse_vectors.py ----
class SparseVector:
    def __init__(self, nums):
        self.nonzeros = []
        for (i, num) in enumerate(nums):
            if num:
                self.nonzeros.append((i, num))
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ptr1 = ptr2 = 0
        res = 0
        while ptr1 < len(self.nonzeros) and ptr2 < len(vec.nonzeros):
            if self.nonzeros[ptr1][0] == vec.nonzeros[ptr2][0]:
                res += self.nonzeros[ptr1][1] * vec.nonzeros[ptr2][1]
                ptr1 += 1
                ptr2 += 1
            
            elif self.nonzeros[ptr1][0] < vec.nonzeros[ptr2][0]:
                ptr1 += 1

            elif self.nonzeros[ptr1][0] > vec.nonzeros[ptr2][0]:
                ptr2 += 1

        return res

# Store the nonzeros of a sparse vector in a hash map because it's the most efficient.
# When calculating the dot product, take the current hash map and see if any of the indices exist in the other vector's nonzeros hash map,
# then multiply accordingly.

# Alternatively, store (index, value) tuples in a list for nonzero values and use 2 pointers to traverse both vectors. Make sure the indices are equal at all times



# ---- File: 1574_shortest_subarray_to_remove_to_make_array_sorted.py ----
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        r = N - 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1

        l = 0
        res = r
        while l < r:
            while r < N and arr[l] > arr[r]:
                r += 1

            res = min(res, r - l - 1)
            if arr[l] > arr[l + 1]:
                break
            l += 1
        return res 
    
# First consider that we might remove the prefix of the array, so move the right pointer to be the first element of the non-decreasing suffix.
# Initialize a left pointer and consider removing everything between it and right. We still need to maintain the fact that arr[l] > arr[r] to merge them,
# so increment r until that's true. If the element after l is less than it, break. Otherwise, increment left

# ---- File: 1590_make_sum_divisible_by_p.py ----
from collections import defaultdict

class Solution:
    def minSubarray(self, nums, p: int) -> int:
        total = sum(nums)
        if total % p == 0: return 0

        target = total % p
        pref_sum = 0
        n = len(nums) 
        removed = n
        modulo_table = defaultdict(int)
        modulo_table[0] = -1
        for (i, num) in enumerate(nums):
            pref_sum = (pref_sum + num) % p
            needed = (pref_sum - target) % p
            if needed in modulo_table:
                removed = min(i - modulo_table[needed], removed)

            modulo_table[pref_sum] = i

        return removed if removed != n else -1 
    
# First, calculate the sum of the array, and take its remainder when divided by p, call it target.
# In order for the sum to be divisible by p, we have to remove the smallest subarray whose sum % p = target
# So let's say the subarray up to index i and index j with j > i has the subarray between from i + 1 to j, and its sum % p = target.
# So its sum is (sum[j] - sum[i]) % p == target. So if we want to find that (i + 1, j) subarray, we remove the prefix subarray until i.
# To find it, its prefix sum is (sum[j] - target + p) % p. Thus, we also use a hash table to store the prefix sums and their last appearances.




# ---- File: 1593_split_string_into_max_unique_substrings.py ----
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0

        def backtracking(index, substrings):
            nonlocal res
            if len(substrings) + (len(s) - index) <= res:
                return
            if index == len(s):
                res = max(res, len(substrings))
                return
            
            for i in range(index, len(s)):
                substr = s[index:i + 1]
                if substr not in substrings:
                    substrings.add(substr)
                    backtracking(i + 1, substrings)
                    substrings.remove(substr)

        backtracking(0, set())
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxUniqueSplit("ababccc"))
    print(sol.maxUniqueSplit("aba"))

# Do backtracking to get every possible combination of substrings, while storing them in a set
# If a substring is already in the set, skip over it. Otherwise, add it onto the set and recurse on the index after

# Optimization:
# At any point start, the maximum number of remaining substrings is len(s) - start, because we consider every letter to be a possible substring
# If our current count + the max number of remaining substrings is < max_count, then there's no point in continuing down that path



# ---- File: 15_3sum.py ----
class Solution:
    def threeSum(self, nums):
        res = set()
        dupes = set()
        
        for i in range(len(nums)):
            if nums[i] not in dupes:
                dupes.add(nums[i])
                hash_set = {}
                for j in range(i + 1, len(nums)):
                    target = -nums[i] - nums[j]
                    if nums[j] in hash_set:
                        res.add(tuple(sorted([nums[i], nums[j], target])))
                    hash_set[target] = nums[j]
        return res
    
    def threeSum_sort(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i == 0 or nums[i] != nums[i - 1]:
                L = i + 1
                R = len(nums) - 1
                
                while L < R:
                    target = nums[i] + nums[L] + nums[R]
                    if target == 0:
                        res.append((nums[i], nums[L], nums[R]))
                        L += 1
                        R -= 1
                        while L < R and nums[L] == nums[L - 1]:
                            L += 1
                    
                    elif target < 0:
                        L += 1
                    
                    else:
                        R -= 1

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum_sort([-1,0,1,2,-1,-4]))

# Approach 1: Sort the array and do 2sum 2 on the rest
# 2sum 2 relies on the array being sorted. We fix an index and do 2sum 2 on the right side of it.
# If the sum of the 3 numbers is negative, then we need to move the left pointer to increase it and vice versa.
# If the sum is 0, then we add it to the result and shrink the window
# We want to handle duplicates as well. If the first index is the same as the previous index then there's no point in processing the same thing again if we only care about the numbers
# If the left pointer is the same as the left pointer - 1 then we keep increasing it because there's no point in processing the same thing again.

# Approach 2: Fix an index and do 2sum on the rest
# Fix an index and do 2sum on the right side of it with a hash map with the target being the negative value of the first index.
# Avoid duplicates by checking if we've already seen the first index

# ---- File: 1609_even_odd_trees.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            prev = 1e9
            for i in range(len(queue)):
                node = queue.pop(0)

                if level % 2 == 0:
                    if node.val % 2 == 0: return False
                    if prev != 1e9 and node.val <= prev: return False
                else:
                    if node.val % 2 != 0: return False
                    if prev != 1e9 and node.val >= prev: return False

                prev = node.val
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            level += 1

        return True
    
# Do BFS to traverse every level. Store the previous node's value
# If the level is even, and the node's value isn't odd or its value is no more than the previous, return false
# If the level is odd, and the node's value isn't even or its value is no less than the previous, return false
# Only compare with the previous value if it's not the first node of the level

# ---- File: 162_find_peak_element.py ----
class Solution:
    def bin_search(self, nums, l, r):
        m = (l + r) // 2
        if m == 0 and nums[m] > nums[m + 1]: return m
        if m == len(nums) - 1 and nums[m] > nums[ m - 1]: return m
        if nums[m - 1] < nums[m] and nums[m] > nums[m + 1]: return m
        if nums[m] < nums[m + 1]: return self.bin_search(nums, m + 1, r)
        return self.bin_search(nums, l, m - 1)
    
    def findPeakElement(self, nums) -> int:
        if len(nums) == 1: return 0
        return self.bin_search(nums, 0, len(nums) - 1)
    
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1,2,3,1]))
    print(sol.findPeakElement([1,2,1,3,5,6,4]))
    print(sol.findPeakElement([1,2]))

# Use binary search. If the middle element is in an increasing trend then a peak element has to be to the right. Otherwise, it's to the left.

# ---- File: 163_missing_ranges.py ----
class Solution:
    def findMissingRanges(self, nums, lower: int, upper: int):
        if not nums: return [[lower, upper]]
        low = []
        high = []
        if lower < nums[0]: low = [lower, nums[0] - 1]
        if upper > nums[-1]: high = [nums[-1] + 1, upper]
        res = []
        if low: res.append(low)

        for i in range(len(nums) - 1):
            start, end = nums[i] + 1, nums[i + 1] - 1
            if start > end: continue
            if start <= lower <= end or start <= upper <= end or lower <= start <= upper or lower <= end <= upper:
                res.append([max(start, lower), min(upper, end)])

        if high: res.append(high)
        return res
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMissingRanges([0,1,3,50,75], 0, 99))
    print(sol.findMissingRanges([-1], -1, -1))

# Each pair of consecutive indices is an interval (start, end).
# If (lower, upper) and that interval overlap, the missing range is (max(start + 1, lower), min(end - 1, upper)) since we don't want to include start/end, just the overlap.

# ---- File: 1650_LCA_binary_tree.py ----
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
        p_path = defaultdict(int)
        q_path = defaultdict(int)
        p_ptr, q_ptr = p, q
        while p_ptr:
            p_path[p_ptr.val] = p_ptr
            p_ptr = p_ptr.parent
        
        while q_ptr:
            q_path[q_ptr.val] = q_ptr
            q_ptr = q_ptr.parent

        for ptr in p_path:
            if ptr in q_path: return p_path[ptr]

# Trace the paths for each node going to the root. See which one is in common first.

# ---- File: 167_2sum_2.py ----
class Solution:
    def twoSum(self, numbers, target: int):
        L = 0
        R = len(numbers) - 1
        while L < R:
            sum = numbers[L] + numbers[R]
            if sum == target:
                return [L + 1, R + 1]

            elif sum < target:
                L += 1
            else:
                R -= 1

# ---- File: 16_3sum_closest.py ----
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = 1e9
        res = 0
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return sum
                
                diff = abs(target - sum)
                if min_diff > diff:
                    res = sum
                    min_diff = diff

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1,2,1,-4], 1))
    print(sol.threeSumClosest([0,0,0], 1))

# ---- File: 173_BST_iterator.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def left_traversal(self, node):
        self.stack.append(node)
        while node.left:
            self.stack.append(node.left)
            node = node.left

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.left_traversal(root)

    def next(self) -> int:
        top = self.stack.pop()

        if top.right:
            self.left_traversal(top.right)
        return top.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Use a stack to store a subtree at all times to use only O(H) space.
# Append all the left nodes, and when we pop them, check if a right child exists, and append itself and its left subtree.

# ---- File: 1762_building_with_ocean_view.py ----
class Solution:
    def findBuildings(self, heights):
        stack = []
        bad_indices = set()
        for (i, height) in enumerate(heights):
            while stack and stack[-1][1] <= height:
                index, hght = stack.pop()
                bad_indices.add(index)
            stack.append((i, height))

        res = [i for i in range(len(heights)) if i not in bad_indices]
        return res
    
    def findBuildings(self, heights: List[int]) -> List[int]:
        cur_max = -1
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if cur_max < heights[i]:
                cur_max = heights[i]
                res.append(i)

        return res[::-1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findBuildings([4,2,3,1]))
    print(sol.findBuildings([4, 3, 2, 1]))
    print(sol.findBuildings([1, 3, 2, 4]))

# We use a monotonically decreasing stack to keep track of valid buildings.
# Buildings that never get popped out of the stack are ones whose right neighbors aren't taller than them


# ---- File: 1778_shortest_path_in_hidden_grid.py ----
# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        visited = set()
        inverse = {"U": "D", "D": "U", "L": "R", "R": "L"}
        directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        target = None
        def dfs(r, c):
            nonlocal target
            if master.isTarget():
                target = (r, c)
            
            visited.add((r, c))

            for d in directions:
                new_r, new_c = r + directions[d][0], c + directions[d][1]
                if (new_r, new_c) not in visited and master.canMove(d):
                    master.move(d)
                    dfs(new_r, new_c)
                    master.move(inverse[d])
        dfs(0, 0)
        if not target: return -1

        queue = [(0, 0, 0)]
        while queue:
            r, c, dist = queue.pop(0)
            
            if (r, c) == target: return dist
            for d in directions:
                new_r, new_c = r + directions[d][0], c + directions[d][1]
                if (new_r, new_c) in visited:
                    visited.remove((new_r, new_c))
                    queue.append((new_r, new_c, dist + 1))
        return -1

                
# First do DFS to mark every grid the robot can traverse to and make sure it can reach the target
# Then do BFS to go through every traverseable cell until you reach the target

# ---- File: 179_largest_number.py ----
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums) -> str:
        def compare(str1, str2):
            combine_1 = str1 + str2
            combine_2 = str2 + str1
            if combine_1 > combine_2:
                return -1
            elif combine_1 < combine_2:
                return 1
            return 0
        
        str_nums = sorted([str(num) for num in nums], key=cmp_to_key(compare))
        res = "".join(str_nums)
        trail_zero = -1
        for i in range(len(res) - 1):
            if res[i] == "0":
                trail_zero = i
            else:
                break
        return res[trail_zero + 1:]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestNumber([10,2]))
    print(sol.largestNumber([3,30,34,5,9]))

# First convert all of the numbers into strings for easier comparison and we want to return a string at the end anywya
# When comparing between 2 strings and seeing what should be put first, just compare the results from combining both strings with 1 before the other and
# use that as the custom comparator function

# ---- File: 17_letter_combinations_phone.py ----
class Solution:
    def letterCombinations(self, digits: str):
        if not digits: return []
        digit_letters =  {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                          "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def backtracking(index = 0, combination = []):
            if index == len(digits):
                res.append("".join(combination))
                return
            
            for ch in digit_letters[digits[index]]:
                combination.append(ch)
                backtracking(index + 1, combination)
                combination.pop()

        backtracking()
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))
    print(sol.letterCombinations(""))
    print(sol.letterCombinations("2"))

# Use the backtracking algorithm
# For each digit, go through every possible letter it can be, and move onto the next index and repeat the process until the end of the array.
# Then we move back and try another combination

# ---- File: 1845_seat_reservation_manager.py ----
import heapq

class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        self.ptr = 1

    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        
        seat = self.ptr
        self.ptr += 1
        return seat
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

# Use a heap to keep track of the smallest unreserved seat
# Use a pointer to move to the next unreserved seat

# ---- File: 1868_product_of_2_rle_arrays.py ----
class Solution:
    def findRLEArray(self, encoded1, encoded2):
        ptr1 = ptr2 = 0
        res =  []
        prev_prod = None
        count = 0
        while ptr1 < len(encoded1) and ptr2 < len(encoded2):
            prod = encoded1[ptr1][0] * encoded2[ptr2][0]
            min_count = min(encoded1[ptr1][1], encoded2[ptr2][1])
            if encoded1[ptr1][1] == encoded2[ptr2][1]:
                ptr1 += 1
                ptr2 += 1
            
            elif min_count == encoded2[ptr2][1]:
                ptr2 += 1
                encoded1[ptr1][1] -= min_count

            else:
                ptr1 += 1
                encoded2[ptr2][1] -= min_count
            
            if prev_prod and prod != prev_prod:
                res.append([prev_prod, count])
                count = 0

            prev_prod = prod
            count += min_count
        
        res.append([prev_prod, count])
        return res
    
# Store 2 pointers to traverse through both arrays.
# If the count in 1 array is smaller than the other, then increment the pointer of that array, and subtract the count of the other by the count.
# If both counts are equal then increment both pointers.
# Once we have the min count, that's the number of times that product will be in the final array.
# If we encounter a different product than the one from before, reset the count and append the previous product and its count into the result

             

# ---- File: 1891_cutting_ribbons.py ----
class Solution:
    def cuttable(self, ribbons, length, k):
        count = 0
        for ribbon in ribbons:
            count += ribbon // length
        return count >= k
    def maxLength(self, ribbons, k: int) -> int:
        left = 1
        right = max(ribbons) + 1

        while left < right:
            mid = (left + right) // 2
            if not self.cuttable(ribbons, mid, k):
                right = mid
            else:
                left = mid + 1

        return left - 1
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxLength([9,7,5], 3))
    print(sol.maxLength([7, 5, 9], 4))
    print(sol.maxLength([5, 7, 9], 22))

# Since we're finding the maximum ribbon length such that we can cut at least k ribbons, do binary search to find the
# smallest ribbon length such that we can't cut k ribbons, and minus 1. The search space should be 1 to the max ribbon length + 1 because we're subtracting 1
# at the end, and the result could be the actual max ribbon length of the original ribbons array

# ---- File: 18_4sum.py ----
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, n):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        L = j + 1
                        R = n - 1

                        while L < R:
                            sum_nums = nums[i] + nums[j] + nums[L] + nums[R]
                            if sum_nums == target:
                                res.append((nums[i], nums[j], nums[L], nums[R]))
                                L += 1
                                R -= 1
                                while L < R and nums[L] == nums[L - 1]:
                                    L += 1
                            
                            elif sum_nums < target:
                                L += 1
                            
                            else:
                                R -= 1

        return res
    
# 3Sum with extra steps

# ---- File: 198_house_robber.py ----
class Solution:
    def rob_2(self, nums) -> int:
        n = len(nums)
        dp = [[0 for i in range(2)] for j in range(n)]
        dp[0][1] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[-1])
    
    def rob(self, nums) -> int:
        n = len(nums)
        not_rob, rob = 0, nums[0]
        for i in range(1, n):
            not_rob, rob = max(not_rob, rob), not_rob + nums[i]
        return max(not_rob, rob)
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([2, 7, 9, 3, 1]))


# Variables: dp(i, j) with i being the house index and j being rob or not. dp(i, 0) means you don't rob house i, and dp(i, 1) means you do
    
# Base case: dp(i, 0) = 0 and dp(i, 1) = nums[i]

# Recurrence relation:
# dp(i, 0) = max(dp(i - 1, 0), dp(i - 1, 1))
# dp(i, 1) = dp(i - 1, 0) + nums[i]

# If you don't steal house i, have it be the maximum value from the previous iteration
# If you do, have it add up to the value of the previous house that you didn't steal from


# ---- File: 199_binary_tree_right_side_view.py ----
from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root: return []
        res = []
        queue = deque([root])
        while queue:
            queue_length = len(queue)
            for i in range(queue_length):
                node = queue.popleft()
                if i == queue_length - 1: res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return res
    
# Do BFS on the tree from left to right for each depth. 
# We store the last node we traversed to so that when we get to a new depth/level of the tree, we can add it to the result array since that's
# the rightmost node in that previous level

# ---- File: 19_remove_nth_node_from_linked_list.py ----
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        slow = head
        fast = head
        while n:
            n -= 1
            fast = fast.next
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if prev:
            prev.next = slow.next
        else:
            return head.next
        
        return head
    
# Traverse to the end of the linked list, and go backwards
# Each time we go backwards, increment a counter. If the counter reaches n, remove that node
# We keep a reference of the previous node, and have the recursive function return the next node.
# If the previous node doesn't exist, then we are removing the head, so we return the next node.
# Otherwise, set the previous node's next pointer to be the next node, and return the current node.

# Iterative:
# Have fast and slow pointers that are n nodes apart, then iterate them both.
# Once fast has reached the end, we know slow is the node we have to remove.
# Keep track of the previous node from slow, and have its next pointer be slow's next.
# If prev is null then the node we are removing is the head node, so just return the node after head
# Otherwise, return the original head

# ---- File: 207_course_schedule.py ----
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        degrees = defaultdict(int)
        neighbors = defaultdict(list)
        for (start, end) in prerequisites:
            degrees[end] += 1
            neighbors[start].append(end)

        queue = [i for i in range(numCourses) if i not in degrees]
        res = []
        while queue:
            node = queue.pop(0)
            for neighbor in neighbors[node]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0: queue.append(neighbor)

            res.append(node)

        return len(res) == numCourses
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1,0]]))
    print(sol.canFinish(2, [[1,0],[0,1]]))
    print(sol.canFinish(3, [[2,0], [1,0],[0,1]]))

# We want to find if there exists a topological sort order for the vertices in the graph.
# Use Kahn's algorithm to see if that's true.
# Store the degrees of every node (how many edges point to it)
# Add nodes with degree 0 to the queue.
# Pop the queue, reduce the degree of every node that the current popped node points to. If the degrees reduce to 0, add the nodes to the queue
# Repeat until the queue is empty
# The topological ordering is the popped nodes, provided every node is popped
# If it exists and is equal to the number of courses, return true. Otherwise, there is a cycle and we return false

# ---- File: 2090_k_radius_subarray_averages.py ----
class Solution:
    def getAverages(self, nums, k: int):
        running_sum = 0
        left = 0
        n = len(nums)
        res = [-1]*n

        for right in range(n):
            running_sum += nums[right]

            if right >= 2*k:
                res[left + k] = running_sum // (2 * k + 1)
                running_sum -= nums[left]
                left += 1

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.getAverages([7,4,3,9,1,8,5,2,6], 3))
    print(sol.getAverages([100000, 100000], 0))
    print(sol.getAverages([8], 100000))

# Just simple sliding window, maintaining a window of size 2*k + 1, and updating the left + k-th index of the result

# ---- File: 20_valid_parentheses.py ----
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        if len(s) == 1: return False
        stack = []
        valid = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch not in valid:
                stack.append(ch)
            else:
                if stack and stack[-1] == valid[ch]:
                    stack.pop()
                else: return False
        return not stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid('{}[]()'))
    print(sol.isValid('[()]'))
    print(sol.isValid(')'))
    print(sol.isValid('(]'))
    print(sol.isValid(')(){}'))

#Use a stack to store only the opening brackets. If a closing bracket matches the front of the stack, then we pop.
#Otherwise, it's an invalid string.
#If the string is empty then we have popped all the correct pair of corresponding brackets.

#Initialize stack s
#For character in s:
#If character is an opening bracket then push it into s
#Else compare it to the front of the stack, if they match in terms of brackers then we pop s, otherwise we return false
#Returns true if s is empty, false otherwise

# ---- File: 210_course_schedule_2.py ----
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        degrees = defaultdict(int)
        neighbors = defaultdict(list)
        for (start, end) in prerequisites:
            degrees[start] += 1
            neighbors[end].append(start)

        queue = [i for i in range(numCourses) if i not in degrees]
        res = []
        while queue:
            node = queue.pop(0)
            for neighbor in neighbors[node]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0: queue.append(neighbor)

            res.append(node)

        return res if len(res) == numCourses else []
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(2, [[1,0]]))
    print(sol.findOrder(2, [[1,0],[0,1]]))
    print(sol.findOrder(3, [[2,0], [1,0],[0,1]]))

# We want to find if there exists a topological sort order for the vertices in the graph.
# Use Kahn's algorithm to see if that's true.
# Store the degrees of every node (how many edges point to it)
# Add nodes with degree 0 to the queue.
# Pop the queue, reduce the degree of every node that the current popped node points to. If the degrees reduce to 0, add the nodes to the queue
# Repeat until the queue is empty
# The topological ordering is the popped nodes, provided every node is popped
# If it exists and is equal to the number of courses, return it. Otherwise, there is a cycle and we return nothing

# ---- File: 215_kth_largest_element.py ----
import heapq

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], 2))

# Put the elements into a min heap. Prevent the heap's size from exceeding k by only pushing elements larger than the current head and popping the head.

# ---- File: 224_basic_calculator.py ----
class Solution:
    def __init__(self):
        self.index = 0

    def calc(self, s):
        res = 0
        num = 0
        last_result = 0
        op = "+"
        while self.index < len(s):
            if s[self.index] == ")":
                res += last_result
                last_result = num if op == "+" else -num
                break

            if s[self.index] == " ":
                self.index += 1
                continue

            if s[self.index].isdigit():
                num = num * 10 + int(s[self.index])
            elif s[self.index] in "+-":
                res += last_result
                last_result = num if op == "+" else -num
                num = 0
                op = s[self.index]
            else:
                self.index += 1
                num = self.calc(s)

            self.index += 1
        return res + last_result 

    def calculate(self, s: str) -> int:
        return self.calc(s + "+")
        

# Use a variable to store the previous operation. By default it should be +. Each time we come across a new operation,
# we finish the previous operation and storing the result. Every time we come across + or -, we update the final result with
# it since it has to be sequential. We add a + onto the string to make sure it finished the previous operation, before adding the last result to the final result.
# Every time we reach an open bracket, do a recursion call to get the inner result, and set the num to be that result. If we see a closing bracket, treat
# it similarly to the + we add onto the end of the string

# ---- File: 227_basic_calculator_2.py ----
class Solution:
    # def calculate(self, s: str) -> int:
    #     stack = []
    #     operation = '+'
    #     cur_num = 0
    #     for ch in s + '+':
    #         if ch == ' ':
    #             continue
    #         if ch.isdigit():
    #             cur_num = cur_num * 10 + int(ch)
    #         if not ch.isdigit():
    #             if operation == '+':
    #                 stack.append(cur_num)
    #             elif operation == '-':
    #                 stack.append(-cur_num)
    #             elif operation == '*':
    #                 stack.append(stack.pop() * cur_num)
    #             elif operation == '/':
    #                 stack.append(int(stack.pop() / cur_num))
    #             cur_num = 0
    #             operation = ch
    #     return sum(stack)

    def calculate(self, s: str) -> int:
        operation = '+'
        cur_num = 0
        res = 0
        last_result = 0
        for (i, ch) in enumerate(s):
            if ch == ' ':
                continue
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            if not ch.isdigit() or i == len(s) - 1:
                print(ch, operation, res, last_result)
                if operation == '+' or operation == '-':
                    res += last_result
                    last_result = cur_num if operation == '+' else -cur_num
                elif operation == '*':
                    last_result *= cur_num
                elif operation == '/':
                    last_result = int(last_result / cur_num)
                cur_num = 0
                operation = ch
        return res + last_result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate("3+2*2"))

# Use a variable to store the previous operation. By default it should be +. Each time we come across a new operation,
# we finish the previous operation and storing the result. Every time we come across + or -, we update the final result with
# it since it has to be sequential. Otherwise, we have to finish calculating the product or division first. We add a + onto the string
# to make sure it finished the previous operation, before adding the last result to the final result.



# ---- File: 229_majority_element_2.py ----
class Solution:

    def majorityElement(self, nums):
        if not nums:
            return []
        
        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)

        return result
    
# Majority Element 1 / Boyer Moore
# The idea is to have two variables, one holding a potential candidate for majority element and a counter to keep track of 
# whether to swap a potential candidate or not. Why can we get away with only two variables? Because there can be at most one majority element which is 
# more than ⌊n/2⌋ times. Therefore, having only one variable to hold the only potential candidate and one counter is enough.

# While scanning the array, the counter is incremented if you encounter an element which is exactly same as the potential candidate but decremented otherwise. 
# When the counter reaches zero, the element which will be encountered next will become the potential candidate. Keep doing this procedure while scanning the array. 
# However, when you have exhausted the array, you have to make sure that the element recorded in the potential candidate variable is the majority element by checking 
# whether it occurs more than ⌊n/2⌋ times in the array.

# ---- File: 22_generate_parentheses.py ----
class Solution:
    def generateParenthesis(self, n: int):
        res = []
        def backtracking(index, stack, word):
            if index == n * 2:
                if not stack:
                    res.append("".join(word))
                return

            if len(stack) > n:
                return
            
            for ch in "()":
                word.append(ch)
                if ch == "(":
                    stack.append(ch)
                    backtracking(index + 1, stack, word)
                    stack.pop()
                else:
                    if stack:
                        stack.pop()
                        backtracking(index + 1, stack, word)
                        stack.append("(")
                word.pop()
        backtracking(0, [], [])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
            
# Do backtracking on every possible combination of (). Stop when the index == n * 2 since that'd be the length of the string
# Use a stack to store the current state of valid parentheses. If ( is in then ) pops it. If the stack is empty we have a valid parentheses string
# Optimizations:
# If the stack is empty then there's no point in pushing ) in if it's never gonna get popped, thus never getting us a valid string
# If the length of the stack is more than n then we have pushed ( in more than n times, and we can't pop it in more than n times since the iterations would be more than n * 2.

# ---- File: 236_LCA_binary_tree.py ----
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = [root]
        ancestors = set()
        parents = {root: None}
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                parents[node.left] = node
            if node.right:
                queue.append(node.right)
                parents[node.right] = node
        while p:
            ancestors.add(p)
            p = parents[p]
        
        while q not in ancestors:
            q = parents[q]
        
        return q
    
# Use BFS to store the parent of every node in the tree
# Store all of the ancestors of p in a set
# Traverse upwards for q. The first ancestor of q that is also in p is the LCA

# ---- File: 238_product_of_array_except_self.py ----
class Solution:
    def productExceptSelf(self, nums):
        res = [1 for i in range(len(nums))]
        prefix_prod = 1
        for i in range(len(nums)):
            res[i] = prefix_prod
            prefix_prod *= nums[i]

        suffix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix_prod
            suffix_prod *= nums[i]

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))

# The product except self is the product of the prefix product before it and the suffix product after it
# In order to save space, we first iterate through the array to calculate the prefix product of the numbers before the number we're at.
# Similarly, we iterate through the array backwards to get the suffix product, and multiply it with the prefix product we were already storing in the results array

# ---- File: 239_sliding_window_maximum.py ----
import collections

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        queue = collections.deque()
        l = r = 0
        res = []
        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop() 
            queue.append(r)

            if queue and l > queue[0]:
                queue.popleft()

            if r >= k - 1:
                res.append(nums[queue[0]])
                l += 1

            r += 1
        return res


# Use a monotonically decreasing deque to keep track of the max of a window, with the leftmost element being the largest one.
# Append the indices. If the front of the queue is out of bounds of the window (check based on index), then pop it.

# ---- File: 23_merge_k_sorted_lists.py ----
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        cur = ListNode()
        heap, res = [], cur
        for (i, head) in enumerate(lists):
            if head: heapq.heappush(heap, (head.val, i, head))

        while heap:
            val, i, head = heapq.heappop(heap)
            cur.next = head
            cur = cur.next
            if head.next:
                heapq.heappush(heap, (head.next.val, i, head.next))
        
        return res.next
    
# Use a priority queue. First add all of the heads into the queue. Each time we pop a node, it's going to be the next node in the final
# sorted list. We then add the next node for that head into the queue and we keep going.

# ---- File: 2406_divide_intervals_into_min_groups.py ----
import heapq

class Solution:
    def minGroups(self, intervals) -> int:
        intervals.sort()
        groups = []
        heapq.heappush(groups, intervals[0][1])

        for (start, end) in intervals[1:]:
            if groups[0] < start:
                heapq.heappop(groups)
            
            heapq.heappush(groups, end)

        return len(groups)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))

# First sort all the intervals by the start time. Then, use a min heap to store all the end points.
# We want the top of the min heap to reflect the earliest end point of an interval.
# When we process a new interval, compare its start with the top to see if there's an overlap.
# If there isn't, pop the top of the heap. Push the new interval's end into the heap.
# The length of the heap is supposed to represent the maximum number of overlaps at any point.

# ---- File: 240_search_a_2d_matrix_2.py ----
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = 0
        col = n - 1
        while row < m and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False
    
# Initialize a pointer at the top right. If the number is less than target, move down. Larger, move left.
# If it's larger than the target then we know every number in the part of the column below it is larger than the target, so we don't need to consider that part of the column
# Similarly, if it's smaller than the target then every number before it in the row is smaller than the target, so we don't need to consider that part either

# ---- File: 246_strobogrammatic_number.py ----
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        reverse = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        new_num = ""
        for ch in num:
            if ch not in reverse: return False
            new_num += reverse[ch]
        return new_num[::-1] == num
    
# Store a dict for corresponding upside down values. Iterate through string, append the upside down values.
# If a number is not in the upside down list, return false. 
# Return whether the reversed new num is equal to the num at the end.

# ---- File: 249_group_shifted_strings.py ----
from collections import defaultdict
import itertools
class Solution:
    def groupStrings(self, strings):
        shifts = defaultdict(list)
        for string in strings:
            diff = [(ord(b) - ord(a)) % 26 for a,b in itertools.pairwise(string)]
            shifts[tuple(diff)].append(string)
        return shifts.values()

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
    
# For any 2 strings, if the pairwise differences between every consecutive characters in the string are exactly the same,
# then shifting them would eventually yield the same result. For example, "abc" has a difference of (1, 1), and "zab" also has a difference of (1, 1).
# This means they are part of the same group.
#  

# ---- File: 24_swap_nodes_in_pairs.py ----
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        cur = head
        next = cur.next
        res = None
        prev = None
        while cur and next:
            after_next = next.next
            next.next, cur.next = cur, after_next
            if prev: prev.next = next
            if not res: res = ListNode(0, next)

            prev = cur
            cur = cur.next
            if cur: next = cur.next
        
        return res.next
    
# If the list is less than 2 nodes long then return the head
# Keep 3 variables, the previous node, the current, and the next
# For each cur and next, cur.next = next.next, next.next = cur, and prev.next = next since next is now at the beginning of the pair


# ---- File: 25_reverse_nodes_in_k_group.py ----
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, head, tail):
        if head == tail:
            return None
        self.reverse_list(head.next, tail)
        head.next.next = head
        head.next = None
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        if k < 2: return head
        cur = head
        res = None
        k_cnt = k
        first = head
        prev_tail = None
        while cur:
            next_node = cur.next
            k_cnt -= 1
            if k_cnt == 0:
                k_cnt = k
                new_tail = self.reverse_list(first, cur)

                new_tail.next = next_node
                if prev_tail:
                    prev_tail.next = cur
                
                prev_tail = new_tail
                first = next_node
                if not res: res = cur

            cur = next_node
        return res

# If k < 2 then we don't do any reversing, just return the head
# Store a first pointer indicating the head of the list we're going to reverse, a prev_tail pointer indicating the tail of the last list we reversed
# cur is our current node pointer
# Everytime we iterate through k nodes, reset the counter. But when that happens, reverse the list from first to cur. The recursive function should return
# the new tail of the linked list, which was originally the first pointer. This new tail is now connected to cur's next pointer, with cur being the original tail
# of this list before we reversed it. The previous tail should now be connected to cur, cur being the new head of the reversed list.
# Update first to be the head node of the next list, and prev_tail to be our current tail
# If result is none then update res to be cur, which is the head of our new list

# ---- File: 266_palindrome_permutation.py ----
from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odd = False
        for key, val in count.items():
            if val % 2 != 0:
                if not odd:
                    odd = True
                else:
                    return False

        return True
    
# If there's more than 1 character with an odd count then return False

# ---- File: 269_alien_dictionary.py ----
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        degree = {}
        neighbors = defaultdict(set)
        for word in words:
            for ch in word:
                degree[ch] = 0

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in neighbors[c]:
                        neighbors[c].add(d)
                        degree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word): return ""

        res = []
        queue = deque([d for d in degree if degree[d] == 0])
        while queue:
            ch = queue.popleft()
            for neighbor in neighbors[ch]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
            res.append(ch)
        
        return "".join(res) if len(res) == len(degree) else ""
    
# For any 2 words, if the 2 letters at the same index of both words are not the same, then the one that goes first has an edge to the other in a graph.
# Otherwise, keep iterating. Add a check to make sure one isn't the prefix of the other 
# Do toposort based on that info

        

# ---- File: 2707_extra_chars_in_string.py ----
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def minExtraChar(self, s: str, dictionary) -> int:
        root = TrieNode()
        for word in dictionary:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                
                cur = cur.children[ch]
            
            cur.is_end = True
        
        dp = [0] * (len(s) + 1)
        
        for start in range(len(s) - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            node = root
            for end in range(start, len(s)):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_end:
                    dp[start] = min(dp[start], dp[end + 1])
        return dp[0]
    
# Use Trie to store dictionary words
# DP(i) backwards to store the minimum characters to be added starting from i.
# DP(i) = min(DP(i), DP(end + 1)) if s[i:end + 1] forms a word

# ---- File: 270_closest_binary_search_tree_value.py ----
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            if abs(root.val - target) < abs(closest-target):
                closest = root.val
            elif abs(root.val - target) == abs(closest-target):
                closest = min(root.val, closest)
            root = root.left if target < root.val else root.right
        return closest

# ---- File: 273_integer_to_english_word.py ----
class Solution:
    def hund_to_word(self, num):
        if len(num) == 1:
            return self.small[num[0]]
        second_third = ""
        if num[-2:] in self.tens:
            second_third = self.tens[num[-2:]]
        elif num[-2:] in self.tens_2:
            second_third = self.tens_2[num[-2:]]
        else:
            if num[-2] != "0":
                second_third += self.tens_2[num[-2] + "0"] + " "
            second_third += self.small[num[-1]]
        
        if len(num) == 2 or num[0] == "0":
            return second_third

        return self.small[num[0]] + " Hundred " + second_third if second_third else self.small[num[0]] + " Hundred"

    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        self.tens = {"10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", \
        "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"}
        self.tens_2 = {"20": "Twenty", "30": "Thirty", "40": "Forty", "50": "Fifty", "60": "Sixty", \
        "70": "Seventy", "80": "Eighty", "90": "Ninety"}
        self.small = {"0": "", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five",\
        "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
        suffixes = {0: "", 1: "Thousand", 2: "Million", 3: "Billion", 4: "Trillion"}
        num = str(num)
        if len(num) % 3 != 0:
            num = "0"*(3 - len(num) % 3) + num
        count = 0
        res = ""
        for i in range(len(num) - 1, -1, -3):
            hund_word = self.hund_to_word(num[i-2:i+1])
            if hund_word:
                if suffixes[count]:
                    hund_word += " " + suffixes[count]
                if res:
                    res = hund_word + " " + res
                else:
                    res = hund_word
            count += 1
        return res




# ---- File: 2807_insert_gcd_in_linked_list.py ----
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if not b: return a
            return gcd(b, a % b)
        if not head or not head.next: return head
        res = ListNode(0, head)
        cur_node = head
        next_node = head.next
        while next_node:
            gcd_node = ListNode(math.gcd(cur_node.val, next_node.val), next_node)
            cur_node.next = gcd_node
            cur_node = next_node
            next_node = next_node.next
        
        return res.next

# GCD function  
# def gcd(a, b):
#     if not b: return a
#     return gcd(b, a % b)

# ---- File: 282_expression_add_operators.py ----
class Solution:
    def addOperators(self, num: str, target: int):
        n = len(num)
        res = []
        def backtracking(index, prev_operand, cur_operand, value, string):
            if index == n:
                if value == target and cur_operand == 0:
                    res.append("".join(string[1:]))
                return
            
            cur_operand = cur_operand * 10 + int(num[index])
            
            if cur_operand > 0:
                backtracking(index + 1, prev_operand, cur_operand, value, string)
            
            string.append("+")
            string.append(str(cur_operand))
            backtracking(index + 1, cur_operand, 0, value + cur_operand, string)
            string.pop()
            string.pop()

            if string:
                string.append("-")
                string.append(str(cur_operand))
                backtracking(index + 1, -cur_operand, 0, value - cur_operand, string)
                string.pop()
                string.pop()

                string.append("*")
                string.append(str(cur_operand))
                backtracking(index + 1, cur_operand * prev_operand, 0, value - prev_operand + (cur_operand * prev_operand), string)
                string.pop()
                string.pop()

        def backtracking_pm_only(index, cur_operand, value, string):
            if index == n:
                if value == target and cur_operand == 0:
                    res.append("".join(string[1:]))
                return
            
            cur_operand = cur_operand * 10 + int(num[index])
            
            if cur_operand > 0:
                backtracking_pm_only(index + 1, cur_operand, value, string)
            
            string.append("+")
            string.append(str(cur_operand))
            backtracking_pm_only(index + 1, 0, value + cur_operand, string)
            string.pop()
            string.pop()

            if string:
                string.append("-")
                string.append(str(cur_operand))
                backtracking_pm_only(index + 1, 0, value - cur_operand, string)
                string.pop()
                string.pop()


        backtracking_pm_only(0, 0, 0, [])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.addOperators("123", 6))

# There's 4 decisions at each index: use +, -, * or no operation and keep expanding the current number by adding the digit to the right of it
# We keep track of the current operand/number and adjust our current value along the way so as to compare it to the target in O(1) when we're at the end.
# When we're at the end, it has to be after we did an operation with the last digit, instead of trying to expand it even more.
# The * complicates things. If we have a *, then we have to keep track of the previous operand as well, so that we may reverse the effect and multiply it with the current operand

# ---- File: 283_move_zeroes.py ----
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1 = ptr2 = 0
        while ptr2 < len(nums):
            if nums[ptr2] != 0:
                nums[ptr2], nums[ptr1] = nums[ptr1], nums[ptr2]
                ptr1 += 1
            ptr2 += 1

# Use 2 pointers. Every time you encounter a nonzero element, move it to the first pointer and increment it.

# ---- File: 286_walls_and_gates.py ----
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs(r, c):
            visited = set((r, c))
            queue = [(r, c, 0)]
            while queue:
                cur_r, cur_c, dist = queue.pop(0)

                for dr, dc in DIRECTIONS:
                    new_r = cur_r + dr
                    new_c = cur_c + dc
                    
                    if not (0 <= new_r < len(rooms) and 0 <= new_c < len(rooms[0])):
                        continue

                    if (new_r, new_c) in visited:
                        continue

                    if rooms[new_r][new_c] == -1:
                        continue
                    
                    if dist + 1 > rooms[new_r][new_c]:
                        continue

                    visited.add((new_r, new_c))
                    rooms[new_r][new_c] = dist + 1
                    queue.append((new_r, new_c, dist + 1))
            
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    bfs(i, j)

# BFS on the gates. Only visit empty cells if the current distance is smaller to save time


# ---- File: 2914_beautiful_binary_string.py ----
class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]: res += 1
        return res
    
# Only check the substrings with length 2

# ---- File: 295_find_median_from_data_stream.py ----
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.median = 1e9
    def addNum(self, num: int) -> None:
        if num <= self.median:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) - len(self.min_heap) == 2:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        elif len(self.min_heap) - len(self.max_heap) == 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        if len(self.max_heap) == len(self.min_heap):
            self.median = (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            self.median = -self.max_heap[0]

    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Similar to sliding window median, keep a max and min heap. Ensure that the difference between the lengths of the 2 heaps never exceeds 2,
# with the length of max heap always being no less than the length of the min heap. 

# ---- File: 296_best_meeting_point.py ----
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = []
        cols = []
        houses = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows.append(i)
                    houses.append((i, j))

        for i in range(n):
            for j in range(m):
                if grid[j][i]:
                    cols.append(i)

        median_rows = rows[len(rows) // 2]
        median_cols = cols[len(cols) // 2]

        return sum([abs(house[0] - median_rows) + abs(house[1] - median_cols) for house in houses])
    
# Median of rows and cols is the best meeting point

# ---- File: 29_divide_2_integers.py ----
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT = -(2 ** 31)
        if dividend == MIN_INT and divisor == -1:
            return 2 ** 31 -1

        dd = abs(dividend)
        dv = abs(divisor)
        res = 0
        while dd >= dv:
            x = 0
            while dd - (dv << (1 + x)) >= 0:
                x += 1
            res += 1 << x
            dd -= dv << x

        if (dividend < 0 and divisor >= 0) or (dividend > 0 and divisor <= 0):
            res = -res
        return res
    
# Multiply divisor exponentially by 2. Once we can't, reduce dividend by that 2 ** (power) * divisor, add 1 << power to the result and keep going.
# Since we can't multiply, we use bit shifting instead with power. If there's exactly 1 negative, change the sign of the result
# If the dividend is the minimum int and the divisor is -1, then it'll overflow, so return 2 ** 31 - 1

# ---- File: 2_add_two_numbers.py ----
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add(self, l1, l2, carry):
        if not l1 and not l2: 
            if carry: return ListNode(carry, None)
            return None
        l1_val = l2_val = 0
        l1_next = None
        l2_next = None
        if l1:
            l1_val = l1.val
            l1_next = l1.next
        
        if l2:
            l2_val = l2.val
            l2_next = l2.next

        sum = l1_val + l2_val + carry
        new_val = sum % 10
        new_carry = sum // 10
        return ListNode(new_val, self.add(l1_next, l2_next, new_carry))
    
    def addTwoNumbers(self, l1, l2):
        return self.add(l1, l2, 0)
        

# Iterate through each of the linked lists one by one. Add the values of the current nodes together while noting a carry for the next node.
# If a node is empty then treat its value as 0, and its next pointer is null.
# If both nodes are empty, we've reached the end of the linked lists. If the carry is 1 then add another node with the value 1, otherwise the node doesn't exist.

# ---- File: 3011_find_if_array_can_be_sorted.py ----
class Solution:
    def count_set_bits(self, n):
        res = 0
        while n:
            res += 1
            n &= (n-1)
        return res

    def canSortArray(self, nums) -> bool:
        sorted_flag = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                sorted_flag = False
                break

        if sorted_flag: return True

        cur_count = -1
        last_max = -1
        cur_max = -1

        for i in range(len(nums)):
            count = self.count_set_bits(nums[i])
            if count != cur_count:
                last_max = cur_max
                cur_max = 0
                cur_count = count
            
            if last_max > nums[i]:
                return False
            
            cur_max = max(cur_max, nums[i])

        return True
    
# For any 2 consecutive sequences with different bit counts, if the max of the left sequence is larger than any element within
# the right, then the array can't be sorted since we can't swap the other element toward the front of the array.

# Count set bits for each element. If the number of bits is different from the current count then update the current count and updated the highest element to be the
# highest element of the last sequence of set bits. Maximize cur_max each time so we can update last_max later

# ---- File: 301_remove_invalid_parentheses.py ----
from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:
    def removeInvalidParentheses(self, s: str):
        count = defaultdict(set)
        print(bisect_left([2,5], 3), bisect_right([2, 5], 3))
        min_removed = len(s)
        def backtracking(index, stack, word, removed):
            nonlocal min_removed
            if index == len(s):
                if not stack:
                    min_removed = min(removed, min_removed)
                    count[removed].add(word)
                return
            if s[index] not in "()":
                backtracking(index + 1, stack, word + s[index], removed)
                return
            if stack and stack[-1] == "(" and s[index] == ")":
                backtracking(index + 1, stack[:-1], word + s[index], removed)
            else:
                backtracking(index + 1, stack + [s[index]], word + s[index], removed)

            backtracking(index + 1, stack, word, removed + 1)

        backtracking(0, [], "", 0)
        return list(count[min_removed])

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeInvalidParentheses("()())()"))
            
# Do backtracking. At each step, we either include the current parentheses or don't include it.
# If we do include it, make sure the stack is updated correctly. If the top is ( and the cur character is ), then don't include the top of the stack. Otherwise, push it and continue to the next index
# If we don't include it, don't update the stack, but increase the number of removed parentheses so far.

# Once we reach the length of s, then check if the stack is empty. If it is, then we have a valid string now. Add the string along with its removed count to a hash table and update the min removed count
# At the end, check all of the strings in the min removed key of the hash table







# ---- File: 3043_length_of_longest_common_prefix.py ----
class TrieNode:
    def __init__(self):
        self.children = [None] * 10

class Solution:
    def insert(self, root, num):
        digits = [int(dig) for dig in str(num)]
        curr = root
        for digit in digits:
            if not curr.children[digit]:
                new_node = TrieNode()
                curr.children[digit] = new_node
            curr = curr.children[digit]

    def search(self, root, num):
        digits = [int(dig) for dig in str(num)]
        curr = root
        length = 0
        for digit in digits:
            if not curr.children[digit]:
                return length
            curr = curr.children[digit]
            length += 1
        return length
        
    def longestCommonPrefix(self, arr1, arr2) -> int:
        res = 0
        root = TrieNode()
        for num in arr1:
            self.insert(root, num)

        for num in arr2:
            res = max(self.search(root, num), res)

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix([1,10,100], [1000]))
    print(sol.longestCommonPrefix([1,2,3], [4, 4, 4]))

# Use a trie to store all of the prefixes in the first array.
# Go through every number in the second array and traverse the trie for each number. We increase the prefix length every
# time the digit exists in a node's children and keep traversing down. If a child for arr2's number doesn't exist, that's the common prefix
# for that number, so we return the length we got so far. We maximize this length

# ---- File: 3097_shortest_subarray_with_or_at_least_k.py ----
class Solution:
    def update_mask(self, mask, num, flag):
        bin_string = "{0:b}".format(num)[::-1]

        for (i, ch) in enumerate(bin_string):
            if ch == "1":
                mask[i] += flag
        
        return mask
    
    def get_value(self, mask):
        res = sum([num * (2 ** i) for (i, num) in enumerate(mask)])
        return res


    def minimumSubarrayLength(self, nums, k: int) -> int:
        if max(nums) >= k: return 1
        bitmask = [0]*32
        res = float("inf")

        left = 0
        mask_value = 0
        for right in range(len(nums)):
            bitmask = self.update_mask(bitmask, nums[right], 1)

            mask_value = self.get_value(bitmask)

            while mask_value >= k and left < len(nums):    
                if right - left + 1 > 0:
                    res = min(res, right - left + 1)
                bitmask = self.update_mask(bitmask, nums[left], -1)
                left += 1
                mask_value = self.get_value(bitmask)
        
        return res if res != float("inf") else -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumSubarrayLength([1,2,3], 2))
    print(sol.minimumSubarrayLength([2,1,8], 10))
    print(sol.minimumSubarrayLength([1, 2], 0))

# Have a bitmask array of size 32 + use sliding window. Every time we encounter a new number, update that bitmask array by incrementing the indices with 1.
# When we remove a number from the window, decrement the indices with 1. To get the value of the bitmask, only add the value of a bit if it's more than 0.
# If it's it more than 0 then it's 2 ** index.
# Only shrink the window if the mask value >= k

# ---- File: 311_sparse_matrix_multiplication.py ----
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def compress(mat):
            compress_dict = defaultdict(list)
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if mat[i][j] != 0:
                        compress_dict[i].append((j, mat[i][j]))
            return compress_dict
        
        m = len(mat1)
        n = len(mat2[0])

        A = compress(mat1)
        B = compress(mat2)
        res = [[0 for _ in range(n)] for _ in range(m)]

        for mat1_row in range(m):
            for col1, val1 in A[mat1_row]:
                for col2, val2 in B[col1]:
                    res[mat1_row][col2] += val1 * val2

        return res

# Have a hash table with the key being a row and the value being (column, val) for non-zero vals for both matrices
# If 2 matrices are A x B and B x C, then the product would be A x C
# Iterate through the rows of the first matrix to get the non-zero columns/vals, multiply them with the corresponding row index (this case being mat1's column) of the other matrix


# ---- File: 3133_min_array_end.py ----
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        i_x = i_n = 1

        while i_n <= n - 1:
            if i_x & x == 0:
                if i_n & (n - 1):
                    res |= i_x
                i_n *= 2
            i_x *= 2
        
        return res
    
# What we care about is the set bits of x, because those have to remain unchanged. The reason is that if we do AND on every number,
# all of them have to have the same set bits as x in order to get x
# The smallest element has to be x because otherwise, we'd lose those set bits.
# Since we're getting n - 1 extra elements with set bits like x's, we iterate through x and fill in the bits of n - 1 only for bits that weren't set in x

# ---- File: 314_binary_tree_vertical_order_traversal.py ----
from collections import defaultdict

class Solution:
    def verticalOrder(self, root):
        if not root: return []
        queue = []
        columns = defaultdict(list)
        queue.append((root, 0))
        min_level = 1e9
        max_level = -1e9
        while queue:
            node, level = queue.pop(0)
            if min_level > level: min_level = level
            if max_level < level: max_level = level

            columns[level].append(node.val)
            if node.left:
                queue.append((node.left, level - 1))
            
            if node.right:
                queue.append((node.right, level + 1))
        
        res = []
        for i in range(min_level, max_level + 1):
            res.append(columns[i])

        return res
    
# Do a BFS traversal. Store the node and its current level in a queue.
# The left child's level will be 1 less, and the right's will be 1 more.
# Store the nodes for each level in a hash table, while keeping track of the min and max levels for easier logging later

# ---- File: 317_shortest_dist_from_all_buildings.py ----
from collections import deque

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
class Solution:
    def shortestDistance(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        total_sum = [[0] * cols for _ in range(rows)]
        
        def bfs(row, col, curr_count):
            min_distance = 1e9
            queue = deque()
            queue.append([row, col, 0])
            while queue:
                curr_row, curr_col, curr_step = queue.popleft()
                for dr, dc in dirs:
                    next_row = curr_row + dr
                    next_col = curr_col + dc
                    
                    if not (0 <= next_row < rows and 0 <= next_col < cols):
                        continue
                    if grid[next_row][next_col] != -curr_count:
                        continue

                    total_sum[next_row][next_col] += curr_step + 1
                    min_distance = min(min_distance, total_sum[next_row][next_col])
                    grid[next_row][next_col] -= 1
                    queue.append([next_row, next_col, curr_step + 1])
            return min_distance
                
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    min_distance = bfs(row, col, count)
                    count += 1
                    if min_distance == 1e9:
                        return -1
        
        return min_distance
    
# During the first BFS we can change the visited empty land values from 0 to -1. Then during the next BFS we will only visit empty lands with a value of -1s (meaning they can 
# reach the first house), then change -1 to -2 and then perform the next BFS only on -2s, and so on...

# This approach allows us to avoid visiting any cell that cannot reach all houses.

# Can we also use this decrement in empty land value to denote that the cell has been visited?

# Imagine we are currently at cell (2, 3) with value -1 and we change its value to -2.
# In the queue the next element is (2, 4), its value is also -1 and we change its value to -2. While exploring paths from (2, 4), we see that the cell (2, 3) is adjacent, and has the value -2. However, currently, we are checking for -1 valued cells only. Hence, (2, 3) will not be inserted again in the queue, so this decrease in value can be used as a visited cell check because when a cell has been visited, then its value will be 1 less and it will not satisfy the condition to be inserted in the queue.

# If there was an empty land cell that was not reachable in the previous iteration, then its value has not been decreased, hence we will not insert that cell in the queue when we start a BFS from another house cell.
# Therefore, this approach prunes many iterations and saves some time since we are not creating a new matrix to track visited cells for each BFS call.



# ---- File: 31_next_permutation.py ----
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        start = i + 1
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

# Notice that an array in descending order would have no next permutation and would have to loop back.
# So we find 2 consecutive indices where nums[i] < nums[i + 1]. Thus, we know that every number after i is sorted in descending order.
# The most logical number to replace nums[i] would be the smallest number nums[j] such that nums[j] > nums[i], so that nums[j] would be the next number in the permutation
# We swap nums[j] with nums[i], thus maintaining the descending order. We want to minimize this array after nums[j] now, so we reverse it since it's in descending order
# and we get our next permutation


# ---- File: 325_max_size_subarray_sum_equals_k.py ----
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        hash_sum = {0: -1}
        res = 0
        pref_sum = 0
        for (i, num) in enumerate(nums):
            pref_sum += num
            if pref_sum - k in hash_sum:
                res = max(res, i - hash_sum[pref_sum - k])
            
            if pref_sum not in hash_sum:
                hash_sum[pref_sum] = i

        return res
    
# Use prefix sum since it's a problem related to subarray sum
# Notice that if sum - k is in the stored hash table of sums then its first appearance is the left index, and i is the right index, and they create a subarray sum of k

# ---- File: 329_longest_increasing_path_matrix.py ----
from collections import defaultdict

class Solution:
    def dfs(self, matrix, r, c):
        if (r,c) in self.cache: return self.cache[(r, c)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]) and matrix[new_r][new_c] > matrix[r][c]:
                self.cache[(r, c)] = max(self.dfs(matrix, new_r, new_c), self.cache[(r, c)])

        self.cache[(r, c)] += 1
        return self.cache[(r, c)]
    def longestIncreasingPath(self, matrix) -> int:
        res = 0
        m, n = len(matrix), len(matrix[0])
        self.cache = defaultdict(int)
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j))

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))

# Do DFS + memoization, while storing the max increasing length of a path starting at (i, j).
# When traversing DFS, only traverse to squares that are larger than the current

# ---- File: 32_longest_valid_parentheses.py ----
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack = [-1]
        res = 0
        for (i, ch) in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
    
    def longestValidParentheses_o1(self, s: str) -> int:
        left = right = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            
            if right > left:
                right = left = 0
            elif right == left:
                res = max(res, left * 2)

        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            
            if right < left:
                right = left = 0
            elif right == left:
                res = max(res, left * 2)

        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestValidParentheses("(()"))
    print(sol.longestValidParentheses(")()())"))

# Approach 1: Stack
# Each time we encounter (, append its index into the stack. When we see ), pop the stack.
# The length of a valid parentheses substring is the current index - the top of the stack.
# The reason why we get the top after we pop the stack is the top at that point is supposed to represent the index before the start of the valid substring.
# That's why at first, we put -1 into the stack because the substring could start from index 0. If ) is encountered before a (, then we discard the substring before that.
# Thus, every time we encounter a ), after we pop the stack and the stack is empty, then we append the current index as well

# Approach 2: Two Pointers
# Have left = right = 0, with left representing the ( count and right representing the ) count.
# Iterate forward. Increment left and right accordingly. If at any point, right > left then reset both. We want to start counting from the index after. If right == left then maximize the result and left * 2
# Iterate backward and do the same thing but with right < left as the reset condition instead.

# ---- File: 333_largest_bst_subtree.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root: return None
        root.is_bst = False
        root.size = 1
        root.min = root.val
        root.max = root.val

        left_max = -1e9
        right_min = 1e9
        left_BST = right_BST = True

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left:
            left_BST = left.is_bst
            root.size += left.size
            left_max = left.max
            root.min = min(root.val, left.min)

        if right:
            right_BST = right.is_bst
            root.size += right.size
            right_min = right.min
            root.max = max(root.val, right.max)

        
        if left_BST and right_BST and left_max < root.val < right_min:
            root.is_bst = True
            self.res = max(self.res, root.size)
        return root
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
        

# Do DFS on every node
# At each node, initialize is_bst (whether the tree with the node as the root is a BST), min (the smallest value of the tree with the node as the root), size = 1 (size of tree), 
# and max (self-explanatory) properties for the node
# Also initialize variables left_max (largest value of left subtree), right_min (smallest value of right subtree), and booleans left_BST and right_BST indicating if the subtrees are BSTs

# Check the left subtree first
# Update the size of the tree, have left_max = left.max, and root.min = min(root.val, left.min) since the smallest value of the tree should be within the left subtree or the node itself.
# Do the same with the right subtree but with right_min = right.min and root.max = max(root.val, right.max) instead

# If both subtrees are BST and left_max < root.val < right_min then root is larger than every node in left and smaller than every node in right, so it's a BST.
# Set is_bst = true, and maximize the result


# ---- File: 334_increasing_triplet_subsequence.py ----
class Solution:
    def increasingTriplet(self, nums) -> bool:
        if len(nums) < 3: return False
        num1 = num2 = float('inf')
        for num in nums:
            if num <= num1: num1 = num
            elif num <= num2: num2 = num
            else: return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.increasingTriplet([1, 2, 3, 4, 5]))
    print(sol.increasingTriplet([2, 3, 1]))
    print(sol.increasingTriplet([5, 4, 3, 2]))

# Have 2 numbers to keep track of the lowest and second lowest numbers so far. If there is a number larger than both then we have an increasing triplet. 


# ---- File: 339_nested_list_weight_sum.py ----
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
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

class Solution:
    def dfs(self, nested_list, depth):
        sum = 0
        for elem in nested_list:
            if not elem.isInteger():
                sum += self.dfs(elem.getList(), depth + 1)
            else:
                sum += elem.getInteger() * depth
        return sum
    
    def depthSum(self, nestedList) -> int:
        return self.dfs(nestedList, 1)
    
# If we see a nested list, then enter that list with an increased depth and calculate its sum. Otherwise, add the integer multiplied by the depth to the sum

# ---- File: 33_search_in_rotated_sorted_array.py ----
class Solution:
    def find_pivot(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid
        return left
    
    def search(self, nums, target: int) -> int:
        pivot = self.find_pivot(nums)
        def binary_search(L, R, target):
            left = L
            right = R
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        left_search = binary_search(0, pivot - 1, target)
        if left_search != -1:
            return left_search
        return binary_search(pivot, len(nums) - 1, target)
    
    # def search(self, nums, target: int) -> int:
    #     n = len(nums)
    #     left, right = 0, n - 1
    #     while left <= right:
    #         mid = left + (right - left) // 2

    #         # Case 1: find target
    #         if nums[mid] == target:
    #             return mid

    #         # Case 2: subarray on mid's left is sorted
    #         elif nums[mid] >= nums[left]:
    #             if target >= nums[left] and target < nums[mid]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1

    #         # Case 3: subarray on mid's right is sorted.
    #         else:
    #             if target <= nums[right] and target > nums[mid]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #     return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4,5,6,7,8,9,10], 0))
    #print(sol.search([4,5,6,7,0,1,2], 0))

# Approach 1: Find the pivot and then do binary search in nums[:pivot] and nums[pivot:]
# The pivot is the first element that <= nums[-1]. Because if the mid element is larger than the final element, the pivot has to be in the right half.

# Approach 2: Do binary search without finding the pivot
# We first compare the middle num with the leftmost num in our subarray. If middle > left then the left array is sorted. But we still have to check if target is inbetween those.
# If not, discard the left subarray. Otherwise, keep it.
# If middle < left then the left subarray is rotated, and the right subarray is sorted. We still have to check if target is in the middle of middle and right, if not then
# discard the right subarray, otherwise keep it

# ---- File: 341_flatten_nested_list_iterator.py ----
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.int_stack = []
        nested_stack = nestedList
        self.ptr = 0
        while nested_stack:
            cur = nested_stack.pop()
            
            nested = cur.getList()
            if not nested and cur.isInteger():
                self.int_stack.append(cur.getInteger())
            else:
                for elem in nested:
                    nested_stack.append(elem)
        
        self.int_stack = self.int_stack[::-1]
    
    def next(self) -> int:
        res = self.int_stack[self.ptr]
        self.ptr += 1
        return res
        
    def hasNext(self) -> bool:
        return self.ptr < len(self.int_stack)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Have nestedList be a stack at first. Every time we pop the stack, check if the elem is a list.
# If it isn't, add it to the int stack if it's an integer
# Otherwise, add every element in that list into the nested stack
# Reverse the int stack at the end, and have a pointer iterate through it

# ---- File: 346_moving_avg_data_stream.py ----
class MovingAverage:

    def __init__(self, size: int):
        self.queue = []
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum += val
        if len(self.queue) > self.size:
            self.sum -= self.queue.pop(0)
        
        return self.sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Use a queue with a max size. Everytime it exceeds it, pop the head.

# ---- File: 347_top_k_frequent_elements.py ----
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k: int):
        count = Counter(nums)
        freq = [(cnt, num) for (num, cnt) in count.items()]
        heap = []
        heap = freq[:k]
        heapq.heapify(heap)
        
        for (cnt, num) in freq[k:]:
            if cnt > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (cnt, num))

        return [hp[1] for hp in heap]
if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))

# Quickselect for O(N)

# ---- File: 348_design_tic_tac_toe.py ----
from collections import defaultdict

class TicTacToe:
    def __init__(self, n: int):
        self.anti_diag_coords = set()
        for i in range(n):
            self.anti_diag_coords.add((i, n - 1 - i))

        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.diag = 0
        self.anti_diag = 0
        self.win = n 

    def move(self, row: int, col: int, player: int) -> int:
        score = 1 if player == 1 else -1
        if row == col: self.diag += score
        if (row, col) in self.anti_diag_coords: self.anti_diag += score
        self.rows[row] += score
        self.cols[col] += score
        if self.rows[row] == score * self.win or self.cols[col] == score*self.win or \
        self.diag == self.win * score or self.anti_diag == self.win * score:
            return 1 if score == 1 else 2
        return 0
    
# Instead of storing a matrix and updating it with O(n^2), we store 2 hash tables + 2 counters to update the game state in O(1).
# We have 2 hash tables for rows and columns and 2 counters for the diagonal and anti-diagonal.
# Every time a player makes a move, the tally for the row/column/diagonal/anti-diagonal it's in increases by 1 if it's player 1 or -1 if it's player 2.
# The game ends when the tally for any of this is equal to n or -n.

# ---- File: 34_first_and_last_of_sorted_arr.py ----
from bisect import bisect_left, bisect_right

class Solution:
    def find_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
    
    def find_right(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left
    
    def searchRange(self, nums, target: int):
        if not nums: return [-1, -1]
        #left = bisect_left(nums, target)
        left = self.find_left(nums, target)
        right = self.find_right(nums, target)
        #right = bisect_right(nums, target)
        if left >= len(nums) or nums[left] != target: return [-1, -1]
        if right == len(nums) - 1 and nums[right] == target: return [left, right]
        if right == 0 or nums[right - 1] != target: return [-1, -1]
        return [left, right - 1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10], 8))
    print(sol.searchRange([5,7,7,8,8,10], 6))
    print(sol.searchRange([], 0))

# Bisect left to find left insertion point. Make sure it's not at the end of the array
# Bisect right to find right insertion point because it will be after the rightmost target element. Check right - 1 and make sure it's not 0

# ---- File: 378_kth_smallest_element_in_sorted_matrix.py ----
import heapq

class Solution:
    def kthSmallest2(self, matrix, k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(n):
            for j in range(n):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[i][j])
                else:
                    if -heap[0] > matrix[i][j]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, -matrix[i][j])
        return -heap[0]
    
    def count_smaller(self, matrix, mid, smaller, larger):
        count = 0
        row = len(matrix) - 1
        col = 0

        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] > mid:
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                count += row + 1
                smaller = max(smaller, matrix[row][col])
                col += 1
        
        return count, smaller, larger

    def kthSmallest(self, matrix, k: int) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2

            count, smaller, larger = self.count_smaller(matrix, mid, left, right)

            if count == k:
                return smaller
            elif count > k:
                right = smaller
            else:
                left = larger

        return left
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))

# Do binary search in the number range (smallest to largest of the matrix)
# Every time we find a point, find the number of elements smaller than it in the matrix.
# Start from bottom left. If the element is smaller than the middle point then by default, every element before that row
# is smaller, so increment the count by the number of rows up to it. Then move to the right.
# If the element is larger then move up. Each time, keep track of the first elements larger/smaller than the middle.
# Once we have a count, compare it to k. If it's k then return the element smaller than the middle.
# If it's less than k then eliminate the left portion by setting left = larger, otherwise right = smaller (eliminating the right)
# Return left at the end

# ---- File: 37_sudoku_solver.py ----
from collections import Counter

class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtracking(r, c):
            if c == 9:
                r += 1
                c = 0

            if r == 9:
                return True
            
            if board[r][c] != ".":
                return backtracking(r, c + 1)
            
            for ch in "123456789":
                if not valid(r, c, ch):
                    continue

                board[r][c] = ch
                if backtracking(r, c + 1):
                    return True
                board[r][c] = "."
            
            return False

        def valid(r, c, val):
            count_row = Counter(board[r])
            if val in count_row: return False
            column = [board[i][c] for i in range(9)]
            count_col = Counter(column)
            if val in count_col: return False

            start_row = 3 * (r // 3)
            start_col = 3 * (c // 3)

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == val: return False
            
            return True

        backtracking(0, 0)


# Do backtracking on every "." cell of the grid. Check every value from "123456789", as long as it's valid.
# We check whether a value is valid in a cell by checking its column, row, and subgrid. To get the subgrid for a current cell,
# find the top left cell of the grid with the formula (3 * (r//3), 3 * (c // 3))
# If it's valid, we go to the next cell (column + 1). If column == 9 then we go to the next row. If we've gone through all 9 rows
# then all of our values are valid, so we return true

# ---- File: 381_insert_delete_getrandom_o1_dupes.py ----
from random import choice
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.lst = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx[val]: return False
        idx = self.idx[val].pop()
        last = self.lst[-1]
        self.idx[last].add(idx)
        self.idx[last].discard(len(self.lst) - 1)
        
        self.lst[idx] = last
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# ---- File: 386_lexicographical_numbers.py ----
class Solution:
    def lexicalOrder(self, n: int):
        res = []
        def dfs(cur_num):
            nonlocal n
            if cur_num > n:
                return

            res.append(cur_num)
            for i in range(10):
                next_num = cur_num * 10 + i
                if next_num <= n:
                    dfs(next_num)
                else:
                    break

        for i in range(1, 10):
            dfs(i)
        return res 
    
# Do DFS on every digit, stop if the current num exceeds n since every digit after would exceed n as well

# ---- File: 38_count_and_say.py ----
class Solution:
    def RLE(self, s):
        res = ""
        count = 1
        cur_ch = None
        for (i, ch) in enumerate(s):
            if ch != cur_ch:
                if cur_ch: res += str(count) + cur_ch
                count = 1
                cur_ch = ch
            else:
                count += 1

        return res + str(count) + cur_ch
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        cur = "1"
        for i in range(2, n + 1):
            next = self.RLE(cur)
            cur = next

        return cur
if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(1))
    print(sol.countAndSay(3))

# Have a function that converts a string into its RLE encoding. Iterate through it and keep track of the count of the current character.
# If we move to a new character, append the count + the character into the encoding.

# ---- File: 392_is_subsequence.py ----
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1 = ptr2 = 0
        while ptr1 < len(s) and ptr2 < len(t):
            if t[ptr2] == s[ptr1]:
                ptr1 += 1
            
            ptr2 += 1
        return ptr1 == len(s)
    
# Just use 2 pointers. Increment the s pointer everytime there's a match in t. If the s pointer makes it all the way to the end, it is a subsequence

# ---- File: 394_decode_string.py ----
class Solution:
    def __init__(self):
        self.index = 0

    def decodeString(self, s: str) -> str:
        res = ""
        while self.index < len(s) and s[self.index] != "]":
            if not s[self.index].isdigit():
                res += s[self.index]
                self.index += 1
            else:
                count = 0
                while self.index < len(s) and s[self.index].isdigit():
                    count = count * 10 + int(s[self.index])
                    self.index += 1
                
                self.index += 1
                decode = self.decodeString(s)

                self.index += 1
                
                res += decode * count
        return res

# Keep a global index indicating how far along we've traversed in s. If we encounter a character then append it to the result string
# Otherwise, check what the count is, then skip over the opening bracket and call recursion on the string within.
# We process that smaller string until we reach ], then we return. The string outside would get the inner string * count, and we skip over the ] bracket
# so that we can continue processing


# ---- File: 398_random_pick_index.py ----
from collections import defaultdict
from random import randrange

class Solution:

    def __init__(self, nums):
        self.indices = defaultdict(list)
        for (i, num) in enumerate(nums):
            self.indices[num].append(i)


    def pick(self, target: int) -> int:
        if len(self.indices[target]) == 1:
            return self.indices[target][0]
        
        rand_index = randrange(0, len(self.indices[target]))
        return self.indices[target][rand_index]
        

# Store all the indices within a hash table list corresponding to a number.
# If there's multiple, do randrange to pick a random index from 0 to that number's indices length


# ---- File: 408_valid_word_abbreviation.py ----
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) > len(word): return False
        ptr1 = 0
        ptr2 = 0
        while ptr2 < len(abbr):
            if abbr[ptr2].isdigit():
                if abbr[ptr2] == "0": return False
                origin = ptr2
                while ptr2 < len(abbr) and abbr[ptr2].isdigit():
                    ptr2 += 1
                ptr1 += int(abbr[origin:ptr2])
            else:
                if ptr1 >= len(word) or word[ptr1] != abbr[ptr2]: return False
                
                ptr1 += 1
                ptr2 += 1

        return ptr1 == len(word)

        
if __name__ == "__main__":
    sol = Solution()
    # print(sol.validWordAbbreviation("internationalization", "i12iz4n"))
    # print(sol.validWordAbbreviation("apple", "a2e"))
    print(sol.validWordAbbreviation("internationalization", "i5a11o1"))


# Iterate through the abbreviation because it might be longer than the word. Have 2 pointers for the word and the abbreviation.
# If ptr2 is a digit then keep track of the number formed by the digits. If the number starts at 0 then it's invalid.
# Add that number to ptr1
# If ptr1 exceeds the word length before ptr2 finishes or the letters at the indices don't match then return false. Otherwise increment both.
# We return whether we've reached the end of the word exactly


# ---- File: 40_combination_sum_2.py ----
class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtracking(index, target, arr):
            if target == 0:
                res.append(arr[:])
                return
            
            if target < 0:
                return
            
            for i in range(index, len(candidates)):
                if i != index and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                backtracking(i + 1, target - candidates[i], arr)
                arr.pop()

        backtracking(0, target, [])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
    print(sol.combinationSum2([1,2], 4))

# Do backtracking on a sorted array. Avoid duplicates with i != index and candidates[i] == candidates[i - 1], signifying the start has to be different each time

# ---- File: 415_add_strings.py ----
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        ptr1 = len(num1) - 1
        ptr2 = len(num2) - 1
        res = ""
        carry = 0
        sum = 0
        while ptr1 >= 0:
            sum = int(num1[ptr1]) + int(num2[ptr2]) + carry
            carry, digit = divmod(sum, 10)
            res = str(digit) + res
            ptr1 -= 1
            ptr2 -= 1
        
        while ptr2 >= 0:
            sum = int(num2[ptr2]) + carry
            carry, digit = divmod(sum, 10)
            res = str(digit) + res
            ptr2 -= 1

        return res if carry == 0 else "1" + res
    
# Do 2 pointers iterating backwards from each num. Take note of the carry when the sum > 10.
# Swap num2 with num1 if len(num1) is larger so num2 is always larger. It's easier to iterate when 1 pointer runs out that way


# ---- File: 419_battleships_in_a_board.py ----
class Solution:
    def countBattleships(self, board) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    res += 1
                    if i >= 1 and board[i - 1][j] == "X":
                        res -= 1
                    elif j >= 1 and board[i][j - 1] == "X":
                        res -= 1

        return res
    
# Every time we see an X, increment the result. If the left or above neighbor is an X and our current cell is an X then decrement the counter to avoid duplicates.

# ---- File: 426_convert_BST_to_doubly_linked_list.py ----
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        if not self.prev:
            self.head.right = root
        if self.prev:
            self.prev.right = root
        root.left = self.prev
        self.prev = root
        self.inorder(root.right)

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        self.head = ListNode(0)
        self.prev = None
        self.inorder(root)
        self.prev.right = self.head.right
        self.head.right.left = self.prev

        return self.head.right
    
# Because we want a sorted list from a BST, we have to do inorder traversal on the BST.
# We save a prev variable to store the node that we processed last so we may update its right pointer to the current node and our current node's left to be prev
# By default, prev is null, so if prev is null we connect the head node to the first node we process
# After the DFS, we reach the "tail" of the doubly linked list. We connect this tail to the head's right pointer, which is the first node of the list
# and we connect the node that the head points to's left pointer to be the tail so it creates the desired cycle.

# ---- File: 42_trapping_rain_water.py ----
class Solution:
    def trap_dp(self, height):
        if not height: return 0
        n = len(height)
        left_max = [-1e9]*n
        right_max = [-1e9]*n
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])
            right_max[-i - 1] = max(right_max[-i], height[-i])
        
        res = 0
        for i in range(1, n):
            res += max(0, min(left_max[i], right_max[i]) - height[i])
        
        return res
    

    def trap(self, height) -> int:
        if not height: return 0
        left_max = height[0]
        right_max = height[-1]
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            print(left, right, res, left_max, right_max)
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    #print(sol.trap([7, 0, 3, 0, 5, 0, 6]))

# From the figure in dynamic programming approach, notice that as long as right_max[i]>left_max[i] (from element 0 to 6), the water trapped depends upon the left_max, 
# and similar is the case when left_max[i]>right_max[i] (from element 8 to 11).
# So, we can say that if there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction 
# (from left to right). As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left).
# We must maintain left_max and right_max during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.

# ---- File: 432_all_o_1_data_structure.py ----
class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        self.head = Node(-1e9)
        self.tail = Node(1e9)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.map = {}

    def inc(self, key: str) -> None:
        if key in self.map:
            cur = self.map[key]
            freq = cur.freq
            cur.keys.remove(key)

            if cur.next.freq != freq + 1:
                new = Node(freq + 1)
                new.next = cur.next
                new.prev = cur

                cur.next.prev = new
                cur.next = new
                new.keys.add(key)
                self.map[key] = new

            else:
                cur.next.keys.add(key)
                self.map[key] = cur.next

            if not cur.keys:
                self.remove(cur)
        else:
            if self.head.next.freq > 1:
                new = Node(1)
                new.next = self.head.next
                self.head.next.prev = new

                new.prev = self.head
                self.head.next = new

                new.keys.add(key)
                self.map[key] = new
            else:
                self.head.next.keys.add(key)
                self.map[key] = self.head.next

        
    def dec(self, key: str) -> None:
        if key not in self.map:
            return  # Key does not exist

        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            # Remove the key from the map if freq is 1
            del self.map[key]
        else:
            prevNode = node.prev
            if prevNode.freq != freq - 1:
                # Create a new node if the previous node does not exist or freq is not freq - 1
                newNode = Node(freq - 1)
                newNode.keys.add(key)
                newNode.prev = prevNode
                newNode.next = node
                prevNode.next = newNode
                node.prev = newNode
                self.map[key] = newNode
            else:
                # Decrement the existing previous node
                prevNode.keys.add(key)
                self.map[key] = prevNode

        # Remove the node if it has no keys left
        if not node.keys:
            self.remove(node)
        
    
    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev        

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head: return ""
        return list(self.tail.prev.keys)[0]
        

    def getMinKey(self) -> str:
        if self.head.next == self.tail: return ""
        return list(self.head.next.keys)[0]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# Use a doubly linked list where the head has the min key and the tail has the max key
# Whenever we increment, if the key doesn't exist then it is either the new head with freq 1 or add the key to the node with freq 1
# If it does exist then find its node and create a node with freq + 1 if it doesn't exist or add it to the node with freq 1
# Do the same with decrement, except when freq = 0 we remove the node from the hash table storing the node's key

# If at any point a node doesn't have any keys, remove it from the linked list


# ---- File: 43_multiply_strings.py ----
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        power_out = 1
        for i in range(len(num2) - 1, -1, -1):
            power_in = 1
            inner_sum = 0
            for j in range(len(num1) - 1, -1, -1):
                prod = int(num1[j]) * int(num2[i]) * power_in
                inner_sum += prod
                power_in *= 10

            res += inner_sum * power_out
            power_out *= 10

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("123", "456"))

# Multiply a multiplier by 10 every time we move to the left

# ---- File: 443_string_compression.py ----
class Solution:
    def compress(self, chars: List[str]) -> int:
        ptr = 0
        count = 0
        cur_char = chars[0]

        def compress_count():
            nonlocal ptr
            chars[ptr] = cur_char
            ptr += 1
            if count != 1:
                for ch in str(count):
                    chars[ptr] = ch
                    ptr += 1
        for i in range(len(chars)):
            if chars[i] == cur_char:
                count += 1
            else:
                compress_count()
                count = 1
                cur_char = chars[i]

        compress_count()
        return ptr
    
# Use 1 pointer to store the current position on the compressed array. Keep track of the current character we're processing as well.
# Each time the character is different from the current character, do compress_count. compress_count first updates chars[ptr] to be the previous character.
# Then it moves ptr forward while updating the elements to be the count.
# Do compress_count again at the end to account for the final character
        


# ---- File: 44_wildcard_matching.py ----
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "*" or p == "*" or p == s: return True
        len_s = len(s)
        len_p = len(p)
        dp = [[False for i in range(len_p + 1)] for j in range(len_s + 1)]
        dp[0][0] = True
        for i in range(1, len_p + 1):
            if p[i - 1] == "*" and dp[0][i - 1]:
                dp[0][i] = True

        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        return dp[-1][-1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a"))
    print(sol.isMatch("aa", "*"))
    print(sol.isMatch("cb", "?a"))
    print(sol.isMatch("abcdde", "a?*e"))

# Recurrence relation: dp(i, j) = whether you can match s[:i + 1] with p[:j + 1]. Initialize with empty string as well for i - 1, j - cases
# dp(0, 0) = True since 2 empty strings match each other.
# If s[i - 1] == p[j - 1] or p[j - 1] == ? then we rely on dp(i - 1, j - 1) to determine whether dp(i, j) is true or not
# If p[j - 1] == "*" then either it can be empty (check dp(i, j - 1)/where you don't include the character in p) or it can replace a character in s (check dp(i - 1, j))



# ---- File: 450_delete_node_in_bst.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, root: TreeNode) -> int:
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root: TreeNode) -> int:
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        if key == root.val:
            if not root.left and not root.right: return None
            
            if root.right:
                root.val = self.successor(root.right)
                root.right = self.deleteNode(root.right, root.val)

            else:
                root.val = self.predecessor(root.left)
                root.left = self.deleteNode(root.left, root.val)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root


# When we remove a node from the BST, the one to take its place would be the first node smaller than it or the first node larger than it.
# In other words, it will be the rightmost child of its left child, or the leftmost child of its right child

# If the key is smaller than the root than traverse the left subtree, otherwise traverse the right subtree
# If key == root.val then find the predecessor (rightmost child of its left child) or the successor (leftmost child of its right child), whichever one's available.
# If neither is available then this is a leaf, so just return null
# Otherwise, replace the current node's val with the predecessor/successor's val, then remove that val by traversing the corresponding subtree it's in.

# ---- File: 451_sort_chars_by_frequency.py ----
class Solution:
    def frequencySort(self, s: str) -> str:
        sort_count = sorted([(val, ch) for (ch, val) in Counter(s).items()], reverse=True)
        res = ""
        for (val, ch) in sort_count:
            res += val * ch
        return res
    
# Sort characters by counters in reverse

# ---- File: 453_min_moves_to_make_array_equal.py ----
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if min(nums) == max(nums): return 0
        minimum = min(nums)
        res = sum([num - minimum for num in nums])
        return res
    
# Instead of thinking it like increasing every number except 1, we should decrement 1 element and leave the rest the same instead.
# Thus, the min moves is the moves it takes to reduce every number to the minimum of the array

# ---- File: 45_jump_game_2.py ----
class Solution:
    def jump(self, nums) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            furthest = 0

            for i in range(l, r + 1):
                furthest = max(furthest, nums[i] + i)
            
            l = r + 1
            r = furthest
            res += 1
        return res
    
# At each step, consider a window that's basically the steps we can jump to. Inside the window, find the step that jumps the furthest,
# that would be the right border of our new window. The new left border would be the previous right border + 1.
# The number of windows we create aside from the first one at 0, 0 is the number of steps we take to get to the final index

# ---- File: 468_validate_ip_address.py ----
class Solution:
    def validate_ipv4(self, tokens):
        for token in tokens:
            if not token or len(token) > 3: return False
            if len(token) > 1 and token[0] == "0": return False
            num = 0
            for i in range(len(token)):
                if not token[i].isdigit():
                    return False

                num = num * 10 + int(token[i])
            if num > 255: return False

        return True

    def validate_ipv6(self, tokens):
        for token in tokens:
            if not token or len(token) > 4: return False
            for i in range(len(token)):
                if token[i].isalpha() and not ("a" <= token[i].lower() <= "f"):
                    return False
        return True

    def validIPAddress(self, queryIP: str) -> str:
        dot_tokens = queryIP.split(".")
        if len(dot_tokens) == 4:
            return "IPv4" if self.validate_ipv4(dot_tokens) else "Neither"
        else:
            colon_tokens = queryIP.split(":")
            if len(colon_tokens) == 8:
                return "IPv6" if self.validate_ipv6(colon_tokens) else "Neither"
        return "Neither"

# ---- File: 46_permutations.py ----
class Solution:
    def permute(self, nums):
        res = []
        def backtracking(index):
            if index == len(nums):
                res.append(nums[:])
                return
            
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtracking(index + 1)
                nums[i], nums[index] = nums[index], nums[i]
        backtracking(0)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))

# Do backtracking. Starting from an index, swap the number at that index with every number after and recurse on that.

# ---- File: 480_sliding_window_median.py ----
import heapq
from collections import defaultdict

class Solution:
    def k_largest(self, nums, k, end):
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:end]:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap
    
    def k_smallest(self, nums, k, end):
        heap = [-num for num in nums[:k]]
        heapq.heapify(heap)
        for num in nums[k:end]:
            if -heap[0] > num:
                heapq.heappop(heap)
                heapq.heappush(heap, -num)

        return heap
    
    def medianSlidingWindow(self, nums, k: int):
        if k == 1: return nums
        max_heap = self.k_smallest(nums, k // 2, k) if k % 2 == 0 else self.k_smallest(nums, k // 2 + 1, k)
        min_heap = self.k_largest(nums, k // 2, k)
        removed = defaultdict(int)
        median = 1
        if k % 2 == 0:
            median = (-max_heap[0] + min_heap[0]) / 2
        else:
            median = -max_heap[0]
        res = []
        res.append(median)
        for i in range(k, len(nums)):
            prev = nums[i - k]
            removed[prev] += 1

            balance = -1 if prev <= median else 1
            if nums[i] <= median:
                balance += 1
                heapq.heappush(max_heap, -nums[i])
            else:
                balance -= 1
                heapq.heappush(min_heap, nums[i])

            if balance < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            elif balance > 0:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

            while max_heap and removed[-max_heap[0]] > 0:
                removed[-max_heap[0]] -= 1
                heapq.heappop(max_heap)

            while min_heap and removed[min_heap[0]] > 0:
                removed[min_heap[0]] -= 1
                heapq.heappop(min_heap)

            if k % 2 == 0:
                median = (-max_heap[0] + min_heap[0]) / 2
            else:
                median = -max_heap[0]

            res.append(median)
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    #print(sol.medianSlidingWindow([1,2,3,4,2,3,1,4,2], 3))


# Have a min heap that stores the largest k/2 elements in a window, and have a max heap that stores the smallest k/2 elements (k/2 + 1 if k is odd).
# The median is the top of the max heap or the average of the tops of the max + min heap. We calculate the median much more easily if we retrieve the top since it's O(1).
# Each time we move the window, we add the removed element into a hash table so that we may remove it from our heaps later.
# We also keep track of the "balance" of the heaps. Ideally, both heaps should have the same size or the max heap should have at most 1 more element than the min heap.

# If the removed element was in the max heap (less than the median) then the balance is -1 (representing the fact that we need an extra element in the max heap).
# Otherwise, it's 1 because we need an extra element in the min heap.

# Now we add a new element into one of the heaps. If it's less than the median then it should be in the max heap, and we increment the balance. Otherwise, put it in the min heap and decrement the balance.
# We observe that if the balance is not 0 then an element has to be moved from the larger heap to the smaller heap.
# We should also pop elements from the tops of the heaps if they should have been removed based on the pre-established hash table.
# Continue calculating the median like before.


# ---- File: 48_rotate_image.py ----
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            matrix[i] = matrix[i][::-1]

# Transpose then reverse every row


# ---- File: 490_the_maze.py ----
from collections import deque

DIRECTIONS = {"R": (0, 1), "D": (1, 0), "U": (-1, 0), "L": (0, -1)}

class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        if start == destination: return True
        m, n= len(maze), len(maze[0])

        queue = deque([(start[0], start[1])])

        visited = set()
        visited.add((start[0], start[1]))

        while queue:
            r, c = queue.popleft()
            if [r, c] == destination:
                return True
            
            for dir in DIRECTIONS:
                dr, dc = DIRECTIONS[dir]
                new_r = r
                new_c = c
                while 0 <= new_r + dr < m and 0 <= new_c + dc < n and maze[new_r + dr][new_c + dc] != 1:
                    new_r += dr
                    new_c += dc

                if (new_r, new_c) in visited:
                    continue

                visited.add((new_r, new_c))
                queue.append((new_r, new_c))

        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0, 4], [4, 4]))
    print(sol.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0, 4], [3, 2]))

# ---- File: 498_diagonal_traverse.py ----
class Solution:
    def valid(self, r, c, m, n):
        return 0 <= r < m and 0 <= c < n
    
    def findDiagonalOrder(self, mat):
        cur_r, cur_c = 0, 0
        m, n = len(mat), len(mat[0])
        dir = (-1, 1)
        res = []
        traversed = 0
        while traversed != m * n:
            res.append(mat[cur_r][cur_c])
            if not self.valid(cur_r + dir[0], cur_c + dir[1], m, n):
                if dir == (-1, 1):
                    if cur_c == n - 1:
                        cur_r += 1
                    else:
                        cur_c += 1
                else:
                    if cur_r == m - 1:
                        cur_c += 1
                    else:
                        cur_r += 1
                dir = (-1, 1) if dir == (1, -1) else (1, -1)
            else:
                cur_r += dir[0]
                cur_c += dir[1]
            traversed += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.findDiagonalOrder([[1,2],[3,4]]))

# We're always only going in 2 directions: up right (-1, 1) and down left (1, -1).
# If we can no longer go up right, we move to the right cell unless we can't anymore, then we move downward instead.
# If we can no longer go down left, we move to the downward cell unless we can't anymore, then we move right instead.
# Keep going until we've traversed every cell in the matrix




# ---- File: 49_group_anagrams.py ----
from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs):
        total = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for ch in str:
                count[ord(ch) - ord('a')] += 1

            total[tuple(count)].append(str)

        return list(total.values())

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# ---- File: 4_median_of_2_sorted_arrays.py ----
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        total_length = len(nums1) + len(nums2)
        half = total_length // 2
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            
        left, right = 0, len(nums2) - 1
        while True:
            mid = (left + right) // 2
            other = half - mid - 2
            
            two_left = nums2[mid] if mid >= 0 else -float('inf')
            two_right = nums2[mid+1] if mid + 1 < len(nums2) else float('inf')
            one_left = nums1[other] if other >= 0 else -float('inf')
            one_right = nums1[other + 1] if other + 1 < len(nums1) else float('inf')
            
            if two_left <= one_right and one_left <= two_right:
                if total_length % 2:
                    return min(two_right, one_right)
                else:
                    return (max(two_left, one_left) + min(one_right, two_right)) / 2
            elif two_left > one_right:
                right = mid - 1
            else:
                left = mid + 1
                
# We want to find the left partition of the combined sorted array.
# Do binary search on the smaller array. Find the midpoint m. Get half of the total length and subtract m from it to get a partition of the other array. Call this n
# If A[m] <= B[n + 1] and B[n] <= A[m + 1] then the subarrays form the left partition of the combined sorted array
# If A[m] > B[n + 1] then we need to push m back. Otherwise, move m forward.
# Account for edge cases when m or n are out of bounds



# ---- File: 50_my_pow.py ----
class Solution:
    def calc_power(self, x, n):
        if n == 0: return 1.0
        if n == 1: return x
        div = self.calc_power(x, n // 2)
        if n % 2 == 0:
            return div * div
        return div * div * x
    
    def myPow(self, x: float, n: int) -> float:
        return self.calc_power(x, n) if n >= 0 else self.calc_power(1/x, -n)

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.0000, 10))
    print(sol.myPow(2.0000, -2))

# The recurrence relation is x^n = x^(n/2) * x^(n/2), multiplied by x if n is odd. We use recursion in order to simulate this
# and solve the problem in O(logn)

# ---- File: 510_inorder_successor_of_bst_2.py ----
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
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent
    
# If the node has a right subtree, the successor is the leftmost node of the right subtree
# If it doesn't, it's somewhere in the parent. Keep climbing the tree until the current node is in the left subtree, then the parent is the successor

# ---- File: 516_longest_palindromic_subsequence.py ----
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for d in range(1, n):
            for i in range(n - d):
                j = d + i
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]
    
# If a number in the array is 0 then at first, the longest mirror symmetric subsequence would be itself since the center is 0. 
# If we compare 2 numbers in the array and they are the same, we check the subsequence between those 2 numbers and promptly update the max subsequence length 
# if the subsequence contains a 0. Otherwise, we check the 2 subsequences that do not contain each number respectively and get the max length between them.

# Let $DP[i, j]$ to be the length of the longest mirror symmetric subsequence for the subarray from index $i$ to index $j$. We want to find $DP[1, n]$. By default $DP[i, i]$ is 1 if $S[i] = 0$ and 0 otherwise since if a single number is 0 then itself is a symmetric subsequence.\\
# As mentioned above, if we compare 2 numbers $S[i]$ and $S[j]$ in the array and they are the same, then they can be candidates for a mirror symmetric subsequence. The other condition is that there is a 0 in-between them. We can elegantly check this by checking the subarray between those 2 numbers. If there was a 0 in it, then $DP[i + 1, j - 1]$ would be larger than 0 since it updates based on the max length of the previous mirror symmetric subsequence. And as established above, $DP[i, i] = 1$ if $S[i] = 0$, so the existence of 0 would cause all of the subarrays containing it to have 1 as the smallest possible length for a mirror symmetric subsequence.\\
# Otherwise, we'd get the max mirror symmetric subsequence length of the subarrays that don't contain $S[i]$ and $S[j]$ respectively since those could have different lengths depending on $S[i]$ and $S[j]$ being included in the subarray from $i + 1$ to $j - 1$. And this works if we fill out the DP table diagonally because to fill out $DP[i, j]$, we'd need the entry to the left of it representing $DP[i, j - 1]$, and the entry below it representing $DP[i + 1 ,j]$, and diagonal filling would ensure that those cells have the appropriate minimum values beforehand.\\
# Furthermore, we do not need to worry about cases of $DP[i, j]$ where $i > j$ since the start of a subarray has to be before its end.\\\\

# ---- File: 523_continuous_subarray_sum.py ----
class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        hash_sum = {0: -1}
        prefix_sum = 0
        for (i, num) in enumerate(nums):
            prefix_sum += num
            prefix_sum %= k
            if prefix_sum in hash_sum:
                if i - hash_sum[prefix_sum] >= 2:
                    return True
            
            else:
                hash_sum[prefix_sum] = i
        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkSubarraySum([23,2,4,6,7], 6))
    print(sol.checkSubarraySum([23,2,6,4,7], 6))
    print(sol.checkSubarraySum([23,2,4,6,7], 13))

# Use prefix sum since it's a problem related to subarray sum
# For prefix sums A and B with B being further than A.
# Notice that A % k = B % k if the a subarray with sum % k = 0 is added to A, aka the subarray divides by k. We use that info to find if there exists a good subarray

# ---- File: 525_contiguous_array.py ----
class Solution:
    def findMaxLength(self, nums) -> int:
        prefix_sum = {0: -1}
        sum = 0
        res = 0
        for (i, num) in enumerate(nums):
            sum += num if num else -1

            if sum in prefix_sum:
                res = max(res, i - prefix_sum[sum])
            else:
                prefix_sum[sum] = i
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxLength([0 ,1]))
    print(sol.findMaxLength([0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0]))

# Use prefix sum, increment by 1 whenever we see a 1, decrement by 1 whenever we see a 0.
# If we see multiple prefix sums of the same value, then the subarray between those is valid

# ---- File: 528_random_picks_with_weight.py ----
from bisect import bisect_right
from random import randrange

class Solution:

    def __init__(self, w):
        self.sum = 0
        self.pref_sum = []
        for num in w:
            self.sum += num
            self.pref_sum.append(self.sum)

    def pickIndex(self) -> int:
        if len(self.pref_sum) == 1: return 0
        rand = randrange(0, self.sum)
        return bisect_right(self.pref_sum, rand)        


if __name__ == "__main__":
    sol = Solution([3, 14, 1, 7])
    print(sol.pickIndex())
    

# Use prefix sum to help emulate the probabilities
# Use a random number generator to get a number, see where the number falls among the prefix sum array with binary search, and return the appropriate index
# The bigger the gap is between 2 numbers, the more likely it is that the random number will tip in favor of the larger number.

# ---- File: 529_minesweeper.py ----
DIRECTIONS = [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 1), (-1, 0), (-1, -1)]

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(r, c):
            mine_count = 0
            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c+ dc
                if not (0 <= new_r < len(board) and 0 <= new_c < len(board[0])):
                    continue

                if board[new_r][new_c] == "M":
                    mine_count += 1

            if mine_count:
                board[r][c] = str(mine_count)
                return
            
            board[r][c] = "B"
            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c+ dc
                if not (0 <= new_r < len(board) and 0 <= new_c < len(board[0])):
                    continue
                
                if board[new_r][new_c] != "E":
                    continue

                dfs(new_r, new_c)

            
        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"
        else:
            dfs(r, c)
        return board

# ---- File: 536_construct_binary_tree_from_string.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.index = 0

    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s: return None
        head = TreeNode()
        num = 0
        mult = 1
        has_left = False

        while self.index < len(s) and s[self.index] != ")":
            if s[self.index] == "-":
                mult = -1

            elif s[self.index].isdigit():
                num = num * 10 + int(s[self.index])
            
            elif s[self.index] == "(":
                head.val = num * mult
                self.index += 1
                if not has_left:
                    has_left = True
                    head.left = self.str2tree(s)
                else:
                    head.right = self.str2tree(s)
            self.index += 1
        head.val = num * mult
        return head
    
# Do recursion while keeping track of the index. If we see a digit then add it to our number. Once we find ( then initialize our head node
# to have num as a value, and assign left, right pointers to the recursive call starting from the next index after (
# If we see ) then we break. At the end, have head be the num.

# ---- File: 539_minimum_time_difference.py ----
from itertools import pairwise

class Solution:
    def findMinDifference(self, timePoints) -> int:
        for (i, time) in enumerate(timePoints):
            hour, minute = time.split(":")
            timePoints[i] = int(hour)*60 + int(minute)
        timePoints.sort()
        timePoints.append(timePoints[0] + 1440)
        res = min([(b - a) % 1440 for a, b in pairwise(timePoints)])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    # print(sol.findMinDifference(["23:59","00:00"]))
    # print(sol.findMinDifference(["23:59","00:00", "00:00"]))
    # print(sol.findMinDifference(["01:01","02:01"]))
    print(sol.findMinDifference(["02:39","10:26","21:43"]))
        

# ---- File: 53_maximum_subarray.py ----
class Solution:
    def maxSubArray(self, nums) -> int:
        prev_max = nums[0]
        res = nums[0]
        for num in nums[1:]:
            prev_max = max(prev_max + num, num)
            res = max(res, prev_max)
        return res
    
# Kadane's algorithm:
# To find the maximum subarray, at each index, the max is the max between the previous max subarray + the current num, or only the num.
# We try to find the maximum subarray ending at each num, essentially

# ---- File: 54_spiral_matrix.py ----
class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m - 1, 0, n - 1
        res = []
        while len(res) < m * n:
            for col in range(left, right + 1):
                res.append(matrix[up][col])
        
            for row in range(up + 1, down + 1):
                res.append(matrix[row][right])

            if up != down:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down][col])

            if left != right:
                for row in range(down - 1, up, -1):
                    res.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1
            
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))


# Traverse with borders in place. Make sure to check up != down and left != right to prevent doing it twice on the same row/column

# ---- File: 556_next_greater_element_2.py ----
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i == -1: return -1
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        
        left = i + 1
        right = len(digits) - 1
        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1

        res = int(''.join(map(str,digits)))
        return res if res <= 2**31 - 1 else -1

# It's Next Permutation.

# ---- File: 55_jump_game.py ----
class Solution:
    def canJump(self, nums) -> bool:
        max_step = 0
        furthest = len(nums) - 1

        for (i, num) in enumerate(nums):
            if i <= max_step:
                max_jump = i + num
                if max_jump >= furthest: return True

                max_step = max(max_jump, max_step)

            else:
                return False
        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2,3,1,1,4]))
    print(sol.canJump([3,2,1,0,4]))

# Store a variable called max_step. If our current index <= max_step, then we can reach that index. Otherwise, we cannot reach any index after, including the last, so return false
# At each step, we attempt to cover as much distance as possible. If our jump >= len(nums) - 1 then we can reach the finish line from the current index.
# Otherwise, we update the max_step variable to maximize the index we can reach

# ---- File: 560_subarray_sum_equals_k.py ----
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        sum = 0
        res = 0
        hash_sum = {0: 1}
        for num in nums:
            sum += num
            if sum not in hash_sum:
                hash_sum[sum] = 0
            
            if sum - k in hash_sum:
                res += hash_sum[sum - k]
            hash_sum[sum] += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1,1,1], 2))
    print(sol.subarraySum([1, 2, 3], 3))

# Use a hash table to store prefix sums. If prefix sum - k is already in the hash table then for the indices i it was incremented it, the subarrays from i + 1
# to the current index have subarray sum = k

# ---- File: 56_merge_intervals.py ----
class Solution:
    def merge(self, intervals):
        res = []
        intervals.sort()

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))

# Sort the intervals first. We only add intervals into the result array if it's empty at first or if the end of the last interval is smaller than the start
# of the next interval, because then it'd be 2 separate intervals that don't overlap.
# We update the end of the last interval to be the maximum of the following intervals' ends and the current end, since we know they overlap

# ---- File: 57_insert_interval.py ----
from bisect import bisect_left, insort_left
class Solution:
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
        res = []
        insort_left(intervals, newInterval)
        
        #intervals = intervals[:position] + [newInterval] + intervals[position:]
        for (start, end) in intervals:
            if res and res[-1][1] >= start:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])
        return res

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1,5]], [0, 1]))
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [5, 8]))
    print(sol.insert([[2,3],[5,7]], [0, 6]))
    print(sol.insert([[1,5]], [6, 8]))
    
# Use binary search to find where to fit the interval, sorted based on starting time
# Go through every interval and slowly add them to the result array. If a new interval were to be added but it overlaps with the most recent one, maximize the end.

# ---- File: 5_longest_palindromic_substring.py ----
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        start, end = 0, 0
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                end = i + 1
        for d in range(2, n):
            for i in range(n - d):
                j = d + i
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    end = j

        return s[start:end + 1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))
    print(sol.longestPalindrome("cbbd"))

# dp(i, j) is whether the substring from i to j forms a palindrome. At first, dp(i, i) = true and dp(i, i + 1) = true if they're the same
# Then, fill out the dp table diagonally. if s[i] == s[j] and the substring without those 2 characters is a palindrome, then the one with them would also be a palindrome.

# ---- File: 605_can_place_flowers.py ----
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ptr1 = -1
        for ptr2 in range(len(flowerbed)):
            if flowerbed[ptr2] == 1:
                gap = ptr2 - ptr1 - 1
                if ptr1 == -1:
                    gap += 1
                
                n -= ((gap - 1) // 2)

                ptr1 = ptr2
        
        gap = len(flowerbed) - ptr1 - 1
        if ptr1 == -1: gap += 1
        
        n -= (gap // 2)
        return n <= 0

# Find the gaps between every pair of 1s, including the first and last where we account for 1s outside of the array
# If ptr1 == -1 then add 1 to the gap since we have more gap when element 0 can have a flower pot
# Same goes for the last element


# ---- File: 616_add_bold_tag.py ----
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Solution:
    def addBoldTag(self, s: str, words) -> str:
        root = TrieNode()
        
        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                
                cur = cur.children[ch]
            
            cur.is_end = True

        is_bold = [False]*len(s)

        for i in range(len(s)):
            
            end = i
            cur = root
            for j in range(i, len(s)):
                ch = s[j]
                if ch not in cur.children:
                    break

                cur = cur.children[ch]
                if cur.is_end:
                    end = j + 1

            for j in range(i, end):
                is_bold[j] = True

        res = []

        for i in range(len(s)):
            if is_bold[i] and (i == 0 or not is_bold[i - 1]):
                res.append('<b>')

            res.append(s[i])

            if is_bold[i] and (i == len(s) - 1 or not is_bold[i + 1]):
                res.append('</b>')

        return "".join(res)
if __name__ == "__main__":
    sol = Solution()
    print(sol.addBoldTag("abcxyz123", ["abc","123"]))

# Have an array indicating which indices to bold
# Store all the dictionary words in a trie
# Iterate through each index of the word and attempt to find if a substring after it is in the trie. If so, mark every index in that window as true in the bold array

# ---- File: 632_smallest_range_covering_k_lists.py ----
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(lst[0], i, 0) for (i, lst) in enumerate(nums)]
        k = len(nums)
        max_val = max([nums[i][0] for i in range(k)])
        heapq.heapify(heap)
        left_res = -1e9
        right_res = 1e9
        
        while len(heap) == k:
            min_val, lst_idx, idx = heapq.heappop(heap)

            if max_val - min_val < right_res - left_res:
                left_res = min_val
                right_res = max_val

            if idx + 1 < len(nums[lst_idx]):
                heapq.heappush(heap, (nums[lst_idx][idx + 1], lst_idx, idx + 1))
                max_val = max(max_val, nums[lst_idx][idx + 1])

        return [left_res, right_res]
    
# It's merge K sorted lists. The heap always contains k elements so we find the min and max within the heap. The min is always the top,
# and the max is always the max of the current max and any element we push into the heap

# ---- File: 636_exclusive_time_of_functions.py ----
class Solution:
    def exclusiveTime(self, n: int, logs):
        res = [0]*n
        stack = []
        for log in logs:
            id, flag, time = log.split(":")
            time = int(time)
            if flag == "start":
                if stack:
                    stack[-1][2] += time - stack[-1][1] 
                stack.append([int(id), time, 0])
            elif flag == "end":
                id, last_start, runtime = stack.pop()
                runtime += time - last_start + 1
                res[id] += runtime
                if stack:
                    stack[-1][1] = time + 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
    print(sol.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
    print(sol.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))


# Since 2 functions can't be ran at once, we use a stack to update which function is running (aka the top of the stack).
# For each element/function in the stack, we store the id, the last time it started running, and its total runtime so far. We ignore the fact that
# multiple functions can have the same id

        

# ---- File: 63_unique_paths_2.py ----
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i - 1]
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(sol.uniquePathsWithObstacles([[0,1],[0,0]]))

# dp(i, j) = number of unique paths to get to (i, j).
# Recurrence relation:
# if grid(i, j) == 1 then there's no way to reach that cell, so dp(i, j) = 0
# otherwise, dp(i, j) = dp(i - 1, j) + dp(i, j - 1)
# Initialize with dp(0, 0) = 1 if it's not an obstacle
# The top row should be all 1s, unless there's an obstacle, then everything to its right including it is 0.
# The leftmost column should be all 1s, unless there's an obstacle, then everything below it including it is 0.


# ---- File: 642_design_search_autocomplete_system.py ----
from functools import cmp_to_key

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class AutocompleteSystem:
    def insert(self, sentence):
        cur = self.root
        for ch in sentence:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            
            cur = cur.children[ch]

        cur.is_end = True

    def update_input(self, ch):
        if self.invalid: return

        if ch not in self.input_node.children:
            self.invalid = True
        else:
            self.input_node = self.input_node.children[ch]
        
    def get_all_children(self, node, word):
        if node.is_end:
            self.word_list.append(word)
        
        if not node.children:
            return

        for children in node.children:
            self.get_all_children(node.children[children], word + children)

    def compare(self, sentence1, sentence2):
        if sentence1[0] < sentence2[0]:
            return 1
        elif sentence1[0] > sentence2[0]:
            return -1
        
        if sentence1[1] < sentence2[1]:
            return -1
        elif sentence1[1] > sentence2[1]:
            return 1
        
        return 0
        
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.frequencies = {sentence: time for (sentence, time) in zip(sentences, times)}
        for sentence in sentences:
            self.insert(sentence)

        self.input_so_far = ""
        self.input_node = self.root
        self.invalid = False
        self.word_list = []

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.insert(self.input_so_far)
            if self.input_so_far not in self.frequencies:
                self.frequencies[self.input_so_far] = 0
            self.frequencies[self.input_so_far] += 1
            
            self.input_so_far = ""
            self.input_node = self.root
            self.invalid = False

            return []
        
        self.input_so_far += c
        self.update_input(c)

        if self.invalid: return []
        self.get_all_children(self.input_node, self.input_so_far)
        
        child_sentences = []
        for word in self.word_list:
            child_sentences.append((self.frequencies[word], word))

        child_sentences = sorted(child_sentences, key=cmp_to_key(self.compare))
        res = []
        for i in range(min(3, len(child_sentences))):
            res.append(child_sentences[i][1])
        self.word_list = []
        return res


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

# Put all the sentences into a trie
# Store sentence frequencies in a hash table
# We have a node corresponding to the user input sentence.
# Each time a character c is taken in, we add it to a string called input_so_far. We'd also attempt to move the input node.
# If the character we added makes the input not a prefix of any of the sentences, then we no longer want to traverse the trie based on that sentence.
# We set a flag to see if this is true or not. If it's true then return [] every time.
# Otherwise, check all strings in the trie that has input_so_far as a prefix, aka do dfs with the latest character as the root.
# Once we have all the children, we sort their frequencies based on the hash table and find the top 3
# If the user inputs "#" then we add input_so_far into the trie and increment its count in the hash_table (0 by default), and reset input_so_far to be empty.

# Potential optimization:
# Instead of doing DFS every time we add a new character, we do DFS on the first character of the input and store all of its children.
# After that, every time we add a new character, we check every children to see if the new character would prevent the input string from being a prefix of any of them.


# ---- File: 658_find_k_closest_elements.py ----
import heapq

class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        heap = [(-abs(num - x), num) for num in arr[:k]]

        for num in arr[k:]:
            cur_diff = abs(num - x)
            if -heap[0][0] == cur_diff:
                if num < heap[0][1]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-cur_diff, num))
            elif -heap[0][0] > cur_diff:
                heapq.heappop(heap)
                heapq.heappush(heap, (-cur_diff, num))
                
        return sorted([i[1] for i in heap])
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k
        
        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
    
# Do a binary search to find the first element of the result window. Let this element be arr[mid]
# arr[mid] and arr[mid + k] cannot be in the same window together. Thus, we compare their differences with x.
# If the diff between arr[mid] and x is smaller than arr[mid + k] and x, then arr[mid + k] cannot be in the window, so we shrink right to mid
# Otherwise, shrink left to be mid + 1 as arr[mid] cannot be in the result window when its difference is larger than with arr[mid + k], who it cannot share the window with 
# We do if x - arr[mid] > arr[mid + k] - x since that checks for elements that have the same value the best. If x > arr[mid] then we ideally want to move the pointer from left to right,
# otherwise, move from right to left

# ---- File: 65_valid_number.py ----
class Solution:
    def sign_check(self, s):
        ptr = 0
        sign_count = 0
        while ptr < len(s) and s[ptr] in "+-":
            ptr += 1
            sign_count += 1
            if sign_count > 1: return (False, -1)
        return (True, ptr)

    def is_integer(self, s):
        flag, ptr = self.sign_check(s)
        if not flag: return False
        digit = False
        while ptr < len(s):
            if not s[ptr].isdigit(): return False
            ptr += 1
            digit = True

        return digit
    
    def is_decimal(self, s):
        dot_count = 0
        flag, ptr = self.sign_check(s)
        if not flag: return False

        digit = False
        while ptr < len(s):
            if s[ptr] == ".":
                dot_count += 1
            elif not s[ptr].isdigit(): return False
            digit = s[ptr].isdigit() or digit
            ptr += 1
        
        return digit and dot_count == 1
            
    def isNumber(self, s: str) -> bool:
        tokens = s.split("E") if "E" in s else s.split("e")
        if len(tokens) > 2: return False
        left = self.is_decimal(tokens[0]) if "." in tokens[0] else self.is_integer(tokens[0])
        return left if len(tokens) == 1 else left and self.is_integer(tokens[1])
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isNumber("0"))
    print(sol.isNumber("e"))
    print(sol.isNumber("."))
    print(sol.isNumber("--90E3"))
    print(sol.isNumber("99e2.5"))
    print(sol.isNumber("3."))

# We check whether a specified string is an integer or a decimal and have different cases accounting for them.
# For example, if there is an e in the string, we split the string based on it. If there are more than 2 splits then that
# means there are more than 2 es, so the string isn't a number
# If there is only 1 e, then we check the parts the string got split into.
# The second part has to be an integer, whereas the first can be either an integer or a decimal, depending on if "." is in it
# If there aren't any es, then check if the string is either an integer or a decimal, depending on if "." is in it

# A number can have an optional leading sign at the beginning. So we increment the counter until we've moved past the signs.
# If there is more than 1 sign then it's not valid (--, -+, +-, ++-, etc.)
# For the integer case, we check if the remaining string is full of digits or not. We have to ensure the existence of a digit and that there are only digits.
# For example, a case like "+" would return incorrectly if we forgo the existence of a digit.

# For the decimal case, we first check if there is more than 1 ".". If yes, return false. Next, we do the same as the integer case where we move past the sign
# We also have to ensure the existence of a digit in the remaining string. Iterate through the rest, if a character is not a digit or "." then return false
# Otherwise, return true if there exists a digit in the rest of the string after the iteration.

# ---- File: 670_maximum_swap.py ----
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [digit for digit in str(num)]
        n = len(digits)

        max_digit_index = -1
        swap_index_1, swap_index_2 = -1, -1
        for i in range(n - 1, -1, -1):
            if max_digit_index == -1 or digits[i] >= digits[max_digit_index]:
                max_digit_index = i
            elif digits[i] < digits[max_digit_index]:
                swap_index_1 = i
                swap_index_2 = max_digit_index
        
        if swap_index_1 != -1 and swap_index_2 != -1:
            digits[swap_index_1], digits[swap_index_2] = digits[swap_index_2], digits[swap_index_1]
            return int("".join(digits))
                
        return num

if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumSwap(2736))


# The idea is that we want to move the largest digit that's the furthest to the right to the left in order to maximize our number.
# We also want to push it left as far as possible, provided the number it's replacing is less than it.
# Find the index of the highest digit for right to left. Make sure there's also a digit to the left that's less than it.
# The 2 digits that we want to swap are the furthest right digit that's the largest and the furthest left digit that's smaller than it.

# ---- File: 692_top_k_frequent_words.py ----
import heapq
from collections import Counter

class Pair:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, p):
        return self.count < p.count or (self.count == p.count and self.word > p.word)

class Solution:
    def topKFrequent(self, words, k: int):
        count = Counter(words)
        freq = [Pair(word, cnt) for (word, cnt) in count.items()]
        heap = []
        for i in range(len(freq)):
            heapq.heappush(heap, freq[i])
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap).word)
        return res[::-1]
    
# Create a custom class with a custom __lt__ comparator so we can compare between 2 pairs of word, cnt. 1 pair is less than the other is its count is smaller, or
# its word is bigger when their counts are equal
# Use a min heap of size k to store the k most frequent strings

# ---- File: 6_zigzag_conversion.py ----
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = [[] for _ in range(numRows)]
        ptr = 0
        pos = -1
        while ptr < len(s):
            while ptr < len(s) and pos + 1 < numRows:
                pos += 1
                rows[pos].append(s[ptr])
                ptr += 1

            while ptr < len(s) and pos - 1 >= 0:
                pos -= 1
                rows[pos].append(s[ptr])
                ptr += 1

        res = ""
        for row in rows:
            res += "".join(row)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))
    print(sol.convert("PAYPALISHIRING", 4))
    print(sol.convert("A", 1))
            

# ---- File: 706_toeplitz_matrix.py ----
class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]: return False
        return True
    
# Check whether every cell is equal to its top left neighbor

# ---- File: 708_insert_node_into_sorted_circular_linked_list.py ----
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        if head.next == head:
            node = Node(insertVal, head)
            head.next = node
            return head

        prev = head
        cur = head.next
        insert = False
        while True:
            if prev.val <= insertVal <= cur.val: insert = True
            elif prev.val > cur.val:
                if insertVal >= prev.val or insertVal <= cur.val:
                    insert = True
            
            if insert:
                prev.next = Node(insertVal, cur)
                return head
            prev = cur
            cur = cur.next
            if prev == head: break
        prev.next = Node(insertVal, cur)
        return head
    
# Edge cases:
# Empty list -> return a new node that points to itself
# List with 1 node -> return the head that points to the new node and the new node points to the head
# Otherwise:
# Use 2 pointers for the previous node and current node.
# If prev.val <= insert <= cur.val then we can insert the node here to maintain order
# If prev.val > cur.val then we're at the end of the sorted list and looping back to the beginning. Here we can insert either the new largest node or the new smallest node.
# If neither of this happens then the max would be the same as the min of the list, so the list only has 1 value. Then we can insert the node anywhere in the list.

# ---- File: 71_simplify_path.py ----
class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == "/": return "/"
        directories = path.split("/")
        stack = []
        for dir in directories:
            if dir == "..":
                if stack: stack.pop()
            elif dir != '.' and dir != '':
                stack.append(dir)
        return '/' + '/'.join(stack)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/home//foo/"))
    print(sol.simplifyPath("/home/user/Documents/../Pictures"))
    print(sol.simplifyPath("/../"))
    print(sol.simplifyPath("/.../a/../b/c/../d/./"))


# Split the path into all of the possible directories separated by /
# For each non .. or . directory, we add it into a stack. If we encounter .., we pop the stack if it has an element.
# After that, join all of the elements of the stack with / and prepend / to it.

# ---- File: 721_accounts_merge.py ----
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def find(self, u):
        if self.parent[u] == u:
            return u
        return self.find(self.parent[u])

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if self.size[u] > self.size[v]:
                self.parent[v] = u
                self.size[u] += self.size[v]
            else:
                self.parent[u] = v
                self.size[v] += self.size[u]


class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        uf = DSU(n)
        email_group = defaultdict(int)
        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]

                if email not in email_group:
                    email_group[email] = i
                else:
                    uf.union(email_group[email], i)
    
        components = defaultdict(list)
        for email in email_group:
            group_index = email_group[email]
            parent = uf.find(group_index)
            components[parent].append(email)
        
        res = []
        for index in components:
            components[index].sort()
            res.append([accounts[index][0]] + components[index])
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))

# We assign each account to the index of the name in the bigger array. We will do DSU on these indices.
# We store each email to an index. If we come across that email again, we join this index and the index assigned to the email
# After all of the union is done, we check which emails are assigned to the parent of the index in the DSU.
# Sort the lists corresponding to each index that way and add the names to them, which can be traced using the index.

# ---- File: 723_candy_crush.py ----
class Solution:
    def candyCrush(self, board):
        m = len(board)
        n = len(board[0])
        def verify():
            nonlocal m, n
            flag = False
            for i in range(m):
                for j in range(n):
                    if board[i][j] != 0:
                        neg_cell = -abs(board[i][j])
                        if 0 < i < m - 1 and abs(board[i][j]) == abs(board[i - 1][j]) == abs(board[i + 1][j]):
                            board[i][j] = board[i - 1][j] = board[i + 1][j] = neg_cell
                            flag = True

                        if 0 < j < n - 1 and abs(board[i][j]) == abs(board[i][j - 1]) == abs(board[i][j + 1]):
                            board[i][j] = board[i][j - 1] = board[i][j + 1] = neg_cell
                            flag = True
            
            return flag
        
        def crush():
            nonlocal m, n
            for i in range(m):
                for j in range(n):
                    if board[i][j] < 0:
                        board[i][j] = 0

            
            for i in range(n):
                ptr1 = m - 1
                for j in range(m - 1, -1, -1):
                    if board[j][i] != 0:
                        board[j][i], board[ptr1][i] = board[ptr1][i], board[j][i]
                        ptr1 -= 1
            
            
        flag = verify()
        while flag:
            crush()
            flag = verify()

        return board
if __name__ == "__main__":
    sol = Solution()
    print(sol.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))
                
# Crush candies by marking ones with same adjacent absolute neighbors as negative first, then 0
# Do 2 pointers on each column from bottom to top to move all the 0s up

# ---- File: 725_split_linked_list_in_parts.py ----
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        list_len = 0
        while cur:
            cur = cur.next
            list_len += 1
        res = []
        extra = list_len % k
        sublist_len = list_len // k if not extra else list_len // k + 1

        prev = None
        cur = head
        first = True
        count = 0
        while cur:
            if count == sublist_len:
                first = True
                extra -= 1
                count = 0
                prev.next = None
                if extra == 0:
                    sublist_len -= 1
                    
            if first:
                first = False
                res.append(cur)
            count += 1
            prev = cur
            cur = cur.next

        while len(res) < k:
            res.append(None)
        return res
    
# Length of each list is n // k, except the first n % k lists, which have an extra node
# Every time we have a counter reach n // k, set the previous node's pointer to be None (aka the tail of the first split linked list), and reset the counter

# ---- File: 735_asteroid_collision.py ----
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            neg_destroyed = False
            while stack and asteroid < 0 < stack[-1] and not neg_destroyed:
                if -asteroid == stack[-1]:
                    stack.pop()
                    neg_destroyed = True
                elif -asteroid > stack[-1]:
                    stack.pop()
                else:
                    neg_destroyed = True

            if not neg_destroyed or asteroid >= 0:
                stack.append(asteroid)
        return stack
    
# If we see a negative asteroid and the top of the stack has a positive asteroid,
# we attempt to keep popping the stack until the negative asteroid is destroyed. However,
# if the negative asteroid destroys all of the positive asteroids then it is appended to the stack. If an asteroid is positive then it is added

# ---- File: 739_daily_temperatures.py ----
class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0]*len(temperatures)
        for (i, temp) in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                res[index] = i - index

            stack.append(i)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))

# Mono decreasing stack to keep track of temps. Whenever a temp is popped, check its index, and increase the index-th element of the result by i - index

# ---- File: 73_set_matrix_zeroes.py ----
class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(R):
                matrix[i][0] = 0

# ---- File: 75_sort_colors.py ----
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[zero_ptr], nums[i] = nums[i], nums[zero_ptr]
                zero_ptr += 1

        for i in range(zero_ptr, len(nums)):
            if nums[i] == 1:
                nums[zero_ptr], nums[i] = nums[i], nums[zero_ptr]
                zero_ptr += 1
        
# Use 2 pointers. Every time you encounter 0, move it to the first pointer and increment it. After all of the 0s have been moved to
# the beginning, do the same but with 1 instead, starting from where the first pointer left off

# ---- File: 767_reorganize_string.py ----
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count_letter = Counter(s)
        freq = [(-val, letter) for (letter, val) in count_letter.items()]
        heapq.heapify(freq)

        res = ""
        while len(freq) > 1:
            val_first, first = freq.pop(0)
            val_second, second = freq.pop(0)

            val_first += 1
            val_second += 1
            res += first + second

            if val_first != 0:
                heapq.heappush(freq, (val_first, first))
            
            if val_second != 0:
                heapq.heappush(freq, (val_second, second))

            heapq.heapify(freq)

        if not freq: return res
        if len(freq) == 1 and freq[0][0] == -1: return res + freq[0][1]
        return ""
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.reorganizeString("aab"))
    print(sol.reorganizeString("aaab"))
    print(sol.reorganizeString("vvvlo"))
    print(sol.reorganizeString("zrhmhyevkojpsegvwolkpystdnkyhcjrdvqtyhucxdcwm"))

# Have a heap that stores the counts of all the letters in the original string
# Alternately place the 2 most frequent letters of the string at a time
# If the heap is empty, return the string
# If the heap has 1 element left and that element's frequency is 1, add it to the string and return it
# Return an empty string otherwise

# ---- File: 76_minimum_window_substring.py ----
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        required = len(t_count)
        s_count = defaultdict(int)
        res = [float('inf'), 0, 0]
        left = 0
        match = 0
        for i in range(len(s)):
            s_count[s[i]] += 1
            if s[i] in t_count and s_count[s[i]] == t_count[s[i]]: match += 1

            while match == required:
                if res[0] > i - left + 1:
                    res = [i - left + 1, left, i]
                
                s_count[s[left]] -= 1
                
                if s[left] in t_count and s_count[s[left]] < t_count[s[left]]: match -= 1
                left += 1

        return s[res[1]:res[2]+1] if res[0] != float('inf') else ""

if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))

# Use a hash set for both s and t, and the sliding window approach
# Keep track of when the number of characters within s_count matches the number of characters within t_count. When that happens, shrink the window
# while updating the number of matches accordingly. We also update the result indices that contain the shortest substring that satisfies the condition.

# ---- File: 78_subsets.py ----
class Solution:
    # def subsets(self, nums):
    #     res = []
    #     n = len(nums)
    #     def backtrack(first = 0, arr = []):
    #         if len(arr) == max_len:
    #             res.append(arr[:])
    #             return
            
    #         for i in range(first, n):
    #             arr.append(nums[i])
    #             backtrack(i + 1, arr)
    #             arr.remove(nums[i])

        
    #     for max_len in range(n+1):
    #         backtrack()
        
    #     return res
    
    def subsets(self, nums):
        res = []
        n = len(nums)
        for bitmask in range(1 << n):
            subset = []
            for i in range(n):
                if (1 << i) & bitmask: subset.append(nums[i])
            res.append(subset)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3])) 

# At each index, we have a choice of whether to include it or not in our subset.
# As such, use a bitmask to keep track of which number to include. For every bitmask from 0 to 2 ** n - 1, if the i-th bit is 1 then include nums[i]


# ---- File: 791_custom_sort_string.py ----
from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        res = ""
        for ch in order:
            if ch in s_count:
                res += ch * s_count[ch]
                s_count[ch] = 0
        for ch in s:
            if s_count[ch]:
                s_count[ch] -= 1
                res += ch
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.customSortString("cba", "abcd"))
    print(sol.customSortString("bcafg", "abcd"))
    print(sol.customSortString("kqep", "pekeq"))


# Iterate through each character in order and see if it exists in s
# If it does, append every single instance of that character into the final string and set the frequency to 0.
# Once we're done with the order, just append any remaining characters in s that haven't been added yet

# ---- File: 796_rotate_string.py ----
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        concat = s + s
        return concat.find(goal) != -1
    
# If the lengths are different then return false
# Concatenate s and s together. If goal isn't a substring in the concatenated string then return false

# ---- File: 79_word_search.py ----
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(r, c, idx):
            if idx == len(word):
                return True
    
            ch = board[r][c]
            board[r][c] = "!"
            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c + dc

                if not (0 <= new_r < len(board) and 0 <= new_c < len(board[0])):
                    continue

                
                if board[new_r][new_c] == word[idx]:
                    if dfs(new_r, new_c, idx + 1):
                        return True
            board[r][c] = ch
            return False
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1): return True

        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
    print(sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))

# Do backtracking starting from the first character of the word. Only traverse to neighbors that's equal to the next index of the word
# Change the current square to an invalid character so we don't have to visit it again, and change it back to normal after we're done traversing its neighbors,
# so that others will have an accurate value

# ---- File: 80_remove_dupes_from_sorted_array_2.py ----
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 1e9
        prev_count = 0
        ptr = 0
        for i in range(len(nums)):
            if nums[i] == prev and prev_count == 2:
                continue
            
            if nums[i] != prev:
                prev_count = 0

            prev_count += 1
            prev = nums[i]
            nums[ptr] = nums[i]
            ptr += 1
        return ptr
    
# Have a pointer to keep track of where we're overwriting some elements in num, call it ptr. Have 2 variables to store the previous value and its count
# Iterate through the array. If the cur num == previous and the count == 2, then we skip this index
# Otherwise, increment prev_count and nums[ptr] = nums[i], and ptr += 1. This means that ptr would not count the duplicate elements after the count exceeds 2,
# so it stays behind. Reset prev_count if the curretn num != prev

# ---- File: 814_binary_tree_pruning.py ----
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if not root.left and not root.right and not root.val:
            return None
        
        return root
    
# If both subtrees are empty and the root itself isn't 0 then prune it by returning null, otherwise return the root

# ---- File: 825_friends_of_appropriate_ages.py ----
from bisect import bisect_right
from collections import Counter
class Solution:
    def numFriendRequests(self, ages) -> int:
        ages.sort()
        res = 0
        for age in ages:
            right = bisect_right(ages, age)
            left = bisect_right(ages, 0.5 * age + 7) + 1
            res += max(0, right - left)

        return res
    
    def numFriendRequests(self, ages):
        count = Counter(ages)
        ans = 0
        for ageA, countA in count.items(): 
            for ageB, countB in count.items():
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans
    
# For each age, do a binary search to find the highest index i where every element from 0 to i - 1 <= age, and the highest index i
# where every element from 0 to i - 1 < 0.5 * age + 7. That is the range of the friends we can send requests to. If left > right then add 0

# O(N):
# Keep track of the frequencies for every age.
# Do a nested for loop through every pair of ages.
# If ageA can add ageB then we increment the result by the count of ageA * the count of ageB. If ageA = ageB then we subtract it by the count of ageA because
# people can't add themselves as friends.


# ---- File: 827_making_a_large_island.py ----
from collections import defaultdict

DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        def dfs(r, c, index):
            nonlocal n
            grid[r][c] = index
            total_area = 1

            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c + dc

                if not (0 <= new_r < n and 0 <= new_c < n):
                    continue

                if grid[new_r][new_c] != 1:
                    continue

                total_area += dfs(new_r, new_c, index)
            
            return total_area

        area = defaultdict(int)
        index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = dfs(i, j, index)
                    index += 1
        
        res = max(area.values()) if area else 0

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbors = set()
                    for dr, dc in DIRECTIONS:
                        new_r = r + dr
                        new_c = c + dc

                        if not (0 <= new_r < n and 0 <= new_c < n):
                            continue

                        if grid[new_r][new_c] == 0:
                            continue
                        
                        neighbors.add(grid[new_r][new_c])
                    
                    surround_sum = 0
                    for neighbor in neighbors:
                        surround_sum += area[neighbor]
                    
                    res = max(res, surround_sum + 1)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestIsland([[1,0],[0,1]]))
    print(sol.largestIsland([[1,1],[1,1]]))
# Do DSU to get the size of each island
# Set the coords of the cells with 1 to be the root. This will be the identifier for an island
# Go through all the 0 cells, and check the neighbors. Add up the sizes of the unique islands + 1

# ---- File: 84_largest_rectangle_in_histogram.py ----
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for (i, h) in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start = index
            
            stack.append((start, h))
        
        for (i, h) in stack:
            res = max(res, h * (len(heights) - i))
        return res
    
# Use a mono increasing stack. For each height, store its start index, aka where it can expand to to the left (the first height larger than it).
# When we pop a height, its max range is its height * width (width = the current index - start)
# Do the same w/ the remaining elements in the monostack

# ---- File: 863_all_nodes_distance_k_binary_tree.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def set_parents(self, root):
        if not root:
            return

        if root.left:
            self.parent[root.left] = root
            self.set_parents(root.left)

        if root.right:
            self.parent[root.right] = root
            self.set_parents(root.right)


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent = {}

        self.set_parents(root)
        queue = [(target, 0)]
        res = []
        visited = set([target.val])
        while queue:
            node, dist = queue.pop(0)

            if dist == k:
                res.append(node.val)

            if node.left and node.left.val not in visited:
                queue.append((node.left, dist + 1))
                visited.add(node.left.val)

            if node.right and node.right.val not in visited:
                queue.append((node.right, dist + 1))
                visited.add(node.right.val)

            if node in self.parent and self.parent[node].val not in visited:
                queue.append((self.parent[node], dist + 1))
                visited.add(self.parent[node].val)

        return res
    
# Set up a hash table tracking the parent of every node, and then do BFS from the target

# ---- File: 864_shortest_path_to_get_all_keys.py ----
class Solution:
    def is_lock(self, value):
        return "A" <= value <= "F"
    
    def is_key(self, value):
        return "a" <= value <= "f"
    
    def unlockable(self, lock, keys):
        return keys & (1 << self.key_table[lock])

    def get_key(self, key_name, keys):
        return keys | (1 << self.key_table[key_name.upper()])
    
    def shortestPathAllKeys(self, grid) -> int:
        queue = []
        m, n = len(grid), len(grid[0])
        key_count = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    queue.append((i, j, 0, 0))
                    visited.add((i, j, 0))
                elif self.is_key(grid[i][j]):
                    key_count += 1

        self.key_table = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c, keys, dist = queue.pop(0)
            for (dr, dc) in directions:
                new_r = r + dr
                new_c = c + dc
                if not (0 <= new_r < m and 0 <= new_c < n):
                    continue

                if (new_r, new_c, keys) in visited:
                    continue
                
                new_cell = grid[new_r][new_c]
                if new_cell in ".@":
                    queue.append((new_r, new_c, keys, dist + 1))
                    visited.add((new_r, new_c, keys))

                elif self.is_lock(new_cell) and self.unlockable(new_cell, keys):
                    queue.append((new_r, new_c, keys, dist + 1))
                    visited.add((new_r, new_c, keys))
                
                elif self.is_key(new_cell):
                    new_keys = self.get_key(new_cell, keys)
                    queue.append((new_r, new_c, new_keys, dist + 1))
                    visited.add((new_r, new_c, new_keys))

                    if new_keys == (1 << key_count) - 1:
                        return dist + 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPathAllKeys(["@.a..","###.#","b.A.B"]))
    print(sol.shortestPathAllKeys(["@..aA","..B#.","....b"]))
    print(sol.shortestPathAllKeys(["@Aa"]))
    print(sol.shortestPathAllKeys(["@...a",".###A","b.BCc"]))

# Do BFS with a (r, c, keys) state. We store the keys we've picked up through a bitmask. We can go to the same (r, c) multiple times as
# long as we have a different set of keys each time.
# Every time we pick up a key, we update the bit for that respective key. Each letter has an index/bit corresponding to it.
# Every time we see a lock, we need to have the appropriate key for it. We can always look it up based on our hash table of indices.
# If we visit the final key, we return the distance we took to get there. Getting all keys would be the equivalent of all key bits being 1, or 2 ^ (key count) - 1.


# ---- File: 875_koko_eating_bananas.py ----
import math

class Solution:
    def eat_all(self, piles, speed, h):
        hours = 0
        for banana in piles:
            hours += math.ceil(banana / speed)
        return hours <= h
    
    def minEatingSpeed(self, piles, h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if self.eat_all(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return left
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([3,6,7,11], 8))
    print(sol.minEatingSpeed([30,11,23,4,20], 5))
    print(sol.minEatingSpeed([30,11,23,4,20], 6))

# Do binary search between 1 and the highest banana count to determine the smallest speed at which Koko can eat all the bananas
# Don't do it from min to max because it wouldn't work for a case where min = max

# ---- File: 885_spiral_matrix_3.py ----
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        traversed = []

        step = 1
        direction = 0
        while len(traversed) < rows * cols:
            # direction = 0 -> East, direction = 1 -> South
            # direction = 2 -> West, direction = 3 -> North
            for _ in range(2):
                for _ in range(step):
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        traversed.append([rStart, cStart])
                    rStart += dir[direction][0]
                    cStart += dir[direction][1]

                direction = (direction + 1) % 4
            step += 1
        return traversed
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralMatrixIII(1, 4, 0, 0))
    print(sol.spiralMatrixIII(5, 6, 1, 4))

# Each step of the way, we got east and south step number of steps, then increment step, then go west and north that amount, increment again, then repeat with east and south
# We can step out of the matrix, but only add cells to the result that are within the matrix

# ---- File: 88_merge_sorted_array.py ----
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        ptr1 = m - 1
        ptr2 = n - 1
        for i in range(m + n - 1, -1, -1):
            if ptr2 < 0: break
            if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1

# Use 3 pointers in this case, one to fill out/update nums1 that starts at the end of nums1, and 2 to iterate through the valid part of num1 and num2.
# p would be n spaces apart from p1, and p would never overtake p1
# If p2 < 0 then nums[p2] is larger than everything before nums[p1] at the current p1, so we break
# If p1 >= 0 and nums1[ptr1] > nums2[ptr2] then nums1[p] = nums1[p1]. p1 >= 0 is important because we might loop back to the end of nums1
# Otherwise, nums1[p] = nums2[p2] 


# ---- File: 8_string_to_integer_atoi.py ----
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s: return 0
        sign = 1
        ptr = 0
        res = 0
        while ptr < len(s) and s[ptr] == " ":
            ptr += 1
        
        if ptr >= len(s) or not (s[ptr] in "+-" or s[ptr].isdigit()):
            return res

        if s[ptr] in "+-":
            sign = -1 if s[ptr] == "-" else 1
            ptr += 1
        while ptr < len(s) and s[ptr].isdigit():
            res = res*10 + int(s[ptr])
            ptr += 1
        
        if sign == 1:
            res = min(2 ** 31 - 1, res)
        else:
            res *= -1
            res = max(-2 ** 31, res)
        return res

# Iterate through the first chunk of the array, skipping through whitespaces.
# After that, check the current character. If we're outside of the array or the character is neither a sign or a digit, then we're done
# Check the sign and change the integer according to it (1 being pos, -1 being neg)
# Iterate through the rest of the array until we hit a non-digit, add up res at the same time
# If it's pos, return the min of res and 2^31 - 1, otherwise it's the max of -res and -2 ** 31
# Handle edge cases!!!
# String only has whitespaces

# ---- File: 91_decode_ways.py ----
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0": return 0
        dp = [0]*n
        dp[0] = 1

        for i in range(1, n):
            if s[i] != "0":
                dp[i] = dp[i - 1]

            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2] if i > 1 else 1

        return dp[-1]
    
    # def numDecodings(self, s: str) -> int:
    #     n = len(s)
    #     if s[0] == "0": return 0
    #     cur = 1
    #     prev = 1
    #     prev_2 = 1
    #     for i in range(1, n):
    #         cur = 0
    #         if s[i] != "0":
    #             cur = prev

    #         if 10 <= int(s[i - 1:i + 1]) <= 26:
    #             cur += prev_2

    #         prev_2 = prev
    #         prev = cur
        
    #     return cur
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("10"))
    # print(sol.numDecodings("12"))
    
    # print(sol.numDecodings("226"))
    # print(sol.numDecodings("06"))

# dp(i) = number of ways to decode up to index i
# Recurrence relation:
# dp(i) += dp(i - 1) if s[i] is nonzero. The reason is that all of the previous valid decoders can now include the current character.
# dp(i) += dp(i - 2) if s[i - 1:i+1] is between 10 and 26. The reason is that all of the previous valid decoders can now include the current 2 characters.
# Very similar to climbing stairs. Could even do this in O(1) memory.

    




# ---- File: 921_min_add_valid_parentheses.py ----
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch in "()":
                if stack and stack[-1] == "(" and ch == ")":
                    stack.pop()
                else:
                    stack.append(ch)

        return len(stack)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minAddToMakeValid("())"))
    print(sol.minAddToMakeValid("((("))
    print(sol.minAddToMakeValid("()))(("))

# Use a stack to store the brackets that don't have a corresponding partner

# ---- File: 930_binary_subarrays_with_sum_goal.py ----
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref_sum = 0
        hash_sum = defaultdict(int)
        hash_sum[0] = 1
        res = 0
        for (i, num) in enumerate(nums):
            pref_sum += num
            if pref_sum - goal in hash_sum:
                res += hash_sum[pref_sum - goal]
            hash_sum[pref_sum] += 1
        return res
    
# Use a hash table to store prefix sums. If prefix sum - k is already in the hash table then for the indices i it was incremented it, the subarrays from i + 1
# to the current index have subarray sum = k

# ---- File: 934_shortest_bridge.py ----
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def shortestBridge(self, grid) -> int:
        n = len(grid)
        start_r, start_c = 0, 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    start_r = i
                    start_c = j
                    break
            
        
        visited = set()
        queue = []
        def dfs(r, c):
            visited.add((r, c))
            queue.append((r, c, 0))
            grid[r][c] = 2

            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c + dc
                if not (0 <= new_r < len(grid) and 0 <= new_c < len(grid)):
                    continue

                if (new_r, new_c) in visited:
                    continue

                if grid[new_r][new_c] == 0:
                    continue
                dfs(new_r, new_c)

        dfs(start_r, start_c)
        visited = set()
        while queue:
            r, c, dist = queue.pop(0)
            
            for dr, dc in DIRECTIONS:
                new_r = r + dr
                new_c = c + dc  
                
                if not (0 <= new_r < n and 0 <= new_c < n):
                    continue
                

                if (new_r, new_c) in visited:
                    continue
                
                if grid[new_r][new_c] == 1:
                    return dist
                
                if grid[new_r][new_c] != 0:
                    continue
                
                
                visited.add((new_r, new_c))
                queue.append((new_r, new_c, dist + 1))

        return -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestBridge([[0,1],[1,0]]))
    print(sol.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
    print(sol.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))

# ---- File: 93_restore_ip_addresses.py ----
class Solution:
    def restoreIpAddresses(self, s: str):
        if len(s) > 12: return []
        res = []
        def backtracking(first, dots, curIP):
            if dots == 3:
                remaining = s[first:]
                if 1 <= len(remaining) <= 3 and remaining:
                    if int(remaining) <= 255 and (first == len(s) - 1 or remaining[0] != "0"):
                        res.append(curIP + s[first:])
                return
            for i in range(first, min(first + 3, len(s))):
                if int(s[first:i+1]) <= 255 and (i == first or s[first] != "0"):
                    backtracking(i + 1, dots + 1, curIP + s[first:i+1] + ".")

        backtracking(0, 0, "")
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreIpAddresses("25525511135"))
    print(sol.restoreIpAddresses("101023"))

# For any index, attempt to put a dot in its position and the 2 positions after. The reason is that the max length of a number is 3 in an IP address.
# That number also has to be less than 255. If the length of the number is not 1 then it can't start with a 0 either. Then backtrack based on that number
# After we've placed 3 dots, we see if the rest of the string is a valid IP number. The length has to be between 1 and 3. If it's 0 then we placed a dot after the string, which is wrong.
# The number has to be less than 255 still and if the length is 1 then it can't start with a 0 either.
# If these are true, add the number along with the current IP to the result array

# ---- File: 953_verifying_an_alien_dictionary.py ----
class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        letters = {letter: i for (i, letter) in enumerate(order)}
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if letters[d] < letters[c]:
                        return False
                    else:
                        break
            else:
                if len(second_word) < len(first_word): return False

        return True
        
        
# Hash table to store the indices of every letter in the order
# Compare every consecutive pair in the words, and the letters at each index. If the second letter is before the first letter in the order, return false
# Otherwise, break the for loop
# If we make it through the for loop, verify that the first word is shorter than the second since the second could be a prefix

# ---- File: 958_check_completeness_of_binary_tree.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        levels = defaultdict(list)

        queue = [(root, 0)]
        level = 0
        while queue:
            for i in range(len(queue)):
                node, idx = queue.pop(0)
                levels[level].append(idx)
                if node.left:
                    queue.append((node.left, idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))
            
            if queue and len(levels[level]) != 2 ** level: return False
            if levels[level][0] != 0: return False
            for i in range(len(levels[level]) - 1):
                if levels[level][i] != levels[level][i + 1] - 1:
                    return False
            level += 1
        
        return True
    
# Store each level in hash table
# If the level isn't the last and its length is different from 2^level, return false
# If the first node in a level is not index 0 then return False
# Check every node in the level to see if it's 1 more than the previous.

# ---- File: 973_k_closest_to_origin.py ----
import math
import heapq

class Solution:
    def kClosest(self, points, k: int):
        dist = [(math.sqrt(x ** 2 + y ** 2), x, y) for (x, y) in points]
        heapq.heapify(dist)
        res = []
        while k:
            dst, x, y = heapq.heappop(dist)
            res.append([x, y])
            k -= 1

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1,3],[-2,2]], 1))
    print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))

# Save time:
# Use binary search from 0 to the max distance. For every midpoint, check how many distances are below that midpoint.
# If it's less than k then check the right subarray while reducing k since the remaining distances will be on the right.
# Otherwise, discard the right subarray.
# This is O(N)

# ---- File: 977_squares_of_sorted_array.py ----
class Solution:
    def sortedSquares(self, nums):
        negatives = []
        positives = []
        for num in nums:
            if num < 0: negatives.append(num)
            else: positives.append(num)

        res = []

        negatives.reverse()
        
        ptr1 = ptr2 = 0
        while ptr1 < len(negatives) and ptr2 < len(positives):
            if negatives[ptr1] ** 2 < positives[ptr2] ** 2:
                res.append(negatives[ptr1] ** 2)
                ptr1 += 1
            else:
                res.append(positives[ptr2] ** 2)
                ptr2 += 1

        while ptr1 < len(negatives):
            res.append(negatives[ptr1] ** 2)
            ptr1 += 1
        
        while ptr2 < len(positives):
            res.append(positives[ptr2] ** 2)
            ptr2 += 1

        return res

# ---- File: 983_minimum_cost_for_tickets.py ----
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(days[-1]+1)
        day_set = set(days)
        for i in range(1, len(dp)):
            if i in day_set:
                dp[i] = min(dp[max(i-1, 0)] + costs[0], dp[max(i-7, 0)] + costs[1], dp[max(i-30, 0)] + costs[2])
            else:
                dp[i] = dp[i-1]

        return dp[-1]
        
        
# dp(i) = min(dp(i - 1) + costs[0], dp(i - 7) + costs[1], dp(i - 30) + costs[2]) if i is a travel day
# dp(i) = dp(i - 1) otherwise

# ---- File: 986_interval_list_intersection.py ----
class Solution:
    def intervalIntersection(self, firstList, secondList):
        if not secondList or not firstList: return []
        ptr1 = ptr2 = 0
        res = []
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            start_1, end_1 = firstList[ptr1]
            start_2, end_2 = secondList[ptr2]
            max_start = max(start_1, start_2)
            min_end = min(end_1, end_2)
            if max_start <= min_end:
                res.append([max_start, min_end])
            if end_1 < end_2:
                ptr1 += 1
            else:
                ptr2 += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))

# Use 2 pointers for both list. Take the max start and min end of the 2 pointers to get the intersection. If max start < min end then we have an intersection
# Move the pointer of the interval with the smaller end because moving the one with the bigger while we already don't have an intersection won't get us an intersection
# Furthermore, one pointer would just be stuck.

# ---- File: 987_vertical_order_traversal_binary_tree.py ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, row, col):
        if not root: return
        self.min_col = min(self.min_col, col)
        self.max_col = max(self.max_col, col)
        self.cols[col].append((row, root.val))
        self.dfs(root.left, row + 1, col - 1)
        self.dfs(root.right, row + 1, col + 1)
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.min_col = 1e9
        self.max_col = -1e9
        self.cols = defaultdict(list)
        self.dfs(root, 0, 0)
        res = []
        for col in self.cols:
            self.cols[col].sort()
        for col in range(self.min_col, self.max_col + 1):
            cur = [val for (r, val) in self.cols[col]]
            res.append(cur)
        return res
        
# Do DFS and store the nodes in each column in a dict with a tuple (row, val)
# Sort each column at the end
# Each cell can have at most 1 collision so worst case scenario, just compare those 2 elements and figure out which one should go first

# Alternatively, do BFS. Use a dict with the column as they key and the value is a list of lists corresponding to each row
# We insert nodes into the list for a column based on its row. If a list has 2 elements (a collision), then compare which one is higher to put last

# Complexity should be O(N + W * H) with W and H being the width and height of the tree

# ---- File: cd_in_linux.py ----
class Solution:
    def simplifyPath(self, path, change) -> str:
        stack = []
        directories = path.split("/")
        for dir in directories:
            if dir != "":
                stack.append(dir)

        directories = change.split("/")

        for dir in directories:
            if dir == "" or dir == ".": continue

            if dir == "..":
                if stack:
                    stack.pop()
            
            else:
                stack.append(dir)

        return "/" + "/".join(stack)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/", "/facebook"))
    print(sol.simplifyPath("/facebook/anin", "../abc/def"))
    print(sol.simplifyPath("/facebook/instagram", "../../../."))

# ---- File: min_stickers_spell_word_singular.py ----
from collections import Counter
import math

class Solution:
    def minStickers(self, sticker, word) -> int:
        sticker_count = Counter(sticker)
        word_count = Counter(word)
        res = 0
        for letter in word_count:
            if letter not in sticker_count: return -1

            res = max(res, math.ceil(word_count[letter] / sticker_count[letter]))
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minStickers("banaasiofdjsodifjhsodif", "banana"))
