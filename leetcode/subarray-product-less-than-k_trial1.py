class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        pos = sorted(position)
        l, r = 1, pos[-1] - pos[0]
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            count = 1
            last = pos[0] 
            for i in range(1, len(pos)): 
                if pos[i] - last >= mid:
                    count += 1
                    last = pos[i]
            if count >= m:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans