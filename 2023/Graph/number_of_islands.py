from typing import List


class Solution:

    def numOfIslands(self, graph: List[List[str]]) -> int:
        ROWS, COLS = len(graph), len(graph[0])
        visited = set()

        def dfs(r, c):
            if ((r not in range(ROWS)) or (c not in range(COLS))
                    or (r, c) in visited or graph[r][c] == '0'):
                return
            visited.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if graph[r][c] == '1' and (r, c) not in visited:
                    res += 1
                    dfs(r, c)

        return res


sol = Solution()
print(
    sol.numOfIslands([["1", "1", "0", "1", "0"], ["1", "1", "0", "1", "0"],
                      ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "1"]]))
