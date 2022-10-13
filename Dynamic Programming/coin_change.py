from typing import List


class Solution:
    def coinChange(self, coin: List[int], amount: int) -> int:
        dp = [amount +1 ] * (amount + 1 )
        dp[0] = 0
       
        for a in range(1, amount +1 ):
            for c in coin:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a -c ])
        print(dp)
        return dp[amount] if dp[amount] != amount +1 else -1
        
solution = Solution()
print(solution.coinChange([2,3,4,5],6))