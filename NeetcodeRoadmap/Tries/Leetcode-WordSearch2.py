from typing import List

class Node:
    def __init__(self) -> None:
        self.child = [None] * 26
        self.isWord = False

    def insert(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            nextPos = ord(word[i]) - ord('a')
            if not curr.child[nextPos]:
                node = Node()
                curr.child[nextPos] = node
                curr = node
            else:
                curr = curr.child[nextPos]
                
        curr.isWord = True
        


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Node()

        for word in words:
            trie.insert(word)

        rows,cols = len(board),len(board[0])
        res = set()
        visit = set()

        def dfs(r,c,node,word):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or not node.child[ord(board[r][c]) - ord('a')]:
                return

            visit.add((r,c))
            node = node.child[ord(board[r][c]) - ord('a')]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)

            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,trie,"")

        return [result for result in res]

        

