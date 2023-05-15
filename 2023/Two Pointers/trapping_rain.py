from typing import List 
class Solution:
    def trappingRain(self, heights: List[int]):
        l, r = 0, len(heights) - 1 
        leftMax, rightMax = heights[l], heights[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, heights[l])
                res += leftMax -heights[l]
            else:
                r -= 1
                rightMax = max(rightMax, heights[r])
                res += rightMax -heights[r]
        return res
sol = Solution()
print(sol.trappingRain([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trappingRain([4,2,0,3,2,5]))