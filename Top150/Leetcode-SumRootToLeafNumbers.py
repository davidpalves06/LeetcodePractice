from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        rootLeafNumbers = []

        def dfs(root : TreeNode,current: int):
            if not root:
                return
            if not root.right and not root.left:
                finalNumber = (current * 10) + root.val
                rootLeafNumbers.append(int(finalNumber))
                return
            else:
                current = (current * 10) + root.val
                dfs(root.left,current)
                dfs(root.right,current)

        dfs(root,0)
        return sum(rootLeafNumbers)
