from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def calculateRobValue(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])

            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],nums[i] + dp[i-2])
            
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        res = max(calculateRobValue(nums[1:]),calculateRobValue(nums[:-1]))
        return res

print(Solution.rob(None,[1,2,3,1]))