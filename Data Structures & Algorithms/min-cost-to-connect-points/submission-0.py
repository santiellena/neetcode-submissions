class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}

        visited = set()
        total = 0

        for x1, y1 in points:
            adj[(x1, y1)] = []
            for x2, y2 in points:
                if (x1, y1) != (x2, y2):
                    adj[(x1, y1)].append((abs(x1 - x2) + abs(y1 - y2), x2, y2))

        minHeap = []
        heapq.heappush(minHeap, (0, points[0][0], points[0][1]))


        while minHeap:
            cost, x, y = heapq.heappop(minHeap)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            total += cost

            for cost, x1, y1 in adj[(x, y)]:
                if (x1, y1) not in visited:
                    heapq.heappush(minHeap, (cost, x1, y1))

        return int(total)

