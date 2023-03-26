class Solution:
    def knightDialer(self, n: int)->int:
        dp = [1] * 10

        mod = (10**9 + 7)
        while n >= 2:
            temp = dp.copy()
            dp[0] = temp[4] + temp[6]
            dp[1] = temp[6] + temp[8]
            dp[2] = temp[7] + temp[9]
            dp[3] = temp[4] + temp[8]
            dp[4] = temp[0] + temp[3]+ temp[9]
            dp[5] = 0
            dp[6] = temp[0] + temp[1]+ temp[7]
            dp[7] = temp[2] + temp[6]
            dp[8] = temp[1] + temp[3]
            dp[9] = temp[2] + temp[4]

            n -= 1
        
        return sum(dp) % mod
sol = Solution()
print(sol.knightDialer(2))
print(sol.knightDialer(1))
print(sol.knightDialer(3131))