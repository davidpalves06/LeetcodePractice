from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordMap = defaultdict(str)

        wordSplit = s.split(" ")
        if len(wordSplit) != len(pattern):
            return False
        
        for i,letter in enumerate(pattern):
            if letter in wordMap and wordMap[letter] != wordSplit[i]:
                return False
            wordMap[letter] = wordSplit[i]

        wordMap = defaultdict(str)
        
        for i,word in enumerate(wordSplit):
            if word in wordMap and wordMap[word] != pattern[i]:
                return False
            wordMap[word] = pattern[i]

        return True
    
print(Solution.wordPattern(None,pattern = "abba", s = "dog cat cat dog"))
print(Solution.wordPattern(None,pattern = "abba", s = "dog cat cat fish"))
print(Solution.wordPattern(None,pattern = "aaaa", s = "dog cat cat dog"))
print(Solution.wordPattern(None,pattern = "abba", s = "dog dog dog dog"))