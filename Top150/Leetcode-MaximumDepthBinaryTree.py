from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        res = 0
        if root:
            queue.append(root)
        while queue:
            queueLen = len(queue)
            for _ in range(queueLen):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res += 1
        
        return res
                