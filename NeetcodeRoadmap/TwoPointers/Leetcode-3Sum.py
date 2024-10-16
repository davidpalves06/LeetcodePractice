from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            left,right = i+1,len(nums)-1
            while left < right:
                target = nums[left] + nums[right] + num
                
                if target > 0:
                    right -= 1
                elif target < 0:
                    left += 1
                else:
                    res.append([num,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res


    
print(Solution.threeSum(None,[0,0,0]))

