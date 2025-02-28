from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        tmp = self.flatten(root.right)
        root.right = self.flatten(root.left)
        root.left = None
        curr = root
        while curr.right:
            curr = curr.right
        curr.right = tmp

        return root

        