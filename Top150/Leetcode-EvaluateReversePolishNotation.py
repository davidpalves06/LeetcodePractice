from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                stack.append(firstOperand + secondOperand)
            elif token == "-":
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                stack.append(firstOperand - secondOperand)
            elif token == "/":
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                stack.append(int(firstOperand / secondOperand))
            elif token == "*":
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                stack.append(firstOperand * secondOperand)
            else:
                stack.append(int(token))
        return stack.pop()
    
print(Solution.evalRPN(None,tokens = ["2","1","+","3","*"]))
print(Solution.evalRPN(None,tokens = ["4","13","5","/","+"]))
print(Solution.evalRPN(None,tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
