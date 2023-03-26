from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> List[int]:
        k = 0
        for i in range(len(nums) - 1):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k

sol = Solution()
print(sol.removeElement([0,1,2,2,3,0,4,2],2))