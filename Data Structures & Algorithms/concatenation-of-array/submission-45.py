class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        duplicate = len(nums)
        answer = [0] * (2 * duplicate)
        for i, nums in enumerate(nums):
            answer[i] = nums
            answer[i + duplicate] = nums
        return answer