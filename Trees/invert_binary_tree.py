from typing import Optional


class TreeNode:
    def __init__(self, val: int, left: None, right: None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right - tmp
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    
        
            