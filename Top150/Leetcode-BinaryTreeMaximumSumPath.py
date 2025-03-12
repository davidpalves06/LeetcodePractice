from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -10001
        def dfs(node):
            nonlocal res
            if not node:
                return float("-infinity")
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            res = max(res,leftSum + node.val,node.val,leftSum + node.val + rightSum,rightSum + node.val)
            return max(node.val,leftSum + node.val,rightSum + node.val)
        
        dfs(root)
        return res