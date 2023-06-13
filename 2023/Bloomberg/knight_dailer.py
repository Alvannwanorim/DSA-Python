class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10

        mod = (10**9) + 7

        while n >= 2:
            tmp = dp.copy()
            dp[0] = tmp[4] + tmp[6]
            dp[1] = tmp[8] + tmp[6]
            dp[2] = tmp[7] + tmp[9]
            dp[3] = tmp[4] + tmp[8]
            dp[4] = tmp[0] + tmp[3] + tmp[9]
            dp[5] = 0
            dp[6] =  tmp[0] + tmp[7] + tmp[1]
            dp[7] = tmp[2] + tmp[6]
            dp[8] = tmp[1] + tmp[3]
            dp[9] = tmp[4] + tmp[2]
            n -= 1
        
        return sum(dp) % mod
        
