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
        row = []
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = matrix[mid]
                break
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        
        l, r = 0, len(row) - 1

        while row and l <= r:
            mid = (l + r) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1


        return False