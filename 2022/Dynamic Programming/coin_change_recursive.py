from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int, memo={}) -> int:
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return []
        if amount < 0:
            return None
        shortsCombination = None
        for c in coins:
            diff = amount - c 
            remainder = self.coinChange(coins, diff, memo)
            if remainder != None:
                combination = [*remainder, c]
                if (shortsCombination ==None or len(shortsCombination)> len(combination)):
                    shortsCombination = combination
        memo[amount] = shortsCombination
        return shortsCombination

solution = Solution()
print(solution.coinChange([ 1, 2, 5, 25 ], 100))