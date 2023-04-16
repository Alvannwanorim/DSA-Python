from typing import (Optional,List)
from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left 
        self.right = right 

class Solution:
    def iteration(self, root: Optional[TreeNode])->List[int]:
        stack = []
        res = []
        cur  = root


        while  stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        
        return res
    
    def recursive(self, root: Optional[TreeNode])-> List[int]:
        res = []
        def helper(root, res):
            if not root:
                return
            res.append(root.val)
            helper(root.left, res)
            helper(root.right, res)
        
        helper(root, res)
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sol = Solution()

print(sol.iteration(root))
print(sol.recursive(root))