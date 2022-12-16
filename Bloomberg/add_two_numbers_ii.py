from typing import Optional

class NodeList:
    def __init__(self, val) -> None:
        self.val = val 
        self.next = None
class Solution:
    def reverseList(node:NodeList):
        prev = None
        curr = node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    def addTwoNumbers(self, l1: Optional[NodeList], l2: Optional[NodeList]) -> Optional[NodeList]:
        dummy = NodeList(0)
        curr = dummy