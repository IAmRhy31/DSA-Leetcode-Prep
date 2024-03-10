# https://leetcode.com/problems/group-shifted-strings/

# https://www.youtube.com/watch?v=g_CWHtPSQmQ&t=69s

# We can shift a string by shifting each of its letters to its successive letter.

#     For example, "abc" can be shifted to be "bcd".

# We can keep shifting the string to form a sequence.

#     For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

# Example 1:

# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

# Example 2:

# Input: strings = ["a"]
# Output: [["a"]]

 

# Constraints:

#     1 <= strings.length <= 200
#     1 <= strings[i].length <= 50
#     strings[i] consists of lowercase English letters.

import collections
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        # Idea is to create a map of:
        # key : tuple of difference between character values in each string
        # value : that specific string value

        grouping_dict = collections.defaultdict(list)

        for string in strings:
            if len(string) == 1:
                grouping_dict[(-1)].append(string)
            else:
                char_diff = []

                i = 1

                while i < len(string):
                    char_diff.append((ord(string[i]) - ord(string[i - 1])) % 26)
                    i += 1

                grouping_dict[tuple(char_diff)].append(string)

        return grouping_dict.values()

        # T: O(N * K), N = number of string in strings, K = length of longest string in strings
        # S: O(N * K)
