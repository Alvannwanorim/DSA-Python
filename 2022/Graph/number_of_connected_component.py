from typing import List


class Solution:
    def ConnectedNodes(self,n:int, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p] 
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res

sol = Solution()
print(sol.ConnectedNodes(5,[[1,2],[1,3],[2,3], [3,4]]))