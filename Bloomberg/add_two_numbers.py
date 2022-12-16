from typing import Optional

class NodeList:
    def __init__(self, val) -> None:
        self.val = val 
        self.next = None
class Solution:
    def addTwoNumbers(self, l1: Optional[NodeList], l2: Optional[NodeList]) -> Optional[NodeList]:
        dummy = NodeList(0)
        curr = dummy

        carry = 0
        while l1 or l2 or carry !=0:
            val1 = l1.val
            val2 = l2.val
            val = val1 + val2

            carry  = val / 10
            node = NodeList(val % 10)
            curr.next = node
            curr = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next