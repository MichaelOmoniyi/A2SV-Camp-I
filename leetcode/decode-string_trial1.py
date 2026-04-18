class Solution:
    def decodeString(self, s: str) -> str:
        digitStack = []
        charStack = []
        num, ans = 0, ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                digitStack.append(num)
                charStack.append(ans)
                num = 0
                ans = ""
            elif char == "]":
                ans = charStack.pop() + ans * digitStack.pop()
            else:
                ans += char
        return ans