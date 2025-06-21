class Solution:
    def maxDifference(self, s: str) -> int:
        counter_map = [0] * 26
        start = 0
        end = len(s)
        max_value = 0 # Why we want these ? 
        min_value = len(s)
        # Now I need to populate counter_map
        for c in s:
            counter_map[ord(c) - ord('a')] += 1
        for i in range(26):
            if counter_map[i] % 2 != 0: # Odd ki max value 
                max_value = max(counter_map[i], max_value)
            if counter_map[i] % 2 == 0 and counter_map[i] > 0: # event ki min value. 
                min_value = min(min_value, counter_map[i])
        return max_value - min_value

        count = Counter(s)
        print(count)
        # How do I iterate over a or Dictionary. 
        # Get min Even
        # Get max Odd 
        # Iterate over the MAP. track Min and max and difference. 
        max_difference = inf(-1)
        for i in count.values():
            max_difference 
        return 0
