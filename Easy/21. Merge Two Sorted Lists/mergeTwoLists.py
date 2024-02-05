# ou are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []

# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

 

# Constraints:

#     The number of nodes in both lists is in the range [0, 50].
#     -100 <= Node.val <= 100
#     Both list1 and list2 are sorted in non-decreasing order.

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode()

        if not list1:
            return list2
        if not list2:
            return list1
        
        while list1 and list2:
            if list1.val < list2.val: # ex, if 2 < 3
                current.next = list1 # -> 2
                list1 = list1.next # -> 2 ->
            else:
                current.next = list2
                list2 = list2.next
            current = current.next 
        
        if list1:
            current.next = list1 # add remaining elements if missing from list 1 to the dummy list
        if list2:
            current.next = list2 # add remaining elements if missing from list 2 to the dummy list
        
        return dummy.next
