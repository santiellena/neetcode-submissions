class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        result = 0
        seen = set()

        def dfs(row: int, col: int):
            # Here I just have to mark all adjacent land as seen (all the island)
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            if grid[row][col] == '0' or (row, col) in seen:
                return

            seen.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row, col) not in seen:
                    dfs(row, col)
                    result += 1

        return result