from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        visited = set()

        def surroundRegion(i,j):
            queue = deque()
            queue.append((i,j))
            regionCells = []
            regionOnEdge = False
            while (queue):
                size = len(queue)
                for _ in range(size):
                    (r,c) = queue.popleft()
                    if r < 0 or r > m-1 or c < 0 or c > n-1 or (r,c) in visited or board[r][c] == "X":
                        continue
                    if r == 0 or r == m-1 or c == 0 or c == n-1:
                        regionOnEdge = True

                    visited.add((r,c))
                    queue.append((r+1,c)) 
                    queue.append((r-1,c)) 
                    queue.append((r,c+1)) 
                    queue.append((r,c-1))

                    regionCells.append((r,c))

            if not regionOnEdge:
                for i in range(len(regionCells)):
                    (r,c) = regionCells[i]
                    board[r][c] = "X"

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in visited:
                    surroundRegion(i,j)

Solution.solve(None,[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])