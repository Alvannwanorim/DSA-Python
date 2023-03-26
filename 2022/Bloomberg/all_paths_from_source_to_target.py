from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1 
        res = []
        def dfs(node, path, res):
            if node == end:
                res.append(path)
            
            for n in graph[node]:
                dfs(n, path+[n], res)
        dfs(0,[0],res)
        return res
sol = Solution()
print(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))


