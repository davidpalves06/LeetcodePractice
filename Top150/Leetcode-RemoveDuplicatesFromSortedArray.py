from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        nodups = []
        for num in nums:
            if num not in seen:
                seen.add(num)
                nodups.append(num)
        
        i = 0
        for num in nodups:
            nums[i] = num
            i += 1

        return len(nodups)
    
print(Solution.removeDuplicates(None,nums = [1,1,2]))
print(Solution.removeDuplicates(None,nums = [0,0,1,1,1,2,2,3,3,4]))
print(Solution.removeDuplicates(None,nums = [-1,0,0,0,0,3,3]))