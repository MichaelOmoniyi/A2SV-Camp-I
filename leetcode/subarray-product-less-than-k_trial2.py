class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        product = 1
        l = 0
        ans = 0

        for r in range(len(nums)):
            product *= nums[r]

            while product >= k:
                product //= nums[l]
                l += 1

            ans += (r - l + 1)

        return ans