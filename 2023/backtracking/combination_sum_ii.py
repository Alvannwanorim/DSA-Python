from typing import List
class Solution:
    def combination_sum(self, candidates:List[int], target: int)->List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(pos, cur, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <0:
                return 
            prev = -1 
            for i in range(pos, len(candidates)):
                if prev == candidates[i]:
                    continue
                cur.append(candidates[i])
                backtrack(i+1, cur, target - candidates[i])
                cur.pop()
        backtrack(0, [], target)
        return res
sol = Solution()
print(sol.combination_sum([1,1,2,3,4,6], 7))
