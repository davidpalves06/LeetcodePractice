from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        wordNodeMapping = {word:i for i,word in enumerate(wordList)}
        wordNodeMapping[beginWord] = -1
        
        wordAdjList = defaultdict(list)
        for i in range(len(wordList)):
            self.addSimilarWord(beginWord,wordList[i],wordNodeMapping,wordAdjList)
        for i in range(len(wordList)):
            for j in range(i + 1,len(wordList)):
                self.addSimilarWord(wordList[i],wordList[j], wordNodeMapping, wordAdjList)
        
        queue = deque()
        visited = set()
        res = 1
        queue.append(-1)
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node != -1 and wordList[node] == endWord:
                    return res

                if node in visited:
                    continue
                visited.add(node)

                for adj in wordAdjList[node]:
                    if adj not in visited:
                        queue.append(adj)
            res += 1
        return 0

    def addSimilarWord(self, firstWord,secondWord, wordNodeMapping, wordAdjList):
        differentChars = 0

        for c in range(len(firstWord)):
            if firstWord[c] != secondWord[c]:
                differentChars += 1
                
        if differentChars == 1:
            wordAdjList[wordNodeMapping[firstWord]].append(wordNodeMapping[secondWord])
            wordAdjList[wordNodeMapping[secondWord]].append(wordNodeMapping[firstWord])

print(Solution.ladderLength(Solution(),"hit","cog",["hot","dot","dog","lot","log","cog"]))