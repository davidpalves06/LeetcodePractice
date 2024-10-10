from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]):
        stack = []
        maxWidth = 0
        for i in range(len(nums)):
            stackSize = len(stack)
            if (stackSize == 0):
                stack.append(i)
            else:
                if (nums[i] < nums[stack[-1]]):
                    stack.append(i)

        for i in range(len(nums) - 1,-1,-1):
            if (len(stack) == 0):
                break
            while (len(stack) != 0 and nums[i] >= nums[stack[-1]]):
                j = stack.pop()
                maxWidth = max(i - j,maxWidth)
        return maxWidth
        
    
print(Solution.maxWidthRamp(None,[9,8,1,0,1,9,4,0,4,1]))