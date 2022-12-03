class Node:
    def __init__(self, val) -> None:
        self.val = val 
        self.prev = None
        self.next = None


class Solution:
    def reverseNode(self, head: Node) -> Node:
        curr, prev = head, None

        while curr:
            tmp = curr.next
            curr.next = prev 
            prev = curr
            curr = tmp
        return prev