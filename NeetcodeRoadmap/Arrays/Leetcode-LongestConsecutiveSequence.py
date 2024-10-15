from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in numSet:
                currentLength = 1
                currentNum = num
                while currentNum + 1 in numSet:
                    currentLength += 1
                    currentNum += 1
                res = max(res,currentLength)
        return res

print(Solution.longestConsecutive(None,[0,3,7,2,5,8,4,6,0,1]))