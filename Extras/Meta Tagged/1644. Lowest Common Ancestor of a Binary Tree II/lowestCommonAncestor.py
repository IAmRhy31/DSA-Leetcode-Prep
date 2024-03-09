# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

# https://www.youtube.com/watch?v=7csj-Elpmmo&t=755s

# Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

 

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.

# Example 3:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
# Output: null
# Explanation: Node 10 does not exist in the tree, so return null.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_found = False
        self.q_found = False

        ans = self.dfs(root, p, q)

        if self.p_found and self.q_found:
            return ans
        return None # return null if p or q doesn't exist in the tree

    # do a post-order traversal: left -> right -> node to first check p_found and q_found are true
    # then return the LCA value if both are true and there
    def dfs(self, node, p, q):
        if not node:
            return None
        
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)

        if node == p or node == q:
            if node == p:
                self.p_found = True
            else:
                self.q_found = True
            return node

        if left and right:
            return node
        else:
            return left or right 

        # T : O(N)
        # S : O(N)
