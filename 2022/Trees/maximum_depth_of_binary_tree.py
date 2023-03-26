from typing import Optional


class TreeNode:
    def __init__(self, val: int, left: None, right: None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameter(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        stack = [root, 1]

        while stack:
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)

            if node.left: stack.append([node.left, depth + 1])
            if node.right: stack.append([node.right, depth + 1])

            return maxDepth
