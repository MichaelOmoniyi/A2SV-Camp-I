class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # pointer for position to write to

        # loop through all the numbers
        for num in nums:
            if num != val:
                nums[i] = num # moves number to the front
                i += 1

        return i
        