from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = Counter(s)
        tCounter = Counter(t)

        return tCounter.__eq__(sCounter)
    
print(Solution.isAnagram(None,s = "anagram", t = "nagaram"))
print(Solution.isAnagram(None,s = "rat", t = "car"))