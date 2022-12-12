from typing import List


class Solution:
    def buyAndSell(self, price: List[int])->int:
        l, r = 0, 1

        res = 0

        while r < len(price):
            if price[r] < price[l]:
                l = r
            res = max(res, price[r] - price[l])
            r += 1
        return res
sol = Solution()
print(sol.buyAndSell([7,1,5,3,6,4]))
print(sol.buyAndSell([7,6,4,3,1]))