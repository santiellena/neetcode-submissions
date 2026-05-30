class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for source, destination, weight in flights:
            adj[source].append((destination, weight))

        minHeap = []
        heapq.heappush(minHeap, (0, 0, src))

        visited = set()

        while minHeap:
            weight, stops, node = heapq.heappop(minHeap)

            if (node, stops) in visited: 
                continue
            visited.add((node, stops))

            if node == dst and stops - 1 <= k:
                return weight


            for dest, cost in adj[node]:
                if dest not in visited:
                    heapq.heappush(minHeap, (weight + cost, stops + 1, dest))

        return -1

            



