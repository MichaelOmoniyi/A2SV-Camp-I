class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))

        while left <= right:
            sumOfSquares = left * left + right * right
            if sumOfSquares > c:
                right -= 1
            elif sumOfSquares < c:
                left += 1
            else:
                return True
        return False