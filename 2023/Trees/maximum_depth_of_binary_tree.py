from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left 
        self.right = right 


class Solution:
    def max_depth_of_Binary_tree(self, root: Optional[TreeNode])->int:
        max_depth = 0 
        stack = [[root, 0]]

        while stack:
            cur, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if cur.left: stack.append([cur.left, depth + 1])
            if cur.right: stack.append([cur.right, depth + 1])
        
        return max_depth 
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left= TreeNode(6)
sol = Solution()
print(sol.max_depth_of_Binary_tree(root))