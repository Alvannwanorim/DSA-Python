from typing import List


class Solution:

    def twoSum(self, num: List[int], target: int) -> List[int]:
        hashMap = {}
        diff = 0
        for i, n in enumerate(num):
            diff = abs(target - n)
            if diff in hashMap:
                return [hashMap[diff], i]

            hashMap[n] = i

        return []


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))
print(sol.twoSum([3, 3], 7))
