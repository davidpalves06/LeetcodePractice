from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums) - 1
        res = 5001
        while left <= right:
            if nums[left] < nums[right]:
                res = min(nums[left],res)
            index = (left + right) //2
            pivot = nums[index]
            res = min(res,pivot)
            if nums[left] <= pivot:
                left = index + 1
            else:
                right = index - 1
        return res

print(Solution.findMin(None,[4,5,6,7,0,1,2]))