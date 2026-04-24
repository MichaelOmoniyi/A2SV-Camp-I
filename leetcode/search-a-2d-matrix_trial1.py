class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        row = 0

        while low <= high:
            mid = (low + high) // 2

            if target <= matrix[mid][-1] and target >= matrix[mid][0]:
                colLow, colHigh = 0, len(matrix[0]) - 1

                while colLow <= colHigh:
                    colMid = (colLow + colHigh) // 2

                    if target == matrix[mid][colMid]:
                        return True
                    elif target > matrix[mid][colMid]:
                        colLow = colMid + 1
                    else:
                        colHigh = colMid - 1
                return False
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                high = mid - 1
        return False