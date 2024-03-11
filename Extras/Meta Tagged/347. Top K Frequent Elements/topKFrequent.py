# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

 

# Constraints:

#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#     k is in the range [1, the number of unique elements in the array].
#     It is guaranteed that the answer is unique.

 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Bucket Sort solution : O(n) time and O(n) space (slightly better than use heap w/heapify where time complexity is O(klogn))

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        countMap = {}  # map to keep track of count - key: num, value: count of num in array nums
        freq = [[] for i in range(n + 1)]  # frequency array to keep track of elements for their certain count, eg. [[], [], [], ...]

        # add nums with their counts to hashmap
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1

        # append num's to the frequency array to their respective count indices
        for num, count in countMap.items():
            freq[count].append(num)

        result = []
        # loop from end of the frequency array to append top k frequent elements to the result array
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
            if len(result) == k:
                return result
            
        # Time Complexity: O(N + K log N)
        # Space Complexity: O(N) for the countMap and freq arrays
