from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        res = []
        queue.append(root)

        while queue:
            rightNode = None
            for _ in range(len(queue)):
                rightNode = queue.popleft()
                if rightNode.left:
                    queue.append(rightNode.left)
                if rightNode.right:
                    queue.append(rightNode.right)
            res.append(rightNode.val)
        
        return res