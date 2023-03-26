from collections import defaultdict, deque
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

        left_col = right_col = 0
        res = []

        queue = deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()

            if not node:
                continue
            left_col = min(left_col, col)
            right_col = max(right_col, col)

            table[col].append((node.val, row))
            queue.append((node.left, row +1, col -1))
            queue.append((node.right, row +1, col + 1))
        
        for col in range(left_col, right_col + 1):
            items = table[col]
            items.sort(key=lambda x: (x[1], x[0]))
            items = [val for val, _ in items]

            res.append(items)
        return res