from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftQueue = deque()
        rightQueue = deque()
        root.right = self.invertTree(root.right)
        leftQueue.append(root.left)
        rightQueue.append(root.right)


        while leftQueue and rightQueue:
            leftLen = len(leftQueue)
            rightLen = len(rightQueue)
            if leftLen != rightLen:
                return False
            for _ in range(leftLen):
                leftNode = leftQueue.popleft()
                rightNode = rightQueue.popleft()

                if (leftNode and rightNode and leftNode.val != rightNode.val) or (leftNode and not rightNode) or (not leftNode and rightNode):
                    return False
                
                if leftNode:
                    leftQueue.append(leftNode.left)
                    leftQueue.append(leftNode.right)
                
                if rightNode:
                    rightQueue.append(rightNode.left)
                    rightQueue.append(rightNode.right)
                
        return True if not leftQueue and not rightQueue else False

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        else:
            tmp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(tmp)
            return root