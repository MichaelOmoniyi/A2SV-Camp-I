class Solution:
    def arrangeCoins(self, n: int) -> int:
        rowLen = 0
        cnt = 0

        while cnt < n:
            if cnt + rowLen + 1 >= n and rowLen >= n - cnt:
                return rowLen
            
            rowLen += 1
            cnt += rowLen
        return rowLen