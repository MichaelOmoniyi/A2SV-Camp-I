class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        valid_path = ''
        path = path.split('/')
        for element in path:
            if element  == '..':
                if stack: 
                    stack.pop()
                continue
            elif element == '.' or not element:
                continue
            stack.append(element)
        for el in stack:
            valid_path += '/' + el
        if not stack:
            valid_path = '/'
        return valid_path