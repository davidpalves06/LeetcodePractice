from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()

        res = []
        queue.append(root)

        while queue:
            queueLength = len(queue)
            level = []

            for _ in range(queueLength):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                   queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)
        
        return res
