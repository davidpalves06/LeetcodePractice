from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        i = len(nums) - 2
        while goal != 0:
            if i == -1:
                return False
            if i + nums[i] >= goal:
                goal = i
            i -= 1
        return True
    
print(Solution.canJump(None,nums = [2,3,1,1,4]))
print(Solution.canJump(None,nums = [3,2,1,0,4]))
