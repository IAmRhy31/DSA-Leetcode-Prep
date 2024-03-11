# https://leetcode.com/problems/find-peak-element/description/

# https://www.youtube.com/watch?v=GAJITCneCPE

# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

 

# Constraints:

#     1 <= nums.length <= 1000
#     -231 <= nums[i] <= 231 - 1
#     nums[i] != nums[i + 1] for all valid i.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + ((r - l)) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l # or return r, doesn't matter

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]: #Time-Complexity: O(log(m) * n
                                                               #Space-Complexity: O(1)
        
        #Approach: You can think of this problem in two ways! Either column-based or row-based! 
        
        #Idea is that we perform binary search on mat grid and utilize search space on rows. ROW BASED
        #for the current middle row we are on, find the maximum element, as it will be bigger than
        #both of its left and right neighboring elements. To verify this element is a peak, we need
        #to make sure that it is also bigger than the immediate top and bottom neighboring elements!
        
        #however, we need to be careful of the bottom and top neighboring elements being out of bounds!
        #in this case, the current peak candidate will always be bigger than such elements since
        #all elements within mat are guaranteed to be positive numbers!
        #Right when we find peak element, we should return its position immediately!
        
        #define my search space by row!
        L, H = 0, len(mat) - 1
        #as long as we have at least one row left to consider, continue binary search!
        while L <= H:
            mid = (L + H) // 2
            mid_row = mat[mid]
            #initialize max_pos and store column pos later!
            max_pos = None
            max_val = float(-inf)
            #iterate linearly through the row since it's not sorted and find the maximum element as well
            #as its position!
            for j in range(len(mid_row)):
                if(mid_row[j] > max_val):
                    max_val = mid_row[j]
                    max_pos = j
                    continue
            #once we have max_pos, then we have to compare relative to top and bottom neighbors!
            top_val = -1 if mid - 1 < 0 else mat[mid-1][max_pos]
            bottom_val = -1 if mid + 1 >= len(mat) else mat[mid+1][max_pos]
            #then it's a peak!
            if(top_val < max_val and bottom_val < max_val):
                return [mid, max_pos]
            #top neighboring element is bigger! -> it has better chance to be peak element!
            if(top_val >= max_val):
                H = mid - 1 
                continue
            if(bottom_val >= max_val):
                L = mid + 1
                continue
