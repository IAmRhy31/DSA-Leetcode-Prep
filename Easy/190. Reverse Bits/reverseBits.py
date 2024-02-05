# Reverse bits of a given 32 bits unsigned integer.

# Note:

#     Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#     In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

 

# Example 1:

# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:

# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

 

# Constraints:

#     The input must be a binary string of length 32

 

# Follow up: If this function is called many times, how would you optimize it?

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1
            if n & 1 == 1:
                result += 1
            n >>= 1
        return result
       
# Explanation:

# Input: n = 00000010100101000001111010011100
# We start with result = 0.
# Now, let's go through the loop step by step:

#     Iteration 1:
#         result = 0
#         n = 00000010100101000001111010011100
#         We left shift result by 1: result = 0
#         The rightmost bit of n is 0, so we don't add anything to result.
#         n becomes 00000001010010100000111101001110
#     Iteration 2:
#         result = 0
#         n = 00000001010010100000111101001110
#         We left shift result by 1: result = 0
#         The rightmost bit of n is 0, so we don't add anything to result.
#         n becomes 00000000101001010000011110100111
#     Iteration 3:
#         result = 0
#         n = 00000000101001010000011110100111
#         We left shift result by 1: result = 0
#         The rightmost bit of n is 1, so we add 1 to result: result = 1
#         n becomes 00000000010100101000001111010011
#     Iteration 4:
#         result = 1
#         n = 00000000010100101000001111010011
#         We left shift result by 1: result = 10
#         The rightmost bit of n is 1, so we add 1 to result: result = 11
#         n becomes 00000000001010010100000111101001


#     Iteration 5:
#         result = 11
#         n = 00000000001010010100000111101001
#         We left shift result by 1: result = 110
#         The rightmost bit of n is 0, so we don't add anything to result.
#         n becomes 00000000000101001010000011110100
#     Iteration 6:
#         result = 110
#         n = 00000000000101001010000011110100
#         We left shift result by 1: result = 1100
#         The rightmost bit of n is 0, so we don't add anything to result.
#         n becomes 00000000000010100101000001111010
#     Iteration 7:
#         result = 1100
#         n = 00000000000010100101000001111010
#         We left shift result by 1: result = 11000
#         The rightmost bit of n is 1, so we add 1 to result: result = 11001
#         n becomes 00000000000001010010100000111101
#     Iteration 8:
#         result = 11001
#         n = 00000000000001010010100000111101
#         We left shift result by 1: result = 110010
#         The rightmost bit of n is 1, so we add 1 to result: result = 110011
#         n becomes 00000000000000101001010000011110

# ... and so on, until we complete 32 iterations.
# The reason we left shift result at the beginning of each iteration is to make space for the next bit that we will add to the result. This effectively moves the bits of result one position to the left, creating space for the next bit to be added.
# After 32 iterations, the final result will be the reversed binary representation of the input integer.
# I hope this detailed explanation helps clarify the process.
