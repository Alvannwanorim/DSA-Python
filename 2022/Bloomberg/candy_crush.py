from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board:
            return board
        
        ROWS, COLS = len(board), len(board[0])
        is_stable = True
        for r in range(ROWS):
            for c in range(COLS - 2):
                num1 = abs(board[r][c])
                num2 = abs(board[r][c + 1])
                num3 = abs(board[r][c + 2])
                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = -num1
                    board[r][c + 1] = -num2
                    board[r][c + 2] = -num3

                    is_stable = False
                    print("here")
        
        for c in range(COLS):
            for r in range(ROWS - 2):
                num1 = abs(board[r][c])
                num2 = abs(board[r + 1][c])
                num3 = abs(board[r + 2][c])
                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = -num1
                    board[r + 1][c] = -num2
                    board[r + 2][c] = -num3
                    is_stable = False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] < 0:
                    board[r][c] = 0
        
        if not is_stable:
            for c in range(COLS):
                index = ROWS -1 
                for r in range(ROWS - 1, -1 , -1):
                    if board[r][c] > 0:
                        board[index][c], board[r][c] = board[r][c], board[index][c]
                        index -= 1
        

        return board if is_stable else self.candyCrush(board)

sol = Solution()
print(sol.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))



