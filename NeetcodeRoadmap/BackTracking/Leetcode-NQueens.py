from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [['.'] * n for _ in range(n)]


        def backtrack(row):
            if row == n:
                solution = [''.join(row) for row in board]
                res.append(solution)
                return
            
            for col in range(n):
                if self.isSafe(row,col,board):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = '.'
            
        backtrack(0)

        return res
    
    def isSafe(self,row,col,board):
        r = row - 1
        while r >= 0:
            if board[r][col] == 'Q':
                return False
            r -= 1
        
        r = row - 1
        c = col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        r = row - 1
        c = col + 1
        while r >= 0 and c < len(board):
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        return True

Solution.solveNQueens(Solution(),4)