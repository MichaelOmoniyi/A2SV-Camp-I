class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        def canEat(k):
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            return hours <= h

        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2

            if canEat(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left