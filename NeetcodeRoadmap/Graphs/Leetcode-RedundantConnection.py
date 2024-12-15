from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodeEdges = {i:[] for i in range(1,len(edges)+1)}

        for i in range(len(edges)):
            edge = edges[i]
            nodeEdges[edge[0]].append(edge[1])
            nodeEdges[edge[1]].append(edge[0])
        
        res = []
        visited = set()
        cycle = set()
        cycleNode = -1
        def dfs(origin,dest):
            nonlocal cycleNode
            if dest in visited:
                cycleNode = dest
                return True
            visited.add(dest)

            for edge in nodeEdges[dest]:
                if edge != origin:
                    if dfs(dest,edge):
                        if cycleNode != -1:
                            cycle.add(dest)
                        if cycleNode == dest:
                            cycleNode = -1
                        return True
            return False
                
        dfs(0,1)

        for edge in edges[::-1]:
            if edge[0] in cycle and edge[1] in cycle:
                return edge
        return []
    
print(Solution.findRedundantConnection(None,[[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]))