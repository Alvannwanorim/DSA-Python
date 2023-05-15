from typing import List
class Solution:
    def containerWithMostWater(self, height: List[int]):
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = abs(l - r) * min(height[l], height[r])
            res = max(res, area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return res 

sol = Solution()
print(sol.containerWithMostWater([1,8,6,2,5,4,8,3,7]))
print(sol.containerWithMostWater([1,1]))