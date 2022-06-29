from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if not root or root.val == None:
            return []
        queue.append(root)
        res = []
        while queue:
            subres = []
            for _ in range(len(queue)):                
                node = queue.popleft()
                subres.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(subres)
        return res