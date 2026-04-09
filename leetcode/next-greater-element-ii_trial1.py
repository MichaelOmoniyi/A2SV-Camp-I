class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums * 2
        n = len(nums)
        stack = []

        for i in range(n):
            print(f"For i: {i}")
            print(f"Stack before: {stack}")
            while stack and nums[stack[-1]] < nums[i]:
                nums[stack.pop()] = nums[i]
            stack.append(i)
        while stack:
            nums[stack.pop()] = -1
        return nums[:n//2]