
from typing import List

class Solution:
    def jumpGame(self, nums: List[int]) -> bool:
        goal = len(nums) + 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        print(goal)
        return True if goal == 0 else False

sol = Solution()
print(sol.jumpGame([3,2,1,1,4]))
