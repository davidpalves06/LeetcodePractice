from collections import deque
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeNeighbours = {i:set() for i in range(n)}

        for edge in edges:
            nodeNeighbours[edge[0]].add(edge[1])
            nodeNeighbours[edge[1]].add(edge[0])

        queue = deque()
        visited = set()
        def bfs(node):
            queue.append((node,-1))
            numberOfNodes = 0
            while queue:
                for _ in range(len(queue)):
                    queueNode,parent = queue.popleft()
                    if queueNode in visited:
                        return False
                    numberOfNodes += 1
                    visited.add(node)
                    for neighbour in nodeNeighbours[queueNode]:
                        if neighbour != parent:
                            queue.append((neighbour,queueNode))
                            visited.add(queueNode)
            if numberOfNodes == n:
                return True
            else:
                return False

        return bfs(0)




print(Solution.validTree(None,5,[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))