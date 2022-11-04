import heapq
from typing import List


class Solution:
   def kthLargestElement(self, nums: List[int], k: int) -> int:
    heap = [-n for n in nums]
    heapq.heapify(heap)
    
    while k > 1:
        heapq.heappop(heap)
        k -= 1
    
    return -heap[0]

sol = Solution()
print(sol.kthLargestElement([1,5,2,4,7,6], 4))