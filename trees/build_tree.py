from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        rootInd = inorder.index(preorder[0]) #find the index of the root in the inorder list
        root.left = self.buildTree(preorder[1:rootInd+1], inorder[:rootInd])
        root.right = self.buildTree(preorder[rootInd+1:], inorder[rootInd+1:])
        
        return root