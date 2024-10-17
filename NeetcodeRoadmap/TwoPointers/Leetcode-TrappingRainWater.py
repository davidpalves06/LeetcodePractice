from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        trappedWater = 0
        left,right = 0,len(height) - 1 
        maxLeft,maxRight = 0,0

        while left <= right:
            if maxLeft <= maxRight:
                maxLeft = max(maxLeft,height[left])
                trappedWater += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight,height[right])
                trappedWater += maxRight - height[right]
                right -= 1
        return trappedWater
    
print(Solution.trap(None,[0,1,0,2,1,0,1,3,2,1,2,1]))