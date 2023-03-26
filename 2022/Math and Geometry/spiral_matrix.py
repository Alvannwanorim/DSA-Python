from typing import List


class Solution:
    def spiralMatrix(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        res = []

        while left < right and top < bottom:
            # Get all items in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Get all items in the right column
            for i in range(top, bottom):
                res.append(matrix[i][right -1])
            right -= 1

            if not(left < right and top < bottom):
                break
            
            #  Get every item in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Get every item in the left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
sol = Solution()
print(sol.spiralMatrix([[1,2,3],[4,5,6],[7,8,9]]))