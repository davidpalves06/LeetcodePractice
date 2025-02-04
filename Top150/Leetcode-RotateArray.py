from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(array,start,end):
            l,r = start,end-1
            while l < r:
                nums[r],nums[l] = nums[l],nums[r]
                l += 1
                r -= 1

        n = len(nums)
        mod = k % n

        reverse(nums,0,n)
        reverse(nums,0,mod)
        reverse(nums,mod,n)

        print(nums)

(Solution.rotate(None,nums = [-1,-100,3,99], k = 2))
(Solution.rotate(None,nums = [1,2,3,4,5,6,7], k = 3))
(Solution.rotate(None,nums = [-1], k = 2))