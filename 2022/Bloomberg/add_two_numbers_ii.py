from typing import Optional

class NodeList:
    def __init__(self, val) -> None:
        self.val = val 
        self.next = None
class Solution:
    def reverseList(self, node:NodeList):
        prev = None
        curr = node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    def addTwoNumbers(self, l1: Optional[NodeList], l2: Optional[NodeList]) -> Optional[NodeList]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        carry = 0
        head = None
        while l1 or l2 or carry !=0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry

            carry  = val // 10
            node = NodeList(val % 10)

            node.next = head
            head = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            node = NodeList(carry)
            node.next = head
            head = node
        
        return head
