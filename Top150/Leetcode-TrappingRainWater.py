from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        rightHigher = [0] * len(height)

        higher = height[-1]
        for i in range(len(height)-2,-1,-1):
            higher = max(higher,height[i])
            rightHigher[i] = higher

        counting = False
        last = 0
        top = 0
        for i in range(len(height)):
            if last > height[i] and rightHigher[i] > height[i] and not counting:
                counting = True
                top = min(last,rightHigher[i])
            elif top <= height[i]:
                counting = False
            
            if counting:
                res += max(0,top - height[i])
            last = height[i]
        return res


print(Solution.trap(None,height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution.trap(None,height = [4,2,0,3,2,5]))
print(Solution.trap(None,height = [4,2,3]))
print(Solution.trap(None,height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))