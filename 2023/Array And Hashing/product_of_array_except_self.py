from typing import List


class Solution:
    def productOfArray(self, nums: List[int]):
        res = [1] * len(nums)
        prefix  = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postFix = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postFix
            postFix *= nums[i]
        
        return res

sol = Solution()
print(sol.productOfArray([1,2,3,4]))
print(sol.productOfArray([1,2,2,4]))
