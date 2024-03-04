# https://leetcode.com/problems/ransom-note/description/

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

 

# Constraints:

#     1 <= ransomNote.length, magazine.length <= 105
#     ransomNote and magazine consist of lowercase English letters.

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)

        for char in magazine:
            if r_counter[char]:
                r_counter[char] -= 1
                if r_counter[char] == 0:
                    del r_counter[char]
        if not r_counter:
            return True
        return False
