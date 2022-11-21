from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict

        def dfs(cur_node, target_node, acc_product, visited):
            visited.add(cur_node)
            neighbors = graph[cur_node]
            rect = -1.0

            if target_node in neighbors:
                rect = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    rect = dfs(neighbor, target_node, acc_product * value, visited)
                    if rect != -1.0:
                        break
            visited.remove(cur_node)
            return rect

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1/value

        res = []

        for dividend, divisor  in queries:
            if dividend not in graph or divisor not in graph:
                rect = -1.0
            elif dividend == divisor:
                rect = 1.0
            else:
                visited = set()
                rect = dfs(dividend, divisor, 1, visited)
            res.append(rect)
        
        return res
sol = Solution()
print(sol.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))