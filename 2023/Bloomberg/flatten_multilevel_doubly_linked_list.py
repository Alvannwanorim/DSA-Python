from typing import Optional


class Node:
    def __init__(self, val, next, prev, child) -> None:
        self.val = val 
        self.next = next
        self.prev = prev 
        self.child = child 

class Solution:
    def flattenList(self, head: Optional[Node]):
        if head is None: return None
        dummy = Node(0)
        stack = [head]
        dummy.next = head
        curr = dummy

        while stack: 
            tmp = stack.pop()
            if tmp.next: stack.append(tmp.next)
            if tmp.child: stack.append(tmp.child)

            curr.next = tmp 
            tmp.prev = curr
            tmp.child = None
            curr = tmp 
        dummy.next.prev = None

        return dummy.next
        