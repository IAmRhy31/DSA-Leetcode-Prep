# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"

# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

 

# Constraints:

#     1 <= s.length <= 3 * 105
#     s consist of printable ASCII characters.

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        n = len(s_list)
        vowels = "aeiouAEIOU"
        l = 0
        r = n - 1

        while l < r:
            if s_list[l] in vowels:
                if s_list[r] in vowels:
                    s_list[l], s_list[r] = s_list[r], s_list[l]
                    l += 1
                    r -= 1
                else:
                    r -= 1
            else:
                l += 1
        return ''.join(s_list)
