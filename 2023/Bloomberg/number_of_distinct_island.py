from typing import List 
class Solution:
    
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        island_count = set()
        self.island_pos =''

        def dfs(r,c,pos):
            if (r not in range(ROW) or c not in range(COL) or grid[r][c] == 0 or (r,c) in visited): return 
            visited.add((r,c))
            self.island_pos += pos
            directions = [[1, 0, 'u'], [-1, 0, 'd'], [0, 1, 'r'], [0, -1, 'l']]
            for dr, dc, point in directions:
                dfs(r + dr, c + dc, point)
            
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visited and grid[r][c] == 1:
                    dfs(r, c, 'o')
                    island_count.add(self.island_pos)
                    self.island_pos = ''
            
        return len(island_count)

sol = Solution()
print(sol.numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
print(sol.numDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))



        