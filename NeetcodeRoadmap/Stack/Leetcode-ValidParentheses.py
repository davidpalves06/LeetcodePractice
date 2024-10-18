

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                open = stack.pop()
                if (c == ')' and open != '(') or (c == ']' and open != '[') or (c == '}' and open != '{'):
                    return False
        if len(stack) > 0:
            return False
        return True