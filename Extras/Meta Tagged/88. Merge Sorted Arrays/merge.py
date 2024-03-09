# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

 

# Constraints:

#     nums1.length == m + n
#     nums2.length == n
#     0 <= m, n <= 200
#     1 <= m + n <= 200
#     -109 <= nums1[i], nums2[j] <= 109

 

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for last index of nums 1
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n-=1
            last -= 1
        
        # fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            last -= 1
            n -= 1
        
# If asked to merge three sorted arrays:    
def merge3sorted(A, B, C):
	(l1, l2, l3) = (len(A), len(B), len(C))
	i = j = k = 0

	# Destination array
	ans = []

	while (i < l1 or j < l2 or k < l3):

		# Assigning a, b, c with max values so that if
		# any value is not present then also we can sort
		# the array
		a = 9999
		b = 9999
		c = 9999

		# a, b, c variables are assigned only if the
		# value exist in the array.
		if (i < l1):
			a = A[i]
		if (j < l2):
			b = B[j]
		if (k < l3):
			c = C[k]

		# Checking if 'a' is the minimum
		if (a <= b and a <= c):
			ans.append(a)
			i += 1

		# Checking if 'b' is the minimum
		elif (b <= a and b <= c):
			ans.append(b)
			j += 1

		# Checking if 'c' is the minimum
		elif (c <= a and c <= b):
			ans.append(c)
			k += 1

	return ans

     # T and S : O(M + N + O) = O(N)

 # If asked to merge three sorted arrays but without duplicates:

def merge_three_sorted_arrays_no_duplicates(arr1, arr2, arr3):
    result = []  # Initialize the result array to store the merged and deduplicated values
    i = j = k = 0  # Initialize pointers for each array

    while i < len(arr1) or j < len(arr2) or k < len(arr3):
        # Extract values at current pointers (or use infinity if pointers are out of bounds)
        val1 = arr1[i] if i < len(arr1) else float('inf')
        val2 = arr2[j] if j < len(arr2) else float('inf')
        val3 = arr3[k] if k < len(arr3) else float('inf')

        # Find the minimum value among the three arrays
        min_val = min(val1, val2, val3)

        # Move the pointers based on the minimum value
        if min_val == val1:
            i += 1
        elif min_val == val2:
            j += 1
        else:
            k += 1

        # Append the distinct value to the result (avoid duplicates)
        if not result or min_val != result[-1]:
            result.append(min_val)

    return result

    # T and S : O(N)
