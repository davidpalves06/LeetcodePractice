class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        
        leftAncestor = self.lowestCommonAncestor(root.left,p,q)
        rightAncestor = self.lowestCommonAncestor(root.right,p,q)

        if leftAncestor and rightAncestor:
            return root
        
        return leftAncestor if leftAncestor else rightAncestor
