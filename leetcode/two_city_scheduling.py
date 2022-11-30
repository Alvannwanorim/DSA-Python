from typing import List


class Solution:
    def twoCitySchedule(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key= lambda x: x[1] - x[0])

        res = 0
        cost = len(costs)
        print(costs[:cost//2])
        print(costs[cost//2:])
        print(costs)
        for c in costs[cost//2:]:
            res += c[0]
        
        for c in costs[:cost//2]:
            res += c[1]
        
        return res
sol = Solution()
print(sol.twoCitySchedule([[10,20],[30,200],[400,50],[30,20]]))
