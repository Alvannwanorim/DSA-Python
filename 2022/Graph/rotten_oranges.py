import collections
from typing import List


class Solution:
    def rottenOranges(self, grid: List[List[int]]):
        time, fresh = 0, 0

        q = collections.deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            r,c = q.popleft()
            for i in range(len(q)):
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row ==len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] == 2):
                        continue
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1 
sol = Solution()
print(sol.rottenOranges([[2,1,1],[1,1,0],[0,1,1]]))


        