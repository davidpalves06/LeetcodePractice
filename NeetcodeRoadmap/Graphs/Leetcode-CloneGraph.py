"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import defaultdict
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = defaultdict(Node)

        if not node:
            return None

        def cloneNode(node: Node) -> Node:
            if node.val not in nodeMap:
                newNode = Node(node.val)
                nodeMap[node.val] = newNode
                for neighbour in node.neighbors:
                    neighbourNode = cloneNode(neighbour)
                    if neighbourNode:
                        newNode.neighbors.append(neighbourNode)
                return newNode
            else:
                return nodeMap[node.val]

        return cloneNode(node)