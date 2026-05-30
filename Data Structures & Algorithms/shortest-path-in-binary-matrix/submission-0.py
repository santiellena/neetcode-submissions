class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        distance = 1

        DIRS = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]

        dq = collections.deque()
        dq.append((0, 0)) # top-left

        found = False

        while dq and not found:
            
            for _ in range(len(dq)):
                row, col = dq.popleft()

                for row_move, col_move in DIRS:
                    final_row = row + row_move
                    final_col = col + col_move

                    if final_row + 1 == ROWS and final_col + 1 == COLS:
                        found = True
                        break

                    if final_row < 0 or final_col < 0 or final_row >= ROWS or final_col >= COLS:
                        continue

                    if grid[final_row][final_col] == 1:
                        continue

                    dq.append((final_row, final_col))
                    grid[final_row][final_col] = 1


            distance += 1

        return distance if found else -1

