# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/

# https://www.youtube.com/watch?v=sQNN4xKC1mA

# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

#     SparseVector(nums) Initializes the object with the vector nums
#     dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

 

# Example 1:

# Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
# Output: 8
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

# Example 2:

# Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
# Output: 0
# Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
# v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

# Example 3:

# Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
# Output: 6

 

# Constraints:

#     n == nums1.length == nums2.length
#     1 <= n <= 10^5
#     0 <= nums1[i], nums2[i] <= 100

from typing import List

# 1st Solution: Naive Approach - Loop through each vector and formulate dot product
# 2nd Solution: Non-Naive but not best as well - Use HashMap to store non-zero values in the form : non-zero index: value

# 3rd Solution(Below): Use Tuples since HashMap's can be terrible sometimes and interviewer may expect a more efficient solution with a follow-up question. Tuple is the answer:

class SparseVector:
    def __init__(self, nums: List[int]):

        self.nums = []

        for i, num in enumerate(nums):
            if num:
                self.nums.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:

        resProduct = 0
        i = j = 0

        while i < len(self.nums) and j < len(vec.nums):
            i_idx, i_val = self.nums[i]
            j_idx, j_val = vec.nums[j]

            if i_idx == j_idx:
                resProduct += i_val * j_val
                i += 1
                j += 1
            elif i_idx > j_idx:
                j += 1
            else:
                i += 1
        return resProduct
    
# T and S - O(N + M)
# If Follow up is asked in an interview: the answer is use Binary Search
