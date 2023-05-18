from typing import List


class Solution:
    def buyAndSell(self, prices: List[int])->int:
        res = 0
        lowest = prices[0]

        for price in prices:
            if lowest > price:
                lowest = price
            
            res = max(res, price - lowest)
        
        return res
sol = Solution()
print(sol.buyAndSell([7,1,5,3,6,4]))
print(sol.buyAndSell([7,6,4,3,1]))