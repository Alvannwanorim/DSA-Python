from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        maxElement = 0
        res = 0
        hashMap = {}

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
            if hashMap[n] > maxElement:
                maxElement = hashMap[n]
                res = n
        return res


sol = Solution()
print(sol.majorityElement([1, 2, 3, 3, 3, 4]))
