from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        rootValue = preorder[0]
        indexInOrder = inorder.index(rootValue)
        root = TreeNode(rootValue)
        root.left = self.buildTree(preorder[1:indexInOrder+1],inorder[0:indexInOrder])
        root.right = self.buildTree(preorder[indexInOrder+1:],inorder[indexInOrder+1:])

        return root
