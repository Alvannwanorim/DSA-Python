from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int):
        l, r  = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1         
sol = Solution()
print(sol.binarySearch([1,2,4,5,6,7], 4))
print(sol.binarySearch([1,2,4,5,6,7], 7))
print(sol.binarySearch([1,2,4,5,6,7], 1))
print(sol.binarySearch([1,2,4,5,6,7], 5))
print(sol.binarySearch([1,2,4,5,6,7], 8))