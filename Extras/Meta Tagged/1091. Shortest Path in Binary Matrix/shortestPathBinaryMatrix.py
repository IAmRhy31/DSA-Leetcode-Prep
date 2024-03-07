# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

# https://www.youtube.com/watch?v=Y2F8EGP3OA4

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

#     All the visited cells of the path are 0.
#     All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 2

# Example 2:

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1

 

# Constraints:

#     n == grid.length
#     n == grid[i].length
#     1 <= n <= 100
#     grid[i][j] is 0 or 1

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        queue = [(0, 0, 1)]  # row, column, and length
        grid[0][0] = 1

        for r, c, l in queue:
            if r == n - 1 and c == n - 1:
                return l

            directions = [
                (r - 1, c), (r - 1, c - 1), (r - 1, c + 1),
                (r, c - 1), (r, c + 1),
                (r + 1, c), (r + 1, c - 1), (r + 1, c + 1)
            ]

            for x, y in directions:
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    queue.append([x, y, l + 1])
        return -1

# T - O(N)
# S - O(N)
    
# Follow-up: If asked to print the path, rather than the length:
    
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        if grid[0][0] or grid[n - 1][n - 1]:
            return []

        queue = [(0, 0, [(0, 0)])]  # row, column, and path
        grid[0][0] = 1

        while queue:
            r, c, path = queue.pop(0)

            if r == n - 1 and c == n - 1:
                return path

            directions = [
                (r - 1, c), (r - 1, c - 1), (r - 1, c + 1),
                (r, c - 1), (r, c + 1),
                (r + 1, c), (r + 1, c - 1), (r + 1, c + 1)
            ]

            for x, y in directions:
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    queue.append((x, y, path + [(x, y)]))

        return []