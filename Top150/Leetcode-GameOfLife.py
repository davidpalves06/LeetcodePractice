from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                liveNeighbour = 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        if x == 0 and y == 0:
                            continue
                        newX = i + x
                        newY = j + y
                        if newX >= 0 and newX < n and newY >= 0 and newY < m and board[newX][newY] > 0:
                            liveNeighbour += 1

                if (liveNeighbour < 2 or liveNeighbour > 3) and board[i][j] == 1:
                    board[i][j] = 2
                
                if liveNeighbour == 3 and board[i][j] == 0:
                    board[i][j] = -1

        for i in range(n):
            for j in range(m):
                if board[i][j] == -1:
                    board[i][j] = 1
                if board[i][j] == 2:
                    board[i][j] = 0
                

print(Solution.gameOfLife(None,board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
print(Solution.gameOfLife(None,board = [[1,1],[1,0]]))