from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # rightProduct = [1] * len(nums)
        # leftProduct = [1] * len(nums)

        # for i in range(1,len(nums)):
        #     leftProduct[i] = leftProduct[i-1] * nums[i - 1]

        # for i in range(len(nums) - 2,-1,-1):
        #     rightProduct[i] = rightProduct[i+1] * nums[i + 1]

        # res = []
        # for i in range(len(nums)):
        #     res.append(leftProduct[i] * rightProduct[i])

        res = [1] * len(nums)

        for i in range(1,len(nums)):
            res[i] = res[i-1] * nums[i - 1] 
        
        rightProd = 1
        for i in range(len(nums) - 1,-1,-1):
            res[i] *= rightProd
            rightProd *= nums[i]
        return res

print(Solution.productExceptSelf(None,nums = [1,2,3,4]))