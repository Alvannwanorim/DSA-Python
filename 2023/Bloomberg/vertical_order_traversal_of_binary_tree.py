
# Definition for a binary tree node.
import collections
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([(root,0)])
        left_col, right_col = 0, 0
        table = collections.defaultdict(list)

        while queue:
            node, col = queue.popleft()
            if node and node.left: queue.append((node.left, col - 1))
            if node and node.right: queue.append((node.right, col + 1))
            if node: table[col].append(node.val)

            left_col = min(left_col, col)
            right_col = max(right_col, col)
        
        return [table[x] for x in range(left_col, right_col + 1)]
