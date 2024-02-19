# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

 

# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters.

# https://www.youtube.com/watch?v=5nug0L9y1h4

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        prefixLen = len(prefix)

        for s in strs[1:]:
            while prefix != s[0:prefixLen]:
                prefix = prefix[0 : prefixLen - 1]
                prefixLen -= 1

                if prefixLen == 0:
                    return ""
        return prefix
