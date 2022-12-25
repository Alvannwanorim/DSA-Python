from typing import List


class Solution:
    def permutation(self, nums: List[int]) -> List[List[int]]:
        res =[]

        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permutation(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        
        return res
sol = Solution()
print(sol.permutation([123]))
            