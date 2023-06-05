from typing import  List, Optional
from collections import  defaultdict, deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        if not root: return []
        res = []
        queue = deque([(root,0, 0)])
        table = defaultdict(list)
        min_col, max_col =0, 0

        while queue:
            node, col, row= queue.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            table[col].append(node.val)
            
            if node.left: queue.append([(node.left,col - 1, row + 1 )])
            if node.right: queue.append([(node.right,col + 1, row + 1 )])
        
        for col in range(min_col, max_col + 1):
            item = table[col]
            item= item.sort(key=lambda x: (x[1], x[0]))
            item = [val for val,_ in item]
            res.append(item)
        
        return res


