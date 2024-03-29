# https://leetcode.com/problems/max-consecutive-ones-iii/

# https://www.youtube.com/watch?v=OPV49AuP9lQ

# https://www.youtube.com/watch?v=97oTiOCuxho

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

 

# Constraints:

#     1 <= nums.length <= 105
#     nums[i] is either 0 or 1.
#     0 <= k <= nums.length

from typing import List

# Approach 1:

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLen = 0

        for right, num in enumerate(nums):
            k -= 1 - num
            if k < 0:
                k += 1 - nums[left]
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen


# Approach 2:
    
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1

                left += 1

            right += 1
        return right - left
