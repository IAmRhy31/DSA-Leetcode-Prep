# https://leetcode.com/problems/add-strings/

# https://www.youtube.com/watch?v=q1RR8gk47Cg

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"

 

# Constraints:

#     1 <= num1.length, num2.length <= 104
#     num1 and num2 consist of only digits.
#     num1 and num2 don't have any leading zeros except for the zero itself.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0:
            if i >= 0:
                curr_i = int(num1[i])
            else:
                curr_i = 0
            
            if j >= 0:
                curr_j = int(num2[j])
            else:
                curr_j = 0
            
            curr_sum = carry + curr_i + curr_j

            result.append(str(curr_sum % 10))

            carry = curr_sum // 10

            i -= 1
            j -= 1
        
        if carry:
            result.append(str(carry))
        
        return "".join(reversed(result))

        # T: O(N + M)
        # S: O(N + M)