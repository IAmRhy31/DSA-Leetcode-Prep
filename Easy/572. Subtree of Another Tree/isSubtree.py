# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:

# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

 

# Constraints:

#     The number of nodes in the root tree is in the range [1, 2000].
#     The number of nodes in the subRoot tree is in the range [1, 1000].
#     -104 <= root.val <= 104
#     -104 <= subRoot.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: # if null subRoot tree
            return True
        if not root: # if null root tree
            return False
        if self.isSameTree(root, subRoot): # check to see if both trees are same using helper function created below
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) # one of root's left nodes or root's right nodes are equal to the subRoot tree
        
    def isSameTree(self, root, subRoot): # helper function to determine if both root and subRoot trees are same (like #100. Same Tree Leetcode Q)
        if not root and not subRoot: # if both null, return true
            return True
        if root and subRoot and root.val == subRoot.val: # if both not null and their root's value is equal, traverse and compare both left and right with values and order
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        return False # return false, for any other case