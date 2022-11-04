import heapq
from multiprocessing import heap
from typing import List


class Solution:
    def canConstruct(self, target: List[int]):
        if len(target) == 1:
            return target[0] == 1
        maxHeap = [-num for num in target]
        total = sum(target)
        heapq.heapify(maxHeap)

        while maxHeap:
            num = (heapq.heappop(maxHeap))
            if num == -1:
                return True
            # Subtract n from the total
            nn = -(-num % (total + num))
           
            if nn == 0:
                nn = -total - num
            total = total + num -nn
            if num == nn or nn > -1:
                return False
            elif nn < -1:
                heapq.heappush(maxHeap, nn)
            
        return True

sol = Solution()
print(sol.canConstruct([3,5,9]))