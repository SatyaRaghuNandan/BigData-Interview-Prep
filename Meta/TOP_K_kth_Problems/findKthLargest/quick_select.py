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
