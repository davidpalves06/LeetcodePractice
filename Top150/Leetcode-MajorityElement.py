from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = nums[0]
        count = 0

        for num in nums:
            if current == num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    current = num
                    count = 1
        
        return current
    
print(Solution.majorityElement(None,nums = [3,2,3]))
print(Solution.majorityElement(None,nums = [2,2,1,1,1,2,2]))
print(Solution.majorityElement(None,[1,3,1,1,4,1,1,5,1,1,6,2,2]))