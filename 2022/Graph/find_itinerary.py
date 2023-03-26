from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]])->List[str]:
        adj ={src: [] for src, dst in tickets}

        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        res =["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1: return True

            if src not in adj:
                return False
            
            temp = list(adj[src])

            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return res
                adj[src].insert(i,v)
                res.pop()
            return False

        dfs("JFK")
        return res
sol =Solution()
print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
