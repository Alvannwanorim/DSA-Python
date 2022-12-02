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
        table = defaultdict(list)
        left_col  = right_col = 0
        queue = deque([(root,0)])

        while queue:
            node, col = queue.popleft()

            if node is not None:
                table[col].append(node.val)
                left_col = min(left_col, col)
                right_col = max(right_col, col)

                
                
                
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
                
        print(table)
        print(right_col)
        print(left_col)
        return [table[x] for x in range(left_col, right_col + 1)]