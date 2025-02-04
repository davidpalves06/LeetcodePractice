from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        minRow,maxRow = 0,m-1
        minCol,maxCol = 0,n-1
        curr = (0,0)
        res = []
        directions = [(0,1),(-1,0),(0,-1),(1,0)]
        dir = 0

        while curr[0] >= minRow and curr[0] <= maxRow and curr[1] >= minCol and curr[1] <= maxCol:
            res.append(matrix[curr[0]][curr[1]])
            direction = directions[dir]
            nextPos = (curr[0] + direction[0],curr[1] + direction[1])
            if nextPos[0] < minRow or nextPos[0] > maxRow or nextPos[1] < minCol or nextPos[1] > maxCol:
                if dir == 0:
                    minRow += 1
                elif dir == 1:
                    minCol += 1
                elif dir == 2:
                    maxRow -= 1
                elif dir == 3:
                    maxCol -= 1
                dir = (dir + 3) % 4
                nextPos = (curr[0] + directions[dir][0],curr[1] + directions[dir][1])
            curr = nextPos
        
        return res
    
print(Solution.spiralOrder(None,matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(Solution.spiralOrder(None,matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))