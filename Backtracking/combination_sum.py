from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return 
            if total > target:
                return 
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])

            curr.pop()

            dfs(i + 1, curr, total + candidates[i])
        dfs(0,[], candidates)
        return res
sol = Solution()
print(sol.combinationSum([1,2,3,4,5],7))