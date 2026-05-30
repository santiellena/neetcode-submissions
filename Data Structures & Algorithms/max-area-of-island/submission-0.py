class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()

        def dfs(row, col) -> int:
            print("row: ", row)
            print("col: ", col)
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 0 
            
            if grid[row][col] == 0 or (row, col) in seen:
                return 0

            
            seen.add((row, col))

            return (1 + 
                dfs(row - 1, col) + 
                dfs(row + 1, col) +
                dfs(row, col - 1) + 
                dfs(row, col + 1))

        result = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in seen:
                    result = max(result, dfs(row, col)) 


        return result