# https://leetcode.com/problems/nested-list-weight-sum/description/

# https://www.youtube.com/watch?v=jR2UC4K-q2U

# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

# Return the sum of each integer in nestedList multiplied by its depth.

 

# Example 1:

# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

# Example 2:

# Input: nestedList = [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.

# Example 3:

# Input: nestedList = [0]
# Output: 0

 

# Constraints:

#     1 <= nestedList.length <= 50
#     The values of the integers in the nested list is in the range [-100, 100].
#     The maximum depth of any integer is less than or equal to 50.

# add the elements of nestedList in a queue
# if it's a single integer, multiple its value to the depth and add it to the result
# if it's a list, append the elements of the list (not the whole list) to end of the queue by using queue.extend(curr.getList())
# increase depth += 1 each round

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


from collections import deque

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        depth = 1
        result = 0

        queue = deque(nestedList)

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr.isInteger():
                    result += curr.getInteger() * depth
                else:
                    queue.extend(curr.getList())

            depth += 1
        return result
