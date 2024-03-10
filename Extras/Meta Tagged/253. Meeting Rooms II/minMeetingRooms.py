# https://leetcode.com/problems/meeting-rooms-ii/

# https://www.youtube.com/watch?v=h_Ej3FFfnek

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

 

# Constraints:

#     1 <= intervals.length <= 104
#     0 <= starti < endi <= 106

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda i: i[0])

        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])

        for i in intervals[1:]:
            if i[0] >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, i[1])

        return len(min_heap)

        # T - O(nlogn)
        # S - O(N)
