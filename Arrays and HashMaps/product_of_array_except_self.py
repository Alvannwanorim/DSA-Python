from typing import List


class Solution:
    def product(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums))

        prefix = 1
        for n in range(len(nums)):
            res[n] = prefix
            prefix *= nums[n]
        
        postFix = 1 

        for n in range(len(nums) - 1, -1, -1):
            res[n] *= postFix
            postFix *= nums[n]

        return res
sol = Solution()
print(sol.product([1,2,3,4]))
