from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        self.position = 0
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.values.append(node.val)
            dfs(node.right)

            return
        dfs(root)

    def next(self) -> int:
        value = self.values[self.position]
        self.position += 1
        return value

    def hasNext(self) -> bool:
        return self.position < len(self.values)
            