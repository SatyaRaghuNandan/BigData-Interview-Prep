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



