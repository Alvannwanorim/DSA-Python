from typing import List


class Solution:

    def replaceElement(self, nums: List[int]) -> List[int]:
        rightMax = -1

        for i in range(len(nums) - 1, -1, -1):
            newMax = max(rightMax, nums[i])
            nums[i] = rightMax
            rightMax = newMax

        return nums


sol = Solution()
print(sol.replaceElement([13, 12, 2, 3, 6, 5, 1]))
print(sol.replaceElement([17, 18, 5, 4, 6, 1]))
