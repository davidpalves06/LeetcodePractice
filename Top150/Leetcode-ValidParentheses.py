from collections import defaultdict


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif ch == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif ch == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif ch == '}':
                if not stack or stack.pop() != '{':
                    return False
        return True if not stack else False