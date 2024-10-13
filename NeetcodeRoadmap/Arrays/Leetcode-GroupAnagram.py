from typing import List


class Solution:
    # Sort words to find anagrams - O(n * mlogm)
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = []
    #     wordDict = dict()
    #     for s in strs:
    #         sortedWord = ''.join(sorted(s))
    #         if sortedWord in wordDict:
    #             wordDict[sortedWord].append(s)
    #         wordDict.setdefault(sortedWord,[s])
    #     for group in wordDict.values():
    #         res.append(group)
    #     return res
    
    # Using count as key - O(n * m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        wordDict = dict()
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            if key in wordDict:
                wordDict[key].append(s)
            else:
                group = [s]
                wordDict[key] = [s]

        for group in wordDict.values():
            res.append(group)
        return res

print(Solution.groupAnagrams(Solution(),["eat","tea","tan","ate","nat","bat"]))