class Node:
    def __init__(self,val, next= None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        

    def visit(self, url: str) -> None:
        tmp = self.homepage
        site = Node(url)
        site.prev = tmp
        tmp.next = site
        self.homepage = site
        

    def back(self, steps: int) -> str:
        while  steps > 0:
            if self.homepage.prev == None: 
                break
            self.homepage = self.homepage.prev
            steps -= 1
        return self.homepage.val
        

    def forward(self, steps: int) -> str:
        while  steps > 0:
            if self.homepage.next == None: 
                break
            self.homepage = self.homepage.next
            steps -= 1
        return self.homepage.val


browserHistory = BrowserHistory("leetcode.come")
browserHistory.visit("google.com");      
browserHistory.visit("facebook.com");     
browserHistory.visit("youtube.com");      
browserHistory.back(1);                   
browserHistory.back(1);                   
browserHistory.forward(1);                
browserHistory.visit("linkedin.com");     
browserHistory.forward(2);                
browserHistory.back(2);                   
browserHistory.back(7);                   