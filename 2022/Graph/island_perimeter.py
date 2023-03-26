from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        def dfs(r,c):
            if r < 0 or r >=ROW or c < 0 or \
                c >= COL or grid[r][c] ==0 :
                return 1
            
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            perim = dfs(r + 1, c)
            perim += dfs(r - 1, c)
            perim += dfs(r, c + 1)
            perim += dfs(r, c - 1)
            return perim
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return dfs(r,c)

sol = Solution()
print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(sol.islandPerimeter([[1]]))