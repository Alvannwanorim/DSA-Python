class Node:
    def __init__(self, val, next=None, prev=None, child=None) -> None:
        self.val = val 
        self.next = next
        self.prev = prev 
        self.child = child
class Solution:
    def flatten(self, head: Node) -> Node:
        if not head: return head 
        
        dummy = Node(0)
        dummy.next = head
        curr, stack = dummy, [head]

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

