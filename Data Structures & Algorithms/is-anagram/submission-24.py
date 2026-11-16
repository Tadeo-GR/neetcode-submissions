class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26                     # ✅ list of 26 zeros
        for char in s:
            count[ord(char) - ord('a')] += 1 # ✅ subtract to map 'a'..'z' → 0..25
        for char in t:
            count[ord(char) - ord('a')] -= 1
        
        return all(i == 0 for i in count)    # ✅ check every slot is 0