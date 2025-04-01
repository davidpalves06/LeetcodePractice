from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        nSquare = n*n
        board.reverse()
        def intToPos(pos):
            r = (pos - 1) // n
            c = (pos - 1) % n

            if r % 2:
                c = n - 1 - c
            
            return [r,c]
        
        queue = deque()
        visited = set()
        queue.append([1,0])
        while queue:
            pos,moves = queue.popleft()
            
            for i in range(1,7):
                nextPos = pos + i
                r,c = intToPos(nextPos)
                if board[r][c] != -1:
                    nextPos = board[r][c]
                if nextPos == nSquare:
                    return moves + 1
                if nextPos not in visited:
                    visited.add(nextPos)
                    queue.append([nextPos,moves + 1])
        
        return -1
                

print(Solution.snakesAndLadders(None,board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(Solution.snakesAndLadders(None,board = [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]))
