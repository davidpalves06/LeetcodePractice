from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        first = 0
        if nums == []:
            return []
        res = []
        for i,num in enumerate(nums):
            if i == 0:
                first = num
            elif nums[i-1] != num - 1:
                if first != nums[i-1]:
                    res.append(str(first) + "->" + str(nums[i-1]))
                else:
                    res.append(str(first))
                first = num
        
        if first != nums[-1]:
            res.append(str(first) + "->" + str(nums[-1]))
        else:
            res.append(str(first))
        return res
    
print(Solution.summaryRanges(None,nums = [0,1,2,4,5,7]))
print(Solution.summaryRanges(None,nums = [0,2,3,4,6,8,9]))
print(Solution.summaryRanges(None,nums = [1]))
