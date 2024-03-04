# https://leetcode.com/problems/maximum-swap/description/

# https://www.youtube.com/watch?v=PALPz9r2Q4A

# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

 

# Example 1:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

# Example 2:

# Input: num = 9973
# Output: 9973
# Explanation: No swap.

 

# Constraints:

#     0 <= num <= 108

from collections import deque

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 11:
            return num

        num_as_list = deque([])

        # adding num in sequence wise to our num_as_list using queue
        while num:
            num_as_list.appendleft(num % 10)
            num //= 10

        max_num_seen = -1  # 1
        max_num_at = len(num_as_list)  # 2
        i = len(num_as_list) - 1

        # traverse right to left to give max_num_seen (#1) and max_num_at (#2) indexes
        while i >= 0:
            curr_num = num_as_list[i]
            num_as_list[i] = (curr_num, max_num_seen, max_num_at)  # add # 1 and # 2 to our nums_as_list[i] value

            if curr_num > max_num_seen:
                max_num_seen = curr_num
                max_num_at = i
            i -= 1

        i = 0
        # traverse left to right to swap
        while i < len(num_as_list):
            curr_num, max_to_right, max_num_at = num_as_list[i]

            if max_to_right > curr_num:
                num_as_list[i], num_as_list[max_num_at] = num_as_list[max_num_at], num_as_list[i]
                break
            i += 1

        # converting our final num_as_list to number
        number = 0
        for num, _, _ in num_as_list:
            number = number * 10 + num
        return number
