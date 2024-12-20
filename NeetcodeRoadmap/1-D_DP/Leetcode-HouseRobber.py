from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        moneyUntilNow = [0] * len(nums)
        moneyUntilNow[0] = nums[0]
        moneyUntilNow[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            moneyUntilNow[i] = max(moneyUntilNow[i-1],nums[i] + moneyUntilNow[i-2])
        return moneyUntilNow[-1]
        
print(Solution.rob(None,[7,2,3,9,1]))