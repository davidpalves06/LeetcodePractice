from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodeDict = {}
        def cloneNode(node:Node):
            if node.val in nodeDict:
                return nodeDict[node.val]
            newNode = Node(node.val)
            nodeDict[node.val] = newNode
            for neighbour in node.neighbors:
                newNeighbour = cloneNode(neighbour)
                newNode.neighbors.append(newNeighbour)
            return newNode
        
        return cloneNode(node)