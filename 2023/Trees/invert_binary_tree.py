from typing import (Optional,List)
from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left 
        self.right = right 

class Solution:
    def invertTree(self, root: Optional[TreeNode])->List[int]:
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sol = Solution()

# print(sol.iteration(root))
print(sol.invertTree(root).left.val)