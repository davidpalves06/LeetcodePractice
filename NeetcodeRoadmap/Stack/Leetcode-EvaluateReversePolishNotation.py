from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                oper1 = int(stack.pop())
                oper2 = int(stack.pop())
                
                stack.append(oper1 + oper2)
            elif token == '-':
                oper1 = int(stack.pop())
                oper2 = int(stack.pop())
                stack.append(oper2 - oper1)
            elif token == '*':
                oper1 = int(stack.pop())
                oper2 = int(stack.pop())
                stack.append(oper1 * oper2)
            elif token == '/':
                oper1 = int(stack.pop())
                oper2 = int(stack.pop())
                stack.append(int(oper2 / oper1))
            else:
                stack.append(token)
        return int(stack.pop())
    
print(Solution.evalRPN(None,["4","13","5","/","+"]))
