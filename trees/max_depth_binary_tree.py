from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepthRecursive(root.left, 1), self.maxDepthRecursive(root.right, 1))
    
    def maxDepthRecursive(self, root: Optional[TreeNode], count: int) -> int:
        if not root:
            return count
        if root.left and root.right:
            return max(self.maxDepthRecursive(root.right, count+1), self.maxDepthRecursive(root.left, count+1))
        elif root.left:
            return self.maxDepthRecursive(root.left, count+1)
        elif root.right:    
            return self.maxDepthRecursive(root.right, count+1)
        return count +1
    
    
