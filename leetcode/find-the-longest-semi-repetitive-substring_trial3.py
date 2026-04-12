class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
            
        left, adjStart, adjStr = 0, 0, 0
        longestSubstring = 0

        for right in range(1, len(s)):
            print(f"At index {right}: Left - {left}")
            if s[right] == s[right - 1]:
                adjStr += 1
                if adjStr > 1:
                    left = adjStart
                adjStart = right

            longestSubstring = max(longestSubstring, right - left + 1)
        return longestSubstring