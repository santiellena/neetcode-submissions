class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        heapq.heappush(minHeap, (0, k))

        visited = set()

        while minHeap:
            dist, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            visited.add(node)

            if len(visited) == n:
                return dist

            for (source, target, time) in times:
                if source == node:
                    heapq.heappush(minHeap, (dist + time, target))

        return -1

