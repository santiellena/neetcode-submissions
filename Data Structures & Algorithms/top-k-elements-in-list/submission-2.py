import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        heap = []

        for key, value in seen.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [value for key, value in heap]







