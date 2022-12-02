from typing import List


class Solution:
    def containerWithWater(self, height: List[int]) ->int:
        l, r  = 0, len(height) - 1
        res = 0 

        while l < r:
            res = max(res, min(height[r], height[r]) * (r -1))

            if height[l] > height[r]:
                r -= 1
            elif height[l] <= height[r]:
                l += 1
        return res 
sol = Solution()
print(sol.containerWithWater([1,8,6,2,5,4,8,3,7]))