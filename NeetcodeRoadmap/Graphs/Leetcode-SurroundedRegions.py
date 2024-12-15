from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def bfs(i,j):
            queue = deque()
            visited = set()
            queue.append((i,j))
            visited.add((i,j))

            def addCell(i,j):
                if 0 > i or i >= len(board) or 0 > j or j >= len(board[0]):
                    return True
                if board[i][j] == 'O' and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                return False
            
            while queue:
                for _ in range(len(queue)):
                    x,y = queue.popleft()
                    res = addCell(x+1,y) or addCell(x-1,y) or addCell(x,y+1) or addCell(x,y-1)
                    if res:
                        return True
            for (x,y) in visited:
                board[x][y] = 'X'
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    bfs(i,j)

board = [["O","O","O","O","O","O"],
         ["O","X","X","X","X","O"],
         ["O","X","O","O","X","O"],
         ["O","X","O","O","X","O"],
         ["O","X","X","X","X","O"],
         ["O","O","O","O","O","O"]]
Solution.solve(None,board)
print(board)