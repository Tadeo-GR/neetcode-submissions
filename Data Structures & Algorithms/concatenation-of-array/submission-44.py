class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * (2 * n)
        
        for i, num in enumerate(nums):
            answer[i] = num
            answer[i + n] = num
        
        return answer