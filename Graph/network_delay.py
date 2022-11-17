import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append([v, w])
        
        minHeap = [(0, k)]
        t = 0
        visit = set()

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            t = max(t, w1)
            if n1 in visit:
                continue
            visit.add(n1)
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1 + w2, n2))
        
        return t if len(visit) == n else -1
sol = Solution()
print(sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))