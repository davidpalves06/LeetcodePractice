from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        def inOrder(root):
            if not root:
                return
            
            inOrder(root.left)
            values.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return values[k-1]