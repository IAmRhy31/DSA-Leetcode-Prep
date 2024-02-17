# Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0

# Example 3:

# Input: nums = [1]
# Output: 0

 

# Constraints:

#     1 <= nums.length <= 104
#     -105 <= nums[i] <= 105

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = list(nums)
        nums2.sort()

        start, end = 0, len(nums) - 1

        while start < len(nums) and nums[start] == nums2[start]:
            start += 1

        while end >= start and nums[end] == nums2[end]:
            end -= 1

        return max(0, end - start + 1)
