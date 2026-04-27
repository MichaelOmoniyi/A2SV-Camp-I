class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            coinNo = (mid * (mid + 1)) // 2

            if coinNo == n:
                return mid
            elif coinNo > n:
                right = mid - 1
            else:
                left = mid + 1
        return right