class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        distinctSort = 0
        operations = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                distinctSort += 1
            operations += distinctSort
        return operations