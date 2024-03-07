# https://leetcode.com/problems/merge-k-sorted-lists/

# https://www.youtube.com/watch?v=RCuBc4Zl-oY

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:

# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []

 

# Constraints:

#     k == lists.length
#     0 <= k <= 104
#     0 <= lists[i].length <= 500
#     -104 <= lists[i][j] <= 104
#     lists[i] is sorted in ascending order.
#     The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # add first elements of all the lists to the min heap
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i))
        
        dummy = curr = ListNode(0)

        while min_heap:
            val, i = heapq.heappop(min_heap) # pop the current smallest element from the heap
            curr.next = ListNode(val) # add to our output list
            if lists[i].next: # add the next element from the list where it's element was popped from heap to add in heap
                heapq.heappush(min_heap, (lists[i].next.val, i))
                lists[i] = lists[i].next
            curr = curr.next
        return dummy.next
        
        # Time Complexity: O(N log k)
        # Space Complexity: O(k)