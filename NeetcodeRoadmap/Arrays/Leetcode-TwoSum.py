from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        supplemantMap = dict()
        for i,num in enumerate(nums):
            supplement = target - num
            if num in supplemantMap:
                return [supplemantMap.get(num),i]
            if not supplement in supplemantMap:
                supplemantMap.setdefault(supplement,i)
        

        