from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        changed = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for dir in directions:
                        x,y = i,j
                        while True:
                            x,y = x+dir[0],y + dir[1]
                            if x < 0 or x >= m or y < 0 or y >= n:
                                break
                            changed.add((x,y))
        for x,y in changed:
            matrix[x][y] = 0
        
print(Solution.setZeroes(None,[[1,1,1],[1,0,1],[1,1,1]]))
print(Solution.setZeroes(None,matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
print(Solution.setZeroes(None,matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]))