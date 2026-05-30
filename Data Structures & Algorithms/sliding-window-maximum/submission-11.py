import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []

        for r in range(len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            while heap[0][1] <= r - k:
                heapq.heappop(heap)

            if r >= k - 1:
                result.append(-heap[0][0])

        return result
