import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # (diff, row, col)
        # so we prioritize by diff (the smaller one gets popped)
        minHeap = [(0, 0, 0)]

        DIRS = [(1,0), (0,1), (-1,0), (0,-1)]

        ROWS, COLS = len(heights), len(heights[0])

        visited = set()

        while minHeap:
            diff, row, col = heapq.heappop(minHeap)

            if (row, col) in visited: continue
            visited.add((row, col))

            if (row, col) == (ROWS - 1, COLS - 1):
                return diff

            for dr, dc in DIRS:
                newRow, newCol = row + dr, col + dc

                if newRow < 0 or newCol < 0 or newRow == ROWS or newCol == COLS:
                    continue

                if (newRow, newCol) in visited: 
                    continue

                newDiff = max(diff, abs(heights[row][col] - heights[newRow][newCol]))
                heapq.heappush(minHeap, (newDiff, newRow, newCol))





