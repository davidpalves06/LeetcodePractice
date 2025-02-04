from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap = defaultdict(str)
        mapped = defaultdict(str)
        for i in range(len(s)):
            if (t[i] in charMap and charMap[t[i]] != s[i]) or (s[i] in mapped and mapped[s[i]] != t[i]):
                    return False
            charMap[t[i]] = s[i]
            mapped[s[i]] = t[i]
        return True
    
print(Solution.isIsomorphic(None,s = "egg", t = "add"))
print(Solution.isIsomorphic(None,s = "foo", t = "bar"))
print(Solution.isIsomorphic(None,s = "badc", t = "baba"))