import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap,-stone)


        while True:
            if len(heap) < 2:
                if heap:
                    return -heap[0]
                else:
                    return 0

            heavier = -heapq.heappop(heap) 
            lighter = -heapq.heappop(heap)

            if heavier > lighter:
                heapq.heappush(heap, -(heavier - lighter))



