class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: empty list → no common prefix
        if not strs:
            return ""
        
        # Take the first string as reference
        first = strs[0]
        
        # Check character by character
        for i in range(len(first)):
            char = first[i]
            # Compare with the same position in every other string
            for s in strs[1:]:   # skip the first string
                # If we reached the end of a string OR character mismatch
                if i >= len(s) or s[i] != char:
                    # Prefix is from 0 to i (exclusive)
                    return first[:i]
        
        # All characters of the first string matched
        return first