from typing import List


class Solution:
    def containerWithMostWater(self, nums: List[int]) -> int:
        res =0
        l, r = 0, len(nums) - 1

        while l < r:
            area = (r - l) * min(nums[r], nums[l])
            res = max(area, res)

            if nums[l] < nums[r]:
                l += 1
            elif nums[r] <= nums[r]:
                r -= 1
            
        return res

sol = Solution()
print(sol.containerWithMostWater([1,8,6,2,5,4,8,3,7]))