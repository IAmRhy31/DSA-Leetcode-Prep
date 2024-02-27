# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# https://www.youtube.com/watch?v=_Froy1yUCWw&t=11s

# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

# Example 2:

# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]

# Example 3:

# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]

 

# Constraints:

#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100

# 1: Create a dictionary to store, column value : to their key's value
# 2: Queue for BFS and popping the first element and adding in to the dict_nodes
# 3: Sort the dictionary by keys (lowest col values) since we traverse left through right and append the respective key's value to the result list

import collections
from typing import List, Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dict_nodes = collections.defaultdict(list)
        queue = [(root, 0)]
        result = []

        while queue:
            curr, col = queue.pop(0)
            dict_nodes[col].append(curr.val)

            if curr.left:
                queue.append((curr.left, col - 1))
            if curr.right:
                queue.append((curr.right, col + 1))

        for key in sorted(dict_nodes.keys()):
            result.append(dict_nodes[key])
        return result

