from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(cur, i, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return
            prev = -1
            for i in range(len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i +1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
        backtrack([], 0, target)
        return res
sol = Solution()
print(sol.combinationSum([1,2,3,4,5],7))