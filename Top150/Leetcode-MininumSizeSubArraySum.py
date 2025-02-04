from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = len(nums) + 1
        sum = 0
        length = 1
        left = 0
        right = 0
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                minLength = min(minLength,length)
                sum -= nums[left]
                left += 1
                length -= 1
            else:
                right += 1
                length += 1
        
        if minLength > len(nums):
            return 0
        return minLength
    
print(Solution.minSubArrayLen(None,target = 7, nums = [2,3,1,2,4,3]))
print(Solution.minSubArrayLen(None,target = 4, nums = [1,4,4]))
print(Solution.minSubArrayLen(None,target = 11, nums = [1,1,1,1,1,1,1,1]))
print(Solution.minSubArrayLen(None,target = 213, nums = [12,28,83,4,25,26,25,2,25,25,25,12]))