class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def sub(a, b):
            return(a - b)

        def add(a, b):
            return(a + b)

        def multiply(a, b):
            return(a * b)

        def divide(a, b):
            return(a / b)

        operators = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in operators:
                secondOperand = int(stack.pop())
                firstOperand = int(stack.pop())
                if token == "+":
                    stack.append(add(firstOperand, secondOperand))
                elif token == "-":
                    stack.append(sub(firstOperand, secondOperand))
                elif token == "*":
                    stack.append(multiply(firstOperand, secondOperand))
                else:
                    stack.append(divide(firstOperand, secondOperand))
            else:
                stack.append(int(token))
        return int(stack[0])