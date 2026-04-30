class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        startIdx = sorted((intervals[i][0], i) for i in range(n))

        res = [-1] * n

        for i in range(n):
            ans = -1

            low, high = 0, n - 1

            while low <= high:
                mid = (low + high) // 2

                if startIdx[mid][0] >= intervals[i][1]:
                    ans = startIdx[mid][1]
                    high = mid - 1
                else:
                    low = mid + 1
            res[i] = ans
        return res