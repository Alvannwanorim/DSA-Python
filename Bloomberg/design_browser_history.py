class NodeTree:
    def __init__(self, val: str, prev=None, next=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = NodeTree(homepage)

    def visit(self, url: str) -> None:
        node = NodeTree(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next

        

    def back(self, steps: int) -> str:
        while steps and self.root.prev:
            self.root = self.root.prev
            steps -= 1
        
        return self.root.val
        

    def forward(self, steps: int) -> str:
        while steps and self.root.next:
            self.root = self.root.next
            steps -= 1
        return self.root.val