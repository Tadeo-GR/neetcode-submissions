from typing import List, Optional

class Solution:
    def hasDuplicate(self, nums: Optional[List[int]]) -> bool:
        # Edge case: input is None or empty
        if not nums:
            return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False