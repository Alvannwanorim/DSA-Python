from typing import List


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return []
