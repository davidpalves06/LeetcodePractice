from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [1001] * len(nums)

        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= len(nums) - 1:
                dp[i] = 1
            elif nums[i] > 0:
                dp[i] = min(dp[i+1:i+nums[i] + 1]) + 1
        # for i in range(len(nums)):
        #     for j in range(1,nums[i] + 1):
        #         if i + j >= len(nums):
        #             break
        #         if dp[i + j] == 0:
        #             dp[i + j] = dp[i] + 1
        #         else:
        #             dp[i+j] = min(dp[i+j],dp[i] + 1)


        return dp[0] if dp[0] != 1001 else 0

print(Solution.jump(None,nums = [2,3,1,1,4]))
print(Solution.jump(None,nums = [2,3,0,1,4]))
print(Solution.jump(None,nums = [0]))