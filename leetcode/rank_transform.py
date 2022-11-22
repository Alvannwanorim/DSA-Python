from typing import List


class Solution:
    def rankTransform(self, nums: List[int])  -> List[int]:
        haspMap = {}
        sorted_nums = sorted(set(nums))

        for i in range(len(sorted_nums)):
            haspMap[sorted_nums[i]] = i + 1
        
        for i in range(len(nums)):
            nums[i] = haspMap[nums[i]]
        return nums

sol = Solution()
print(sol.rankTransform([4,5,3,6,7]))
print(sol.rankTransform([40, 10, 20, 30]))