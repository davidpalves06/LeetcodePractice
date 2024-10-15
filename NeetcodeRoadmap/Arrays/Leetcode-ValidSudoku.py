from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numChecker = {}
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                square = 0
                if i < 3 and j < 3:
                    square = 1
                elif i < 3 and j < 6:
                    square = 2
                elif i < 3:
                    square = 3
                elif i < 6 and j < 3:
                    square = 4
                elif i < 6 and j < 6:
                    square = 5
                elif i < 6:
                    square = 6
                elif j < 3:
                    square = 7
                elif j < 6:
                    square = 8
                else:
                    square = 9
                
                if not numChecker.get(num):
                    numChecker[num] = {"row":[i],"column":[j],"square":[square]}
                else:
                    checker = numChecker[num]
                    if i in checker["row"] or j in checker["column"] or square in checker["square"]:
                        return False
                    else:
                        checker["row"].append(i)
                        checker["column"].append(j)
                        checker["square"].append(square)
        return True
    
print(Solution.isValidSudoku(None,[["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))