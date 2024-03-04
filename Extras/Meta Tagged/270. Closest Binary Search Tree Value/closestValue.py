# https://leetcode.com/problems/closest-binary-search-tree-value/description/

# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

 

# Example 1:

# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4

# Example 2:

# Input: root = [1], target = 4.428571
# Output: 1

 

# Constraints:

#     The number of nodes in the tree is in the range [1, 104].
#     0 <= Node.val <= 109
#     -109 <= target <= 109

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_value = float("inf")
        curr = root

        while curr:
            if curr.val == target:
                return curr.val
            if abs(curr.val - target) < abs(closest_value - target):
                closest_value = curr.val
            if abs(curr.val - target) == abs(closest_value - target):
                closest_value = min(curr.val, closest_value)

            if curr.val > target:
                curr = curr.left
            else:
                curr = curr.right
        return closest_value
