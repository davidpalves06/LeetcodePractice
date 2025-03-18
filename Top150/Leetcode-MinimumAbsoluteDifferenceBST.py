import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        def helper(root,res):
            if not root:
                return None
            
            helper(root.left,res)
            res.append(root.val)
            helper(root.right,res)


        helper(root,res)
        min_dif=math.inf
        for i in range(1,len(res)):
            min_dif = min(min_dif,res[i]-res[i-1])

        return min_dif