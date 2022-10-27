
from typing import List


class Solution: 
    def matrixZeros(self, matrix: List[List[int]]) -> List[List[int]]:
        COLS, ROWS = len(matrix[0]), len(matrix)
        zeroRow = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        zeroRow = True
        
        for r in range(1,ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] == 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if zeroRow:
            for c in range(COLS):
                matrix[0][c] = 0


        return matrix

sol = Solution()
print(sol.matrixZeros([[1,1,1],[1,0,1],[1,1,1]]))