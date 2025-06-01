# Node class for doubly linked list
class ListNode:
    def __init__(self, key, value):
        self.key = key                     # Telugu: Ee node ki key value
        self.value = value                 # Telugu: Ee node ki actual data
        self.prev = None                   # Telugu: Previous node pointer
        self.next = None                   # Telugu: Next node pointer

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_map = dict()            # Telugu: Key -> Node mapping for O(1) access
        self.capacity = capacity           # Telugu: Maximum capacity of the cache

        # Telugu: Dummy head and tail nodes (simplify edge cases)
        self.head = ListNode(0, 0)         
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache_map:
            node = self.cache_map[key]

            # Telugu: Node ni list nundi remove cheyyadam
            self._remove_node(node)

            # Telugu: Node ni head degara insert cheyyadam (most recently used)
            self._insert_at_head(node)

            return node.value
        else:
            return -1  # Telugu: Key lekapote -1 return cheyyadam

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            # Telugu: Old node ni update cheyyadam
            node = self.cache_map[key]
            self._remove_node(node)
            node.value = value
            self._insert_at_head(node)
        else:
            # Telugu: Capacity reach ayite tail node ni remove cheyyadam
            if len(self.cache_map) >= self.capacity:
                self._remove_from_tail()

            # Telugu: New node create cheyyadam and head lo insert cheyyadam
            new_node = ListNode(key, value)
            self.cache_map[key] = new_node
            self._insert_at_head(new_node)

    def _remove_node(self, node: ListNode):
        # Telugu: Node ni double linked list nundi remove cheyyadam
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_at_head(self, node: ListNode):
        # Telugu: Head tarvata insert cheyyadam (most recently used)
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def _remove_from_tail(self):
        # Telugu: Least recently used node (tail.prev) ni remove cheyyadam
        if len(self.cache_map) == 0:
            return
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        del self.cache_map[tail_node.key]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def BFS(root):
            nonlocal min_column, max_column
            queue = deque([(root, 0, 0)])

            while queue:
                node, row, column = queue.popleft()

                if node is not None:
                    columnTable[column].append((row, node.val))
                    min_column = min(min_column, column)
                    max_column = max(max_column, column)

                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). BFS traversal
        BFS(root)

        # step 2). extract the values from the columnTable
        ret = []
        for col in range(min_column, max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def DFS(node, row, column):
            if node is not None:
                node_list.append((column, row, node.val))
                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        # step 1). construct the node list, with the coordinates
        DFS(root, 0, 0)

        # step 2). sort the node list globally, according to the coordinates
        node_list.sort()

        # step 3). retrieve the sorted results grouped by the column index
        ret = []
        curr_column_index = node_list[0][0]
        curr_column = []
        for column, row, value in node_list:
            if column == curr_column_index:
                curr_column.append(value)
            else:
                # end of a column, and start the next column
                ret.append(curr_column)
                curr_column_index = column
                curr_column = [value]
        # add the last column
        ret.append(curr_column)

        return ret

  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.matching_nodes_count = 0  # Telugu: Count maintain cheyyali

        def postorder(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # Telugu: Null unte 0 sum return cheyyadam

            # Telugu: Left subtree sum
            left_sum = postorder(node.left)

            # Telugu: Right subtree sum
            right_sum = postorder(node.right)

            # Telugu: Ee node ki match aite count increment cheyyadam
            if node.val == left_sum + right_sum:
                self.matching_nodes_count += 1

            # Telugu: Ee node ki total sum return cheyyadam (including itself)
            return node.val + left_sum + right_sum

        postorder(root)
        return self.matching_nodes_count



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        # Telugu: Answer ni maintain cheyyadam ki oka variable
        self.maxAverage = 0.0

        def dfs(node: TreeNode) -> (int, int):
            """
            Telugu: Ee function return chesthundi (subtree_sum, subtree_node_count)
            """
            if not node:
                return (0, 0)

            # Telugu: Left subtree ni recurse cheyyadam
            leftSum, leftCount = dfs(node.left)

            # Telugu: Right subtree ni recurse cheyyadam
            rightSum, rightCount = dfs(node.right)

            # Telugu: Total sum and count for current subtree
            totalSum = leftSum + rightSum + node.val
            totalCount = leftCount + rightCount + 1

            # Telugu: Average ni calculate cheyyadam
            average = totalSum / totalCount

            # Telugu: maxAverage update cheyyadam
            self.maxAverage = max(self.maxAverage, average)

            return (totalSum, totalCount)

        dfs(root)
        return self.maxAverage


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        # Telugu: Answer ni maintain cheyyadam ki oka variable
        self.maxAverage = 0.0

        def dfs(node: TreeNode) -> (int, int):
            """
            Telugu: Ee function return chesthundi (subtree_sum, subtree_node_count)
            """
            if not node:
                return (0, 0)

            # Telugu: Left subtree ni recurse cheyyadam
            leftSum, leftCount = dfs(node.left)

            # Telugu: Right subtree ni recurse cheyyadam
            rightSum, rightCount = dfs(node.right)

            # Telugu: Total sum and count for current subtree
            totalSum = leftSum + rightSum + node.val
            totalCount = leftCount + rightCount + 1

            # Telugu: Average ni calculate cheyyadam
            average = totalSum / totalCount

            # Telugu: maxAverage update cheyyadam
            self.maxAverage = max(self.maxAverage, average)

            return (totalSum, totalCount)

        dfs(root)
        return self.maxAverage


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # Telugu: Total matching node count ni maintain cheyyadam
        self.matchingCount = 0

        def postOrderDFS(currentNode: TreeNode) -> (int, int):
            """
            Returns: (totalSum, totalCount) for the current subtree
            """
            if not currentNode:
                return (0, 0)

            # Telugu: Left subtree recurse cheyyadam
            leftSum, leftCount = postOrderDFS(currentNode.left)

            # Telugu: Right subtree recurse cheyyadam
            rightSum, rightCount = postOrderDFS(currentNode.right)

            # Telugu: Current node tho total sum and count calculate cheyyadam
            totalSum = leftSum + rightSum + currentNode.val
            totalCount = leftCount + rightCount + 1

            # Telugu: Average match cheste, count increment cheyyadam
            if totalSum // totalCount == currentNode.val:
                self.matchingCount += 1

            return (totalSum, totalCount)

        postOrderDFS(root)
        return self.matchingCount


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:


        def recur(node):
            nonlocal ans

            if not node:
                return (0, 0)

            left_count, left_sum = recur(node.left)
            right_count, right_sum = recur(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if total_sum // total_count == node.val:
                ans += 1

            return (total_count, total_sum)

        ans = 0
        recur(root)

        return ans





""" 
| Metric                  | Value  | Explanation                            |
| ----------------------- | ------ | -------------------------------------- |
| ⏱ **Time Complexity**   | `O(n)` | You traverse the array once            |
| \U0001f5c2 **Space Complexity** | `O(n)` | Because of the extra `arr[]` list used |
"""
class Solution(object):
    def maxSubArray(self, nums):
        # Create an array...
        arr = []
        arr.append(nums[0])
        # Initialize the max sum...
        maxSum = arr[0]
        # Traverse all the element through the loop...
        for i in range(1, len(nums)):
            # arr[i] represents the largest sum of all subarrays ending with index i...
            # then its value should be the larger one between nums[i]...
            # arr[i-1] + nums[i] (largest sum plus current number with using prefix)...
            # calculate arr[0], arr[1]…, arr[n] while comparing each one with current largest sum...
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            # if arr[i] > maxSum then maxSum = arr[i].
            if arr[i] > maxSum:
                maxSum = arr[i]
        return maxSum       # Return the contiguous subarray which has the largest sum...




"""


| Metric              | Value                            |
| ------------------- | -------------------------------- |
| ⏱ Time Complexity   | `O(n)`                           |
| \U0001f5c2 Space Complexity | `O(1)` ✅ ← **Preferred at Meta** |



class Solution:
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]  # Start with the first element
        for num in nums[1:]:
            # Either start fresh or add to previous sum
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

"""        




class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size:int = size
        self.queue:int = []
        self.length:int = 0
        self.total:int = 0
        
    def next(self, val: int) -> float:
        if self.length < self.size:
            self.queue.append(val)
            self.total += val
            self.length += 1
            return self.total/self.length
        else:
            subtract = self.queue.pop(0)
            self.queue.append(val)
            self.total = self.total - subtract + val
            return self.total/self.size
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


""" 
| Metric                  | Value  | Explanation                            |
| ----------------------- | ------ | -------------------------------------- |
| ⏱ **Time Complexity**   | `O(n)` | You traverse the array once            |
| \U0001f5c2 **Space Complexity** | `O(n)` | Because of the extra `arr[]` list used |
"""
class Solution(object):
    def maxSubArray(self, nums):
        # Create an array...
        arr = []
        arr.append(nums[0])
        # Initialize the max sum...
        maxSum = arr[0]
        # Traverse all the element through the loop...
        for i in range(1, len(nums)):
            # arr[i] represents the largest sum of all subarrays ending with index i...
            # then its value should be the larger one between nums[i]...
            # arr[i-1] + nums[i] (largest sum plus current number with using prefix)...
            # calculate arr[0], arr[1]…, arr[n] while comparing each one with current largest sum...
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            # if arr[i] > maxSum then maxSum = arr[i].
            if arr[i] > maxSum:
                maxSum = arr[i]
        return maxSum       # Return the contiguous subarray which has the largest sum...




"""


| Metric              | Value                            |
| ------------------- | -------------------------------- |
| ⏱ Time Complexity   | `O(n)`                           |
| \U0001f5c2 Space Complexity | `O(1)` ✅ ← **Preferred at Meta** |



class Solution:
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]  # Start with the first element
        for num in nums[1:]:
            # Either start fresh or add to previous sum
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

"""        



""" 
| Metric                  | Value  | Explanation                            |
| ----------------------- | ------ | -------------------------------------- |
| ⏱ **Time Complexity**   | `O(n)` | You traverse the array once            |
| \U0001f5c2 **Space Complexity** | `O(n)` | Because of the extra `arr[]` list used |
"""
class Solution(object):
    def maxSubArray(self, nums):
        # Create an array...
        arr = []
        arr.append(nums[0])
        # Initialize the max sum...
        maxSum = arr[0]
        # Traverse all the element through the loop...
        for i in range(1, len(nums)):
            # arr[i] represents the largest sum of all subarrays ending with index i...
            # then its value should be the larger one between nums[i]...
            # arr[i-1] + nums[i] (largest sum plus current number with using prefix)...
            # calculate arr[0], arr[1]…, arr[n] while comparing each one with current largest sum...
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            # if arr[i] > maxSum then maxSum = arr[i].
            if arr[i] > maxSum:
                maxSum = arr[i]
        return maxSum       # Return the contiguous subarray which has the largest sum...




"""
class Solution:
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]  # Start with the first element
        for num in nums[1:]:
            # Either start fresh or add to previous sum
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

"""        



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Pointer for the last valid element in nums1
        index_nums1 = m - 1

        # Pointer for the last element in nums2
        index_nums2 = n - 1

        # Pointer for the last position in nums1 (including extra space)
        write_index = m + n - 1

        # Loop as long as there are elements left in nums2 to merge
        while index_nums2 >= 0:
            # If nums1 still has elements, and current nums1 is greater than nums2
            if index_nums1 >= 0 and nums1[index_nums1] > nums2[index_nums2]:
                nums1[write_index] = nums1[index_nums1]  # Copy from nums1
                index_nums1 -= 1  # Move pointer left in nums1
            else:
                nums1[write_index] = nums2[index_nums2]  # Copy from nums2
                index_nums2 -= 1  # Move pointer left in nums2

            write_index -= 1  # Move write pointer left


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_index = 0     # Pointer for word
        abbr_index = 0     # Pointer for abbr
        len_word = len(word)
        len_abbr = len(abbr)

        while word_index < len_word and abbr_index < len_abbr:
            # Case 1: If characters match → move both pointers
            if word[word_index] == abbr[abbr_index]:
                word_index += 1
                abbr_index += 1

            # Case 2: Leading zero is NOT allowed in abbreviation
            elif abbr[abbr_index] == "0":
                return False

            # Case 3: If abbreviation has a number → skip characters in `word`
            elif abbr[abbr_index].isdigit():
                start = abbr_index  # Start of the numeric substring

                # Move to the end of the number
                while abbr_index < len_abbr and abbr[abbr_index].isdigit():
                    abbr_index += 1

                # Convert that number to integer
                num_to_skip = int(abbr[start:abbr_index])
                word_index += num_to_skip  # Skip `num_to_skip` characters in word

            # Case 4: If no match and not a digit → invalid abbreviation
            else:
                return False

        # Finally, both indices must reach the end for a valid match
        return word_index == len_word and abbr_index == len_abbr


class Solution:
    def findPeakGrid(self, matrix: List[List[int]]) -> List[int]:
        num_rows = len(matrix)               # Total number of rows
        num_cols = len(matrix[0])            # Total number of columns
        row = 0                              # Start row
        col = 0                              # Start column

        while row < num_rows and col < num_cols:
            # Check 4 directions: up, down, left, right
            top = matrix[row - 1][col] if row > 0 else -1
            bottom = matrix[row + 1][col] if row < num_rows - 1 else -1
            left = matrix[row][col - 1] if col > 0 else -1
            right = matrix[row][col + 1] if col < num_cols - 1 else -1

            # ✅ If current element is greater than all 4 neighbors, it's a peak
            if matrix[row][col] > top and matrix[row][col] > bottom and \
               matrix[row][col] > left and matrix[row][col] > right:
                return [row, col]

            # \U0001f50d Step 1: Find the max element in the current column
            max_row_in_col = row
            max_value_in_col = -1
            for r in range(num_rows):
                if matrix[r][col] > max_value_in_col:
                    max_row_in_col = r
                    max_value_in_col = matrix[r][col]
            row = max_row_in_col

            # Check left and right neighbors of the updated (row, col)
            left = matrix[row][col - 1] if col > 0 else -1
            right = matrix[row][col + 1] if col < num_cols - 1 else -1

            # ✅ If current element is greater than left and right, return
            if matrix[row][col] > left and matrix[row][col] > right:
                return [row, col]

            # \U0001f50d Step 2: Find the max element in the current row
            max_col_in_row = col
            max_value_in_row = -1
            for c in range(num_cols):
                if matrix[row][c] > max_value_in_row:
                    max_col_in_row = c
                    max_value_in_row = matrix[row][c]
            col = max_col_in_row

            # Check top and bottom neighbors of the updated (row, col)
            top = matrix[row - 1][col] if row > 0 else -1
            bottom = matrix[row + 1][col] if row < num_rows - 1 else -1

            # ✅ If current element is greater than top and bottom, return
            if matrix[row][col] > top and matrix[row][col] > bottom:
                return [row, col]



class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)             # Number of rows
        n = len(mat[0])          # Number of columns
        i = 0                    # Start with top-left corner
        j = 0

        # Keep looping until a peak is found
        while i < m and j < n:
            # \U0001f50d Check 4 neighbors (up, down, left, right), if out of bounds use -1
            up = mat[i - 1][j] if i > 0 else -1
            down = mat[i + 1][j] if i < m - 1 else -1
            left = mat[i][j - 1] if j > 0 else -1
            right = mat[i][j + 1] if j < n - 1 else -1

            # ✅ Condition for Peak
            if mat[i][j] > up and mat[i][j] > down and mat[i][j] > left and mat[i][j] > right:
                return [i, j]

            # \U0001f501 Check full column at current j → pick max in this column
            maxRow = i
            maxVal = 0
            for row in range(m):
                if mat[row][j] > maxVal:
                    maxRow = row
                    maxVal = mat[row][j]
            i = maxRow  # Move to the row with max value in this column

            # \U0001f4c9 Check only left and right neighbors (we’re staying in same row)
            left = mat[i][j - 1] if j > 0 else -1
            right = mat[i][j + 1] if j < n - 1 else -1
            if mat[i][j] > left and mat[i][j] > right:
                return [i, j]

            # \U0001f501 Now check full row at current i → pick max in this row
            maxCol = j
            maxVal = 0
            for col in range(n):
                if mat[i][col] > maxVal:
                    maxCol = col
                    maxVal = mat[i][col]
            j = maxCol  # Move to the column with max value in this row

            # \U0001f4c9 Check up and down neighbors (we’re staying in same column now)
            up = mat[i - 1][j] if i > 0 else -1
            down = mat[i + 1][j] if i < m - 1 else -1
            if mat[i][j] > up and mat[i][j] > down:
                return [i, j]


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start=0
        end=len(arr)-1
        while(start<end):
            mid=(start+end)//2
            if(arr[mid]>arr[mid+1]):
                end=mid
            else:
                start=mid+1
        return end



class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1   # Initialize search boundaries

        while left < right:
            mid = (left + right) >> 1    # Bitwise divide by 2 (same as // 2)

            # If mid element is greater than its right neighbor
            # That means a peak lies on the left half (including mid)
            if nums[mid] > nums[mid + 1]:
                right = mid              # Move search space to left side
            else:
                # If mid+1 is greater → increasing slope → peak on right
                left = mid + 1           # Move search space to right side

        return left                      # left == right at the peak


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Stack ni list laga use chestunnadu - charecter tho count ni store cheyyadam kosam

        for char in s:  # Oka oka character ni loop lo teesukuntunnadu
            if stack and stack[-1][0] == char:
                # Last element stack lo same character aithe, count ni increment chestunnadu
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    # Count k ki equal aithe andulo pattesi remove chestunnadu (pop)
                    stack.pop()
            else:
                # First time vachina char aithe, char ni and count 1 tho stack lo pettadu
                stack.append([char, 1])

        # Stack lo unna elements ni character * count format lo repeat chesi join chestunnadu
        return "".join([s * count for s, count in stack])
        """
            StringBuilder sb = new StringBuilder();
            for (Pair p : stack) {
                for (int i = 0; i < p.count; i++) {
                    sb.append(p.ch);
                }
            }
            return sb.toString();
        """


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


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        heap=[(-count[key],key) for key in count.keys()]
		
        def partition(A,l,r):
            pivot=A[r]
            pstart=l
            for i in range(l,r):
                if A[i]<pivot:
                    A[i],A[pstart]=A[pstart],A[i]
                    pstart+=1
            A[r],A[pstart]=A[pstart],A[r]
            return pstart
                    
        def quickselect(A,l,r):
            if l<r:
                pindex=partition(A,l,r)
                if pindex<k:
                    quickselect(A,pindex+1,r)
                elif pindex>k:
                    quickselect(A,l,pindex-1)
                else:
                    return
            else: return
        
        quickselect(heap,0,len(heap)-1)
        out=heap[:k]
        out.sort()
        return [tmp[1] for tmp in out]

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid+1]>nums[mid]:
                l=mid+1
            elif nums[mid-1]>nums[mid]:
                r=mid
            else:
                return mid
        return l
        


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []

        for char in s:

            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        return "".join([s * count for s, count in stack])

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) //2
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            elif nums[mid - 1] > nums[mid]:
                right = mid
            else: 
                return mid
        return left



class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for x in words:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        res = sorted(dict, key=lambda x: (-dict[x], x))
        return res[:k]

class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int num : nums) {
            // Count digits by dividing num by 10 repeatedly
            int digits = 0;
            int temp = num;
            while (temp > 0) {
                digits++;
                temp /= 10;
            }
            // Check if digit count is even
            if (digits % 2 == 0) {
                count++;
            }
        }
        return count;
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

---------------------------------------------------------------------------


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



--------------------------------------------------------------------

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


------------------------------------------------------------------------------

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



---------------------------------------------------------------------------

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Keep t_counter of char counts in t
        
        We make a sliding window across s, tracking the char counts in s_counter
        We keep track of matches, the number of chars with matching counts in s_counter and t_counter
        Increment or decrement matches based on how the sliding window changes
        When matches == len(t_counter.keys()), we have a valid window. Update the answer accordingly
        
        How we slide the window:
        Extend when matches < chars, because we can only get a valid window by adding more.
        Contract when matches == chars, because we could possibly do better than the current window.
        
        How we update matches:
        This only applies if t_counter[x] > 0.
        If s_counter[x] is increased to match t_counter[x], matches += 1
        If s_counter[x] is increased to be more than t_counter[x], do nothing
        If s_counter[x] is decreased to be t_counter[x] - 1, matches -= 1
        If s_counter[x] is decreased to be less than t_counter[x] - 1, do nothing
        
        Analysis:
        O(s + t) time: O(t) to build t_counter, then O(s) to move our sliding window across s. Each index is only visited twice.
        O(s + t) space: O(t) space for t_counter and O(s) space for s_counter
        '''
        
        if not s or not t or len(s) < len(t):
            return ''
        
        t_counter = Counter(t)
        chars = len(t_counter.keys())
        
        s_counter = Counter()
        matches = 0
        
        answer = ''
        
        i = 0
        j = -1 # make j = -1 to start, so we can move it forward and put s[0] in s_counter in the extend phase 
        
        while i < len(s):
            
            # extend
            if matches < chars:
                
                # since we don't have enough matches and j is at the end of the string, we have no way to increase matches
                if j == len(s) - 1:
                    return answer
                
                j += 1
                s_counter[s[j]] += 1
                if t_counter[s[j]] > 0 and s_counter[s[j]] == t_counter[s[j]]:
                    matches += 1

            # contract
            else:
                s_counter[s[i]] -= 1
                if t_counter[s[i]] > 0 and s_counter[s[i]] == t_counter[s[i]] - 1:
                    matches -= 1
                i += 1
                
            # update answer
            if matches == chars:
                if not answer:
                    answer = s[i:j+1]
                elif (j - i + 1) < len(answer):
                    answer = s[i:j+1]
        
        return answer



------------------------------------------------------------------------------


