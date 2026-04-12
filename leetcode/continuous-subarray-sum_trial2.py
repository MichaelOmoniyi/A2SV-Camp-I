class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remDict = {0: -1}
        remSum = 0

        for i in range(len(nums)):
            remSum = (remSum + nums[i]) % k

            if remSum not in remDict:
                remDict[remSum] = i
            else:
                if i - remDict[remSum] > 1:
                    return True
        return False