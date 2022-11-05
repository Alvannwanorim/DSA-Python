from collections import deque
import heapq
from typing import Counter, List


class Solution:
    def setIntervals(self, tasks: List[str], n: int):
        count = Counter(tasks)
        maxHeap = [ -cnt for cnt in count.values()]

        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
sol = Solution()

print(sol.setIntervals(['A','B','A','B','B'], 2))