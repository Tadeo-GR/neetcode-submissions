from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            # Build a character-count signature for this string
            count = [0] * 26  # one slot per lowercase letter
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Use a tuple as the dict key (lists aren't hashable)
            groups[tuple(count)].append(s)

        return list(groups.values())
