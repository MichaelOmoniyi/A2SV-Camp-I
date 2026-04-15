class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n.is_integer() or n < 1:
            return False

        if n == 1:
            return True

        return self.isPowerOfThree(n / 3)