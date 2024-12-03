from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMaxSum = 0
        res = nums[0]
        for num in nums:
            currMaxSum += num
            res = max(res,currMaxSum)
            if currMaxSum < 0:
                currMaxSum = 0

        return res