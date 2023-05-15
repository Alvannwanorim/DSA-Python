from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            targetSum = numbers[l] + numbers[r]
            if targetSum > target:
                r -= 1
            elif targetSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([2,3,4], target = 6))
print(sol.twoSum([-1,0], target = -1))

