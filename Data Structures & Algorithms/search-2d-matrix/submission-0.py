class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # rows in increasing order

        # pick the row with binary search then pick the column with binary search

        # [
        #   [1, 2, 3]
        #   [4, 5, 6]
        #   [7, 8, 9]
        # ]

        l, r = 0, len(matrix) - 1
        row = -1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = mid
                l = r + 1 # break while
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1


        return False