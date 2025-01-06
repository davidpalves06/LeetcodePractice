from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)
        for i in range(n+1):
            xor = xor ^ i

        for num in nums:
            xor = xor ^ num

        return xor
    
print(Solution.missingNumber(None,nums = [2,0,1]))
print(Solution.missingNumber(None,nums = [0,1]))
print(Solution.missingNumber(None,nums = [9,6,4,2,3,5,7,0,1]))