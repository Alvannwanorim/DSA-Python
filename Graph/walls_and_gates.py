from collections import deque
from dis import dis
from operator import le
from typing import List


class Solution:
    def awall_and_gates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])

        visited = set()
        q = deque()
        # loop through the rooms and append all the empty rooms to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        # Initialize the distance to the closest gate to 0
        dist = 0

        # Now, loop through the q and pop and the position
        # Use the position to update its neighbor

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                # Perform a BSF to update the rooms 
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1
        def addRoom(r,c):
            if(r < 0 or c < 0 
                or r == ROWS 
                or c == COLS 
                or (r, c) in visited 
                or rooms[r][c] == -1):
                return
            visited.add(r,c)
            q.append([r, c])