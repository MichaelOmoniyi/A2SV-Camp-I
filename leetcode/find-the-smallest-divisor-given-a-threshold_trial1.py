class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        import math

        low, high = 1, max(nums)
        res = high

        while low <= high:
            mid = (low + high) // 2

            currSum = 0
            for num in nums:
                currSum += math.ceil(num / mid)

            if currSum <= threshold:
                res = mid
                high = mid - 1   # try smaller divisor
            else:
                low = mid + 1    # need bigger divisor

        return res