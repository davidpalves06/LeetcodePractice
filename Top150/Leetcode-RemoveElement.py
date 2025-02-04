from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rightSwap = len(nums) - 1
        res = 0

        for i in range(len(nums) - 1,-1,-1):
            if nums[i] == val: 
                nums[i],nums[rightSwap] = nums[rightSwap],nums[i]
                rightSwap -= 1
            else:
                res += 1

        return res
            
print(Solution.removeElement(None,nums = [3,2,2,3], val = 3))
print(Solution.removeElement(None,nums = [0,1,2,2,3,0,4,2], val = 2))
