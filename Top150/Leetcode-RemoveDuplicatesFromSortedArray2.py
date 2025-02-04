from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        lastValue = nums[0]
        twice = set()
        for num in nums[1:]:
            if num in twice:
                continue
            if lastValue != num:
                lastValue = num
                nums[i] = num
                i += 1
            elif lastValue == num and num not in twice:
                twice.add(num)
                nums[i] = num
                i += 1
        
        return i

print(Solution.removeDuplicates(None,nums = [1,1,1,2,2,3]))
print(Solution.removeDuplicates(None,nums = [0,0,1,1,1,1,2,3,3]))
print(Solution.removeDuplicates(None,nums = [1]))