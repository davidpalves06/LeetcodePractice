from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i,height in enumerate(heights):
            if not stack:
                stack.append((i,height))
                continue
            lastpopIndex = i
            while stack and stack[-1][1] > height:
                (index,popHeight) = stack.pop()
                maxArea = max(maxArea,(i-index) * popHeight)
                lastpopIndex = index
            stack.append((lastpopIndex,height))
        while stack:
            (index,popHeight) = stack.pop()
            maxArea = max(maxArea,(len(heights)-index) * popHeight)
        return maxArea
    
print(Solution.largestRectangleArea(None,[3,6,5,7,4,8,1,0]))