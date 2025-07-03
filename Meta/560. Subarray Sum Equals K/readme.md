```text

Q2: Given an array of positive integers and a target K, return a boolean to tell if there is any continuous sub-array that sums to the target. Variation of (560. Subarray Sum Equals K)

Two Sum ki Extension laga ne untadi. 

```

```java

Intuition
We want to count the number of subarrays whose elements sum up to a given value k.
Instead of checking every possible subarray (which is slow), we use the idea of prefix sums and a HashMap to track how often a cumulative sum has occurred.

If at some index j, the current prefix sum is sum, and there's a previous prefix sum sum - k, then the subarray between those two indices adds up to k.

Approach
Initialize a HashMap to store the frequency of prefix sums.
Start with map.put(0, 1) to handle subarrays starting at index 0.

Traverse through the array, calculating the prefix sum sum at each index.

For each index:

Check if sum - k exists in the map. If it does, it means there's a subarray ending at the current index which sums to k. Add the frequency of sum - k to your answer.

Update the map with the current sum.

Return the final count of valid subarrays.

Complexity
Time complexity:
O(n) — Single pass through the array.

Space complexity:
O(n) — In the worst case, the HashMap may store up to n different prefix sums


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
