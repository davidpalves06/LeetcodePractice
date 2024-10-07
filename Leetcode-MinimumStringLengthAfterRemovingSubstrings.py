class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            stack.append(c)

            if (len(stack) >= 2):
                firstSub = stack[-2]
                lastSub = stack[-1]
                if (firstSub == 'A' and lastSub == 'B') or (firstSub == 'C' and lastSub == 'D'):
                    stack.pop()
                    stack.pop()
        
        return len(stack)
print(Solution.minLength(None,"ABFCACDB"))