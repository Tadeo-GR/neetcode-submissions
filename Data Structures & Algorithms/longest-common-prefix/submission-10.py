from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_str = min(strs)
        max_str = max(strs)
        for i, char in enumerate(min_str):
            if char != max_str[i]:
                return min_str[:i]
        return min_str          # <-- missing before

      