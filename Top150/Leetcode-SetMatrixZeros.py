
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        
        for i in range(len(matrix)):
            for col in cols:
                matrix[i][col] = 0
        

