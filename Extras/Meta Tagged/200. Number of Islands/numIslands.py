# https://leetcode.com/problems/number-of-islands/description/

# https://www.youtube.com/watch?v=BJ8KHYx_hXc

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

 

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 300
#     grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def island_to_zero(grid, r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                grid[r][c] = "0"

                for row_inc, col_inc in directions:
                    island_to_zero(grid, r + row_inc, c + col_inc)

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    island_count += 1
                    island_to_zero(grid, row, column)
        return island_count

        # T = O(R * C)
        # S = O(R * C), O(1) if not counting stack frames