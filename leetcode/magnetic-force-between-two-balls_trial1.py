class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        res = 0

        while left <= right:
            mid = (left + right) // 2
            count = 1
            last = position[0]

            for i in range(len(position)):
                if position[i] - last >= mid:
                    count += 1
                    last = position[i]
            if count >= m:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res