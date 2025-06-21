```python
from collections import Counter
import random
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count frequency of each word
        freq = Counter(words)  # Dict {word: count}

        # Step 2: Convert to list of (freq, word)
        # Invert order to (frequency, word) to prioritize frequency
        items = [(count, word) for word, count in freq.items()]

        # Step 3: QuickSelect to find top k frequent items
        def quickSelect(left, right, k):
            if left >= right:
                return

            # Step 3.1: Random pivot selection
            pivot_idx = random.randint(left, right)
            items[pivot_idx], items[right] = items[right], items[pivot_idx]
            pivot = items[right]  # (freq, word)

            # Step 3.2: Custom partition logic
            def compare(a, b):
                # Higher frequency first
                if a[0] != b[0]:
                    return a[0] < b[0]
                # For same frequency, smaller word first
                return a[1] > b[1]

            store_idx = left
            for i in range(left, right):
                if compare(items[i], pivot):
                    items[i], items[store_idx] = items[store_idx], items[i]
                    store_idx += 1

            items[store_idx], items[right] = items[right], items[store_idx]

            # Step 3.3: Decide which side to recurse on
            if store_idx == len(items) - k:
                return
            elif store_idx > len(items) - k:
                quickSelect(left, store_idx - 1, k)
            else:
                quickSelect(store_idx + 1, right, k)

        # Step 4: Perform QuickSelect
        quickSelect(0, len(items) - 1, k)

        # Step 5: Extract top-k frequent, sort by freq DESC and word ASC
        result = items[-k:]
        result.sort(key=lambda x: ( -x[0], x[1]))  # frequency descending, then lexicographically

        # Step 6: Return just the words
        return [word for _, word in result]



from collections import Counter
import random
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        freq = Counter(nums)  # Dictionary {num: frequency}

        # Step 2: Convert dictionary to list of tuples (freq, num)
        items = [(count, num) for num, count in freq.items()]

        # Step 3: QuickSelect to partition top k frequent elements to the right
        def quickSelect(left, right, k):
            if left >= right:
                return  # Only one element left

            # Step 3.1: Randomly select pivot to avoid worst-case
            pivot_idx = random.randint(left, right)
            items[pivot_idx], items[right] = items[right], items[pivot_idx]
            pivot_freq = items[right][0]  # Use frequency for comparison

            # Step 3.2: Partition: group elements <= pivot to the left
            store_idx = left
            for i in range(left, right):
                if items[i][0] <= pivot_freq: [i][0] --> you are working on the Frequency. 
                    items[store_idx], items[i] = items[i], items[store_idx]
                    store_idx += 1

            # Step 3.3: Place pivot in its correct position
            items[store_idx], items[right] = items[right], items[store_idx]

            # Step 4: Recurse on the correct side to find top k
            if store_idx == len(items) - k:
                return  # Found kth largest freq
            elif store_idx > len(items) - k:
                quickSelect(left, store_idx - 1, k)
            else:
                quickSelect(store_idx + 1, right, k)

        # Step 5: Perform QuickSelect
        quickSelect(0, len(items) - 1, k)

        # Step 6: Extract top-k frequent elements
        return [num for _, num in items[-k:]]



from typing import List
import random

class Solution:
TC: O(N)
Space complexity: O(1).

The QuickSelect algorithm conducts the partial sort of points in place with no recursion, so only constant extra space is required.

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Step 1: Compute squared distances and store with original coordinates
        # This avoids computing sqrt, which is not necessary for comparisons
        points_with_dist = [(x * x + y * y, x, y) for x, y in points]

        # Helper function: QuickSelect to partition points so top-k smallest distances are at the front
        def quickSelect(left: int, right: int, k: int) -> None:
            # Base case: If subarray has one element, done
            if left >= right:
                return

            # Step 2: Pick a random pivot index to prevent worst-case O(n^2)
            pivot_idx = random.randint(left, right)

            # Move pivot to end for convenience
            points_with_dist[pivot_idx], points_with_dist[right] = points_with_dist[right], points_with_dist[pivot_idx]
            pivot_dist = points_with_dist[right][0]

            # Step 3: Partition elements smaller than pivot to the left
            store_idx = left
            for i in range(left, right):
                if points_with_dist[i][0] <= pivot_dist:
                    points_with_dist[store_idx], points_with_dist[i] = points_with_dist[i], points_with_dist[store_idx]
                    store_idx += 1

            # Move pivot to its final place
            points_with_dist[store_idx], points_with_dist[right] = points_with_dist[right], points_with_dist[store_idx]

            # Step 4: Recur on correct partition to find top-k smallest distances
            if store_idx == k:
                return  # Done: Exactly k elements in left partition
            elif store_idx > k:
                quickSelect(left, store_idx - 1, k)  # Search left partition
            else:
                quickSelect(store_idx + 1, right, k)  # Search right partition

        # Step 5: Perform QuickSelect on the full array
        quickSelect(0, len(points_with_dist) - 1, k)

        # Step 6: Return only the coordinates (x, y) of the k closest points
        return [(x, y) for _, x, y in points_with_dist[:k]]

Approach 2: Max Heap or Max Priority Queue
ty: O(N⋅logk)
xity: O(k)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Since heap is sorted in increasing order,
        # negate the distance to simulate max heap
        # and fill the heap with the first k elements of points
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)] # Store the first k elements in the heap.
        print("What is the TYPE of the heap ? ")
        print(type(heap))
        heapq.heapify(heap)
        """
            Then only add new elements that are closer than the top point in the heap 
            while removing the top point to keep the heap at k elements.
        """
        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])
            if dist > heap[0][0]:
                # If this point is closer than the kth farthest,
                # discard the farthest point and add this one
                heapq.heappushpop(heap, (dist, i))
        
        # Return all points stored in the max heap
        return [points[i] for (_, i) in heap]
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2


Approach 3: Binary Search
Time complexity: O(N)
Space complexity: O(N)




class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Precompute the Euclidean distance for each point
        distances = [self.euclidean_distance(point) for point in points]
        # Create a reference list of point indices
        remaining = [i for i in range(len(points))]
        # Define the initial binary search range
        low, high = 0, max(distances)
        
        # Perform a binary search of the distances
        # to find the k closest points
        closest = []
        while k:
            mid = (low + high) / 2
            closer, farther = self.split_distances(remaining, distances, mid)
            if len(closer) > k:
                # If more than k points are in the closer distances
                # then discard the farther points and continue
                remaining = closer
                high = mid
            else:
                # Add the closer points to the answer array and keep
                # searching the farther distances for the remaining points
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                low = mid
                
        # Return the k closest points using the reference indices
        return [points[i] for i in closest]

    def split_distances(self, remaining: List[int], distances: List[float],
                        mid: int) -> List[List[int]]:
        """Split the distances around the midpoint
        and return them in separate lists."""
        closer, farther = [], []
        for index in remaining:
            if distances[index] <= mid:
                closer.append(index)
            else:
                farther.append(index)
        return [closer, farther]

    def euclidean_distance(self, point: List[int]) -> float:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2



import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Convert "kth largest" to "kth smallest" index
        target_idx = len(nums) - k  # E.g., 2nd largest in size 6 → index 4

        # Step 2: QuickSelect implementation
        def quickSelect(left: int, right: int) -> int:
            # Step 2.1: Choose a random pivot
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            pivot_val = nums[right]

            # Step 2.2: Partition — elements ≤ pivot go left
            store_idx = left
            for i in range(left, right):
                if nums[i] <= pivot_val:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1

            # Step 2.3: Place pivot in final sorted position
            nums[store_idx], nums[right] = nums[right], nums[store_idx]

            # Step 2.4: Recurse based on target position
            if store_idx < target_idx:
                return quickSelect(store_idx + 1, right)
            elif store_idx > target_idx:
                return quickSelect(left, store_idx - 1)
            else:
                return nums[store_idx]  # Found kth largest

        # Step 3: Call QuickSelect on the full array
        return quickSelect(0, len(nums) - 1)


Example of Worst-Case Without Randomization
Suppose you always pick the last element as the pivot, and the input array is already sorted in ascending order: [1, 2, 3, 4, 5, 6], with k = 2 (find the 2nd largest, which is 5 at index 4).

First call: Pivot = 6, partition places 6 at the end, and all smaller elements (1, 2, 3, 4, 5) are to the left. The partition index is 5.
Since the target index is 4, recurse on the left subarray [1, 2, 3, 4, 5].
Next call: Pivot = 5, partition places 5 at the end of the subarray, and so on.
Each step processes nearly the entire remaining array, leading to O(n²) complexity.
With randomization, the pivot is unlikely to consistently be the largest or smallest element, so the partitions are more balanced, and the algorithm typically processes much smaller subarrays in each step.

Why Randomization Works
Randomly selecting a pivot ensures that, over many runs, the pivot is likely to be somewhere in the middle of the array’s values, leading to balanced partitions on average.
The probability of repeatedly choosing bad pivots (e.g., the smallest or largest element) is low, so the expected number of recursive steps is proportional to n, yielding O(n) average-case complexity.

| **Aspect**         | **`nums[:k]`**          | **`nums[k:]`**            |
| ------------------ | ----------------------- | ------------------------- |
| **Start Index**    | `0` (beginning of list) | `k`                       |
| **End Index**      | `k` (exclusive)         | `len(nums)` (end of list) |
| **Elements**       | First `k` elements      | Elements from `k` to end  |
| **Length**         | `k`                     | `len(nums) - k`           |
| **Example Output** | `nums[:3] → [1, 2, 3]`  | `nums[3:] → [4, 5]`       |

heap = nums[:k]
List<Integer> heap = new ArrayList<>(nums.subList(0, k));


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]
		
		
		
	703. Kth Largest Element in a Stream
	
		
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```
