from typing import List

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def wordSearch(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        visited, res  = set(), set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(r ,c, word, node):
            if (r < 0 or c < 0 
                or r == ROWS  or c == COLS
                or (r,c) in visited or 
                board[r][c] not in node.children):
                return
            visited.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.isWord:
                res.add(word)
            
            dfs(r - 1, c, word, node)
            dfs(r + 1, c, word, node)
            dfs(r, c - 1, word, node)
            dfs(r, c + 1, word, node)

            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)

        return list(res)
sol = Solution()
print(sol.wordSearch([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))