class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], 0, 0))

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()

        while minHeap:
            time, row, col = heapq.heappop(minHeap)

            if (row, col) in visited:
                continue
            visited.add((row, col))

            if row == ROWS - 1 and col == COLS - 1:
                return time

            for dr, dc in DIRS:
                fr = row + dr
                fc = col + dc

                if fr < 0 or fc < 0 or fr == ROWS or fc == COLS:
                    continue

                if (fr, fc) in visited:
                    continue

                # prev is greater than curr (stays equal)
                # curr is greater than prev (t = curr)
                print("row: ", row)
                print("col: ", col)
                print("prev: ", time)
                print("new_row: ", fr)
                print("new_col: ", fc)
                print("cu")
                if time >= grid[fr][fc]:
                    heapq.heappush(minHeap, (time, fr, fc))
                else:
                    heapq.heappush(minHeap, (grid[fr][fc], fr, fc))






