from turtle import left
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums, count = sorted(nums), 0

        for i in range(2,len(nums)):
            l, r = 0, i- 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += (r - l)
                    r -= 1
                else:
                    l += 1
        return count

    