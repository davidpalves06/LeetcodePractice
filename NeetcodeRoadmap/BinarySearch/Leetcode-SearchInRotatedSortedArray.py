from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums) - 1
        while left <= right:
            pivotIndex = left + ((right - left) // 2)
            pivot = nums[pivotIndex]
            if target == pivot:
                return pivotIndex
            if nums[left] <= pivot:
                if target > pivot or target < nums[left]:
                    left = pivotIndex + 1
                else:
                    right = pivotIndex - 1
            else:
                if target < pivot or target > nums[right]:
                    right = pivotIndex - 1
                else:
                    left = pivotIndex + 1
        return -1

print(Solution.search(None,[5,1,2,3,4],1))