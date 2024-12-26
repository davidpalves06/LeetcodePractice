from collections import defaultdict
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c : [] for w in words for c in w}
        for i in range(len(words) - 1):
            smaller = words[i]
            larger = words[i + 1]
            minLen = min(len(smaller),len(larger))
            if len(smaller) > len(larger) and smaller[:minLen] == larger[:minLen]:
                return ""
            for j in range(len(smaller)):
                if smaller[j] != larger[j]:
                    adjList[smaller[j]].append(larger[j])
                    break
        
        
        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for biggerChar in adjList[char]:
                if dfs(biggerChar):
                    return True
                
            visited[char] = False

            res.append(char)

            return False
        
        for key in adjList:
            if dfs(key):
                return ""
        res.reverse()
        return "".join(res)

print(Solution.foreignDictionary(None,["z","o"]))
print(Solution.foreignDictionary(None,["hrn","hrf","er","enn","rfnn"]))
print(Solution.foreignDictionary(None,words=["wrtkj","wrt"]))
print(Solution.foreignDictionary(None,words=["z","z"]))