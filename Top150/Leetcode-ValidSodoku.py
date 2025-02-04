from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = {i:[] for i in range(1,10)}
        colDict = {i:[] for i in range(1,10)}
        squareDict = {i:[] for i in range(1,10)}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    num = board[i][j]
                    squareNum = 0 
                    if i < 3:
                        if j < 3:
                            squareNum = 1
                        elif j < 6:
                            squareNum = 2
                        elif j < 9:
                            squareNum = 3
                    elif i < 6:
                        if j < 3:
                            squareNum = 4
                        elif j < 6:
                            squareNum = 5
                        elif j < 9:
                            squareNum = 6
                    else:
                        if j < 3:
                            squareNum = 7
                        elif j < 6:
                            squareNum = 8
                        elif j < 9:
                            squareNum = 9
                    if num in rowDict[i + 1] or num in colDict[j + 1] or num in squareDict[squareNum]:
                        return False
                    
                    rowDict[i + 1].append(num)
                    colDict[j + 1].append(num)
                    squareDict[squareNum].append(num)
        return True


print(Solution.isValidSudoku(None,board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(Solution.isValidSudoku(None,board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))