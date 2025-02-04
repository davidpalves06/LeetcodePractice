from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = strs[0]
        for str in strs:
            i = 0
            while i < len(commonPrefix) and i < len(str):
                if str[i] != commonPrefix[i]:
                    break
                i += 1
            commonPrefix = commonPrefix[:i]
            if commonPrefix == "":
                return ""
            
        return commonPrefix
    
print(Solution.longestCommonPrefix(None,strs = ["flower","flow","flight"]))
print(Solution.longestCommonPrefix(None,strs = ["dog","racecar","car"]))