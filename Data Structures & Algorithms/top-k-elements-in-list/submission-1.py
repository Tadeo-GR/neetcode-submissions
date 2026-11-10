from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        n = len(nums)

        # buckets[i] = list of elements that appear exactly i times
        buckets = [[] for _ in range(n + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)

        result = []
        for freq in range(n, 0, -1):        # highest frequency first
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result