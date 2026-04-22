class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        if n == 0:
            return [-1, -1]

        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                while nums[low] != target:
                    low += 1

                while nums[high] != target:
                    high -= 1
                return [low, high]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid  + 1
        else:
            return [-1, -1]