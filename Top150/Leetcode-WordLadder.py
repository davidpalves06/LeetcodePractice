from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordLength = len(beginWord)
        visited = set()
        queue = deque()
        queue.append(beginWord)
        wordSet = set(wordList)
        visited.add(beginWord)
        res = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res
                
                for i in range(wordLength):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = word[:i] + char + word[i+1:]
                        if (nextWord not in visited and nextWord in wordSet):
                            queue.append(nextWord)
                            visited.add(nextWord)
                
    
            res += 1

        return 0
    
print(Solution.ladderLength(None,beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(Solution.ladderLength(None,beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))