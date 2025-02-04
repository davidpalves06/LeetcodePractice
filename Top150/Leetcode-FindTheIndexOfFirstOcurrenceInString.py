class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window = len(needle)

        for i in range(len(haystack) - window + 1):
            if haystack[i:i + window] == needle:
                return i
        
        return -1
    
print(Solution.strStr(None,haystack = "butsad", needle = "sad"))
print(Solution.strStr(None,haystack = "leetcode", needle = "leeto"))