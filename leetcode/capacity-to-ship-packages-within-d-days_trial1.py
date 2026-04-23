class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            curWeight, noOfDays = 0, 1

            for weight in weights:
                curWeight += weight

                if curWeight > capacity:
                    noOfDays += 1
                    curWeight = weight
            return noOfDays <= days


        left, right = max(weights), sum(weights)
        firstTrueIndex = -1

        while left <= right:
            mid = (left + right) // 2

            if feasible(mid):
                firstTrueIndex = mid
                right = mid - 1
            else:
                left = mid + 1
        return firstTrueIndex