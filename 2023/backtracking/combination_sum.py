from typing import List
class Solution:
    def combination_sum(self, nums:List[int], target: int)->List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if i >= len(nums) or total > target:
                return 
            if total == target:
                res.append(cur.copy())
                return 
            cur.append(nums[i])
            dfs(i , cur, total + nums[i ])
            cur.pop()
            dfs(i+ 1, cur, total)
        dfs(0, [], 0)

        return res
sol = Solution()
print(sol.combination_sum([1,2,3, 4, 5, 6], 7))
