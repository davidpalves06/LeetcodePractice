from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixSet = set()
        maxLength = 0
        for number in arr1:
            numberString = str(number)
            for i in range(1,len(numberString) + 1):
               prefixSet.add(numberString[0:i])
        print(prefixSet)
        for number in arr2:
            numberString = str(number)
            for i in range(1,len(numberString) + 1):
               prefix = numberString[0:i]
               if (prefix in prefixSet and len(prefix) > maxLength):
                    maxLength = len(prefix)
        return maxLength