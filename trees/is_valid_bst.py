from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
        def subBST(node, minVal, maxVal):
            leftValid, rightValid = True, True
            if not node:
                return True
            if not (node.val < maxVal and node.val > minVal):
                    return False
            return (subBST(node.left, minVal, node.val) and subBST(node.right, node.val, maxVal))
        
        return subBST(root, float("-inf"), float("inf"))