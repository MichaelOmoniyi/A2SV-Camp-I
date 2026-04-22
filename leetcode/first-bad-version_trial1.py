# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if isBadVersion(mid):
                if isBadVersion(mid - 1):
                    high = mid - 1
                else:
                    return mid
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    low = mid + 1