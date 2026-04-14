class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Recursion
        memo = {}
        def get(row, col):
            if col == 0 or col == row:
                return 1

            if (row, col) in memo:
                return memo[(row, col)]
                
            memo[(row, col)] = get(row - 1, col - 1) + get(row - 1, col)
            return memo[(row, col)]

        indexedRow = []

        for col in range(rowIndex + 1):
            indexedRow.append(get(rowIndex, col))
        
        return indexedRow