from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)

        def isSorted(values):
            curr = values[0]
            for i in range(1,len(values)):
                if curr >= values[i]:
                    return False
                curr = values[i]
            
            return True

        return isSorted(values)