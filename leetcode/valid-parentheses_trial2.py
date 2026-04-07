class Solution:
    def isValid(self, s: str) -> bool:
        closingMatch = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for char in s:
            if char not in closingMatch:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1] != closingMatch[char]:
                        return False
                    else:
                        stack.pop()
        return len(stack) <= 0