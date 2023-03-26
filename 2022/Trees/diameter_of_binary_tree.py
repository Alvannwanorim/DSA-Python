class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class SOlution:
    def diameter(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res,left + right)

            return 1 + max(right, left)
        
        dfs(root)

        return res

