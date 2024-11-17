from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        isBalanced = True


        def dfs(root):
            nonlocal isBalanced
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if (left - 1 > right or right - 1 > left):
                isBalanced = False

            return max(left,right) + 1
        
        dfs(root)
        return isBalanced
        

        