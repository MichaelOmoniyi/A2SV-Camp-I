class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}

        for c in s:
            chars[c] = chars.get(c, 0) + 1

        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i

        return -1
        