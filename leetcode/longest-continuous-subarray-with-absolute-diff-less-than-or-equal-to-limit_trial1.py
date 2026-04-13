from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQueue = deque()
        maxQueue = deque()
        left, ans = 0, 0

        for right in range(len(nums)):
            while minQueue and nums[right] < minQueue[-1]:
                minQueue.pop()
            while maxQueue and nums[right] > maxQueue[-1]:
                maxQueue.pop()

            maxQueue.append(nums[right])
            minQueue.append(nums[right])

            while maxQueue[0] - minQueue[0] > limit:
                if nums[left] == minQueue[0]:
                    minQueue.popleft()
                if nums[left] == maxQueue[0]:
                    maxQueue.popleft()
                left += 1

            ans = max(ans, right - left + 1)
        return ans