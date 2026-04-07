class Solution:
    def isValid(self, s: str) -> bool:
        closingMatch = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        if s[0] in closingMatch:
            return False

        for char in s:
            print(char)
            if not stack:
                stack.append(char)
                print(f"new stack: {s}")
            else:
                if char not in closingMatch:
                    stack.append(char)
                else:
                    if closingMatch[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        else:
            return True