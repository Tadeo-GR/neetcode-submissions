from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_strs =  min(strs)
        max_strs =  max(strs)
        for i, char in enumerate(min_strs):
            if char not in max_strs[i]:
                return min_strs[:i]
        return min_strs

    