```python

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # You need to remove intervals to Avoid merging. 
        intervals.sort(key = lambda x: x[1]) # You are sorting based on the End Time. 
        result = 0
        k = -inf # What does this mean 

        # x = interval[]
        for x, y in intervals:
            if x >= k: # Here X and Y ante ? 
                k = y # What does this mean ? 
            else:
                result += 1 # increment chestunnav.
        
        return result

```
