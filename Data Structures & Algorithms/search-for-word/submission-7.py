class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1,0), (0,1), (-1,0), (0,-1)]

        visited = set()

        def dfs(row, col, index) -> bool:
            if len(word) == index:
                return True

            if row < 0 or col < 0 or row == ROWS or col == COLS or (row, col) in visited:
                return False

            if word[index] != board[row][col]:
                return False

            visited.add((row, col))

            found = False

            for dr, dc in DIRS:
                found = found or dfs(row + dr, col + dc, index + 1)

            visited.remove((row, col))

            return found


        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    visited = set()
                    if dfs(row, col, 0):
                        return True

        return False