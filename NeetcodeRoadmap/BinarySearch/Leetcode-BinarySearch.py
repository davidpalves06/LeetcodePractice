from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums) -1
        
        while left <= right:
            pivotIndex = left + ((right-left)//2)
            pivot = nums[pivotIndex]
            print(pivot)
            if pivot == target:
                return pivotIndex
            elif pivot > target:
                right = pivotIndex-1
            else:
                left = pivotIndex+1
        return -1
        
print(Solution.search(None,[5],5))