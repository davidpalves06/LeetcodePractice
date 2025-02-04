from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l,r = i + 1,len(nums) - 1
            firstNum = nums[i]
            while l < r:
                sum = firstNum + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                else:
                    if sum == 0:
                        res.append([firstNum,nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
    
print(Solution.threeSum(None,nums = [-1,0,1,2,-1,-4]))
print(Solution.threeSum(None,nums = [0,1,1]))
print(Solution.threeSum(None,nums = [0,0,0]))
print(Solution.threeSum(None,nums = [0,0,0,0]))