from turtle import left


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def ValidTree(self,root: TreeNode):
        def dfs(node, left, right):
            if not node:
                return True
            if not (node.val < right  and node.val >left):
                return False
            return (dfs(node.left, left, node.val) and dfs(node.right, node.val, right))
        return dfs(root,float("-inf"), float("inf"))