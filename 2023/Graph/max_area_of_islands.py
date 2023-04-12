from typing import List


class Solution:

    def maxAreaOfIslands(self, graph: List[List[str]]) -> int:

        ROWS, COLS = len(graph), len(graph[0])
        visited = set()
        maxArea = 0

        def dfs(r, c):
            if ((r not in range(ROWS)) or (c not in range(COLS))
                    or ((r, c) in visited) or graph[r][c] == '0'):
                return 0
            visited.add((r, c))
            res = 1
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                res += dfs(r + dr, c + dc)

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if graph[r][c] == '1' and (r, c) not in visited:
                    area = dfs(r, c)
                    maxArea = max(area, maxArea)

        return maxArea


sol = Solution()
print(
    sol.maxAreaOfIslands([["1", "1", "0", "1", "0"], ["1", "0", "0", "1", "0"],
                          ["1", "1", "0", "0", "0"], ["0", "0", "0", "0",
                                                      "1"]]))
