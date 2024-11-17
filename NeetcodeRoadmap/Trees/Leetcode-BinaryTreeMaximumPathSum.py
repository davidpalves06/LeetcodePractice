from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            leftSum,rightSum = dfs(node.left),dfs(node.right)

            res = max(res,node.val,node.val + leftSum + rightSum)

            return node.val + leftSum + rightSum
        
        dfs(root)
        return res

                
            