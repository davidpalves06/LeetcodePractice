from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        visited = set()
        curr = (0,0)
        res = []

        directions = [(0,1),(-1,0),(0,-1),(1,0)]
        dir = 0
        while len(res) != m * n:
            visited.add(curr)

            res.append(matrix[curr[0]][curr[1]])
            
            newPos = (curr[0] + directions[dir][0],curr[1] + directions[dir][1])
            if newPos[0] < 0 or newPos[0] >= m or newPos[1] < 0 or newPos[1] >= n or newPos in visited:
                dir = (dir + 3) % 4
                newPos = (curr[0] + directions[dir][0],curr[1] + directions[dir][1])

            curr = newPos

        return res

print(Solution.spiralOrder(None,matrix = [[1,2,3],[4,5,6],[7,8,9]])) 
print(Solution.spiralOrder(None,matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])) 
print(Solution.spiralOrder(None,matrix = [[1,2],[3,4]])) 
