class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = collections.deque()
        fresh = 0
        minutes = 0
        ROWS, COLS = len(grid), len(grid[0])

        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2: # starting points
                    dq.append((row, col))

        
        while dq and fresh > 0: # this means: 
            # as long as i have rotten fruits that could make fresh fruit rotten, continue the process
            # if there is no more fresh fruit stop

            for _ in range(len(dq)):
                (row, col) = dq.popleft()

                for row_move, col_move in DIRS:
                    final_row = row + row_move
                    final_col = col + col_move

                    if final_row < 0 or final_row >= ROWS or final_col < 0 or final_col >= COLS:
                        continue

                    if grid[final_row][final_col] == 1:
                        dq.append((final_row, final_col))
                        grid[final_row][final_col] = 2
                        fresh -= 1
                
            
            minutes += 1


        if fresh == 0:
            return minutes
        else:
            return -1

        




