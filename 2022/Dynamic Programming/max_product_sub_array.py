from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue
            temp = n * currMax
            currMax = max( n * currMax, n * currMin, n)
            currMin = min(temp, n * currMin, n)
            res = max(res, currMax)
        return res