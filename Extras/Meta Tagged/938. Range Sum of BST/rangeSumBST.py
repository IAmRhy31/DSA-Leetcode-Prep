# https://leetcode.com/problems/range-sum-of-bst/

# Iterative : https://www.youtube.com/watch?v=6dT3ZWhgDAU

# Recursive: https://www.youtube.com/watch?v=uLVG45n4Sbg

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Example 1:

# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# Example 2:

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

# Constraints:

#     The number of nodes in the tree is in the range [1, 2 * 104].
#     1 <= Node.val <= 105
#     1 <= low <= high <= 105
#     All Node.val are unique.

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Iterative Solution (preferred, in case recursive since recursion can result in stack overflow in real-world problems - if asked in an interview)
        # T : O(N)
        # S : O(N)

        if not root:
            return 0

        result = 0
        stack = [root]

        while stack:
            curr = stack.pop()

            if curr:
                if low <= curr.val and curr.val <= high:
                    result += curr.val

                if curr.val > low:
                    stack.append(curr.left)

                if curr.val < high:
                    stack.append(curr.right)
        return result

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Recursive Solution
        # T : O(N)
        # S : O(N)

        if not root:
            return 0

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )
