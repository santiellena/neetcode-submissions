import heapq
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heap = []

        for i in range(len(heights)):
            for j in range(1, len(heights)):
                max_height = min(heights[i], heights[j])

                area = (j - i) * max_height

                heapq.heappush(heap, area)

                if len(heap) > 1:
                    heapq.heappop(heap)

        return heap[0]