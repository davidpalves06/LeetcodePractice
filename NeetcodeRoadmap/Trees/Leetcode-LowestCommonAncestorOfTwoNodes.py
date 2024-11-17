class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if min(p.val,q.val) > curr.val:
                curr = curr.right
                continue
            if max(p.val,q.val) < curr.val:
                curr = curr.left
                continue
            return curr