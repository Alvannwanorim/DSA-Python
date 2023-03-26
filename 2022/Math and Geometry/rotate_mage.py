from turtle import left
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]):
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r 
                # Save the top left
                topLeft = matrix[top][l + i]

                # move bottom left into top left 
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bothom left 
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top right into bottom right 
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left  into top right 
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
        return matrix
sol = Solution()
print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))