from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COL = len(rooms), len(rooms[0])

        visit = set()
        q = deque()
        
        def addRoom(r,c):
            if (r < 0 or r==ROWS or c < 0 or c == COL or rooms[r][c]== -1 or (r,c) in visit):
                return 
            visit.add((r,c))
            q.append((r,c))

        for r in range(ROWS):
            for c in range(COL):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r ,c + 1)
                addRoom(r ,c - 1)
            dist += 1
        return rooms

s = Solution()

print(s.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))