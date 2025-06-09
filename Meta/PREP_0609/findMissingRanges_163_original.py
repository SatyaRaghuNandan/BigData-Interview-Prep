class Solution:
    def findMissingRanges(
        self, nums: list[int], lower: int, upper: int
    ) -> list[list[int]]:
        n = len(nums)
        missing_ranges = []

        # nums empty ayithe, entire range missing
        if n == 0:
            missing_ranges.append([lower, upper])
            return missing_ranges

        # lower ki nums[0] madhya lo gap unda check cheyyadam
        if lower < nums[0]:
            missing_ranges.append([lower, nums[0] - 1])

        # middle lo gaps unte collect cheyyadam
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue  # adjacent or same → gap ledu, skip
            missing_ranges.append([nums[i] + 1, nums[i + 1] - 1])

        # nums[-1] to upper madhya lo gap check cheyyadam
        if upper > nums[-1]:
            missing_ranges.append([nums[-1] + 1, upper])

        return missing_ranges
