from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, numbers: List[int], k: int) -> List[int]:
        # Step 1: Count each number frequency
        number_to_count = Counter(numbers)

        # Step 2: Binary Search over frequency range
        min_freq = 1
        max_freq = max(number_to_count.values())

        def count_ge_freq(freq_threshold):
            # Ee freq kanna ekkuva or equal unna elements yentha unnayo count cheddam
            return sum(1 for count in number_to_count.values() if count >= freq_threshold)

        # Binary Search to find threshold frequency
        low, high = min_freq, max_freq
        while low < high:
            mid = (low + high + 1) // 2
            if count_ge_freq(mid) >= k:
                low = mid  # Try higher frequency
            else:
                high = mid - 1

        # Now `low` is the highest frequency that still gives ≥ k elements
        threshold = low

        # Step 3: Collect all elements with frequency ≥ threshold
        result = [num for num, count in number_to_count.items() if count >= threshold]

        # Step 4: If result has more than k, we sort and trim
        result.sort(key=lambda x: -number_to_count[x])  # Highest freq first
        return result[:k]
