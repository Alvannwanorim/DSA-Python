from typing import List


class Solution:
    def houseRobber(self, nums: List[int]) -> int:
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, nums):
        rob1, rob2 =0,0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2, 
            rob2 = temp
        return rob2