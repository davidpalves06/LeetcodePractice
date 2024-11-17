from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        res = 0

        def diameterDFS(root):
            nonlocal res
            if not root:
                return 0
            
            left = diameterDFS(root.left)
            right = diameterDFS(root.right)
            
            res = max(res,left + right)

            return 1 + max(left,right)

        diameterDFS(root)
        return res