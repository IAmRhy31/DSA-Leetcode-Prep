# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:

# Input: head = [1,2]
# Output: [2,1]

# Example 3:

# Input: head = []
# Output: []

 

# Constraints:

#     The number of nodes in the list is the range [0, 5000].
#     -5000 <= Node.val <= 5000

 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recursive_reverse(prev, curr):
            if curr is None:
                return prev
            else:
                next_node = curr.next # this is tmp from our iterative solution
                curr.next = prev
                return recursive_reverse(curr, next_node)

        return recursive_reverse(None, head)