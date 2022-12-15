from typing import List


class Solution:
    def wordSearch(self, board: List[List[str]], word: str) -> int:
        path = set()

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if ( 0 > r or r >= ROWS or 
                0 > c or c >= COLS or
                board[r][c] != word[i] 
                or (r,c) in path ):
                return False
            path.add((r,c))

            res = (dfs(r + 1, c, i + 1) or 
                    dfs(r - 1, c, i + 1) or 
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1)) 
            path.remove((r,c))
            # print(res)
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
        
        return False
sol = Solution()
print(sol.wordSearch([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))