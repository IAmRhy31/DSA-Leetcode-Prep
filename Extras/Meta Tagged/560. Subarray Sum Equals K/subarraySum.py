# https://leetcode.com/problems/subarray-sum-equals-k/description/

# https://www.youtube.com/watch?v=xvNwoz-ufXA

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

 

# Constraints:

#     1 <= nums.length <= 2 * 104
#     -1000 <= nums[i] <= 1000
#     -107 <= k <= 107

import collections
from typing import List

# Intuition for O(N) efficient approach:
# 1) Initialize Hashmap to start with "0: 1 ( prefixSum: count )"
# 2) Do prefix sum as you loop through the input array, and check whether remove = (prefixSum - k) is in our map. 
# 3) If yes, increment the count of remove and add to count/result (line 48)
# 4) If not, add in map (line 49)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_counts = collections.defaultdict(int)
        prefix_sum_counts[0] = 1
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            remove = prefix_sum - k
            count += prefix_sum_counts[remove]
            prefix_sum_counts[prefix_sum] += 1
        return count
