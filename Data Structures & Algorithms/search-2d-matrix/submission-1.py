class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            m = (l + r) // 2

            row = m // cols
            col = m % cols

            val = matrix[row][col]

            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return True

        return False