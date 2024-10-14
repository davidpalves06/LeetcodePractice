from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        print(nums)
        for i in range(len(nums)):
            if (i == 0):
                res[i] = 1
            else:
                res[i] = res[i-1] * nums[i-1]

        suffix = 1
        for i in range(len(nums) - 1,-1,-1):
            if (i == len(nums) - 1):
                suffix = nums[i]
            else:
                res[i] = res[i] * suffix
                suffix *= nums[i]

        return res
    

print(Solution.productExceptSelf(None,[1,2,4,6]))