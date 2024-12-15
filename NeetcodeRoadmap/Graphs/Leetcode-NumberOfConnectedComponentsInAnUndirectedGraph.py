from collections import deque
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeNeighbours = {i:set() for i in range(n)}

        for edge in edges:
            nodeNeighbours[edge[0]].add(edge[1])
            nodeNeighbours[edge[1]].add(edge[0])
        res = 0
        visited = set()
        
        def bfs(node):
            queue = deque()
            queue.append(node)

            while queue:
                for _ in range(len(queue)):
                    queueNode = queue.popleft()
                    if queueNode not in visited:
                        visited.add(queueNode)
                        for neighbour in nodeNeighbours[queueNode]:
                            queue.append(neighbour)

        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1

        return res
    
print(Solution.countComponents(None,6,[[0,1], [1,2], [2,3], [4,5]]))