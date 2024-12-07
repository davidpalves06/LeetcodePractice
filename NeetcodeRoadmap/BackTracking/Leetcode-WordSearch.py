from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def backtrack(i,j,size):
            if size == len(word):
                return True
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i,j) not in visited and board[i][j] == word[size]:
                visited.add((i,j))
                res =  (backtrack(i+1,j,size + 1) or
                backtrack(i,j+1,size + 1) or
                backtrack(i-1,j,size + 1) or
                backtrack(i,j-1,size + 1))
                visited.remove((i,j))
                return res
            else:
                return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False
