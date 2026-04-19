class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        midPoint = 1 << (n - 2)

        if k <= midPoint:
            return self.kthGrammar(n - 1, k)

        return self.kthGrammar(n - 1, k - midPoint) ^ 1