import heapq
from typing import List


class Solution:
    def lastWeightStone(self, stones: List[int]):
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])
sol = Solution()

print(sol.lastWeightStone([1,1,2,4,7,8]))