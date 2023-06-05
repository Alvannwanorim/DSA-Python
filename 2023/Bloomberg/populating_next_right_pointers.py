import collections
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = collections.deque([root])

        while queue:
            curr = []
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if queue:
                    node.next = queue[0]
                if node.left: curr.append(node.left)
                if node.right: curr.append(node.right)
            queue.extend(curr)
        return root 