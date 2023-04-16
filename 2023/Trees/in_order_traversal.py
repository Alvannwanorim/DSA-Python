from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left 
        self.right = right 

class Solution:
    def in_order_traversal(self, root: Optional[TreeNode]):
        res, stack = [], []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
    def in_order_traversal_recursive(self, root: Optional[TreeNode]):
        res = []
        def helper(root, res):
            if not root:
                return
            helper(root.left, res)
            res.append(root.val)
            helper(root.right, res)
        helper(root, res)
        return res
        



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sol = Solution()

print(sol.in_order_traversal(root))
print(sol.in_order_traversal_recursive(root))
