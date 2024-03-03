# https://leetcode.com/problems/strobogrammatic-number/description/


# Given a string num which represents an integer, return true if num is a strobogrammatic number.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

# Example 1:

# Input: num = "69"
# Output: true

# Example 2:

# Input: num = "88"
# Output: true

# Example 3:

# Input: num = "962"
# Output: false

 

# Constraints:

#     1 <= num.length <= 50
#     num consists of only digits.


class Solution:
    def isStrobogrammatic(self, num):
        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        i,j = 0, len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in maps:
                return False
            i += 1
            j -= 1
        return True
        