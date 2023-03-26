from typing import List


class solution:
    def findCheapestPrice(self, flights: List[List[int]], src: int, dist: int, k: int, n: int) -> int:
        prices = [float("inf")] * n 
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices.copy()

            for  s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d]  = prices[s] + p
            prices = tempPrices
        
        return -1 if prices[dist] == float('inf') else prices[dist]

sol = solution()
print(sol.findCheapestPrice([[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1, 4))