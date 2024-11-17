from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node,minimum,maximum):
            if not node:
                return True
            
            if node.val <= minimum or node.val >= maximum:
                return False 

            return dfs(node.left,minimum,node.val) and dfs(node.right,node.val,maximum)
        
        return dfs(root,float("-inf"),float("inf"))