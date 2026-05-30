class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dq = collections.deque()
        distance = 1

        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # add all tresures to do multi-source BFS from them
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    dq.append((row, col))

        
        while dq:

            for _ in range(len(dq)):
                row, col = dq.popleft()

                for dr, dc in DIRS:
                    final_row = row + dr
                    final_col = col + dc

                    if final_row < 0 or final_col < 0 or final_row >= ROWS or final_col >= COLS:
                        continue

                    if grid[final_row][final_col] != 2147483647:
                        continue

                    dq.append((final_row, final_col))
                    grid[final_row][final_col] = distance


            distance += 1

        
