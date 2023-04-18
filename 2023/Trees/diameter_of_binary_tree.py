from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left 
        self.right = right 

class Solution:
    def diameter_of_binary_tree(self, root: Optional[TreeNode])->int:
        res = 0 

        def dfs(root):
            nonlocal res 
            if not root: 
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sol = Solution()
print(sol.diameter_of_binary_tree(root))