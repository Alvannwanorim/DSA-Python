from typing import List


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[num] = i
sol = Solution()
print(sol.twoSum([2,3,5,6,7], 9))