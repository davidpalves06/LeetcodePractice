class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def dfs(maximum,node):
            if not node:
                return 0
            if node.val >= maximum:
                return 1 + dfs(node.val,node.right) + dfs(node.val,node.left)
            else:
                return dfs(maximum,node.right) + dfs(maximum,node.left)
            
        return dfs(root.val,root)

            