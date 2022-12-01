from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) ->bool:
        count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(maxCount, count[n])
        return res
sol =Solution()
print(sol.majorityElement([3,3,3,4,1]))
