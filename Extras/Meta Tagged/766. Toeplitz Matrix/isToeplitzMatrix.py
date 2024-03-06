# https://leetcode.com/problems/toeplitz-matrix/description/

# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

# Example 1:

# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.

# Example 2:

# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.

 

# Constraints:

#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 20
#     0 <= matrix[i][j] <= 99

 
# Follow up:

#     What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
#     What if the matrix is so large that you can only load up a partial row into the memory at once?

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        for r in range(row - 1):
            for c in range(col - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True

        # T - O(M * N) in worst case
        # S - O(1)

# Follow-ups:
    
# 1) Matrix Stored on Disk with Limited Memory:
    
# In this scenario, you can iterate through the matrix one row at a time. Load the current row into memory and compare it with the next row. 
# This way, you only need to keep two rows in memory at any given time. 
# Continue this process until you reach the end of the matrix.
    
# 2) Matrix So Large Partial Row Fits in Memory:

# If the matrix is so large that you can only load a partial row into memory at once, you can still use a sliding window approach. 
# Load a portion of the current row into memory, compare it with the corresponding portion of the next row, and slide the window through the entire row.
# Repeat this process for each row.