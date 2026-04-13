class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n

        for first, last, seats in bookings:
            ans[first - 1] += seats

            if last < n:
                ans[last] -= seats

        prefixSum = 0
        for i in range(n):
            prefixSum += ans[i]
            ans[i] = prefixSum
        return ans