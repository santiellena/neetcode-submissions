class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        pairs = list(seen.items())

        pairs.sort(key=lambda pair: pair[1], reverse=True)

        return [key for key, value in pairs[:k]]



