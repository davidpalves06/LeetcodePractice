from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        curMin,curMax = 1,1

        for num in nums:
            if num == 0:
                curMin,curMax = 1,1
                res = max(0,res)
            else:
                tmpMin,tmpMax = num * curMin,num * curMax
                curMax = max(tmpMax,tmpMin,num)
                curMin = min(tmpMin,tmpMax,num)
                res = max(curMax,res)

        return res
    
print(Solution.maxProduct(None,[-2,0,-1]))