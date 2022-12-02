from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) -1 
        res = [] 
        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                res.append([l +1, r + 1])
                l += 1
        return res
sol = Solution()
print(sol.twoSum([2,7,11,15], 11))