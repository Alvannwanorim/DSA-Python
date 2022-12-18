from typing import List


class Solution:
    def surroundedRegion(self, board: List[List[int]]):
        ROWS, COLS = len(board), len(board[0])

        def capture(r,c):
            if( r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            # print(board[r][c] )
            capture(r + 1, c)
            capture(r - 1,c)
            capture(r , c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] =="O" and (r in [0, ROWS - 1] or  c in [0, COLS - 1])):
                    capture(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] =="T":
                    board[r][c] = "O"
        
        return board

sol = Solution()
print(sol.surroundedRegion([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))