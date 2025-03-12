from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        def dfs(node):
            if not node:
                return
            nonlocal res
            res += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res
    
"""
if not root:
            return 0
        left = root
        right = root
        heightL = 0
        heightR = 0
        while left:
            heightL += 1
            left = left.left

        while right:
            heightR += 1
            right = right.right

        if heightL == heightR: 
            return pow(2, heightL) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)""
"""