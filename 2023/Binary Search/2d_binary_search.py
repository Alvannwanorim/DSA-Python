from typing import List


class Solution:
    def binarySearch(self, nums: List[List[int]], target: int)->int:
        ROW, COLS = len(nums), len(nums[0])

        top, bot = 0, ROW - 1 
        while top <= bot:
            
            row = (top + bot) // 2 
            if target > nums[row][-1]:
                top = row + 1
            elif target < nums[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
        l, r = 0, COLS -1 
        while l <= r:
            m = (r + l) // 2
            
            if target > nums[row][m]:
                l = m + 1
            elif target < nums[row][m]:
                r = m - 1
            else:
                return True

        return False
sol = Solution()
print(sol.binarySearch([[1,2,4,5,6,7], [9,10,11,12,13,14]], 4))
print(sol.binarySearch([[1,2,4,5,6,7], [9,10,11,12,13,14]], 14))
print(sol.binarySearch([[1,2,4,5,6,7], [9,10,11,12,13,14]], 20))
print(sol.binarySearch([[1,2,4,5,6,7], [9,10,11,12,13,14]], 12))
