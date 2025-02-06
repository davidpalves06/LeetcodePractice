from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        wordDict = {}

        for s in strs:
            sortedWord = ''.join(sorted(s))
            if sortedWord in wordDict:
                wordDict[sortedWord].append(s)
            else:
                wordDict[sortedWord] = [s]

        for group in wordDict.values():
            res.append(group)

        return res
            