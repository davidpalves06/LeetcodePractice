from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sumOfAllElements = sum(nums)
        remain = sumOfAllElements % p

        if remain == 0:
            return 0
        
        res = len(nums)
        cur_sum = 0

        remain_to_index = {
            0:-1
        }

        for i,n in enumerate(nums):
            cur_sum = (cur_sum + n) % p
            prefix = (cur_sum - remain + p) % p
            if prefix in remain_to_index:
                length = i - remain_to_index[prefix]
                res = min(res,length)
            remain_to_index[cur_sum] = i

        return -1 if res == len(nums) else res

print(Solution.minSubarray(None,[6,3,6,2],9))
