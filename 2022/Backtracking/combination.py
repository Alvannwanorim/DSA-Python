from typing import List


class Solution:
    def combination(self, n: int, k: int) -> List[int]:
        res = []
        
        def dfs(i, sub):
            if len(sub) == k:
                res.append(sub.copy())
                return
            for start in range(i, n + 1):
                sub.append(start)
                dfs(start + 1, sub)
                sub.pop()
        dfs(1,[])

        return res

sol = Solution()
print(sol.combination(4,2))
            