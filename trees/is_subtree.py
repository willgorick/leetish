from typing import Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.subtreeCheck(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def subtreeCheck(self, root, subRoot):
            if not root and not subRoot: #if the values have been the same up to this point but now they're both None, return true, we got to the bottom
                return True
            if root and subRoot and root.val == subRoot.val:
                return self.subtreeCheck(root.left, subRoot.left) and self.subtreeCheck(root.right, subRoot.right)
            return False #if the values weren't the same return False