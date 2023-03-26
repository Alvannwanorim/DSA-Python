from typing import List


class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        max_right = -1 

        for i in range(len(nums) - 1, -1, -1):
            new_right = max(max_right, nums[i])
            nums[i] =max_right
            max_right = new_right
        
        return nums
sol = Solution()
print(sol.replaceElements([17,18,5,4, 6, 1]))