from collections import defaultdict, deque
from lib2to3.pytree import Node
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        table = defaultdict(List)
        min_col  = max_col = 0
        queue = deque([root,0])

        while queue:
            node, col = queue.popleft()

            if node is not Node:
                table[col].append(node.val)
                min_col == min(min_col, col)
                max_col = max(max_col, col)

                queue.append(node.left, col - 1)
                queue.append(node.right, col + 1)
        return [table[x] for x in range(min_col, max_col + 1)]