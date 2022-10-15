import collections
from typing import List


class Solution:
    def rottenOranges(self, grid: List[List[int]]):
        # initialize a data storage for the postion of rotten oranges
        q = collections.deque()

        fresh = 0
        time = 0
        # loop through the grid to fetch all rotten oranges
        # and also record the fresh ones
        ROWS,COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        # Loop through the queue and mark neighbors or the rotten oranges as rotten
        # decrease the number of fresh oranges and increase the time
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc 

                    if(row in range(len(grid)) 
                        and col in range(len(grid[0])) 
                        and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


        