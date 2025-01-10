from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        matrix.reverse()
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        

Solution.rotate(None,matrix = [[1,2,3],[4,5,6],[7,8,9]])
Solution.rotate(None,matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
Solution.rotate(None,matrix = [
  [1,2],
  [3,4]
])