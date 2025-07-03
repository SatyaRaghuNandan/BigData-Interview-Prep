```text

Q2: Given an array of positive integers and a target K, return a boolean to tell if there is any continuous sub-array that sums to the target. Variation of (560. Subarray Sum Equals K)

Two Sum ki Extension laga ne untadi. 

```

```java



Complexity Analysis

Time complexity : O(n). The entire nums array is traversed only once.

Space complexity : O(n). Hashmap map can contain up to n distinct entries in the worst case.



class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int sum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum - k)) {
                count += map.get(sum - k);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }   
        return count;
    }
}

```


![image](https://github.com/user-attachments/assets/59a8ce51-b4a7-49dc-871c-62b72fbbbe48)
