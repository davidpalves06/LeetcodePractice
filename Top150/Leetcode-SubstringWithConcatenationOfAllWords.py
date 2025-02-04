from typing import Counter, List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        memo = {}
        wordLen = len(words[0])
        substringLen = len(words) * wordLen
        i = 0
        while i < len(s) - substringLen + 1:
            word = s[i:i + substringLen]
            if memo.get(word,False) or self.isConcatenatedWithWords(word,words):
                memo[word] = True
                res.append(i)
            i += 1
        return res



    def isConcatenatedWithWords(self,s:str,words: List[str]) -> bool:
        wordLen = len(words[0])
        counter = Counter(words)
        i = 0
        while i < len(s):
            word = s[i:i+wordLen]
            if word in counter and counter[word] > 0:
                i += wordLen
                counter[word] -= 1
            else:
                return False
        return True
    
print(Solution.findSubstring(Solution(),s = "barfoothefoobarman", words = ["foo","bar"]))
print(Solution.findSubstring(Solution(),s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
print(Solution.findSubstring(Solution(),s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))
print(Solution.findSubstring(Solution(),s = "aaaaaaaaaaaaaaaaaaaaaaa", words = ["a","a","a","a","a"]))