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
