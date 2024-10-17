from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        currentMax = 0
        left,right = 0, len(height) - 1
        while left < right:
            area = min(height[left],height[right]) * (right-left)
            currentMax = max(area,currentMax)
            

            if (height[left] > height[right]):
                right -= 1
            else:
                left +=1
        return currentMax
    
print(Solution.maxArea(None,[1,1]))