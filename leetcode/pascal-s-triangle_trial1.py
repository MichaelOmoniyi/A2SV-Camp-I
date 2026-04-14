class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Recursion
        memo = {}
        def get(row, col):
            if col == 0 or col == row:
                return 1

            if (row, col) in memo:
                return memo[(row, col)]
                
            memo[(row, col)] = get(row - 1, col - 1) + get(row - 1, col)
            return memo[(row, col)]

        triangle = []

        for row in range(numRows):
            tempRow = []
            for col in range(row + 1):
                tempRow.append(get(row, col))
            triangle.append(tempRow)
        return triangle

        # triangle = [[1]] # starts the triangle with the first row

        # while len(triangle) < numRows:
        #     lastRow = triangle[-1] # stores the last row of the triangle
        #     row = [1] # initializes a new row
        #     for i in range(1, len(lastRow)):
        #         row.append(lastRow[i] + lastRow[i - 1]) # appends to the new row the sum of two numbers directly above the current index
        #     row.append(1)
        #     triangle.append(row)

        # return triangle