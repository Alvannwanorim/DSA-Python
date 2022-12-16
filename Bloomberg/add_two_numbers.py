from typing import Optional

class NodeList:
    def __init__(self, val) -> None:
        self.val = val 
        self.next = None
        self.prev = None
class Solution:
    def addTwoNumbers(self, l1: Optional[NodeList], l2: Optional[NodeList]) -> Optional[NodeList]:
        dummy = NodeList(0)