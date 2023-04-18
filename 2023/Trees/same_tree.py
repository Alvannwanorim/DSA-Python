from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left 
        self.right = right 

class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode])->int:
        if not p and not q:
            return True
        if q and q and p.val == q.val:
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
        
        return False

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)
p.left.right = TreeNode(7)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
q.left.left = TreeNode(4)
q.left.right = TreeNode(7)
sol = Solution()
print(sol.is_same_tree(p, q))