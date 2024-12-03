from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        left,right = 0,0
        maxDistance = 0
        res = 0
        while right < len(nums) - 1:
            for i in range(left,right + 1):
                maxDistance = max(maxDistance,i + nums[i])
            left = right + 1
            right = maxDistance
            res += 1
        
        return res