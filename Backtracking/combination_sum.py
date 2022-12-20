from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            
            if total == target:
                res.append(curr.copy())
                return 
            if total > target or i>= len(candidates):
                return 
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])

            curr.pop()

            dfs(i + 1, curr, total)

        dfs(0,[], 0)
        return res
sol = Solution()
print(sol.combinationSum([1,2,3,4,5],7))
print(sol.combinationSum([2,3,6,7],7))