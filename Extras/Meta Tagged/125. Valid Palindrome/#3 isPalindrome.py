# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

 

# Constraints:

#     1 <= s.length <= 2 * 105
#     s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the beginning and end of the string
        l, r = 0, len(s) - 1

        # Iterate until the two pointers meet
        while l < r:
            # Move the left pointer to the next alphanumeric character
            while l < r and not self.isAlphaNum(s[l]):
                l += 1

            # Move the right pointer to the next alphanumeric character
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1

            # Check if the corresponding characters are equal (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False

            # Move the pointers towards each other
            l += 1
            r -= 1

        # If the loop completes, the string is a palindrome
        return True

    def isAlphaNum(self, c):
        # Check if a character is alphanumeric (letters or digits)
        return (
            ord('A') <= ord(c) <= ord('Z')
            or ord('0') <= ord(c) <= ord('9')
            or ord('a') <= ord(c) <= ord('z')
        )
