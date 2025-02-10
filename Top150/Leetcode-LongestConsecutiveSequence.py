from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numDict = set(nums)
        res = 0
        length = 0
        for num in numDict:
            if num - 1 not in numDict:
                pointer = num + 1
                length = 1
                while pointer in numDict:
                    pointer += 1
                    length += 1
                
                res = max(res,length)
        
        return res

print(Solution.longestConsecutive(None,nums = [100,4,200,1,3,2]))
print(Solution.longestConsecutive(None,nums = [0,3,7,2,5,8,4,6,0,1]))
print(Solution.longestConsecutive(None,[1,3,5,2,4]))