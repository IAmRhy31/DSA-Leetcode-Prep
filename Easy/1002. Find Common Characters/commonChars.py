# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

 

# Constraints:

#     1 <= words.length <= 100
#     1 <= words[i].length <= 100
#     words[i] consists of lowercase English letters.

from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        charCount = Counter(words[0])

        for word in words[1:]:
            wordCount = Counter(word)
            for key in list(charCount.keys()):
                if key not in wordCount:
                    del charCount[key]
                else:
                    charCount[key] = min(charCount[key], wordCount[key])

        res = []
        for key in charCount:
            res += [key] * charCount[key]

        return res
