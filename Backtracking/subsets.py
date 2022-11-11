from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset =[]

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            print(i)
            print(subset)
            # remove nums[i] from dfs
            subset.pop()
            dfs(i + 1)
        dfs(0)

        return res
sol = Solution()
print(sol.subsets([1,2,3,4]))